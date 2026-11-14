"""Repositories for models and settings."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from uuid import uuid4

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from cursor_switch.adapters.persistence.models import CallRow, ModelRow, SettingsRow


@dataclass(slots=True)
class ModelRecord:
    id: str
    display_name: str
    provider_type: str
    base_url: str
    api_key: str
    model_name: str
    notes: str = ""
    context_tokens: int = 128_000
    max_output_tokens: int = 8_192
    enabled: bool = True
    sort_order: int = 0
    extra: dict[str, object] | None = None
    headers: dict[str, str] | None = None
    group_name: str = ""

    def public_dict(self) -> dict[str, object]:
        data = asdict(self)
        data["extra"] = self.extra or {}
        data["headers"] = self.headers or {}
        return data


@dataclass(slots=True)
class PortSettings:
    proxy_port: int = 8788
    service_port: int = 8787


@dataclass(slots=True)
class ProxySettings:
    mode: str = "default"
    address: str = ""
    auth_enabled: bool = False
    username: str = ""
    password: str = ""


@dataclass(slots=True)
class DesktopSettings:
    silent_start: bool = False
    show_dock_icon: bool = True


@dataclass(slots=True)
class HarnessSettings:
    enabled: bool = False


def _row_to_model(row: ModelRow) -> ModelRecord:
    return ModelRecord(
        id=row.id,
        display_name=row.display_name,
        provider_type=row.provider_type,
        base_url=row.base_url,
        api_key=row.api_key,
        model_name=row.model_name,
        notes=row.notes,
        context_tokens=row.context_tokens,
        max_output_tokens=row.max_output_tokens,
        enabled=row.enabled,
        sort_order=row.sort_order,
        extra=json.loads(row.extra_json or "{}"),
        headers=json.loads(row.headers_json or "{}"),
        group_name=row.group_name or "",
    )


class ModelRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def list(self) -> list[ModelRecord]:
        result = await self._session.scalars(
            select(ModelRow).order_by(ModelRow.sort_order, ModelRow.display_name)
        )
        return [_row_to_model(row) for row in result.all()]

    async def get(self, model_id: str) -> ModelRecord | None:
        row = await self._session.get(ModelRow, model_id)
        return None if row is None else _row_to_model(row)

    async def create(self, data: ModelRecord) -> ModelRecord:
        model_id = data.id or uuid4().hex
        row = ModelRow(
            id=model_id,
            display_name=data.display_name,
            provider_type=data.provider_type,
            base_url=data.base_url,
            api_key=data.api_key,
            model_name=data.model_name,
            notes=data.notes,
            context_tokens=data.context_tokens,
            max_output_tokens=data.max_output_tokens,
            enabled=data.enabled,
            sort_order=data.sort_order,
            extra_json=json.dumps(data.extra or {}),
            headers_json=json.dumps(data.headers or {}),
            group_name=data.group_name,
        )
        self._session.add(row)
        await self._session.flush()
        return _row_to_model(row)

    async def update(self, model_id: str, data: ModelRecord) -> ModelRecord | None:
        row = await self._session.get(ModelRow, model_id)
        if row is None:
            return None
        row.display_name = data.display_name
        row.provider_type = data.provider_type
        row.base_url = data.base_url
        row.api_key = data.api_key
        row.model_name = data.model_name
        row.notes = data.notes
        row.context_tokens = data.context_tokens
        row.max_output_tokens = data.max_output_tokens
        row.enabled = data.enabled
        row.sort_order = data.sort_order
        row.extra_json = json.dumps(data.extra or {})
        row.headers_json = json.dumps(data.headers or {})
        row.group_name = data.group_name
        await self._session.flush()
        return _row_to_model(row)

    async def delete(self, model_id: str) -> bool:
        row = await self._session.get(ModelRow, model_id)
        if row is None:
            return False
        await self._session.delete(row)
        return True

    async def reorder(self, ordered_ids: list[str]) -> list[ModelRecord]:
        for index, model_id in enumerate(ordered_ids):
            row = await self._session.get(ModelRow, model_id)
            if row is not None:
                row.sort_order = index + 1
        await self._session.flush()
        return await self.list()

    async def update_group(
        self,
        group_name: str,
        *,
        base_url: str | None,
        api_key: str | None,
    ) -> list[ModelRecord]:
        result = await self._session.scalars(select(ModelRow).where(ModelRow.group_name == group_name))
        for row in result.all():
            if base_url is not None:
                row.base_url = base_url
            if api_key is not None and api_key != "":
                row.api_key = api_key
        await self._session.flush()
        return await self.list()


@dataclass(slots=True)
class CallRecord:
    id: str
    model_id: str = ""
    display_name: str = ""
    provider_type: str = ""
    model_name: str = ""
    status: str = "ok"
    created_at_ms: int = 0
    first_token_ms: int | None = None
    duration_ms: int | None = None
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_tokens: int = 0
    cache_write_tokens: int = 0
    error_message: str = ""
    detailed: bool = False
    request_json: str = ""
    response_text: str = ""

    def summary(self) -> dict[str, object]:
        return {
            "id": self.id,
            "model_id": self.model_id,
            "display_name": self.display_name,
            "provider_type": self.provider_type,
            "model_name": self.model_name,
            "status": self.status,
            "created_at_ms": self.created_at_ms,
            "first_token_ms": self.first_token_ms,
            "duration_ms": self.duration_ms,
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "cache_read_tokens": self.cache_read_tokens,
            "cache_write_tokens": self.cache_write_tokens,
            "error_message": self.error_message,
            "detailed": self.detailed,
        }

    def detail(self) -> dict[str, object]:
        data = self.summary()
        data["request_json"] = self.request_json if self.detailed else ""
        data["response_text"] = self.response_text if self.detailed else ""
        return data


def _row_to_call(row: CallRow) -> CallRecord:
    return CallRecord(
        id=row.id,
        model_id=row.model_id,
        display_name=row.display_name,
        provider_type=row.provider_type,
        model_name=row.model_name,
        status=row.status,
        created_at_ms=row.created_at_ms,
        first_token_ms=row.first_token_ms,
        duration_ms=row.duration_ms,
        input_tokens=row.input_tokens,
        output_tokens=row.output_tokens,
        cache_read_tokens=row.cache_read_tokens,
        cache_write_tokens=row.cache_write_tokens,
        error_message=row.error_message,
        detailed=row.detailed,
        request_json=row.request_json,
        response_text=row.response_text,
    )


class CallRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def add(self, record: CallRecord) -> CallRecord:
        row = CallRow(
            id=record.id or uuid4().hex,
            model_id=record.model_id,
            display_name=record.display_name,
            provider_type=record.provider_type,
            model_name=record.model_name,
            status=record.status,
            created_at_ms=record.created_at_ms,
            first_token_ms=record.first_token_ms,
            duration_ms=record.duration_ms,
            input_tokens=record.input_tokens,
            output_tokens=record.output_tokens,
            cache_read_tokens=record.cache_read_tokens,
            cache_write_tokens=record.cache_write_tokens,
            error_message=record.error_message,
            detailed=record.detailed,
            request_json=record.request_json if record.detailed else "",
            response_text=record.response_text if record.detailed else "",
        )
        self._session.add(row)
        await self._session.flush()
        return _row_to_call(row)

    async def list_recent(self, limit: int = 200) -> list[CallRecord]:
        result = await self._session.scalars(
            select(CallRow).order_by(CallRow.created_at_ms.desc()).limit(limit)
        )
        return [_row_to_call(row) for row in result.all()]

    async def get(self, call_id: str) -> CallRecord | None:
        row = await self._session.get(CallRow, call_id)
        return None if row is None else _row_to_call(row)

    async def between(self, start_ms: int, end_ms: int, model_ids: list[str] | None) -> list[CallRecord]:
        query = select(CallRow).where(
            CallRow.created_at_ms >= start_ms,
            CallRow.created_at_ms < end_ms,
        )
        if model_ids:
            query = query.where(CallRow.model_id.in_(model_ids))
        result = await self._session.scalars(query.order_by(CallRow.created_at_ms))
        return [_row_to_call(row) for row in result.all()]

    async def counts(self) -> tuple[int, int]:
        rows = (await self._session.scalars(select(CallRow))).all()
        detailed = sum(1 for row in rows if row.detailed and (row.request_json or row.response_text))
        return len(rows), detailed

    async def clear(self, scope: str) -> None:
        rows = (await self._session.scalars(select(CallRow))).all()
        if scope == "all":
            for row in rows:
                await self._session.delete(row)
            return
        for row in rows:
            row.request_json = ""
            row.response_text = ""
            row.detailed = False


class SettingsRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_json(self, key: str, default: dict[str, object]) -> dict[str, object]:
        row = await self._session.get(SettingsRow, key)
        if row is None:
            return dict(default)
        return json.loads(row.value_json)

    async def put_json(self, key: str, value: dict[str, object]) -> dict[str, object]:
        row = await self._session.get(SettingsRow, key)
        payload = json.dumps(value)
        if row is None:
            self._session.add(SettingsRow(key=key, value_json=payload))
        else:
            row.value_json = payload
        await self._session.flush()
        return value
