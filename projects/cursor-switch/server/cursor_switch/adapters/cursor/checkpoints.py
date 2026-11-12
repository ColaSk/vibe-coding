"""In-memory CheckpointPort used by the gateway until persistence wiring lands."""

from __future__ import annotations

from cursor_switch.runtime.domain.types import ConversationId, Message


class MemoryCheckpoints:
    def __init__(self) -> None:
        self._saved: dict[ConversationId, list[Message]] = {}

    async def save(self, conversation_id: ConversationId, messages: list[Message]) -> None:
        self._saved[conversation_id] = list(messages)

    async def restore(self, conversation_id: ConversationId) -> list[Message]:
        return list(self._saved.get(conversation_id, []))
