"""AvailableModels / GetUsableModels merge: upstream catalog + local models."""

from __future__ import annotations

import struct

import pytest

from cursor_switch.adapters.cursor.connect import encode_message
from cursor_switch.adapters.cursor.services.model_catalog import (
    ModelCatalog,
    encode_available_models,
    merge_catalog_payload,
    resolve_upstream_url,
)
from cursor_switch.adapters.local_access.routing import UPSTREAM_URL_HEADER
from cursor_switch.adapters.persistence.repositories import ModelRecord


def _row(model_id: str = "local-1") -> ModelRecord:
    return ModelRecord(
        id=model_id,
        display_name="Local One",
        provider_type="openai_chat",
        base_url="https://example.invalid/v1",
        api_key="sk-test",
        model_name="gpt-local",
        notes="",
        context_tokens=128000,
        max_output_tokens=8192,
        enabled=True,
        sort_order=1,
        extra={},
        headers={},
    )


def test_merge_catalog_payload_raw() -> None:
    upstream = encode_available_models([])
    # fabricate a minimal upstream name list
    upstream = b"\x0a\x08upstream"
    local = encode_available_models([_row()])
    merged = merge_catalog_payload(upstream, local)
    assert merged.startswith(upstream)
    assert merged.endswith(local)
    assert b"local-1" in merged


def test_merge_catalog_payload_framed() -> None:
    upstream_payload = b"\x0a\x08upstream"
    framed = encode_message(upstream_payload)
    local = b"\x0a\x07local-1"
    merged = merge_catalog_payload(framed, local)
    assert merged[0] == 0
    length = struct.unpack(">I", merged[1:5])[0]
    assert length == len(upstream_payload) + len(local)
    assert merged[5:] == upstream_payload + local


def test_merge_catalog_payload_rejects_compressed() -> None:
    body = bytes([1]) + struct.pack(">I", 3) + b"abc"
    with pytest.raises(ValueError, match="compressed"):
        merge_catalog_payload(body, b"extra")


def test_resolve_upstream_url_uses_stamped_header() -> None:
    url = resolve_upstream_url(
        "/aiserver.v1.AiService/AvailableModels",
        {UPSTREAM_URL_HEADER: "https://api3.cursor.sh/aiserver.v1.AiService/AvailableModels"},
    )
    assert url.startswith("https://api3.cursor.sh/")


def test_resolve_upstream_url_rejects_non_cursor_host() -> None:
    url = resolve_upstream_url(
        "/aiserver.v1.AiService/AvailableModels",
        {UPSTREAM_URL_HEADER: "https://evil.example/aiserver.v1.AiService/AvailableModels"},
    )
    assert url.startswith("https://api2.cursor.sh/")


@pytest.mark.asyncio
async def test_available_models_appends_local_to_upstream() -> None:
    upstream = encode_message(b"\x0a\x08official")

    async def fake_fetch(**_: object) -> bytes:
        return upstream

    async def list_models() -> list[ModelRecord]:
        return [_row("local-abc")]

    catalog = ModelCatalog(list_models, upstream_fetch=fake_fetch)
    body = await catalog.available_models_proto(headers={}, body=b"")
    assert body[0] == 0
    payload = body[5:]
    assert payload.startswith(b"\x0a\x08official")
    assert b"local-abc" in payload


@pytest.mark.asyncio
async def test_available_models_falls_back_when_upstream_missing() -> None:
    async def fake_fetch(**_: object) -> None:
        return None

    async def list_models() -> list[ModelRecord]:
        return [_row("local-only")]

    catalog = ModelCatalog(list_models, upstream_fetch=fake_fetch)
    body = await catalog.available_models_proto()
    assert b"local-only" in body
    assert b"official" not in body
