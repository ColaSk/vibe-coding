"""RunInference decode + hello frame helpers."""

from __future__ import annotations

from pathlib import Path

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
)
from cursor_switch.adapters.cursor.run_inference import (
    decode_run_inference_client_message,
    encode_run_ready,
    encode_text_part,
    is_run_inference_client_message,
)


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
    assert item.messages[-1] == ("user", "你能帮我做什么")
    append = decode_agent_client_message(raw, request_id="req-1", seqno=3)
    assert append.action is ClientActionKind.RUN_INFERENCE_INVOKE
    assert append.text == "你能帮我做什么"


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
