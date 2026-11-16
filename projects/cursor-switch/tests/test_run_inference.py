"""RunInference decode + hello frame helpers."""

from __future__ import annotations

from collections.abc import AsyncIterator
from pathlib import Path

import pytest

from cursor_switch.adapters.cursor.agent_ws_frames import (
    HELLO_FRAME,
    decode_client_frame,
    encode_hello_frame,
    encode_run_accepted,
)
from cursor_switch.adapters.cursor.envelope import ClientActionKind, decode_agent_client_message
from cursor_switch.adapters.cursor.proto_min import (
    encode_bool,
    encode_int64,
    encode_message_field,
    encode_string,
    iter_fields,
)
from cursor_switch.adapters.cursor import run_inference as run_inference_mod
from cursor_switch.adapters.cursor.run_inference import (
    decode_run_inference_client_message,
    encode_run_ready,
    encode_text_part,
    is_run_inference_client_message,
)
from cursor_switch.runtime.domain.types import ModelEvent, ModelEventKind, ToolCall
from cursor_switch.runtime.ports.model import ModelInvocation


def _run_inference_run_request(*, conversation_id: str, model_id: str, text: str) -> bytes:
    requested = encode_string(1, model_id) + encode_bool(2, False)
    routing = encode_int64(1, 1) + encode_string(2, text)  # USER + text
    run_request = (
        encode_string(1, conversation_id)
        + encode_message_field(3, requested)
        + encode_message_field(4, routing)
        + encode_string(5, "agent")
    )
    return encode_message_field(1, run_request)


def _invoke_with_parts(*, stable_text: str, user_text: str) -> bytes:
    """Last user message carries text only inside InferenceContentParts."""
    stable = encode_int64(1, 1) + encode_string(2, stable_text)
    text_part = encode_string(1, user_text)
    content_part = encode_message_field(1, text_part)
    parts = encode_message_field(1, content_part)
    latest = encode_int64(1, 1) + encode_message_field(3, parts)
    request = encode_message_field(1, stable) + encode_message_field(1, latest)
    invoke = encode_string(1, "inv-1") + encode_message_field(2, request)
    return encode_message_field(2, invoke)


def test_invoke_reads_user_text_from_parts() -> None:
    raw = _invoke_with_parts(stable_text="x" * 40, user_text="你能帮我做什么")
    item = decode_run_inference_client_message(raw)
    assert item.kind == "invoke_model"
    assert item.messages[-1]["role"] == "user"
    assert item.messages[-1]["content"] == "你能帮我做什么"
    append = decode_agent_client_message(raw, request_id="req-1", seqno=3)
    assert append.action is ClientActionKind.RUN_INFERENCE_INVOKE
    assert append.text == "你能帮我做什么"


def _assistant_with_tool_call(*, call_id: str, name: str, args: dict) -> bytes:
    from cursor_switch.adapters.cursor.run_inference import _encode_struct

    tool_call = (
        encode_string(1, call_id)
        + encode_string(2, name)
        + encode_message_field(3, _encode_struct(args))
    )
    return encode_int64(1, 2) + encode_message_field(4, tool_call)  # ASSISTANT + tool_calls


def _tool_result_message(*, call_id: str, content: str, via: str = "value") -> bytes:
    from cursor_switch.adapters.cursor.run_inference import _encode_protobuf_value

    part = encode_string(1, call_id) + encode_string(2, "Shell")
    if via == "value":
        part += encode_message_field(3, _encode_protobuf_value(content))
    else:
        # experimental_content: repeated InferenceContentPart { text: { text } }
        text_part = encode_string(1, content)
        content_part = encode_message_field(1, text_part)
        part += encode_message_field(5, content_part)
    tool_content = encode_message_field(1, part)
    return encode_int64(1, 3) + encode_message_field(6, tool_content)  # TOOL + tool_content


def test_decode_invoke_preserves_tool_call_history() -> None:
    user = encode_int64(1, 1) + encode_string(2, "读 README")
    assistant = _assistant_with_tool_call(
        call_id="call-abc", name="Read", args={"path": "README.md"}
    )
    tool = _tool_result_message(call_id="call-abc", content="hello from readme")
    request = (
        encode_message_field(1, user)
        + encode_message_field(1, assistant)
        + encode_message_field(1, tool)
        + encode_string(5, "local-model")
    )
    invoke = encode_string(1, "inv-hist") + encode_message_field(2, request)
    raw = encode_message_field(2, invoke)
    item = decode_run_inference_client_message(raw)
    assert [m["role"] for m in item.messages] == ["user", "assistant", "tool"]
    assert item.messages[1]["tool_calls"][0]["id"] == "call-abc"
    assert item.messages[1]["tool_calls"][0]["name"] == "Read"
    assert item.messages[2]["tool_call_id"] == "call-abc"
    assert item.messages[2]["content"] == "hello from readme"
    append = decode_agent_client_message(raw, request_id="req-h", seqno=1)
    assert append.messages[2]["tool_call_id"] == "call-abc"


