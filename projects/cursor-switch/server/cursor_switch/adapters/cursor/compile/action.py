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
    ERROR = "error"


INSERT_ACTIONS = frozenset(
    {
        ClientActionKind.BACKGROUND_TASK,
        ClientActionKind.BACKGROUND_SHELL,
        ClientActionKind.BACKGROUND_SUBAGENT,
        ClientActionKind.ASYNC_ASK,
        ClientActionKind.SUBSCRIPTION,
        ClientActionKind.GOAL_CONTINUATION,
        ClientActionKind.RESUME,
    }
)

BREAK_ACTIONS = frozenset(
    {
        ClientActionKind.USER_MESSAGE,
        ClientActionKind.INJECT_CONTEXT,
        ClientActionKind.RUN_INFERENCE_INVOKE,
        ClientActionKind.START_PLAN,
        ClientActionKind.EXECUTE_PLAN,
        ClientActionKind.SUMMARIZE,
    }
)

CANCEL_ACTIONS = frozenset(
    {
        ClientActionKind.CANCEL,
        ClientActionKind.CANCEL_SUBAGENT,
    }
)

# Still unsupported mid-run semantics (align with byok): shell_command → explicit error text
ERROR_ACTIONS = frozenset(
    {
        ClientActionKind.SHELL_COMMAND,
    }
)

IGNORE_ACTIONS = frozenset(
    {
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
    if action in ERROR_ACTIONS:
        return MessageDelivery.ERROR
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

    if delivery is MessageDelivery.ERROR:
        messages = [
            Message(
                id=new_id("msg"),
                role=MessageRole.USER,
                content=(
                    append.text
                    or f"[unsupported action {append.action.value}: "
                    "cursor-switch does not execute ShellCommandAction mid-run]"
                ),
            )
        ]
        return CompiledAction(
            delivery=MessageDelivery.BREAK,
            command=BreakMessages(
                messages=messages,
                command_id=event_id,
                target_run_id=append.target_run_id,
            ),
            event_id=event_id,
        )

    if append.action is ClientActionKind.RESUME:
        content = append.text or "[resume] continue from checkpoint with refreshed request_context"
    elif append.action is ClientActionKind.START_PLAN:
        content = append.text or "[plan] start planning"
    elif append.action is ClientActionKind.EXECUTE_PLAN:
        content = append.text or "[plan] execute the current plan"
    elif append.action is ClientActionKind.SUMMARIZE:
        content = append.text or "[summarize] compress conversation context"
    else:
        content = append.text or f"[{append.action.value}]"

    messages = [
        Message(
            id=new_id("msg"),
            role=MessageRole.USER,
            content=content,
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
