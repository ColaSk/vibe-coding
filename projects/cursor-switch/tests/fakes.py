"""Test doubles for runtime ports."""

from __future__ import annotations

from collections.abc import AsyncIterator

from cursor_switch.runtime.domain.types import (
    ConversationId,
    Message,
    ModelEvent,
    ModelEventKind,
    ToolCall,
    ToolResult,
)
from cursor_switch.runtime.ports.model import ModelInvocation


class FakeModel:
    def __init__(self, events: list[list[ModelEvent]] | None = None) -> None:
        self._cycles = list(events or [[ModelEvent(kind=ModelEventKind.TEXT_DELTA, text="ok"), ModelEvent(kind=ModelEventKind.END)]])
        self.calls = 0

    def stream(self, invocation: ModelInvocation) -> AsyncIterator[ModelEvent]:
        async def gen() -> AsyncIterator[ModelEvent]:
            index = min(self.calls, len(self._cycles) - 1)
            self.calls += 1
            _ = invocation
            for event in self._cycles[index]:
                yield event

        return gen()


class FakeToolHandle:
    def __init__(self, result: ToolResult) -> None:
        self._result = result

    async def result(self) -> ToolResult:
        return self._result

    async def cancel(self) -> None:
        return None


class FakeTools:
    async def dispatch(self, call: ToolCall) -> FakeToolHandle:
        return FakeToolHandle(
            ToolResult(tool_call_id=call.id, content=f"result:{call.name}")
        )


class FakeCheckpoints:
    def __init__(self) -> None:
        self.saved: dict[ConversationId, list[Message]] = {}

    async def save(self, conversation_id: ConversationId, messages: list[Message]) -> None:
        self.saved[conversation_id] = list(messages)

    async def restore(self, conversation_id: ConversationId) -> list[Message]:
        return list(self.saved.get(conversation_id, []))
