"""Connect-RPC unary and SSE frame helpers."""

from __future__ import annotations

import json
import struct
from dataclasses import dataclass
from enum import Enum

END_STREAM_FLAG = 0x02


class ConnectCode(str, Enum):
    CANCELED = "canceled"
    INVALID_ARGUMENT = "invalid_argument"
    NOT_FOUND = "not_found"
    UNAVAILABLE = "unavailable"
    INTERNAL = "internal"


@dataclass(frozen=True, slots=True)
class ConnectStreamError:
    code: ConnectCode
    message: str


def encode_frame(payload: bytes, *, flags: int = 0) -> bytes:
    return bytes([flags]) + struct.pack(">I", len(payload)) + payload


def encode_message(payload: bytes) -> bytes:
    return encode_frame(payload, flags=0)


def encode_end_stream(payload: bytes | None = None) -> bytes:
    return encode_frame(payload or b"{}", flags=END_STREAM_FLAG)


def encode_error_end_stream(error: ConnectStreamError) -> bytes:
    body = json.dumps(
        {"error": {"code": error.code.value, "message": error.message}},
        separators=(",", ":"),
    ).encode("utf-8")
    return encode_end_stream(body)


def decode_frames(body: bytes) -> list[tuple[int, bytes]]:
    frames: list[tuple[int, bytes]] = []
    offset = 0
    while offset + 5 <= len(body):
        flags = body[offset]
        length = struct.unpack(">I", body[offset + 1 : offset + 5])[0]
        start = offset + 5
        end = start + length
        if end > len(body):
            break
        frames.append((flags, body[start:end]))
        offset = end
    return frames


def decode_unary(body: bytes) -> bytes:
    """Accept Connect-framed or raw protobuf bodies.

    Flag bit 0 means the payload is gzip-compressed. Treating that payload as
    raw protobuf mis-parses and raises ``unsupported wire type``.
    """
    if len(body) >= 5:
        flags = body[0]
        length = struct.unpack(">I", body[1:5])[0]
        if flags & END_STREAM_FLAG == 0 and length == len(body) - 5:
            payload = body[5:]
            if flags & 0x01:
                import gzip

                payload = gzip.decompress(payload)
            return payload
    return body


def is_end_stream_frame(frame: bytes) -> bool:
    return bool(frame) and (frame[0] & END_STREAM_FLAG) != 0
