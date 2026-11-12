"""Strategy router implementing ModelPort."""

from __future__ import annotations

from collections.abc import AsyncIterator, Callable
from typing import Any, Protocol

from cursor_switch.adapters.providers.anthropic import AnthropicMessagesStrategy
from cursor_switch.adapters.providers.base import ProviderConfig
from cursor_switch.adapters.providers.openai_chat import OpenAiChatStrategy
from cursor_switch.adapters.providers.openai_responses import OpenAiResponsesStrategy
from cursor_switch.adapters.providers.retry import with_retries
from cursor_switch.runtime.domain.types import ModelEvent
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
    ) -> None:
        self._lookup = lookup

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
            try:
                async for event in with_retries(lambda: strategy.stream(invocation)):
                    yield event
            except Exception as exc:  # noqa: BLE001 — keep agent SSE from hanging on transport errors
                yield error_event(str(exc) or type(exc).__name__)
                yield end_event()

        return guarded()
