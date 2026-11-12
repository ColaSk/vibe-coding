"""Compile Cursor client actions into runtime commands."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from cursor_switch.adapters.cursor.envelope import ClientActionKind, ClientAppend
from cursor_switch.runtime.domain.types import Message, MessageRole, new_id
from cursor_switch.runtime.session.commands import (
    BreakMessages,
    Cancel,
    InsertMessages,
    RunCommand,
)


class MessageDelivery(str, Enum):
    IGNORE = "ignore"
    INSERT = "insert"
    BREAK = "break"
    CANCEL = "cancel"


INSERT_ACTIONS = frozenset(
    {
        ClientActionKind.BACKGROUND_TASK,
        ClientActionKind.BACKGROUND_SHELL,
        ClientActionKind.BACKGROUND_SUBAGENT,
        ClientActionKind.ASYNC_ASK,
        ClientActionKind.SUBSCRIPTION,
        ClientActionKind.GOAL_CONTINUATION,
    }
)

BREAK_ACTIONS = frozenset(
    {
        ClientActionKind.USER_MESSAGE,
        ClientActionKind.INJECT_CONTEXT,
        ClientActionKind.RUN_INFERENCE_INVOKE,
    }
)

CANCEL_ACTIONS = frozenset(
    {
        ClientActionKind.CANCEL,
        ClientActionKind.CANCEL_SUBAGENT,
    }
)

IGNORE_ACTIONS = frozenset(
    {
        ClientActionKind.RESUME,
        ClientActionKind.SUMMARIZE,
        ClientActionKind.SHELL_COMMAND,
        ClientActionKind.START_PLAN,
        ClientActionKind.EXECUTE_PLAN,
        ClientActionKind.HEARTBEAT,
        ClientActionKind.RUN_INFERENCE_START,
        ClientActionKind.RUN_INFERENCE_FINISH,
        ClientActionKind.UNKNOWN,
    }
)


def delivery_for(action: ClientActionKind) -> MessageDelivery:
    if action in INSERT_ACTIONS:
        return MessageDelivery.INSERT
    if action in BREAK_ACTIONS:
        return MessageDelivery.BREAK
    if action in CANCEL_ACTIONS:
        return MessageDelivery.CANCEL
    return MessageDelivery.IGNORE


@dataclass(frozen=True, slots=True)
class CompiledAction:
    delivery: MessageDelivery
    command: RunCommand | None
    event_id: str


def compile_append(append: ClientAppend) -> CompiledAction:
    delivery = delivery_for(append.action)
    event_id = append.command_id or new_id("evt")
    if delivery is MessageDelivery.IGNORE:
        return CompiledAction(delivery=delivery, command=None, event_id=event_id)

    messages = [
        Message(
            id=new_id("msg"),
            role=MessageRole.USER,
            content=append.text or f"[{append.action.value}]",
        )
    ]
    if delivery is MessageDelivery.INSERT:
        return CompiledAction(
            delivery=delivery,
            command=InsertMessages(
                messages=messages,
                command_id=event_id,
                target_run_id=append.target_run_id,
            ),
            event_id=event_id,
        )
    if delivery is MessageDelivery.BREAK:
        return CompiledAction(
            delivery=delivery,
            command=BreakMessages(
                messages=messages,
                command_id=event_id,
                target_run_id=append.target_run_id,
            ),
            event_id=event_id,
        )
    return CompiledAction(
        delivery=MessageDelivery.CANCEL,
        command=Cancel(command_id=event_id, target_run_id=append.target_run_id),
        event_id=event_id,
    )
