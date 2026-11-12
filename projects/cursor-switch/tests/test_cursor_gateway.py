"""Cursor gateway: BidiAppend → runtime → RunSSE."""

from __future__ import annotations

import json
from pathlib import Path

from fastapi.testclient import TestClient

from cursor_switch.adapters.cursor.connect import decode_frames
from cursor_switch.adapters.cursor.envelope import ClientActionKind, ClientAppend
from cursor_switch.adapters.cursor.proto_min import (
    BidiAppendRequest,
    BidiRequestId,
    encode_bidi_append_request,
    encode_bidi_request_id,
)
from cursor_switch.adapters.cursor.connect import encode_message
from cursor_switch.adapters.cursor.compile import MessageDelivery, delivery_for
from cursor_switch.control.app import create_app
from tests.fakes import FakeModel


def test_delivery_mapping() -> None:
    assert delivery_for(ClientActionKind.USER_MESSAGE) is MessageDelivery.BREAK
    assert delivery_for(ClientActionKind.BACKGROUND_TASK) is MessageDelivery.INSERT
    assert delivery_for(ClientActionKind.CANCEL) is MessageDelivery.CANCEL
    assert delivery_for(ClientActionKind.SUMMARIZE) is MessageDelivery.IGNORE


def test_local_model_id_accepts_variant_suffixes() -> None:
    from cursor_switch.adapters.cursor.gateway import CursorGateway, normalize_model_id

    model_id = "f3e5cc06bb68477dbaaa6a6a8d1862b7"
    gateway = CursorGateway(known_model_ids=lambda: {model_id})
    assert normalize_model_id(f"{model_id}[context=200k,reasoning=high,fast=false]") == model_id
    assert gateway.is_local_model(model_id)
    assert gateway.is_local_model(f"{model_id}[context=200k,reasoning=high,fast=false]")
    assert gateway.is_local_model(f"{model_id}-200k-high")
    assert gateway.resolve_local_model_id(f"{model_id}-200k-high-fast") == model_id
    assert not gateway.is_local_model("default")
    assert not gateway.is_local_model("auto")


def test_bidi_append_streams_model_events(tmp_path: Path) -> None:
    append = ClientAppend(
        request_id="req-1",
        seqno=0,
        conversation_id="conv-1",
        model_id="fake-model",
        action=ClientActionKind.USER_MESSAGE,
        text="hello",
        command_id="cmd-1",
    )
    app = create_app(
        f"sqlite+aiosqlite:///{tmp_path / 'gw.db'}",
        ca_dir=tmp_path / "ca",
        model=FakeModel(),
    )
    with TestClient(app) as client:
        body = encode_message(
            encode_bidi_append_request(
                BidiAppendRequest(
                    data=append.to_hex(),
                    request_id=append.request_id,
                    append_seqno=append.seqno,
                )
            )
        )
        response = client.post(
            "/aiserver.v1.BidiService/BidiAppend",
            content=body,
            headers={"content-type": "application/proto"},
        )
        assert response.status_code == 200

        sse_body = encode_message(encode_bidi_request_id(BidiRequestId(request_id="req-1")))
        with client.stream(
            "POST",
            "/agent.v1.AgentService/RunSSE",
            content=sse_body,
            headers={"content-type": "application/proto"},
        ) as stream:
            assert stream.status_code == 200
            raw = b"".join(stream.iter_bytes())

    frames = decode_frames(raw)
    assert frames
    kinds = []
    for flags, payload in frames:
        if flags & 0x02:
            continue
        kinds.append(json.loads(payload.decode("utf-8"))["kind"])
    assert "text_delta" in kinds
    assert "end" in kinds


def _agent_run_request_hex(*, text: str, model_id: str, conversation_id: str) -> str:
    """Build hex(AgentClientMessage{run_request=...}) like real Cursor traffic."""
    from cursor_switch.adapters.cursor.proto_min import (
        encode_bool,
        encode_message_field,
        encode_string,
    )

    user_message = encode_string(1, text)
    user_message_action = encode_message_field(1, user_message)
    conversation_action = encode_message_field(1, user_message_action)  # user_message_action
    model_details = encode_string(1, model_id)
    requested = encode_string(1, model_id) + encode_bool(2, False)
    run_request = (
        encode_message_field(2, conversation_action)
        + encode_message_field(3, model_details)
        + encode_string(5, conversation_id)
        + encode_message_field(9, requested)
    )
    agent_client = encode_message_field(1, run_request)  # run_request
    return agent_client.hex()


