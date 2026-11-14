"""RunInference (local_loop) protobuf codec for BidiAppend + RunInferenceSSE."""

from __future__ import annotations

from dataclasses import dataclass, field

from cursor_switch.adapters.cursor.proto_min import (
    encode_bool,
    encode_bytes,
    encode_message_field,
    encode_string,
    iter_fields,
)


@dataclass(frozen=True, slots=True)
class RunInferenceAppend:
    kind: str  # run_request | invoke_model | finish_run | heartbeat | other
    conversation_id: str = ""
    model_id: str = ""
    routing_text: str = ""
    agent_mode: str = ""
    invocation_id: str = ""
    messages: list[tuple[str, str]] = field(default_factory=list)  # (role, text)


def _field_bytes(data: bytes, field_no: int) -> bytes | None:
    for field, wire, value in iter_fields(data):
        if field == field_no and wire == 2 and isinstance(value, bytes):
            return value
    return None


def _field_string(data: bytes, field_no: int) -> str:
    raw = _field_bytes(data, field_no)
    return raw.decode("utf-8") if raw else ""


def _decode_requested_model(raw: bytes) -> str:
    return _field_string(raw, 1)


def _decode_routing_text(run_request: bytes) -> str:
    texts: list[str] = []
    for field, wire, value in iter_fields(run_request):
        if field != 4 or wire != 2 or not isinstance(value, bytes):
            continue
        # RunInferenceRoutingMessage { role, text }
        role = None
        text = ""
        for f2, w2, v2 in iter_fields(value):
            if f2 == 1 and w2 == 0 and isinstance(v2, int):
                role = v2
            elif f2 == 2 and w2 == 2 and isinstance(v2, bytes):
                text = v2.decode("utf-8", errors="replace")
        if text and (role is None or role == 1):  # USER
            texts.append(text)
    return "\n".join(texts)


def _decode_text_part(part: bytes) -> str:
    """InferenceContentPart { text: InferenceTextPart { text } }."""
    for field, wire, value in iter_fields(part):
        if field != 1 or wire != 2 or not isinstance(value, bytes):
            continue
        return _field_string(value, 1)
    return ""


def _decode_message_text(message: bytes) -> str:
    """InferenceCoreMessage content oneof: field 2 text, or field 3 parts."""
    direct = _field_string(message, 2)
    if direct:
        return direct
    chunks: list[str] = []
    for field, wire, value in iter_fields(message):
        if field != 3 or wire != 2 or not isinstance(value, bytes):
            continue
        for f2, w2, v2 in iter_fields(value):
            if f2 == 1 and w2 == 2 and isinstance(v2, bytes):
                text = _decode_text_part(v2)
                if text:
                    chunks.append(text)
    return "\n".join(chunks)


def _decode_core_messages(request: bytes) -> list[tuple[str, str]]:
    role_names = {1: "user", 2: "assistant", 3: "tool", 4: "system"}
    out: list[tuple[str, str]] = []
    for field, wire, value in iter_fields(request):
        if field != 1 or wire != 2 or not isinstance(value, bytes):
            continue
        role_num = 0
        for f2, w2, v2 in iter_fields(value):
            if f2 == 1 and w2 == 0 and isinstance(v2, int):
                role_num = v2
                break
        text = _decode_message_text(value)
        if text:
            out.append((role_names.get(role_num, "user"), text))
    return out


def _decode_run_request(run_request: bytes) -> RunInferenceAppend:
    conversation_id = _field_string(run_request, 1)
    model_id = ""
    requested = _field_bytes(run_request, 3)
    if requested:
        model_id = _decode_requested_model(requested)
    return RunInferenceAppend(
        kind="run_request",
        conversation_id=conversation_id,
        model_id=model_id,
        routing_text=_decode_routing_text(run_request),
        agent_mode=_field_string(run_request, 5),
    )


def _decode_invoke_model(invoke: bytes) -> RunInferenceAppend:
    invocation_id = _field_string(invoke, 1)
    request = _field_bytes(invoke, 2) or b""
    model_id = _field_string(request, 5)
    if not model_id:
        requested = _field_bytes(request, 7)
        if requested:
            model_id = _decode_requested_model(requested)
    messages = _decode_core_messages(request)
    return RunInferenceAppend(
        kind="invoke_model",
        conversation_id=_field_string(request, 8),
        model_id=model_id,
        invocation_id=invocation_id or _field_string(request, 6),
        messages=messages,
    )


def is_run_inference_client_message(raw: bytes) -> bool:
    """Detect RunInferenceClientMessage (run_request / invoke_model / …)."""
    fields = {f for f, w, _ in iter_fields(raw) if w == 2}
    # AgentClientMessage uses overlapping field numbers, so also sniff run_request.
    for field, wire, value in iter_fields(raw):
        if field == 1 and wire == 2 and isinstance(value, bytes):
            for f2, w2, v2 in iter_fields(value):
                if f2 == 1 and w2 == 2 and isinstance(v2, bytes):
                    try:
                        text = v2.decode("utf-8")
                    except UnicodeDecodeError:
                        break
                    # RunInferenceRunRequest.conversation_id is a plain UUID string.
                    if len(text) >= 8 and all(32 <= ord(c) < 127 for c in text):
                        return True
                break
        if field == 2 and wire == 2 and isinstance(value, bytes):
            # invoke_model: field1 invocation_id string
            for f2, w2, v2 in iter_fields(value):
                if f2 == 1 and w2 == 2 and isinstance(v2, bytes):
                    try:
                        text = v2.decode("utf-8")
                    except UnicodeDecodeError:
                        break
                    if text:
                        return True
                break
    # Mid-run RI frames without run_request: invoke already handled; finish/heartbeat.
    if 1 not in fields and fields & {4, 5}:
        return True
    return False


