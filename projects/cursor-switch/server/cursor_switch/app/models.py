"""Application service for model configuration."""

from __future__ import annotations

from cursor_switch.adapters.persistence.repositories import ModelRecord
from cursor_switch.adapters.persistence.unit_of_work import UnitOfWorkFactory
from cursor_switch.adapters.providers.base import ProviderConfig
from cursor_switch.adapters.providers.tester import ConnectivityResult, test_provider


def to_provider_config(record: ModelRecord) -> ProviderConfig:
    return ProviderConfig(
        provider_type=record.provider_type,
        base_url=record.base_url,
        api_key=record.api_key,
        model_name=record.model_name,
        headers=dict(record.headers or {}),
        extra=dict(record.extra or {}),
    )


class ModelService:
    def __init__(self, uow_factory: UnitOfWorkFactory) -> None:
        self._uow_factory = uow_factory

    async def list_models(self) -> list[ModelRecord]:
        async with self._uow_factory.begin() as uow:
            return await uow.models.list()

    async def create_model(self, data: ModelRecord) -> ModelRecord:
        async with self._uow_factory.begin() as uow:
            return await uow.models.create(data)

    async def update_model(self, model_id: str, data: ModelRecord) -> ModelRecord | None:
        async with self._uow_factory.begin() as uow:
            return await uow.models.update(model_id, data)

    async def delete_model(self, model_id: str) -> bool:
        async with self._uow_factory.begin() as uow:
            return await uow.models.delete(model_id)

    async def reorder(self, ordered_ids: list[str]) -> list[ModelRecord]:
        async with self._uow_factory.begin() as uow:
            return await uow.models.reorder(ordered_ids)

    async def test_model(self, model_id: str) -> ConnectivityResult | None:
        async with self._uow_factory.begin() as uow:
            record = await uow.models.get(model_id)
        if record is None:
            return None
        return await test_provider(to_provider_config(record))
