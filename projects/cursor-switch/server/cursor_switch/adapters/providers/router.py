"""Strategy router implementing ModelPort."""

from __future__ import annotations

import time
from collections.abc import AsyncIterator, Awaitable, Callable
from typing import Any, Protocol

from cursor_switch.adapters.providers.anthropic import AnthropicMessagesStrategy
from cursor_switch.adapters.providers.base import ProviderConfig
from cursor_switch.adapters.providers.openai_chat import OpenAiChatStrategy
from cursor_switch.adapters.providers.openai_responses import OpenAiResponsesStrategy
from cursor_switch.adapters.providers.retry import with_retries
from cursor_switch.runtime.domain.types import ModelEvent, ModelEventKind, Usage
from cursor_switch.runtime.ports.model import ModelInvocation, ModelPort


class Strategy(Protocol):
    def stream(self, invocation: ModelInvocation) -> AsyncIterator[ModelEvent]: ...


def build_strategy(config: ProviderConfig) -> Strategy:
    if config.provider_type == "openai_chat":
        return OpenAiChatStrategy(config)
    if config.provider_type == "openai_responses":
        return OpenAiResponsesStrategy(config)
    if config.provider_type == "anthropic":
        return AnthropicMessagesStrategy(config)
    raise ValueError(f"unsupported provider_type: {config.provider_type}")


class ProviderRouter(ModelPort):
    """Looks up provider config by model id, then streams via the matching strategy."""

    def __init__(
        self,
        lookup: Callable[[str], ProviderConfig | None],
        on_finished: Callable[..., Awaitable[None]] | None = None,
    ) -> None:
        self._lookup = lookup
        self._on_finished = on_finished

    def stream(self, invocation: ModelInvocation) -> AsyncIterator[ModelEvent]:
        from cursor_switch.adapters.providers.base import end_event, error_event

        config = self._lookup(invocation.model_id)
        if config is None:

            async def missing() -> AsyncIterator[ModelEvent]:
                yield error_event(f"unknown model id: {invocation.model_id}")
                yield end_event()

            return missing()
        strategy = build_strategy(config)

        async def guarded() -> AsyncIterator[ModelEvent]:
            started = time.perf_counter()
            first_ms: int | None = None
            usage = Usage()
            error: str | None = None
            text: list[str] = []
            try:
                async for event in with_retries(lambda: strategy.stream(invocation)):
                    if event.kind is ModelEventKind.TEXT_DELTA and event.text:
                        if first_ms is None:
                            first_ms = int((time.perf_counter() - started) * 1000)
                        text.append(event.text)
                    elif event.kind is ModelEventKind.USAGE and event.usage is not None:
                        usage = event.usage
                    elif event.kind is ModelEventKind.ERROR:
                        error = event.error or "error"
                    yield event
            except Exception as exc:  # noqa: BLE001 — keep agent SSE from hanging on transport errors
                error = str(exc) or type(exc).__name__
                yield error_event(error)
                yield end_event()
            if self._on_finished is not None:
                try:
                    await self._on_finished(
                        model_id=invocation.model_id,
                        status="error" if error else "ok",
                        first_token_ms=first_ms,
                        duration_ms=int((time.perf_counter() - started) * 1000),
                        input_tokens=usage.input_tokens,
                        output_tokens=usage.output_tokens,
                        cache_read_tokens=usage.cache_read_tokens,
                        cache_write_tokens=usage.cache_write_tokens,
                        error_message=error or "",
                        response_text="".join(text),
                    )
                except Exception:
                    pass

        return guarded()
