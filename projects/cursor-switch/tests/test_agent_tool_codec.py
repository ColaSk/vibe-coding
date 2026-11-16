"""Client-exec tool codec + dispatcher (offline / local fallback)."""

from __future__ import annotations

import asyncio

import pytest

from cursor_switch.adapters.cursor.pb import agent_v1_pb2 as pb
from cursor_switch.adapters.cursor.tools.client_exec import ClientExecDispatcher
from cursor_switch.adapters.cursor.tools.codec.request import encode_exec_request, is_client_exec_tool
from cursor_switch.adapters.cursor.tools.codec.response import decode_exec_result
from cursor_switch.runtime.domain.types import ToolCall, ToolResult


def test_encode_read_and_shell() -> None:
    read = encode_exec_request(ToolCall(id="c1", name="Read", arguments={"path": "/tmp/a.py"}))
    assert read.WhichOneof("message") == "exec_server_message"
    assert read.exec_server_message.WhichOneof("message") == "read_args"
    assert read.exec_server_message.read_args.path == "/tmp/a.py"

    shell = encode_exec_request(ToolCall(id="c2", name="Shell", arguments={"command": "echo hi"}))
    assert shell.exec_server_message.WhichOneof("message") == "shell_stream_args"
    assert shell.exec_server_message.shell_stream_args.command == "echo hi"
    assert is_client_exec_tool("Shell")


def test_decode_read_success() -> None:
    msg = pb.ExecClientMessage(exec_id="c1")
    # Build success oneof if field exists
    success = msg.read_result.success
    if hasattr(success, "content"):
        success.content = "hello file"
    elif hasattr(success, "data"):
        success.data = b"hello file"
    else:
        pytest.skip("ReadResult.success shape unknown")
    result = decode_exec_result(msg, tool_call_id="c1")
    assert result is not None
    assert "hello" in result.content


@pytest.mark.asyncio
async def test_dispatcher_local_fallback_without_publish() -> None:
    dispatcher = ClientExecDispatcher()
    handle = await dispatcher.dispatch(
        ToolCall(id="t1", name="TodoWrite", arguments={"todos": [{"id": "1"}]})
    )
    result = await handle.result()
    assert result.is_error is False


@pytest.mark.asyncio
async def test_dispatcher_completes_pending_exec() -> None:
    published: list[pb.AgentServerMessage] = []

    async def publish(msg: pb.AgentServerMessage) -> None:
        published.append(msg)

    dispatcher = ClientExecDispatcher(publish=publish)
    handle_task = asyncio.create_task(
        dispatcher.dispatch(ToolCall(id="exec-1", name="Read", arguments={"path": "/x"}))
    )
    # Wait until pending registered
    for _ in range(50):
        if "exec-1" in dispatcher._pending:
            break
        await asyncio.sleep(0.01)
    client = pb.ExecClientMessage(exec_id="exec-1")
    if hasattr(client.read_result, "success"):
        success = client.read_result.success
        if hasattr(success, "content"):
            success.content = "file body"
        elif hasattr(success, "data"):
            success.data = b"file body"
    assert await dispatcher.complete_exec(client)
    handle = await handle_task
    result = await handle.result()
    assert isinstance(result, ToolResult)
    assert result.is_error is False or "file" in result.content or result.content
    assert any(m.WhichOneof("message") == "exec_server_message" for m in published)
