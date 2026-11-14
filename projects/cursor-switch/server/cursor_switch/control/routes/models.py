"""Model configuration routes."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field

from cursor_switch.adapters.persistence.repositories import ModelRecord
from cursor_switch.control.schemas import ConnectivityResultOut, ModelInput, ModelOut, ReorderInput

router = APIRouter(prefix="/api/models", tags=["models"])


def _to_record(payload: ModelInput, model_id: str = "") -> ModelRecord:
    return ModelRecord(
        id=model_id,
        display_name=payload.display_name,
        provider_type=payload.provider_type,
        base_url=payload.base_url,
        api_key=payload.api_key,
        model_name=payload.model_name,
        notes=payload.notes,
        context_tokens=payload.context_tokens,
        max_output_tokens=payload.max_output_tokens,
        enabled=payload.enabled,
        sort_order=payload.sort_order,
        extra=payload.extra,
        headers=payload.headers,
        group_name=payload.group_name,
    )


def _to_out(record: ModelRecord) -> ModelOut:
    return ModelOut(**record.public_dict())  # type: ignore[arg-type]


@router.get("", response_model=list[ModelOut])
async def list_models(request: Request) -> list[ModelOut]:
    records = await request.app.state.services.models.list_models()
    return [_to_out(record) for record in records]


@router.post("", response_model=ModelOut, status_code=201)
async def create_model(payload: ModelInput, request: Request) -> ModelOut:
    record = await request.app.state.services.models.create_model(_to_record(payload))
    return _to_out(record)


class DiscoverIn(BaseModel):
    provider_type: str
    base_url: str
    api_key: str = ""
    headers: dict[str, str] = Field(default_factory=dict)


class GroupUpdateIn(BaseModel):
    group_name: str
    base_url: str | None = None
    api_key: str | None = None


@router.post("/discover")
async def discover_models(payload: DiscoverIn, request: Request) -> dict[str, list[str]]:
    try:
        ids = await request.app.state.services.models.discover_ids(
            provider_type=payload.provider_type,
            base_url=payload.base_url,
            api_key=payload.api_key,
            headers=payload.headers,
        )
    except Exception as error:  # noqa: BLE001
        raise HTTPException(status_code=400, detail=str(error)) from error
    return {"model_ids": ids}


@router.put("/group", response_model=list[ModelOut])
async def update_group(payload: GroupUpdateIn, request: Request) -> list[ModelOut]:
    records = await request.app.state.services.models.update_group(
        payload.group_name,
        base_url=payload.base_url,
        api_key=payload.api_key,
    )
    return [_to_out(record) for record in records]


@router.put("/order", response_model=list[ModelOut])
async def reorder_models(payload: ReorderInput, request: Request) -> list[ModelOut]:
    records = await request.app.state.services.models.reorder(payload.ordered_ids)
    return [_to_out(record) for record in records]


@router.put("/{model_id}", response_model=ModelOut)
async def update_model(model_id: str, payload: ModelInput, request: Request) -> ModelOut:
    record = await request.app.state.services.models.update_model(
        model_id, _to_record(payload, model_id)
    )
    if record is None:
        raise HTTPException(status_code=404, detail="model not found")
    return _to_out(record)


@router.delete("/{model_id}", status_code=204)
async def delete_model(model_id: str, request: Request) -> None:
    deleted = await request.app.state.services.models.delete_model(model_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="model not found")


@router.post("/{model_id}/test", response_model=ConnectivityResultOut)
async def test_model(model_id: str, request: Request) -> ConnectivityResultOut:
    result = await request.app.state.services.models.test_model(model_id)
    if result is None:
        raise HTTPException(status_code=404, detail="model not found")
    return ConnectivityResultOut(
        ok=result.ok,
        first_token_ms=result.first_token_ms,
        total_ms=result.total_ms,
        text=result.text,
        error=result.error,
        usage=result.usage,
    )
