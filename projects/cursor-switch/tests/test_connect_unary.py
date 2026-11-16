"""Connect-RPC unary body decoding, including gzip envelopes."""

from __future__ import annotations

import gzip
import struct

from cursor_switch.adapters.cursor.connect import decode_unary, encode_message
from cursor_switch.adapters.cursor.proto_min import (
    encode_bidi_append_request,
    encode_string,
    BidiAppendRequest,
    decode_bidi_append_request,
)


def test_decode_unary_raw_protobuf() -> None:
    payload = encode_string(1, "hello")
    assert decode_unary(payload) == payload


def test_decode_unary_connect_frame() -> None:
    payload = encode_string(1, "hello")
    assert decode_unary(encode_message(payload)) == payload


def test_decode_unary_connect_gzip_flag() -> None:
    payload = encode_string(1, "gzipped-via-flag")
    compressed = gzip.compress(payload)
    framed = bytes([0x01]) + struct.pack(">I", len(compressed)) + compressed
    assert decode_unary(framed) == payload


def test_decode_unary_raw_gzip_body() -> None:
    """Cursor sometimes posts a bare gzip body (no Connect envelope)."""
    payload = encode_bidi_append_request(
        BidiAppendRequest(data="deadbeef", request_id="req-gz", append_seqno=3)
    )
    body = gzip.compress(payload)
    assert body.startswith(b"\x1f\x8b")
    raw = decode_unary(body)
    decoded = decode_bidi_append_request(raw)
    assert decoded.request_id == "req-gz"
    assert decoded.append_seqno == 3
    assert decoded.data == "deadbeef"
