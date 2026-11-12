"""Internal Agent append envelope.

Real Cursor BidiAppend `data` is hex-encoded AgentClientMessage protobuf.
Tests may also send hex-encoded JSON of ClientAppend.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from enum import Enum

from cursor_switch.adapters.cursor.proto_min import iter_fields


class ClientActionKind(str, Enum):
    USER_MESSAGE = "user_message"
    INJECT_CONTEXT = "inject_context"
    BACKGROUND_TASK = "background_task"
    BACKGROUND_SHELL = "background_shell"
    BACKGROUND_SUBAGENT = "background_subagent"
    ASYNC_ASK = "async_ask"
    SUBSCRIPTION = "subscription"
    GOAL_CONTINUATION = "goal_continuation"
    CANCEL = "cancel"
    CANCEL_SUBAGENT = "cancel_subagent"
    RESUME = "resume"
    SUMMARIZE = "summarize"
    SHELL_COMMAND = "shell_command"
    START_PLAN = "start_plan"
    EXECUTE_PLAN = "execute_plan"
    HEARTBEAT = "heartbeat"
    RUN_INFERENCE_START = "run_inference_start"
    RUN_INFERENCE_INVOKE = "run_inference_invoke"
    RUN_INFERENCE_FINISH = "run_inference_finish"
    UNKNOWN = "unknown"


@dataclass(frozen=True, slots=True)
class ClientAppend:
    request_id: str
    seqno: int
    conversation_id: str
    model_id: str
    action: ClientActionKind
    text: str = ""
    command_id: str = ""
    target_run_id: str | None = None
    invocation_id: str = ""
    protocol: str = "agent"  # agent | run_inference

    def to_json_bytes(self) -> bytes:
        return json.dumps(
            {
                "request_id": self.request_id,
                "seqno": self.seqno,
                "conversation_id": self.conversation_id,
                "model_id": self.model_id,
                "action": self.action.value,
                "text": self.text,
                "command_id": self.command_id,
                "target_run_id": self.target_run_id,
                "invocation_id": self.invocation_id,
                "protocol": self.protocol,
            },
            separators=(",", ":"),
        ).encode("utf-8")

    def to_hex(self) -> str:
        return self.to_json_bytes().hex()


_ACTION_FIELD = {
    1: ClientActionKind.USER_MESSAGE,
    2: ClientActionKind.RESUME,
    3: ClientActionKind.CANCEL,
    4: ClientActionKind.SUMMARIZE,
    5: ClientActionKind.SHELL_COMMAND,
    6: ClientActionKind.START_PLAN,
    7: ClientActionKind.EXECUTE_PLAN,
    8: ClientActionKind.ASYNC_ASK,
    10: ClientActionKind.CANCEL_SUBAGENT,
    12: ClientActionKind.BACKGROUND_TASK,
    13: ClientActionKind.BACKGROUND_SHELL,
    14: ClientActionKind.BACKGROUND_SUBAGENT,
    16: ClientActionKind.SUBSCRIPTION,
    18: ClientActionKind.GOAL_CONTINUATION,
    19: ClientActionKind.INJECT_CONTEXT,
}


def _field_bytes(data: bytes, field_no: int) -> bytes | None:
    for field, wire, value in iter_fields(data):
        if field == field_no and wire == 2 and isinstance(value, bytes):
            return value
    return None


def _field_string(data: bytes, field_no: int) -> str:
    raw = _field_bytes(data, field_no)
    return raw.decode("utf-8") if raw else ""


def _extract_user_text(user_message_action: bytes) -> str:
    user_message = _field_bytes(user_message_action, 1) or b""
    return _field_string(user_message, 1)


def _decode_conversation_action(
    action_msg: bytes,
    *,
    request_id: str,
    seqno: int,
    model_id: str = "",
    conversation_id: str = "",
) -> ClientAppend:
    action = ClientActionKind.UNKNOWN
    text = ""
    for field, wire, value in iter_fields(action_msg):
        if wire != 2 or not isinstance(value, bytes):
            continue
        mapped = _ACTION_FIELD.get(field)
        if mapped is None:
            continue
        action = mapped
        if field == 1:  # UserMessageAction
            text = _extract_user_text(value)
            # Newer Cursor may put text in text_blob_id (field 18) instead of text.
            if not text:
                user_message = _field_bytes(value, 1) or b""
                if _field_bytes(user_message, 18):
                    text = ""  # blob-backed; still treat as user_message
        break
    return ClientAppend(
        request_id=request_id,
        seqno=seqno,
        conversation_id=conversation_id,
        model_id=model_id,
        action=action,
        text=text,
        command_id=f"cmd-{request_id}-{seqno}",
    )


def _decode_run_request(run_request: bytes, *, request_id: str, seqno: int) -> ClientAppend:
    conversation_id = _field_string(run_request, 5)
    model_id = ""
    requested = _field_bytes(run_request, 9)
    if requested:
        model_id = _field_string(requested, 1)
    if not model_id:
        model_details = _field_bytes(run_request, 3)
        if model_details:
            model_id = _field_string(model_details, 1)

    action_msg = _field_bytes(run_request, 2)  # ConversationAction
    if action_msg:
        return _decode_conversation_action(
            action_msg,
            request_id=request_id,
            seqno=seqno,
            model_id=model_id,
            conversation_id=conversation_id,
        )

    return ClientAppend(
        request_id=request_id,
        seqno=seqno,
        conversation_id=conversation_id,
        model_id=model_id,
        action=ClientActionKind.UNKNOWN,
        text="",
        command_id=f"cmd-{request_id}-{seqno}",
    )


def _decode_run_inference_as_append(
    raw: bytes, *, request_id: str, seqno: int
) -> ClientAppend:
    from cursor_switch.adapters.cursor.run_inference import (
        decode_run_inference_client_message,
    )

    item = decode_run_inference_client_message(raw)
    if item.kind == "run_request":
        text = item.routing_text
        return ClientAppend(
            request_id=request_id,
            seqno=seqno,
            conversation_id=item.conversation_id,
            model_id=item.model_id,
            action=ClientActionKind.RUN_INFERENCE_START,
            text=text,
            command_id=f"cmd-{request_id}-{seqno}",
            protocol="run_inference",
        )
    if item.kind == "invoke_model":
        # Prefer last user message; fall back to concatenated user texts.
        user_texts = [t for role, t in item.messages if role == "user"]
        text = user_texts[-1] if user_texts else "\n".join(t for _, t in item.messages)
        return ClientAppend(
            request_id=request_id,
            seqno=seqno,
            conversation_id=item.conversation_id,
            model_id=item.model_id,
            action=ClientActionKind.RUN_INFERENCE_INVOKE,
            text=text,
            command_id=f"cmd-{request_id}-{seqno}",
            invocation_id=item.invocation_id,
            protocol="run_inference",
        )
    if item.kind == "finish_run":
        return ClientAppend(
            request_id=request_id,
            seqno=seqno,
            conversation_id="",
            model_id="",
            action=ClientActionKind.RUN_INFERENCE_FINISH,
            command_id=f"cmd-{request_id}-{seqno}",
            protocol="run_inference",
        )
    if item.kind == "heartbeat":
        return ClientAppend(
            request_id=request_id,
            seqno=seqno,
            conversation_id="",
            model_id="",
            action=ClientActionKind.HEARTBEAT,
            command_id=f"cmd-{request_id}-{seqno}",
            protocol="run_inference",
        )
    return ClientAppend(
        request_id=request_id,
        seqno=seqno,
        conversation_id="",
        model_id="",
        action=ClientActionKind.UNKNOWN,
        command_id=f"cmd-{request_id}-{seqno}",
        protocol="run_inference",
    )


def decode_agent_client_message(
    raw: bytes, *, request_id: str, seqno: int
) -> ClientAppend:
    """Decode AgentClientMessage or RunInferenceClientMessage into a ClientAppend."""
    from cursor_switch.adapters.cursor.run_inference import is_run_inference_client_message

    if is_run_inference_client_message(raw):
        return _decode_run_inference_as_append(
            raw, request_id=request_id, seqno=seqno
        )

    for field, wire, value in iter_fields(raw):
        if wire != 2 or not isinstance(value, bytes):
            continue
        if field == 1:  # run_request
            return _decode_run_request(value, request_id=request_id, seqno=seqno)
        if field == 4:  # conversation_action (mid-run)
            return _decode_conversation_action(
                value, request_id=request_id, seqno=seqno
            )
        if field == 7:  # client_heartbeat
            return ClientAppend(
                request_id=request_id,
                seqno=seqno,
                conversation_id="",
                model_id="",
                action=ClientActionKind.HEARTBEAT,
                command_id=f"cmd-{request_id}-{seqno}",
            )
        # Exec/KV/interaction frames are acknowledged but ignored for now.
        return ClientAppend(
            request_id=request_id,
            seqno=seqno,
            conversation_id="",
            model_id="",
            action=ClientActionKind.UNKNOWN,
            command_id=f"cmd-{request_id}-{seqno}",
        )
    raise ValueError("BidiAppend contains no AgentClientMessage")


def parse_client_append(*, request_id: str, seqno: int, data_hex: str) -> ClientAppend:
    if not data_hex:
        raise ValueError("BidiAppend data is required")
    try:
        raw = bytes.fromhex(data_hex)
    except ValueError as exc:
        raise ValueError("invalid BidiAppend hex") from exc
    try:
        payload = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return decode_agent_client_message(raw, request_id=request_id, seqno=seqno)
    action_raw = str(payload.get("action") or ClientActionKind.UNKNOWN.value)
    try:
        action = ClientActionKind(action_raw)
    except ValueError:
        action = ClientActionKind.UNKNOWN
    return ClientAppend(
        request_id=str(payload.get("request_id") or request_id),
        seqno=int(payload.get("seqno") or seqno),
        conversation_id=str(payload.get("conversation_id") or ""),
        model_id=str(payload.get("model_id") or ""),
        action=action,
        text=str(payload.get("text") or ""),
        command_id=str(payload.get("command_id") or f"cmd-{request_id}-{seqno}"),
        target_run_id=payload.get("target_run_id"),
        invocation_id=str(payload.get("invocation_id") or ""),
        protocol=str(payload.get("protocol") or "agent"),
    )
