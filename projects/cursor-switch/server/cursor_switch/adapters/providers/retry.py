"""Retry wrapper for one logical model call."""

from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator, Callable

from cursor_switch.adapters.providers.base import end_event, error_event
from cursor_switch.runtime.domain.types import ModelEvent, ModelEventKind

MAX_MODEL_RETRIES = 8
MODEL_RETRY_DELAY_SECONDS = 5.0


def is_retryable(event: ModelEvent) -> bool:
    if event.kind is not ModelEventKind.ERROR or not event.error:
        return False
    text = event.error.lower()
    return any(
        token in text
        for token in ("timeout", "429", "500", "502", "503", "504", "temporarily", "overload")
    )


def with_retries(
    start: Callable[[], AsyncIterator[ModelEvent]],
    *,
    max_retries: int = MAX_MODEL_RETRIES,
    delay_seconds: float = MODEL_RETRY_DELAY_SECONDS,
) -> AsyncIterator[ModelEvent]:
    async def gen() -> AsyncIterator[ModelEvent]:
        attempt = 0
        while True:
            failed: ModelEvent | None = None
            async for event in start():
                if event.kind is ModelEventKind.ERROR and is_retryable(event):
                    failed = event
                    break
                yield event
                if event.kind in {ModelEventKind.END, ModelEventKind.ERROR}:
                    return
            if failed is None:
                yield end_event()
                return
            if attempt >= max_retries:
                yield failed
                yield end_event()
                return
            attempt += 1
            await asyncio.sleep(delay_seconds)

    return gen()
