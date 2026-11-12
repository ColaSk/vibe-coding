"""Minimal hand-rolled protobuf codec for BidiAppend / RunSSE envelopes."""

from __future__ import annotations

from dataclasses import dataclass


def _encode_varint(value: int) -> bytes:
    out = bytearray()
    while value > 0x7F:
        out.append((value & 0x7F) | 0x80)
        value >>= 7
    out.append(value & 0x7F)
    return bytes(out)


def _decode_varint(data: bytes, offset: int) -> tuple[int, int]:
    shift = 0
    result = 0
    while True:
        if offset >= len(data):
            raise ValueError("truncated varint")
        byte = data[offset]
        offset += 1
        result |= (byte & 0x7F) << shift
        if byte & 0x80 == 0:
            return result, offset
        shift += 7
        if shift > 70:
            raise ValueError("varint too long")


def _encode_key(field: int, wire: int) -> bytes:
    return _encode_varint((field << 3) | wire)


def encode_string(field: int, value: str) -> bytes:
    raw = value.encode("utf-8")
    return _encode_key(field, 2) + _encode_varint(len(raw)) + raw


def encode_bytes(field: int, value: bytes) -> bytes:
    return _encode_key(field, 2) + _encode_varint(len(value)) + value


def encode_int64(field: int, value: int) -> bytes:
    return _encode_key(field, 0) + _encode_varint(value & ((1 << 64) - 1))


def encode_bool(field: int, value: bool) -> bytes:
    return _encode_key(field, 0) + _encode_varint(1 if value else 0)


def encode_message_field(field: int, payload: bytes) -> bytes:
    return _encode_key(field, 2) + _encode_varint(len(payload)) + payload


def iter_fields(data: bytes) -> list[tuple[int, int, bytes | int]]:
    """Parse protobuf fields; skip fixed32/fixed64 so nested Cursor messages don't abort."""
    fields: list[tuple[int, int, bytes | int]] = []
    offset = 0
    while offset < len(data):
        key, offset = _decode_varint(data, offset)
        field = key >> 3
        wire = key & 0x07
        if wire == 0:
            value, offset = _decode_varint(data, offset)
            fields.append((field, wire, value))
        elif wire == 1:  # 64-bit
            offset += 8
            if offset > len(data):
                raise ValueError("truncated fixed64 field")
        elif wire == 2:
            length, offset = _decode_varint(data, offset)
            end = offset + length
            if end > len(data):
                raise ValueError("truncated length-delimited field")
            fields.append((field, wire, data[offset:end]))
            offset = end
        elif wire == 5:  # 32-bit
            offset += 4
            if offset > len(data):
                raise ValueError("truncated fixed32 field")
        else:
            raise ValueError(f"unsupported wire type {wire}")
    return fields


@dataclass(frozen=True, slots=True)
class BidiAppendRequest:
    data: str = ""
    request_id: str = ""
    append_seqno: int = 0
    data_binary: bytes = b""


@dataclass(frozen=True, slots=True)
class BidiRequestId:
    request_id: str = ""


def encode_bidi_request_id(message: BidiRequestId) -> bytes:
    return encode_string(1, message.request_id) if message.request_id else b""


def decode_bidi_request_id(data: bytes) -> BidiRequestId:
    request_id = ""
    for field, wire, value in iter_fields(data):
        if field == 1 and wire == 2 and isinstance(value, bytes):
            request_id = value.decode("utf-8")
    return BidiRequestId(request_id=request_id)


def encode_bidi_append_request(message: BidiAppendRequest) -> bytes:
    parts = bytearray()
    if message.data:
        parts.extend(encode_string(1, message.data))
    if message.request_id:
        parts.extend(encode_message_field(2, encode_bidi_request_id(BidiRequestId(message.request_id))))
    if message.append_seqno:
        parts.extend(encode_int64(3, message.append_seqno))
    if message.data_binary:
        parts.extend(encode_bytes(4, message.data_binary))
    return bytes(parts)


def decode_bidi_append_request(data: bytes) -> BidiAppendRequest:
    payload = BidiAppendRequest()
    data_text = ""
    request_id = ""
    seqno = 0
    data_binary = b""
    for field, wire, value in iter_fields(data):
        if field == 1 and wire == 2 and isinstance(value, bytes):
            data_text = value.decode("utf-8")
        elif field == 2 and wire == 2 and isinstance(value, bytes):
            request_id = decode_bidi_request_id(value).request_id
        elif field == 3 and wire == 0 and isinstance(value, int):
            seqno = value
        elif field == 4 and wire == 2 and isinstance(value, bytes):
            data_binary = value
    return BidiAppendRequest(
        data=data_text,
        request_id=request_id,
        append_seqno=seqno,
        data_binary=data_binary,
    )


def encode_bidi_append_response() -> bytes:
    return b""