def test_decode_tool_result_from_experimental_content() -> None:
    tool = _tool_result_message(
        call_id="call-exp", content="README line 1\nline 2", via="experimental"
    )
    request = encode_message_field(1, tool) + encode_string(5, "local-model")
    invoke = encode_string(1, "inv-exp") + encode_message_field(2, request)
    raw = encode_message_field(2, invoke)
    item = decode_run_inference_client_message(raw)
    assert item.messages[0]["role"] == "tool"
    assert item.messages[0]["tool_call_id"] == "call-exp"
    assert "README line 1" in item.messages[0]["content"]


def test_hello_frame_roundtrip() -> None:
    assert encode_hello_frame() == HELLO_FRAME
    assert decode_client_frame(HELLO_FRAME).kind == "hello"


def test_decode_run_inference_run_request() -> None:
    raw = _run_inference_run_request(
        conversation_id="7fe741ff-52e4-405e-adf0-3843ff086577",
        model_id="f3e5cc06bb68477dbaaa6a6a8d1862b7",
        text="测试",
    )
    assert is_run_inference_client_message(raw)
    item = decode_run_inference_client_message(raw)
    assert item.kind == "run_request"
    assert item.model_id == "f3e5cc06bb68477dbaaa6a6a8d1862b7"
    assert item.routing_text == "测试"
    assert item.agent_mode == "agent"

    append = decode_agent_client_message(raw, request_id="req-1", seqno=0)
    assert append.action is ClientActionKind.RUN_INFERENCE_START
    assert append.protocol == "run_inference"
    assert append.text == "测试"
    assert append.model_id == "f3e5cc06bb68477dbaaa6a6a8d1862b7"


def test_decode_captured_bidi_msg_if_present() -> None:
    path = Path("/tmp/cursor-switch-bidi-last-msg.bin")
    if not path.exists() or path.stat().st_size < 32:
        return
    raw = path.read_bytes()
    if not is_run_inference_client_message(raw):
        return
    append = decode_agent_client_message(raw, request_id="live", seqno=0)
    assert append.protocol == "run_inference"
    assert append.action in {
        ClientActionKind.RUN_INFERENCE_START,
        ClientActionKind.RUN_INFERENCE_INVOKE,
        ClientActionKind.RUN_INFERENCE_FINISH,
        ClientActionKind.HEARTBEAT,
        ClientActionKind.UNKNOWN,
    }


def test_encode_run_ready_and_text() -> None:
    ready = encode_run_ready(model_id="m1")
    assert ready.startswith(b"\x12")  # field 2 run_ready
    assert b"anthropic" in ready
    assert b"latest" in ready
    assert b"local" not in ready  # unknown prompt_version → unrecognized-model-family
    # Empty fingerprint so local_loop won't sticky-cache a bad run_ready.
    assert b"cursor-switch" not in ready
    part = encode_text_part(invocation_id="inv-1", text="hi", is_final=False)
    assert b"hi" in part
    assert b"inv-1" in part


def test_encode_run_accepted() -> None:
    from cursor_switch.adapters.cursor.agent_ws_frames import WsRunIdentity

    frame = encode_run_accepted(WsRunIdentity(run_id="r1", request_id="req"))
    assert frame[0] == 0x12  # field 2 run_accepted


def test_encode_tool_call_part_structure() -> None:
    encode_tool_call_part = getattr(run_inference_mod, "encode_tool_call_part", None)
    assert encode_tool_call_part is not None, "encode_tool_call_part missing"
    raw = encode_tool_call_part(
        invocation_id="inv-1",
        tool_call_id="call-1",
        tool_name="Shell",
        args={"command": "echo hi"},
        is_complete=True,
        tool_index=0,
    )
    assert raw.startswith(b"\x1a")  # field 3 invocation_response
    assert b"inv-1" in raw
    assert b"call-1" in raw
    assert b"Shell" in raw
    assert b"echo hi" in raw
    # response.tool_call_part is field 2 inside invocation_response.body.field2
    inv = next(v for f, w, v in iter_fields(raw) if f == 3 and w == 2 and isinstance(v, bytes))
    response = next(v for f, w, v in iter_fields(inv) if f == 2 and w == 2 and isinstance(v, bytes))
    tool_part = next(v for f, w, v in iter_fields(response) if f == 2 and w == 2 and isinstance(v, bytes))
    fields = {f: v for f, w, v in iter_fields(tool_part)}
    assert fields[1] == b"call-1"
    assert fields[2] == b"Shell"


