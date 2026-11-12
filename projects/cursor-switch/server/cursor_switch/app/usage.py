"""Usage / overview application service (read path)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class OverviewStats:
    model_count: int
    enabled_model_count: int
    call_count: int
    total_input_tokens: int
    total_output_tokens: int
    avg_first_token_ms: float | None


class UsageService:
    def __init__(self, *, model_count: int = 0, enabled_model_count: int = 0) -> None:
        self._model_count = model_count
        self._enabled_model_count = enabled_model_count

    def set_model_counts(self, *, total: int, enabled: int) -> None:
        self._model_count = total
        self._enabled_model_count = enabled

    def overview(self) -> OverviewStats:
        return OverviewStats(
            model_count=self._model_count,
            enabled_model_count=self._enabled_model_count,
            call_count=0,
            total_input_tokens=0,
            total_output_tokens=0,
            avg_first_token_ms=None,
        )
