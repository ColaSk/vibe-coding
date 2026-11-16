"""ToolPort that asks Cursor to execute tools via ExecServerMessage."""

from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from typing import Any

from cursor_switch.adapters.cursor.pb import agent_v1_pb2 as pb
from cursor_switch.adapters.cursor.protocol.events import tool_call_completed, tool_call_started
from cursor_switch.adapters.cursor.tool_wire import gate_tool_result
from cursor_switch.adapters.cursor.tools.codec.request import (
    encode_exec_request,
    encode_interaction_query,
    is_client_exec_tool,
    is_interaction_tool,
    normalize,
)
from cursor_switch.adapters.cursor.tools.codec.response import decode_exec_result
from cursor_switch.adapters.tools.catalog import AgentMode, tools_for_mode
from cursor_switch.adapters.tools.handlers import EchoHandler, ToolHandler, default_handlers
from cursor_switch.runtime.domain.types import ToolCall, ToolResult

PublishFn = Callable[[pb.AgentServerMessage], Awaitable[None]]


class _PendingHandle:
    def __init__(self, future: asyncio.Future[ToolResult]) -> None:
        self._future = future

    async def result(self) -> ToolResult:
        return await self._future

    async def cancel(self) -> None:
        if not self._future.done():
            self._future.set_exception(asyncio.CancelledError())


class _ImmediateHandle:
    def __init__(self, result: ToolResult) -> None:
        self._result = result

    async def result(self) -> ToolResult:
        return self._result

    async def cancel(self) -> None:
        return None


class ClientExecDispatcher:
    """Dispatch tools to Cursor client-exec, with local fallback handlers."""

    def __init__(
        self,
        *,
        mode: AgentMode = "agent",
        handlers: dict[str, ToolHandler] | None = None,
        publish: PublishFn | None = None,
        conversation_id: str = "",
    ) -> None:
        self._mode = mode
        self._handlers = handlers or default_handlers()
        self._echo = EchoHandler()
        self._allowed = {normalize(n): n for n in tools_for_mode(mode)}
        self._publish = publish
        self._conversation_id = conversation_id
        self._pending: dict[str, asyncio.Future[ToolResult]] = {}
        self._exec_seq = 0

    def set_mode(self, mode: AgentMode) -> None:
        self._mode = mode
        self._allowed = {normalize(n): n for n in tools_for_mode(mode)}

    def set_publish(self, publish: PublishFn | None) -> None:
        self._publish = publish

    def set_conversation_id(self, conversation_id: str) -> None:
        self._conversation_id = conversation_id

    def _allowed_name(self, name: str) -> str | None:
        return self._allowed.get(normalize(name))

    async def dispatch(self, call: ToolCall) -> _PendingHandle | _ImmediateHandle:
        if self._allowed_name(call.name) is None:
            return _ImmediateHandle(
                gate_tool_result(
                    ToolResult(
                        tool_call_id=call.id,
                        content=f"tool '{call.name}' is not available in mode '{self._mode}'",
                        is_error=True,
                    )
                )
            )

        # Local-only tools (search / todos) stay server-side.
        key = normalize(call.name)
        if key in {"todowrite", "updatetodos", "updatecurrentstep", "semblesearch", "semblefindrelated"}:
            handler = self._handlers.get(call.name) or self._handlers.get(self._allowed_name(call.name) or "")
            if handler is None:
                handler = self._echo
            return _ImmediateHandle(gate_tool_result(await handler.run(call)))

        if self._publish is None:
            # Tests / offline: fall back to local handlers (Shell still disabled).
            handler = self._handlers.get(call.name) or self._handlers.get(
                self._allowed_name(call.name) or "", self._echo
            )
            return _ImmediateHandle(gate_tool_result(await handler.run(call)))

        await self._publish(tool_call_started(call))

        if is_client_exec_tool(call.name):
            self._exec_seq += 1
            try:
                request = encode_exec_request(
                    call,
                    exec_id_num=self._exec_seq,
                    conversation_id=self._conversation_id,
                )
            except ValueError as exc:
                return _ImmediateHandle(
                    gate_tool_result(
                        ToolResult(tool_call_id=call.id, content=str(exc), is_error=True)
                    )
                )
            future: asyncio.Future[ToolResult] = asyncio.get_running_loop().create_future()
            self._pending[call.id] = future
            await self._publish(request)
            return _PendingHandle(future)

        if is_interaction_tool(call.name):
            self._exec_seq += 1
            future = asyncio.get_running_loop().create_future()
            self._pending[call.id] = future
            await self._publish(encode_interaction_query(call, query_id=self._exec_seq))
            # Also emit a completed placeholder if client never answers (timeout elsewhere).
            return _PendingHandle(future)

        # Unknown client tool: local echo / handler.
        handler = self._handlers.get(call.name, self._echo)
        result = gate_tool_result(await handler.run(call))
        await self._publish(tool_call_completed(call, content=result.content, is_error=result.is_error))
        return _ImmediateHandle(result)

    async def complete_exec(self, message: pb.ExecClientMessage) -> bool:
        """Resolve a pending tool from an ExecClientMessage. Returns True if matched."""
        exec_id = message.exec_id or ""
        # Also try nested tool_call_id fields.
        if not exec_id:
            kind = message.WhichOneof("message")
            if kind:
                nested = getattr(message, kind)
                exec_id = getattr(nested, "tool_call_id", "") or ""
        future = self._pending.get(exec_id)
        if future is None or future.done():
            # Try any single pending if ids mismatch (lenient).
            if len(self._pending) == 1:
                exec_id, future = next(iter(self._pending.items()))
            else:
                return False
        result = decode_exec_result(message, tool_call_id=exec_id)
        if result is None:
            return True  # stream delta; keep waiting
        self._pending.pop(exec_id, None)
        gated = gate_tool_result(result)
        if self._publish is not None:
            await self._publish(
                tool_call_completed(
                    ToolCall(id=exec_id, name="tool", arguments={}),
                    content=gated.content,
                    is_error=gated.is_error,
                )
            )
        if not future.done():
            future.set_result(gated)
        return True

    def resolve_local(self, tool_call_id: str, result: ToolResult) -> bool:
        future = self._pending.pop(tool_call_id, None)
        if future is None or future.done():
            return False
        future.set_result(gate_tool_result(result))
        return True
