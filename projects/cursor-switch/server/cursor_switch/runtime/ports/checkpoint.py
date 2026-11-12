"""Checkpoint persistence port."""

from __future__ import annotations

from typing import Protocol

from cursor_switch.runtime.domain.types import ConversationId, Message


class CheckpointPort(Protocol):
    async def save(self, conversation_id: ConversationId, messages: list[Message]) -> None:
        """Persist the stable message prefix for a conversation."""

    async def restore(self, conversation_id: ConversationId) -> list[Message]:
        """Load the last checkpointed messages, or an empty list."""