def decode_run_inference_client_message(raw: bytes) -> RunInferenceAppend:
    for field, wire, value in iter_fields(raw):
        if wire != 2 or not isinstance(value, bytes):
            continue
        if field == 1:
            return _decode_run_request(value)
        if field == 2:
            return _decode_invoke_model(value)
        if field == 4:
            return RunInferenceAppend(kind="finish_run")
        if field == 5:
            return RunInferenceAppend(kind="heartbeat")
        return RunInferenceAppend(kind="other")
    raise ValueError("empty RunInferenceClientMessage")


def encode_requested_model(model_id: str) -> bytes:
    return encode_string(1, model_id) + encode_bool(2, False) + encode_bool(4, False)


def _encode_agent_mode_config(mode_id: str) -> bytes:
    """RunInferenceAgentModeConfig { mode_id }."""
    return encode_string(1, mode_id)


def encode_prompt_model_metadata(
    *,
    vendor: str = "anthropic",
    prompt_version: str = "latest",
    reasoning_effort: str = "high",
) -> bytes:
    """RunInferencePromptModelMetadata recognized by agent_host_local_loop.

    Mirrors Cursor's pinned `unclassified` defaults closely enough for family
    recognition: vendor+promptVersion must be in the client's allowlists.
    """
    known_vendors = {
        "anthropic",
        "openai",
        "google",
        "xai",
        "zai",
        "cursor",
        "unknown",
    }
    if vendor == "gemini":
        vendor = "google"
    if vendor not in known_vendors:
        vendor = "anthropic"
    known_versions = {
        "dsv3-1018",
        "dsv3-1205",
        "cursor-0226",
        "latest",
        "gpt5-codex",
        "codex-cloud",
        "haiku",
    }
    if prompt_version not in known_versions:
        prompt_version = "latest"
    # Local model path: Claude 4.x prompt. Never set use_dsv3_harness.
    parts = bytearray()
    parts.extend(encode_string(1, vendor))
    parts.extend(encode_string(2, prompt_version))
    parts.extend(encode_bool(16, True))  # is_claude_4x
    parts.extend(encode_bool(31, False))  # use_dsv3_harness
    parts.extend(encode_bool(40, True))  # supports_assistant_message_prefill
    parts.extend(encode_bool(41, True))  # enable_line_numbers
    parts.extend(encode_string(30, reasoning_effort))
    parts.extend(encode_string(35, "anonymous"))  # persona
    parts.extend(encode_string(44, "Claude"))  # self_identity_name
    parts.extend(encode_bool(45, False))  # dsv3_is_thinking
    parts.extend(encode_bool(52, True))  # enable_semantic_search
    for mode_id in ("agent", "chat", "plan", "debug", "triage", "multitask"):
        parts.extend(encode_message_field(46, _encode_agent_mode_config(mode_id)))
    return bytes(parts)


def encode_run_ready(
    *,
    model_id: str,
    vendor: str = "anthropic",
    prompt_version: str = "latest",
    reasoning_effort: str = "high",
) -> bytes:
    """RunInferenceServerMessage { run_ready: { resolved_model, prompt_model_metadata, ... } }.

    Leave config_fingerprint empty on purpose. A non-empty fingerprint makes
    agent_host cache run_ready and re-use it via speculationArm=speculate on
    later turns — sticky failures if an older bad metadata blob was cached
    (e.g. prompt_version=local). Empty fingerprint disables that cache arm so
    each attempt waits for the live run_ready we just encoded.
    """
    ready = (
        encode_message_field(1, encode_requested_model(model_id))
        + encode_message_field(
            4,
            encode_prompt_model_metadata(
                vendor=vendor,
                prompt_version=prompt_version,
                reasoning_effort=reasoning_effort,
            ),
        )
        + encode_bool(7, True)  # accepts_client_heartbeat
        + encode_bool(8, True)  # accepts_agent_events
        + encode_bool(13, True)  # accepts_aborted_finish
        # field 17 config_fingerprint intentionally omitted (see docstring)
    )
    return encode_message_field(2, ready)


def encode_text_part(*, invocation_id: str, text: str, is_final: bool = False) -> bytes:
    """RunInferenceServerMessage { invocation_response: { id, response: { text_part } } }."""
    text_part = encode_string(1, text) + encode_bool(2, is_final)
    response = encode_message_field(1, text_part)
    body = encode_string(1, invocation_id) + encode_message_field(2, response)
    return encode_message_field(3, body)


def encode_invocation_end(*, invocation_id: str) -> bytes:
    """RunInferenceServerMessage { invocation_end: { invocation_id } }."""
    end = encode_string(1, invocation_id)
    return encode_message_field(4, end)


def encode_heartbeat() -> bytes:
    """RunInferenceServerMessage { heartbeat: {} }."""
    return encode_message_field(1, b"")
