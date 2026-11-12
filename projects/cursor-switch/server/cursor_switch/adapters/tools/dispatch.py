"""ToolPort implementation that dispatches by tool name."""

from __future__ import annotations

from cursor_switch.adapters.cursor.tool_wire import gate_tool_result
from cursor_switch.adapters.tools.catalog import AgentMode, tools_for_mode
from cursor_switch.adapters.tools.handlers import EchoHandler, ToolHandler, default_handlers
from cursor_switch.runtime.domain.types import ToolCall, ToolResult


class _Handle:
    def __init__(self, result: ToolResult) -> None:
        self._result = result

    async def result(self) -> ToolResult:
        return self._result

    async def cancel(self) -> None:
        return None


class ToolDispatcher:
    def __init__(
        self,
        *,
        mode: AgentMode = "agent",
        handlers: dict[str, ToolHandler] | None = None,
    ) -> None:
        self._mode = mode
        self._handlers = handlers or default_handlers()
        self._echo = EchoHandler()
        self._allowed = set(tools_for_mode(mode))

    def set_mode(self, mode: AgentMode) -> None:
        self._mode = mode
        self._allowed = set(tools_for_mode(mode))

    async def dispatch(self, call: ToolCall) -> _Handle:
        if call.name not in self._allowed:
            result = ToolResult(
                tool_call_id=call.id,
                content=f"tool '{call.name}' is not available in mode '{self._mode}'",
                is_error=True,
            )
            return _Handle(gate_tool_result(result))
        handler = self._handlers.get(call.name, self._echo)
        raw = await handler.run(call)
        return _Handle(gate_tool_result(raw))
