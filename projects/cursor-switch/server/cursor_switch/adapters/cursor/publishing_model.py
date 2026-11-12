"""ModelPort decorator that mirrors events onto a transport request_id."""

from __future__ import annotations

from collections.abc import AsyncIterator

from cursor_switch.runtime.domain.types import ModelEvent
from cursor_switch.runtime.ports.model import ModelInvocation, ModelPort
from cursor_switch.runtime.ports.transport import TransportPort


class PublishingModel:
    def __init__(
        self,
        inner: ModelPort,
        transport: TransportPort,
        request_id: str,
    ) -> None:
        self._inner = inner
        self._transport = transport
        self._request_id = request_id

    def stream(self, invocation: ModelInvocation) -> AsyncIterator[ModelEvent]:
        async def gen() -> AsyncIterator[ModelEvent]:
            async for event in self._inner.stream(invocation):
                await self._transport.publish(self._request_id, event)
                yield event

        return gen()
