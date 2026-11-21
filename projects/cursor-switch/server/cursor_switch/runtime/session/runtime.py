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

# One user turn can need many tool rounds. The cap only stops a model that
# never finishes; a normal task must not end after the first tool batch.
_MAX_MODEL_CYCLES = 32


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
        tool_definitions: list[dict] | None = None,
        system_prompt: str = "",
        initial_messages: list[Message] | None = None,
    ) -> None:
        self.conversation_id = conversation_id
        self._model = model
        self._tools = tools
        self._checkpoints = checkpoints
        self._model_id = model_id
        self._tool_definitions = list(tool_definitions or [])
        self._system_prompt = system_prompt
        self._messages: list[Message] = list(initial_messages or [])
        self._phase = RunPhase.ENDED
        self._current_run_id: RunId | None = None
        self._seen_commands: set[str] = set()
        self._pending_inserts: list[Message] = []
        self._break_requested = False
        self._cancel_requested = False
        self._lock = asyncio.Lock()
        self._run_task: asyncio.Task[None] | None = None

    def set_tool_definitions(self, tools: list[dict]) -> None:
        self._tool_definitions = list(tools)

    def set_system_prompt(self, prompt: str) -> None:
        self._system_prompt = prompt

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
            cycles = 0
            while self._phase is RunPhase.RUNNING:
                if self._cancel_requested:
                    break
                cycles += 1
                continued = await self._model_cycle()
                if self._cancel_requested:
                    break
                if self._pending_inserts:
                    self._messages.extend(self._pending_inserts)
                    self._pending_inserts.clear()
                    self._break_requested = False
                    continue
                # A tool result is input for the next model turn. Stopping here
                # ends the agent task after the first tool batch.
                if continued and cycles < _MAX_MODEL_CYCLES:
                    continue
                if continued:
                    self._messages.append(
                        Message(
                            id=new_id("msg"),
                            role=MessageRole.ASSISTANT,
                            content="stopped: model cycle limit reached",
                        )
                    )
                break
        finally:
            async with self._lock:
                self._phase = RunPhase.FINALIZING
            await self._checkpoints.save(self.conversation_id, list(self._messages))
            async with self._lock:
                self._phase = RunPhase.ENDED
                self._current_run_id = None
                self._run_task = None

    async def _model_cycle(self) -> bool:
        tool_calls: list[ToolCall] = []
        text_parts: list[str] = []
        messages = list(self._messages)
        if self._system_prompt and not any(m.role is MessageRole.SYSTEM for m in messages):
            messages = [
                Message(id=new_id("sys"), role=MessageRole.SYSTEM, content=self._system_prompt),
                *messages,
            ]
        async for event in self._model.stream(
            ModelInvocation(
                model_id=self._model_id,
                messages=messages,
                tools=list(self._tool_definitions),
            )
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
                return False
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

        executed = False
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
            executed = True
            self._messages.append(
                Message(
                    id=new_id("msg"),
                    role=MessageRole.TOOL,
                    content=result.content,
                    tool_call_id=result.tool_call_id,
                )
            )
        return executed and not self._cancel_requested and not self._break_requested

    async def wait_until_idle(self) -> None:
        task = self._run_task
        if task is not None:
            await task
