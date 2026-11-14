"""Overview and call-record control routes."""

from __future__ import annotations

import time

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel

router = APIRouter(prefix="/api", tags=["usage"])


class OverviewOut(BaseModel):
    model_count: int
    enabled_model_count: int
    call_count: int
    total_input_tokens: int
    total_output_tokens: int
    avg_first_token_ms: float | None
    successful_calls: int
    failed_calls: int
    cache_read_tokens: int
    cache_write_tokens: int
    estimated_value: float
    estimated_cache_value: float = 0
    token_usage_granularity: str
    token_usage_series: list[dict[str, int]]


class CallIn(BaseModel):
    model_id: str = ""
    display_name: str = ""
    provider_type: str = ""
    model_name: str = ""
    status: str = "ok"
    created_at_ms: int | None = None
    first_token_ms: int | None = None
    duration_ms: int | None = None
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_tokens: int = 0
    cache_write_tokens: int = 0
    error_message: str = ""
    request_json: str = ""
    response_text: str = ""


class StorageOut(BaseModel):
    call_count: int
    trace_count: int


@router.get("/overview", response_model=OverviewOut)
async def overview(
    request: Request,
    start_ms: int | None = None,
    end_ms: int | None = None,
    model_ids: str = "",
) -> OverviewOut:
    from cursor_switch.app.usage import resolve_pricing

    models = await request.app.state.services.models.list_models()
    enabled = sum(1 for row in models if row.enabled)
    usage = request.app.state.services.usage
    usage.set_model_counts(total=len(models), enabled=enabled)
    now = int(time.time() * 1000)
    start = 0 if start_ms is None else start_ms
    end = now + 1 if end_ms is None else end_ms
    selected = [item for item in model_ids.split(",") if item]
    fallback = resolve_pricing(await request.app.state.services.settings.get_pricing())
    pricing_by_model = {
        row.id: resolve_pricing(row.extra, fallback)
        for row in models
    }
    stats = await usage.overview(
        start_ms=start,
        end_ms=end,
        model_ids=selected or None,
        pricing_by_model=pricing_by_model,
        fallback_pricing=fallback,
    )
    return OverviewOut(
        model_count=stats.model_count,
        enabled_model_count=stats.enabled_model_count,
        call_count=stats.call_count,
        total_input_tokens=stats.total_input_tokens,
        total_output_tokens=stats.total_output_tokens,
        avg_first_token_ms=stats.avg_first_token_ms,
        successful_calls=stats.successful_calls,
        failed_calls=stats.failed_calls,
        cache_read_tokens=stats.cache_read_tokens,
        cache_write_tokens=stats.cache_write_tokens,
        estimated_value=stats.estimated_value,
        estimated_cache_value=stats.estimated_cache_value,
        token_usage_granularity=stats.granularity,
        token_usage_series=stats.series,
    )


@router.get("/calls")
async def list_calls(request: Request) -> list[dict[str, object]]:
    return await request.app.state.services.usage.list_calls()


@router.post("/calls", status_code=201)
async def create_call(payload: CallIn, request: Request) -> dict[str, object]:
    from cursor_switch.adapters.persistence.repositories import CallRecord

    detailed = bool(await request.app.state.services.settings.get_detailed())
    record = CallRecord(
        id="",
        model_id=payload.model_id,
        display_name=payload.display_name,
        provider_type=payload.provider_type,
        model_name=payload.model_name,
        status=payload.status,
        created_at_ms=payload.created_at_ms or int(time.time() * 1000),
        first_token_ms=payload.first_token_ms,
        duration_ms=payload.duration_ms,
        input_tokens=payload.input_tokens,
        output_tokens=payload.output_tokens,
        cache_read_tokens=payload.cache_read_tokens,
        cache_write_tokens=payload.cache_write_tokens,
        error_message=payload.error_message,
        detailed=detailed,
        request_json=payload.request_json,
        response_text=payload.response_text,
    )
    saved = await request.app.state.services.usage.record(record)
    return saved.detail()


@router.get("/calls/{call_id}")
async def get_call(call_id: str, request: Request) -> dict[str, object]:
    found = await request.app.state.services.usage.get_call(call_id)
    if found is None:
        raise HTTPException(status_code=404, detail="call not found")
    return found


@router.get("/storage", response_model=StorageOut)
async def storage(request: Request) -> StorageOut:
    return StorageOut(**await request.app.state.services.usage.storage())


@router.delete("/storage", response_model=StorageOut)
async def clear_storage(request: Request, scope: str = "details") -> StorageOut:
    if scope not in {"details", "all"}:
        raise HTTPException(status_code=400, detail="scope must be details or all")
    return StorageOut(**await request.app.state.services.usage.clear(scope))
