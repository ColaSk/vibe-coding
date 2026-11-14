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

    async def get_model(self, model_id: str) -> ModelRecord | None:
        async with self._uow_factory.begin() as uow:
            return await uow.models.get(model_id)

    async def reorder(self, ordered_ids: list[str]) -> list[ModelRecord]:
        async with self._uow_factory.begin() as uow:
            return await uow.models.reorder(ordered_ids)

    async def update_group(
        self, group_name: str, *, base_url: str | None, api_key: str | None
    ) -> list[ModelRecord]:
        async with self._uow_factory.begin() as uow:
            return await uow.models.update_group(group_name, base_url=base_url, api_key=api_key)

    async def discover_ids(self, *, provider_type: str, base_url: str, api_key: str, headers: dict[str, str]) -> list[str]:
        import httpx

        root = base_url.rstrip("/")
        path = "/models" if root.endswith("/v1") else "/v1/models"
        if provider_type == "anthropic":
            path = "/v1/models"
        request_headers = {"authorization": f"Bearer {api_key}", **headers}
        if provider_type == "anthropic":
            request_headers["x-api-key"] = api_key
            request_headers["anthropic-version"] = "2023-06-01"
        async with httpx.AsyncClient(timeout=20) as client:
            response = await client.get(f"{root}{path}", headers=request_headers)
            response.raise_for_status()
            payload = response.json()
        data = payload.get("data") if isinstance(payload, dict) else None
        if not isinstance(data, list):
            return []
        return [str(item.get("id")) for item in data if isinstance(item, dict) and item.get("id")]

    async def test_model(self, model_id: str) -> ConnectivityResult | None:
        async with self._uow_factory.begin() as uow:
            record = await uow.models.get(model_id)
        if record is None:
            return None
        return await test_provider(to_provider_config(record))
