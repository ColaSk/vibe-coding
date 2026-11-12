"""FastAPI dependency wiring."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from sqlalchemy.ext.asyncio import AsyncEngine

from cursor_switch.adapters.cursor.gateway import CursorGateway
from cursor_switch.adapters.cursor.services.account import AccountFacade
from cursor_switch.adapters.cursor.services.knowledge import KnowledgeStore
from cursor_switch.adapters.cursor.services.model_catalog import ModelCatalog
from cursor_switch.adapters.cursor.services.telemetry import NullTelemetry
from cursor_switch.adapters.local_access.ca import CaManager
from cursor_switch.adapters.local_access.facade import LocalAccessFacade
from cursor_switch.adapters.local_access.proxy import CursorProxy
from cursor_switch.adapters.persistence.db import (
    create_engine,
    create_session_factory,
    init_schema,
)
from cursor_switch.adapters.persistence.unit_of_work import UnitOfWorkFactory
from cursor_switch.adapters.providers.base import ProviderConfig
from cursor_switch.adapters.search.index import CodeSearchIndex
from cursor_switch.adapters.tools.dispatch import ToolDispatcher
from cursor_switch.adapters.tools.handlers import default_handlers
from cursor_switch.app.harness import HarnessService
from cursor_switch.app.models import ModelService, to_provider_config
from cursor_switch.app.settings import SettingsService
from cursor_switch.app.usage import UsageService
from cursor_switch.runtime.ports.model import ModelPort


@dataclass
class AppServices:
    engine: AsyncEngine
    models: ModelService
    settings: SettingsService
    harness: HarnessService
    usage: UsageService
    local_access: LocalAccessFacade
    gateway: CursorGateway
    model_catalog: ModelCatalog
    account: AccountFacade
    knowledge: KnowledgeStore
    telemetry: NullTelemetry
    model_index: _ModelConfigIndex
    search_index: CodeSearchIndex


class _ModelConfigIndex:
    """Sync lookup cache for ProviderRouter, refreshed from ModelService."""

    def __init__(self, models: ModelService) -> None:
        self._models = models
        self._by_id: dict[str, ProviderConfig] = {}

    async def refresh(self) -> None:
        rows = await self._models.list_models()
        self._by_id = {
            row.id: to_provider_config(row) for row in rows if row.enabled
        }

    def lookup(self, model_id: str) -> ProviderConfig | None:
        return self._by_id.get(model_id)

    def known_ids(self) -> set[str]:
        return set(self._by_id)


async def build_services(
    database_url: str | None = None,
    *,
    ca_dir: Path | None = None,
    cursor_settings_path: Path | None = None,
    model: ModelPort | None = None,
) -> AppServices:
    engine = create_engine(database_url)
    await init_schema(engine)
    factory = create_session_factory(engine)
    uow = UnitOfWorkFactory(factory)
    ca = CaManager(ca_dir) if ca_dir is not None else CaManager()
    local_access = LocalAccessFacade(
        ca=ca,
        proxy=CursorProxy(ca),
        cursor_settings_path=cursor_settings_path,
    )
    models = ModelService(uow)
    index = _ModelConfigIndex(models)
    await index.refresh()
    search_index = CodeSearchIndex()
    await search_index.init()
    tools = ToolDispatcher(handlers=default_handlers(search_index=search_index))
    gateway = CursorGateway(
        model=model,
        tools=tools,
        model_lookup=None if model is not None else index.lookup,
        known_model_ids=index.known_ids,
    )
    return AppServices(
        engine=engine,
        models=models,
        settings=SettingsService(uow),
        harness=HarnessService(local_access, uow),
        usage=UsageService(),
        local_access=local_access,
        gateway=gateway,
        model_catalog=ModelCatalog(models.list_models),
        account=AccountFacade(),
        knowledge=KnowledgeStore(),
        telemetry=NullTelemetry(),
        model_index=index,
        search_index=search_index,
    )
