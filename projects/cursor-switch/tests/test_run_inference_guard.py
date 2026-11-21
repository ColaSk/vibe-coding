"""RunInference thrash / empty-result guards."""

from __future__ import annotations

from cursor_switch.adapters.cursor.run_inference_guard import (
    empty_tool_result_streak,
    repeated_tool_loop,
)
from cursor_switch.runtime.domain.types import Message, MessageRole, ToolCall


def _assistant_call(name: str, **args: object) -> Message:
    return Message(
        id="a",
        role=MessageRole.ASSISTANT,
        content="",
        tool_calls=(ToolCall(id="c", name=name, arguments=dict(args)),),
    )


def test_reject_tool_call_blocks_unadvertised_and_missing_required() -> None:
    from cursor_switch.adapters.cursor.run_inference_guard import (
        reject_tool_call,
        tool_parameter_schemas,
    )

    tools = [
        {
            "type": "function",
            "function": {
                "name": "Read",
                "parameters": {
                    "type": "object",
                    "properties": {"path": {"type": "string"}},
                    "required": ["path"],
                },
            },
        }
    ]
    schemas = tool_parameter_schemas(tools)
    assert reject_tool_call(ToolCall(id="1", name="Await", arguments={}), schemas)
    assert reject_tool_call(ToolCall(id="2", name="Read", arguments={}), schemas)
    assert reject_tool_call(ToolCall(id="3", name="Read", arguments={"path": "a"}), schemas) is None


def test_repeated_tool_loop_detects_identical_calls() -> None:
    messages = [
        Message(id="u", role=MessageRole.USER, content="read readme"),
        _assistant_call("Grep", pattern="README"),
        Message(id="t1", role=MessageRole.TOOL, content="", tool_call_id="c"),
        _assistant_call("Grep", pattern="README"),
        Message(id="t2", role=MessageRole.TOOL, content="", tool_call_id="c"),
        _assistant_call("Grep", pattern="README"),
    ]
    assert repeated_tool_loop(messages, threshold=3) is True
    assert repeated_tool_loop(messages[:4], threshold=3) is False
    resent = [*messages, Message(id="again", role=MessageRole.USER, content="retry")]
    assert repeated_tool_loop(resent, threshold=3) is False


def test_empty_tool_result_streak() -> None:
    messages = [
        Message(id="t1", role=MessageRole.TOOL, content="", tool_call_id="a"),
        Message(id="t2", role=MessageRole.TOOL, content="   ", tool_call_id="b"),
        Message(id="t3", role=MessageRole.TOOL, content="", tool_call_id="c"),
    ]
    assert empty_tool_result_streak(messages, threshold=3) is True
    messages[-1] = Message(id="t3", role=MessageRole.TOOL, content="ok", tool_call_id="c")
    assert empty_tool_result_streak(messages, threshold=3) is False


def test_compact_tool_history_shrinks_old_results() -> None:
    from cursor_switch.adapters.cursor.run_inference_guard import compact_tool_history

    messages = [
        Message(id=f"t{i}", role=MessageRole.TOOL, content="x" * 4000, tool_call_id=str(i))
        for i in range(6)
    ]
    compacted = compact_tool_history(messages, keep_recent=2, limit=200)
    assert len(compacted[0].content) < 4000
    assert len(compacted[-1].content) == 4000


def test_truncate_message_content_caps_tool_blobs() -> None:
    from cursor_switch.adapters.cursor.run_inference_guard import truncate_message_content

    short = "ok"
    assert truncate_message_content(short, limit=100) == short
    long = "x" * 500
    out = truncate_message_content(long, limit=100)
    assert len(out) < len(long)
    assert "truncated" in out.lower()
    assert out.startswith("x" * 20)


def test_default_httpx_timeout_is_agent_grade() -> None:
    from cursor_switch.adapters.providers.base import default_httpx_timeout

    timeout = default_httpx_timeout()
    assert timeout.read >= 120.0
    assert timeout.connect >= 10.0
