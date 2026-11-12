"""Registry mapping conversation_id to a single runtime."""

from __future__ import annotations

from cursor_switch.runtime.domain.types import ConversationId
from cursor_switch.runtime.ports.checkpoint import CheckpointPort
from cursor_switch.runtime.ports.model import ModelPort
from cursor_switch.runtime.ports.tool import ToolPort
from cursor_switch.runtime.session.runtime import ConversationRuntime


class ConversationRegistry:
    def __init__(
        self,
        *,
        model: ModelPort,
        tools: ToolPort,
        checkpoints: CheckpointPort,
        model_id: str,
    ) -> None:
        self._model = model
        self._tools = tools
        self._checkpoints = checkpoints
        self._model_id = model_id
        self._runtimes: dict[ConversationId, ConversationRuntime] = {}

    def get_or_create(
        self,
        conversation_id: ConversationId,
        *,
        model_id: str | None = None,
        model: ModelPort | None = None,
    ) -> ConversationRuntime:
        runtime = self._runtimes.get(conversation_id)
        if runtime is None:
            runtime = ConversationRuntime(
                conversation_id,
                model=model or self._model,
                tools=self._tools,
                checkpoints=self._checkpoints,
                model_id=model_id or self._model_id,
            )
            self._runtimes[conversation_id] = runtime
        return runtime

    def get(self, conversation_id: ConversationId) -> ConversationRuntime | None:
        return self._runtimes.get(conversation_id)
