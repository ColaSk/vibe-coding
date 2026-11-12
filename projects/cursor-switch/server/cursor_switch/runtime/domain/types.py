"""Value objects shared by the session runtime and adapters."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any
from uuid import uuid4


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex}"


type ConversationId = str
type RunId = str


class RunPhase(str, Enum):
    RUNNING = "running"
    FINALIZING = "finalizing"
    ENDED = "ended"


class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"
    SYSTEM = "system"


class ModelEventKind(str, Enum):
    TEXT_DELTA = "text_delta"
    REASONING_DELTA = "reasoning_delta"
    TOOL_CALL = "tool_call"
    USAGE = "usage"
    ERROR = "error"
    END = "end"


@dataclass(frozen=True, slots=True)
class Usage:
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_tokens: int = 0
    cache_write_tokens: int = 0


@dataclass(frozen=True, slots=True)
class Message:
    id: str
    role: MessageRole
    content: str
    tool_call_id: str | None = None


@dataclass(frozen=True, slots=True)
class ToolCall:
    id: str
    name: str
    arguments: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class ToolResult:
    tool_call_id: str
    content: str
    is_error: bool = False


@dataclass(frozen=True, slots=True)
class ModelEvent:
    kind: ModelEventKind
    text: str = ""
    tool_call: ToolCall | None = None
    usage: Usage | None = None
    error: str | None = None
