"""Connectivity test against one provider configuration."""

from __future__ import annotations

import time
from dataclasses import dataclass

from cursor_switch.adapters.providers.base import ProviderConfig
from cursor_switch.adapters.providers.router import build_strategy
from cursor_switch.runtime.domain.types import Message, MessageRole, ModelEventKind, new_id
from cursor_switch.runtime.ports.model import ModelInvocation


@dataclass(slots=True)
class ConnectivityResult:
    ok: bool
    first_token_ms: int | None
    total_ms: int
    text: str
    error: str | None
    usage: dict[str, int] | None


async def test_provider(config: ProviderConfig) -> ConnectivityResult:
    strategy = build_strategy(config)
    started = time.perf_counter()
    first_token_ms: int | None = None
    chunks: list[str] = []
    error: str | None = None
    usage: dict[str, int] | None = None
    invocation = ModelInvocation(
        model_id=config.model_name,
        messages=[
            Message(
                id=new_id("msg"),
                role=MessageRole.USER,
                content="Reply with the single word: pong",
            )
        ],
    )
    try:
        async for event in strategy.stream(invocation):
            if event.kind is ModelEventKind.TEXT_DELTA and event.text:
                if first_token_ms is None:
                    first_token_ms = int((time.perf_counter() - started) * 1000)
                chunks.append(event.text)
            elif event.kind is ModelEventKind.ERROR:
                error = event.error
            elif event.kind is ModelEventKind.USAGE and event.usage is not None:
                usage = {
                    "input_tokens": event.usage.input_tokens,
                    "output_tokens": event.usage.output_tokens,
                    "cache_read_tokens": event.usage.cache_read_tokens,
                    "cache_write_tokens": event.usage.cache_write_tokens,
                }
            elif event.kind is ModelEventKind.END:
                break
    except Exception as exc:  # noqa: BLE001 — connectivity probe must never 500
        error = str(exc) or type(exc).__name__
    total_ms = int((time.perf_counter() - started) * 1000)
    text = "".join(chunks)
    return ConnectivityResult(
        ok=error is None and bool(text),
        first_token_ms=first_token_ms,
        total_ms=total_ms,
        text=text,
        error=error,
        usage=usage,
    )
