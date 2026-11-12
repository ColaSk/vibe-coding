"""Commands accepted by the conversation runtime."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from cursor_switch.runtime.domain.types import Message, RunId, ToolResult


class CommandResult(str, Enum):
    APPLIED = "applied"
    DUPLICATE = "duplicate"
    RUN_CLOSING = "run_closing"
    RUN_ENDED = "run_ended"
    STALE_TARGET = "stale_target"


@dataclass(frozen=True, slots=True)
class InsertMessages:
    messages: list[Message]
    command_id: str
    target_run_id: RunId | None = None


@dataclass(frozen=True, slots=True)
class BreakMessages:
    messages: list[Message]
    command_id: str
    target_run_id: RunId | None = None


@dataclass(frozen=True, slots=True)
class ToolResultCommand:
    result: ToolResult
    command_id: str
    target_run_id: RunId | None = None


@dataclass(frozen=True, slots=True)
class Cancel:
    command_id: str
    target_run_id: RunId | None = None


type RunCommand = InsertMessages | BreakMessages | ToolResultCommand | Cancel