def test_bidi_append_accepts_agent_client_protobuf(tmp_path: Path) -> None:
    app = create_app(
        f"sqlite+aiosqlite:///{tmp_path / 'proto.db'}",
        ca_dir=tmp_path / "ca",
        model=FakeModel(),
    )
    with TestClient(app) as client:
        body = encode_message(
            encode_bidi_append_request(
                BidiAppendRequest(
                    data=_agent_run_request_hex(
                        text="ping from cursor",
                        model_id="fake-model",
                        conversation_id="conv-proto-1",
                    ),
                    request_id="req-proto-1",
                    append_seqno=0,
                )
            )
        )
        response = client.post(
            "/aiserver.v1.BidiService/BidiAppend",
            content=body,
            headers={"content-type": "application/proto"},
        )
        assert response.status_code == 200, response.text

        sse_body = encode_message(encode_bidi_request_id(BidiRequestId(request_id="req-proto-1")))
        with client.stream(
            "POST",
            "/agent.v1.AgentService/RunSSE",
            content=sse_body,
            headers={"content-type": "application/proto"},
        ) as stream:
            assert stream.status_code == 200
            raw = b"".join(stream.iter_bytes())
    kinds = [
        json.loads(payload.decode("utf-8"))["kind"]
        for flags, payload in decode_frames(raw)
        if not (flags & 0x02)
    ]
    assert "text_delta" in kinds


def test_parse_agent_client_protobuf_heartbeat() -> None:
    from cursor_switch.adapters.cursor.envelope import parse_client_append
    from cursor_switch.adapters.cursor.proto_min import encode_message_field

    heartbeat = encode_message_field(7, b"").hex()  # client_heartbeat
    append = parse_client_append(request_id="r", seqno=1, data_hex=heartbeat)
    assert append.action is ClientActionKind.HEARTBEAT


def test_is_connected_and_catalog(tmp_path: Path) -> None:
    from cursor_switch.adapters.cursor.proto_min import iter_fields

    app = create_app(
        f"sqlite+aiosqlite:///{tmp_path / 'stub.db'}",
        ca_dir=tmp_path / "ca",
        model=FakeModel(),
    )
    with TestClient(app) as client:
        # seed one model so catalog is non-empty
        created = client.post(
            "/api/models",
            json={
                "display_name": "本地测试",
                "provider_type": "openai_chat",
                "base_url": "https://example.invalid/v1",
                "api_key": "sk-test",
                "model_name": "gpt-test",
                "notes": "",
                "context_tokens": 128000,
                "max_output_tokens": 8192,
                "enabled": True,
                "sort_order": 1,
                "extra": {},
                "headers": {},
            },
        )
        assert created.status_code in {200, 201}
        model_id = created.json()["id"]

        connected = client.post("/aiserver.v1.NetworkService/IsConnected")
        assert connected.status_code == 200
        assert connected.headers["content-type"].startswith("application/proto")

        available = client.post("/aiserver.v1.AiService/AvailableModels")
        assert available.status_code == 200
        assert available.headers["content-type"].startswith("application/proto")
        assert not available.content.startswith(b"{")
        names = [
            value.decode("utf-8")
            for field, wire, value in iter_fields(available.content)
            if field == 1 and wire == 2 and isinstance(value, bytes)
        ]
        assert model_id in names
        models = [
            value
            for field, wire, value in iter_fields(available.content)
            if field == 2 and wire == 2 and isinstance(value, bytes)
        ]
        assert models
        model_fields = iter_fields(models[0])
        assert any(field == 30 and wire == 2 for field, wire, _ in model_fields)
        assert any(field == 29 and wire == 2 for field, wire, _ in model_fields)
        assert b"\xe6\x9c\xac\xe5\x9c\xb0\xe6\xb5\x8b\xe8\xaf\x95" in available.content  # 本地测试

        usable = client.post("/aiserver.v1.AiService/GetUsableModels")
        assert usable.status_code == 200
        assert usable.headers["content-type"].startswith("application/proto")
        assert not usable.content.startswith(b"{")
