"""Model streaming port."""

from __future__ import annotations

from collections.abc import AsyncIterator
from dataclasses import dataclass, field
from typing import Any, Protocol

from cursor_switch.runtime.domain.types import Message, ModelEvent


@dataclass(frozen=True, slots=True)
class ModelInvocation:
    model_id: str
    messages: list[Message]
    tools: list[dict[str, Any]] = field(default_factory=list)
    extra: dict[str, Any] = field(default_factory=dict)


class ModelPort(Protocol):
    def stream(self, invocation: ModelInvocation) -> AsyncIterator[ModelEvent]:
        """Yield normalized model events until END or ERROR."""
