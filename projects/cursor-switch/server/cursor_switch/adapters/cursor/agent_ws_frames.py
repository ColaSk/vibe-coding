"""Agent / RunInference WebSocket framing (shared AgentWebSocket* protos)."""

from __future__ import annotations

from dataclasses import dataclass

from cursor_switch.adapters.cursor.proto_min import (
    encode_int64,
    encode_message_field,
    encode_string,
    iter_fields,
)

# AgentWebSocketHello { protocol_version = V1 }
HELLO_FRAME = bytes.fromhex("0a020801")


@dataclass(frozen=True, slots=True)
class WsRunIdentity:
    run_id: str = ""
    request_id: str = ""


@dataclass(frozen=True, slots=True)
class WsClientFrame:
    kind: str  # hello | run_start | client_message | half_close | cancel_run
    identity: WsRunIdentity | None = None
    run_id: str = ""
    sequence: int = 0
    message: bytes = b""


def encode_hello_frame() -> bytes:
    return HELLO_FRAME


def encode_run_identity(identity: WsRunIdentity) -> bytes:
    parts = bytearray()
    if identity.run_id:
        parts.extend(encode_string(1, identity.run_id))
    if identity.request_id:
        parts.extend(encode_string(2, identity.request_id))
    return bytes(parts)


def encode_run_accepted(identity: WsRunIdentity) -> bytes:
    """AgentWebSocketServerFrame { run_accepted: { identity } }."""
    accepted = encode_message_field(1, encode_run_identity(identity))
    return encode_message_field(2, accepted)


def encode_server_message(*, run_id: str, sequence: int, message: bytes) -> bytes:
    """AgentWebSocketServerFrame { server_message: { run_id, sequence, message } }."""
    from cursor_switch.adapters.cursor.proto_min import encode_bytes

    body = encode_string(1, run_id) + encode_int64(2, sequence) + encode_bytes(3, message)
    return encode_message_field(3, body)


def encode_run_end(identity: WsRunIdentity) -> bytes:
    """AgentWebSocketServerFrame { run_end: { identity } }."""
    end = encode_message_field(1, encode_run_identity(identity))
    return encode_message_field(4, end)


def _decode_identity(raw: bytes) -> WsRunIdentity:
    run_id = ""
    request_id = ""
    for field, wire, value in iter_fields(raw):
        if wire != 2 or not isinstance(value, bytes):
            continue
        if field == 1:
            run_id = value.decode("utf-8", errors="replace")
        elif field == 2:
            request_id = value.decode("utf-8", errors="replace")
    return WsRunIdentity(run_id=run_id, request_id=request_id)


def decode_client_frame(raw: bytes) -> WsClientFrame:
    for field, wire, value in iter_fields(raw):
        if wire != 2 or not isinstance(value, bytes):
            continue
        if field == 1:  # hello
            return WsClientFrame(kind="hello")
        if field == 2:  # run_start
            identity = WsRunIdentity()
            for f2, w2, v2 in iter_fields(value):
                if f2 == 1 and w2 == 2 and isinstance(v2, bytes):
                    identity = _decode_identity(v2)
            return WsClientFrame(kind="run_start", identity=identity)
        if field == 3:  # client_message
            run_id = ""
            sequence = 0
            message = b""
            for f2, w2, v2 in iter_fields(value):
                if f2 == 1 and w2 == 2 and isinstance(v2, bytes):
                    run_id = v2.decode("utf-8", errors="replace")
                elif f2 == 2 and w2 == 0 and isinstance(v2, int):
                    sequence = v2
                elif f2 == 3 and w2 == 2 and isinstance(v2, bytes):
                    message = v2
            return WsClientFrame(
                kind="client_message",
                run_id=run_id,
                sequence=sequence,
                message=message,
            )
        if field == 4:
            run_id = ""
            for f2, w2, v2 in iter_fields(value):
                if f2 == 1 and w2 == 2 and isinstance(v2, bytes):
                    run_id = v2.decode("utf-8", errors="replace")
            return WsClientFrame(kind="half_close", run_id=run_id)
        if field == 5:
            run_id = ""
            for f2, w2, v2 in iter_fields(value):
                if f2 == 1 and w2 == 2 and isinstance(v2, bytes):
                    run_id = v2.decode("utf-8", errors="replace")
            return WsClientFrame(kind="cancel_run", run_id=run_id)
    return WsClientFrame(kind="unknown")
