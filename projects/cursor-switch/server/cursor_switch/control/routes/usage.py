"""Overview and call-record control routes."""

from __future__ import annotations

from fastapi import APIRouter, Request
from pydantic import BaseModel

router = APIRouter(prefix="/api", tags=["usage"])


class OverviewOut(BaseModel):
    model_count: int
    enabled_model_count: int
    call_count: int
    total_input_tokens: int
    total_output_tokens: int
    avg_first_token_ms: float | None


@router.get("/overview", response_model=OverviewOut)
async def overview(request: Request) -> OverviewOut:
    models = await request.app.state.services.models.list_models()
    enabled = sum(1 for row in models if row.enabled)
    request.app.state.services.usage.set_model_counts(total=len(models), enabled=enabled)
    stats = request.app.state.services.usage.overview()
    return OverviewOut(
        model_count=stats.model_count,
        enabled_model_count=stats.enabled_model_count,
        call_count=stats.call_count,
        total_input_tokens=stats.total_input_tokens,
        total_output_tokens=stats.total_output_tokens,
        avg_first_token_ms=stats.avg_first_token_ms,
    )


@router.get("/calls")
async def list_calls() -> list[dict[str, object]]:
    # Call recorder hooks land with provider attempt persistence.
    return []
