"""Phase 0/1: AgentServerMessage TextDelta / TurnEnded round-trip."""

from __future__ import annotations

from cursor_switch.adapters.cursor.pb import agent_v1_pb2 as pb
from cursor_switch.adapters.cursor.protocol.events import (
    server_interaction,
    text_delta,
    turn_ended,
)
from cursor_switch.runtime.domain.types import Usage


def test_text_delta_roundtrip() -> None:
    msg = text_delta("hello")
    raw = msg.SerializeToString()
    back = pb.AgentServerMessage.FromString(raw)
    assert back.WhichOneof("message") == "interaction_update"
    assert back.interaction_update.WhichOneof("message") == "text_delta"
    assert back.interaction_update.text_delta.text == "hello"


def test_turn_ended_roundtrip() -> None:
    msg = turn_ended(Usage(input_tokens=3, output_tokens=5))
    back = pb.AgentServerMessage.FromString(msg.SerializeToString())
    ended = back.interaction_update.turn_ended
    assert ended.input_tokens == 3
    assert ended.output_tokens == 5


def test_server_interaction_helper() -> None:
    upd = pb.InteractionUpdate(
        heartbeat=pb.HeartbeatUpdate(),
    )
    msg = server_interaction(upd)
    assert msg.interaction_update.WhichOneof("message") == "heartbeat"
