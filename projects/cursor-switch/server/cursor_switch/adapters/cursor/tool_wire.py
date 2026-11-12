"""Tool-call wire codec stubs for Cursor exec / interaction messages."""

from __future__ import annotations

import json
from dataclasses import dataclass

from cursor_switch.runtime.domain.types import ToolCall, ToolResult


@dataclass(frozen=True, slots=True)
class EncodedToolCall:
    tool_call_id: str
    name: str
    arguments_json: str


@dataclass(frozen=True, slots=True)
class EncodedToolResult:
    tool_call_id: str
    content: str
    is_error: bool = False


def encode_tool_call(call: ToolCall) -> EncodedToolCall:
    return EncodedToolCall(
        tool_call_id=call.id,
        name=call.name,
        arguments_json=json.dumps(call.arguments, separators=(",", ":")),
    )


def decode_tool_result(payload: EncodedToolResult) -> ToolResult:
    return ToolResult(
        tool_call_id=payload.tool_call_id,
        content=payload.content,
        is_error=payload.is_error,
    )


def gate_tool_result(result: ToolResult, *, max_chars: int = 200_000) -> ToolResult:
    """Clamp oversized tool output before it re-enters the model loop."""
    if len(result.content) <= max_chars:
        return result
    clipped = result.content[:max_chars] + "\n...[truncated]"
    return ToolResult(
        tool_call_id=result.tool_call_id,
        content=clipped,
        is_error=result.is_error,
    )