def _invoke_with_tools(*, user_text: str, tools: list[tuple[str, str]]) -> bytes:
    """InferenceStreamRequest with tools advertised by the client."""
    text_part = encode_string(1, user_text)
    content_part = encode_message_field(1, text_part)
    parts = encode_message_field(1, content_part)
    latest = encode_int64(1, 1) + encode_message_field(3, parts)
    tool_msgs = b""
    for name, description in tools:
        # InferenceAgentTool { name, description, parameters=empty Struct }
        tool = encode_string(1, name) + encode_string(2, description) + encode_message_field(3, b"")
        tool_msgs += encode_message_field(2, tool)
    request = encode_message_field(1, latest) + tool_msgs + encode_string(5, "local-model")
    invoke = encode_string(1, "inv-tools") + encode_message_field(2, request)
    return encode_message_field(2, invoke)


def test_decode_invoke_includes_tools() -> None:
    raw = _invoke_with_tools(
        user_text="读取 README",
        tools=[("Shell", "Run a shell command"), ("Read", "Read a file")],
    )
    item = decode_run_inference_client_message(raw)
    assert item.kind == "invoke_model"

    def _tool_name(tool: dict) -> str:
        return str(tool.get("name") or tool.get("function", {}).get("name") or "")

    assert [_tool_name(t) for t in item.tools] == ["Shell", "Read"]
    append = decode_agent_client_message(raw, request_id="req-1", seqno=1)
    assert append.action is ClientActionKind.RUN_INFERENCE_INVOKE
    assert [_tool_name(t) for t in append.tools] == ["Shell", "Read"]


class _RecordingModel:
    def __init__(self, events: list[list[ModelEvent]]) -> None:
        self.invocations: list[ModelInvocation] = []
        self._cycles = list(events)

    def stream(self, invocation: ModelInvocation) -> AsyncIterator[ModelEvent]:
        self.invocations.append(invocation)

        async def gen() -> AsyncIterator[ModelEvent]:
            index = min(len(self.invocations) - 1, len(self._cycles) - 1)
            for event in self._cycles[index]:
                yield event

        return gen()


@pytest.mark.asyncio
async def test_run_inference_dispatch_passes_tools_and_streams_tool_calls() -> None:
    from cursor_switch.adapters.cursor.gateway import CursorGateway
    from cursor_switch.adapters.cursor.proto_min import BidiAppendRequest

    model = _RecordingModel(
        [
            [
                ModelEvent(
                    kind=ModelEventKind.TOOL_CALL,
                    tool_call=ToolCall(
                        id="call-1",
                        name="Shell",
                        arguments={"command": "echo hello-switch"},
                    ),
                ),
                ModelEvent(kind=ModelEventKind.END),
            ]
        ]
    )
    gateway = CursorGateway(model=model, accept_all_models=True)
    handle = await gateway.transport.get_or_create("req-ri-tools")
    queue = handle.subscribe()

    start = _run_inference_run_request(
        conversation_id="conv-ri",
        model_id="local-model",
        text="执行 echo hello-switch",
    )
    await gateway.handle_bidi_append(
        BidiAppendRequest(data=start.hex(), request_id="req-ri-tools", append_seqno=0)
    )
    invoke = _invoke_with_tools(
        user_text="执行 echo hello-switch",
        tools=[("Shell", "Run a shell command")],
    )
    await gateway.handle_bidi_append(
        BidiAppendRequest(data=invoke.hex(), request_id="req-ri-tools", append_seqno=1)
    )

    assert model.invocations, "model was never invoked"
    invocation = model.invocations[-1]
    assert invocation.tools, "run_inference must attach tools to the model"
    assert any(
        (t.get("name") or t.get("function", {}).get("name")) == "Shell" for t in invocation.tools
    )
    assert any(m.role.value == "system" for m in invocation.messages) or any(
        m.role.value == "user" for m in invocation.messages
    )

    payloads: list[bytes] = []
    while True:
        try:
            import asyncio

            chunk = await asyncio.wait_for(queue.get(), timeout=0.5)
        except TimeoutError:
            break
        if chunk is None:
            break
        payloads.append(chunk)

    joined = b"".join(payloads)
    assert b"Shell" in joined
    assert b"hello-switch" in joined
    assert b"call-1" in joined
