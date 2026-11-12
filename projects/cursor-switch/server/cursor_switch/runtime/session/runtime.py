"""Conversation runtime with a single current run."""

from __future__ import annotations

import asyncio

from cursor_switch.runtime.domain.types import (
    ConversationId,
    Message,
    MessageRole,
    ModelEventKind,
    RunId,
    RunPhase,
    ToolCall,
    new_id,
)
from cursor_switch.runtime.ports.checkpoint import CheckpointPort
from cursor_switch.runtime.ports.model import ModelInvocation, ModelPort
from cursor_switch.runtime.ports.tool import ToolPort
from cursor_switch.runtime.session.commands import (
    BreakMessages,
    Cancel,
    CommandResult,
    InsertMessages,
    RunCommand,
    ToolResultCommand,
)


class ConversationRuntime:
    """Owns one conversation and at most one current run."""

    def __init__(
        self,
        conversation_id: ConversationId,
        *,
        model: ModelPort,
        tools: ToolPort,
        checkpoints: CheckpointPort,
        model_id: str,
    ) -> None:
        self.conversation_id = conversation_id
        self._model = model
        self._tools = tools
        self._checkpoints = checkpoints
        self._model_id = model_id
        self._messages: list[Message] = []
        self._phase = RunPhase.ENDED
        self._current_run_id: RunId | None = None
        self._seen_commands: set[str] = set()
        self._pending_inserts: list[Message] = []
        self._break_requested = False
        self._cancel_requested = False
        self._lock = asyncio.Lock()
        self._run_task: asyncio.Task[None] | None = None

    @property
    def phase(self) -> RunPhase:
        return self._phase

    @property
    def current_run_id(self) -> RunId | None:
        return self._current_run_id

    @property
    def messages(self) -> list[Message]:
        return list(self._messages)

    async def handle(self, command: RunCommand) -> CommandResult:
        async with self._lock:
            if command.command_id in self._seen_commands:
                return CommandResult.DUPLICATE
            self._seen_commands.add(command.command_id)

            target = getattr(command, "target_run_id", None)
            if target is not None and target != self._current_run_id:
                return CommandResult.STALE_TARGET

            if self._phase is RunPhase.ENDED:
                if isinstance(command, (InsertMessages, BreakMessages)):
                    return await self._start_run(command.messages)
                return CommandResult.RUN_ENDED

            if self._phase is RunPhase.FINALIZING:
                return CommandResult.RUN_CLOSING

            # RUNNING
            if isinstance(command, InsertMessages):
                self._pending_inserts.extend(command.messages)
                return CommandResult.APPLIED
            if isinstance(command, BreakMessages):
                self._break_requested = True
                self._pending_inserts.extend(command.messages)
                return CommandResult.APPLIED
            if isinstance(command, Cancel):
                self._cancel_requested = True
                return CommandResult.APPLIED
            if isinstance(command, ToolResultCommand):
                self._messages.append(
                    Message(
                        id=new_id("msg"),
                        role=MessageRole.TOOL,
                        content=command.result.content,
                        tool_call_id=command.result.tool_call_id,
                    )
                )
                return CommandResult.APPLIED
            return CommandResult.APPLIED

    async def _start_run(self, initial: list[Message]) -> CommandResult:
        self._messages.extend(initial)
        self._current_run_id = new_id("run")
        self._phase = RunPhase.RUNNING
        self._break_requested = False
        self._cancel_requested = False
        self._pending_inserts.clear()
        self._run_task = asyncio.create_task(self._run_loop())
        return CommandResult.APPLIED

    async def _run_loop(self) -> None:
        try:
            while self._phase is RunPhase.RUNNING:
                if self._cancel_requested:
                    break
                await self._model_cycle()
                if self._cancel_requested:
                    break
                if self._pending_inserts:
                    self._messages.extend(self._pending_inserts)
                    self._pending_inserts.clear()
                    self._break_requested = False
                    continue
                break
        finally:
            async with self._lock:
                self._phase = RunPhase.FINALIZING
            await self._checkpoints.save(self.conversation_id, list(self._messages))
            async with self._lock:
                self._phase = RunPhase.ENDED
                self._current_run_id = None
                self._run_task = None

    async def _model_cycle(self) -> None:
        tool_calls: list[ToolCall] = []
        text_parts: list[str] = []
        async for event in self._model.stream(
            ModelInvocation(model_id=self._model_id, messages=list(self._messages))
        ):
            if self._break_requested or self._cancel_requested:
                break
            if event.kind is ModelEventKind.TEXT_DELTA:
                text_parts.append(event.text)
            elif event.kind is ModelEventKind.TOOL_CALL and event.tool_call is not None:
                tool_calls.append(event.tool_call)
            elif event.kind is ModelEventKind.ERROR:
                self._messages.append(
                    Message(
                        id=new_id("msg"),
                        role=MessageRole.ASSISTANT,
                        content=event.error or "model error",
                    )
                )
                return
            elif event.kind is ModelEventKind.END:
                break

        if text_parts or not tool_calls:
            self._messages.append(
                Message(
                    id=new_id("msg"),
                    role=MessageRole.ASSISTANT,
                    content="".join(text_parts),
                )
            )

        for call in tool_calls:
            if self._break_requested or self._cancel_requested:
                self._messages.append(
                    Message(
                        id=new_id("msg"),
                        role=MessageRole.TOOL,
                        content="interrupted",
                        tool_call_id=call.id,
                    )
                )
                continue
            handle = await self._tools.dispatch(call)
            result = await handle.result()
            self._messages.append(
                Message(
                    id=new_id("msg"),
                    role=MessageRole.TOOL,
                    content=result.content,
                    tool_call_id=result.tool_call_id,
                )
            )

    async def wait_until_idle(self) -> None:
        task = self._run_task
        if task is not None:
            await task
