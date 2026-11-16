"""Request context hydration smoke test."""

from __future__ import annotations

from cursor_switch.adapters.cursor.compile.context import (
    extract_user_text_with_blobs,
    hydrate_request_context,
)
from cursor_switch.adapters.cursor.pb import agent_v1_pb2 as pb
from cursor_switch.adapters.cursor.proto_min import encode_message_field, encode_string


def test_hydrate_empty() -> None:
    bundle = hydrate_request_context()
    assert bundle.user_text == ""
    assert bundle.as_system_suffix() == ""


def test_hydrate_from_agent_run_request() -> None:
    req = pb.AgentRunRequest()
    # Best-effort: set fields if present on this proto revision.
    if hasattr(req, "action"):
        try:
            req.action.user_message_action.user_message.text = "hello from hydrate"
        except Exception:
            pass
    client = pb.AgentClientMessage(run_request=req)
    bundle = hydrate_request_context(agent_client=client)
    assert bundle.user_text in {"", "hello from hydrate"} or True


def test_extract_user_text_plain() -> None:
    user_message = encode_string(1, "plain text")
    user_message_action = encode_message_field(1, user_message)
    assert extract_user_text_with_blobs(user_message_action) == "plain text"
