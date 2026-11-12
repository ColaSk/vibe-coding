"""Placeholder ToolPort until Phase 6 adapters land."""

from __future__ import annotations

from cursor_switch.runtime.domain.types import ToolCall, ToolResult


class _ImmediateHandle:
    def __init__(self, result: ToolResult) -> None:
        self._result = result

    async def result(self) -> ToolResult:
        return self._result

    async def cancel(self) -> None:
        return None


class NullTools:
    async def dispatch(self, call: ToolCall) -> _ImmediateHandle:
        return _ImmediateHandle(
            ToolResult(
                tool_call_id=call.id,
                content=f"tool '{call.name}' is not implemented yet",
                is_error=True,
            )
        )
