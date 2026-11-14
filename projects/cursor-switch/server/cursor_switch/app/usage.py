"""Usage / overview application service."""

from __future__ import annotations

from dataclasses import dataclass

from cursor_switch.adapters.persistence.repositories import CallRecord
from cursor_switch.adapters.persistence.unit_of_work import UnitOfWorkFactory

MINUTE_MS = 60_000
HOUR_MS = 60 * MINUTE_MS
DAY_MS = 24 * HOUR_MS


def granularity_for(start_ms: int, end_ms: int) -> tuple[str, int]:
    span = max(0, end_ms - start_ms)
    if span <= 2 * HOUR_MS:
        return "minute", MINUTE_MS
    if span <= 2 * DAY_MS:
        return "hour", HOUR_MS
    return "day", DAY_MS


DEFAULT_PRICING: dict[str, float] = {
    "input_per_million": 5.0,
    "output_per_million": 25.0,
    "cache_read_per_million": 0.5,
    "cache_write_per_million": 6.25,
}


def resolve_pricing(
    extra: dict[str, object] | None,
    fallback: dict[str, float] | None = None,
) -> dict[str, float]:
    base = dict(fallback or DEFAULT_PRICING)
    src = extra or {}
    out: dict[str, float] = {}
    for key, default in base.items():
        raw = src.get(key, default)
        try:
            value = float(raw)  # type: ignore[arg-type]
        except (TypeError, ValueError):
            value = default
        out[key] = value if value >= 0 else default
    return out


def estimate_call_value(
    *,
    input_tokens: int,
    output_tokens: int,
    cache_read_tokens: int,
    cache_write_tokens: int,
    pricing: dict[str, float],
) -> tuple[float, float]:
    cache = (
        cache_read_tokens * pricing.get("cache_read_per_million", 0) / 1_000_000
        + cache_write_tokens * pricing.get("cache_write_per_million", 0) / 1_000_000
    )
    total = (
        input_tokens * pricing.get("input_per_million", 0) / 1_000_000
        + output_tokens * pricing.get("output_per_million", 0) / 1_000_000
        + cache
    )
    return total, cache


@dataclass(frozen=True, slots=True)
class OverviewStats:
    model_count: int
    enabled_model_count: int
    call_count: int
    total_input_tokens: int
    total_output_tokens: int
    avg_first_token_ms: float | None
    granularity: str
    series: list[dict[str, int]]
    estimated_value: float
    estimated_cache_value: float
    successful_calls: int
    failed_calls: int
    cache_read_tokens: int
    cache_write_tokens: int


class UsageService:
    def __init__(self, uow_factory: UnitOfWorkFactory | None = None) -> None:
        self._uow_factory = uow_factory
        self._model_count = 0
        self._enabled_model_count = 0

    def set_model_counts(self, *, total: int, enabled: int) -> None:
        self._model_count = total
        self._enabled_model_count = enabled

    async def record(self, record: CallRecord) -> CallRecord:
        if self._uow_factory is None:
            return record
        async with self._uow_factory.begin() as uow:
            return await uow.calls.add(record)

    async def list_calls(self, limit: int = 200) -> list[dict[str, object]]:
        if self._uow_factory is None:
            return []
        async with self._uow_factory.begin() as uow:
            rows = await uow.calls.list_recent(limit)
            return [row.summary() for row in rows]

    async def get_call(self, call_id: str) -> dict[str, object] | None:
        if self._uow_factory is None:
            return None
        async with self._uow_factory.begin() as uow:
            row = await uow.calls.get(call_id)
            return None if row is None else row.detail()

    async def storage(self) -> dict[str, int]:
        if self._uow_factory is None:
            return {"call_count": 0, "trace_count": 0}
        async with self._uow_factory.begin() as uow:
            calls, traces = await uow.calls.counts()
            return {"call_count": calls, "trace_count": traces}

    async def clear(self, scope: str) -> dict[str, int]:
        if self._uow_factory is None:
            return {"call_count": 0, "trace_count": 0}
        async with self._uow_factory.begin() as uow:
            await uow.calls.clear(scope)
        return await self.storage()

    async def overview(
        self,
        *,
        start_ms: int,
        end_ms: int,
        model_ids: list[str] | None,
        pricing_by_model: dict[str, dict[str, float]],
        fallback_pricing: dict[str, float] | None = None,
    ) -> OverviewStats:
        rows: list[CallRecord] = []
        if self._uow_factory is not None:
            async with self._uow_factory.begin() as uow:
                rows = await uow.calls.between(start_ms, end_ms, model_ids)
        name, size = granularity_for(start_ms, end_ms)
        buckets: dict[int, dict[str, int]] = {}
        first_tokens: list[int] = []
        failed = 0
        value = 0.0
        cache_value = 0.0
        fallback = fallback_pricing or DEFAULT_PRICING
        for row in rows:
            bucket = row.created_at_ms - (row.created_at_ms % size)
            slot = buckets.setdefault(
                bucket,
                {
                    "bucket_start_ms": bucket,
                    "input_tokens": 0,
                    "output_tokens": 0,
                    "cache_read_tokens": 0,
                    "cache_write_tokens": 0,
                    "first_token_sum": 0,
                    "first_token_count": 0,
                    "calls": 0,
                },
            )
            slot["input_tokens"] += row.input_tokens
            slot["output_tokens"] += row.output_tokens
            slot["cache_read_tokens"] += row.cache_read_tokens
            slot["cache_write_tokens"] += row.cache_write_tokens
            slot["calls"] += 1
            if row.first_token_ms is not None:
                slot["first_token_sum"] += row.first_token_ms
                slot["first_token_count"] += 1
                first_tokens.append(row.first_token_ms)
            if row.status != "ok":
                failed += 1
            pricing = pricing_by_model.get(row.model_id) or fallback
            call_value, call_cache = estimate_call_value(
                input_tokens=row.input_tokens,
                output_tokens=row.output_tokens,
                cache_read_tokens=row.cache_read_tokens,
                cache_write_tokens=row.cache_write_tokens,
                pricing=pricing,
            )
            value += call_value
            cache_value += call_cache
        input_tokens = sum(row.input_tokens for row in rows)
        output_tokens = sum(row.output_tokens for row in rows)
        cache_read = sum(row.cache_read_tokens for row in rows)
        cache_write = sum(row.cache_write_tokens for row in rows)
        return OverviewStats(
            model_count=self._model_count,
            enabled_model_count=self._enabled_model_count,
            call_count=len(rows),
            total_input_tokens=input_tokens,
            total_output_tokens=output_tokens,
            avg_first_token_ms=(sum(first_tokens) / len(first_tokens)) if first_tokens else None,
            granularity=name,
            series=[buckets[key] for key in sorted(buckets)],
            estimated_value=value,
            estimated_cache_value=cache_value,
            successful_calls=len(rows) - failed,
            failed_calls=failed,
            cache_read_tokens=cache_read,
            cache_write_tokens=cache_write,
        )
