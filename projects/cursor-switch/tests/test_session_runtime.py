"""Session runtime state machine."""

from cursor_switch.runtime.domain.types import (
    Message,
    MessageRole,
    ModelEvent,
    ModelEventKind,
    ToolCall,
    new_id,
)
from cursor_switch.runtime.session.commands import (
    BreakMessages,
    Cancel,
    CommandResult,
    InsertMessages,
)
from cursor_switch.runtime.session.registry import ConversationRegistry
from tests.fakes import FakeCheckpoints, FakeModel, FakeTools


def _user(text: str) -> Message:
    return Message(id=new_id("msg"), role=MessageRole.USER, content=text)


async def test_insert_starts_run_and_persists_checkpoint() -> None:
    checkpoints = FakeCheckpoints()
    registry = ConversationRegistry(
        model=FakeModel(),
        tools=FakeTools(),
        checkpoints=checkpoints,
        model_id="fake",
    )
    runtime = registry.get_or_create("c1")
    result = await runtime.handle(
        InsertMessages(messages=[_user("hi")], command_id="cmd-1")
    )
    assert result is CommandResult.APPLIED
    await runtime.wait_until_idle()
    assert runtime.phase.value == "ended"
    assert checkpoints.saved["c1"]
    assert any(m.content == "ok" for m in runtime.messages)


async def test_duplicate_command_is_ignored() -> None:
    registry = ConversationRegistry(
        model=FakeModel(),
        tools=FakeTools(),
        checkpoints=FakeCheckpoints(),
        model_id="fake",
    )
    runtime = registry.get_or_create("c2")
    command = InsertMessages(messages=[_user("hi")], command_id="same")
    assert await runtime.handle(command) is CommandResult.APPLIED
    assert await runtime.handle(command) is CommandResult.DUPLICATE
    await runtime.wait_until_idle()


async def test_break_requests_another_model_cycle() -> None:
    model = FakeModel(
        [
            [
                ModelEvent(kind=ModelEventKind.TEXT_DELTA, text="one"),
                ModelEvent(kind=ModelEventKind.END),
            ],
            [
                ModelEvent(kind=ModelEventKind.TEXT_DELTA, text="two"),
                ModelEvent(kind=ModelEventKind.END),
            ],
        ]
    )
    registry = ConversationRegistry(
        model=model,
        tools=FakeTools(),
        checkpoints=FakeCheckpoints(),
        model_id="fake",
    )
    runtime = registry.get_or_create("c3")
    await runtime.handle(InsertMessages(messages=[_user("start")], command_id="a"))
    # Give the run a moment to enter RUNNING before break.
    result = await runtime.handle(
        BreakMessages(messages=[_user("more")], command_id="b")
    )
    assert result in {CommandResult.APPLIED, CommandResult.RUN_CLOSING, CommandResult.RUN_ENDED}
    await runtime.wait_until_idle()
    assert model.calls >= 1


async def test_stale_target_is_rejected() -> None:
    registry = ConversationRegistry(
        model=FakeModel(),
        tools=FakeTools(),
        checkpoints=FakeCheckpoints(),
        model_id="fake",
    )
    runtime = registry.get_or_create("c4")
    result = await runtime.handle(
        Cancel(command_id="x", target_run_id="run_missing")
    )
    assert result is CommandResult.STALE_TARGET


async def test_tool_call_is_dispatched() -> None:
    model = FakeModel(
        [
            [
                ModelEvent(
                    kind=ModelEventKind.TOOL_CALL,
                    tool_call=ToolCall(id="t1", name="Shell", arguments={"cmd": "echo"}),
                ),
                ModelEvent(kind=ModelEventKind.END),
            ]
        ]
    )
    registry = ConversationRegistry(
        model=model,
        tools=FakeTools(),
        checkpoints=FakeCheckpoints(),
        model_id="fake",
    )
    runtime = registry.get_or_create("c5")
    await runtime.handle(InsertMessages(messages=[_user("run")], command_id="t"))
    await runtime.wait_until_idle()
    assert any(m.tool_call_id == "t1" for m in runtime.messages)
