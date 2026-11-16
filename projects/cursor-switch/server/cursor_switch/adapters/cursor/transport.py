"""request_id-scoped transport registry for BidiAppend / RunSSE."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from enum import Enum

from cursor_switch.adapters.cursor.connect import (
    ConnectCode,
    ConnectStreamError,
    encode_end_stream,
    encode_error_end_stream,
    encode_message,
)
from cursor_switch.runtime.domain.types import ModelEvent
from cursor_switch.runtime.ports.transport import TransportPort


class TransportRoute(str, Enum):
    LOCAL = "local"
    UPSTREAM = "upstream"
    UNKNOWN = "unknown"


@dataclass
class _OrderedInbox:
    next_seq: int = 0
    pending: dict[int, bytes] = field(default_factory=dict)
    closed: bool = False

    def push(self, seqno: int, payload: bytes) -> list[bytes]:
        if self.closed:
            return []
        self.pending[seqno] = payload
        ready: list[bytes] = []
        while self.next_seq in self.pending:
            ready.append(self.pending.pop(self.next_seq))
            self.next_seq += 1
        return ready


class TransportHandle:
    def __init__(self, request_id: str) -> None:
        self.request_id = request_id
        self.conversation_id: str | None = None
        self.model_id: str | None = None
        self.protocol: str = "agent"  # agent | run_inference
        self.routing_text: str = ""
        self.run_ready_sent: bool = False
        self.prompt_vendor: str = "anthropic"
        self.reasoning_effort: str = "high"
        self.route = TransportRoute.UNKNOWN
        self._inbox = _OrderedInbox()
        self._subscribers: list[asyncio.Queue[bytes | None]] = []
        self._history: list[bytes] = []
        self._closed = False
        self._lock = asyncio.Lock()
        self._route_ready = asyncio.Event()

    async def set_route(self, route: TransportRoute) -> None:
        self.route = route
        self._route_ready.set()

    async def wait_route(self, timeout: float = 30.0) -> TransportRoute:
        try:
            await asyncio.wait_for(self._route_ready.wait(), timeout=timeout)
        except TimeoutError:
            return TransportRoute.UNKNOWN
        return self.route

    async def append(self, seqno: int, payload: bytes) -> list[bytes]:
        async with self._lock:
            return self._inbox.push(seqno, payload)

    async def publish_bytes(self, chunk: bytes) -> None:
        async with self._lock:
            if self._closed:
                return
            self._history.append(chunk)
            for queue in list(self._subscribers):
                await queue.put(chunk)

    async def publish_payload(self, payload: bytes) -> None:
        await self.publish_bytes(encode_message(payload))

    async def close(self, error: ConnectStreamError | None = None) -> None:
        async with self._lock:
            if self._closed:
                return
            self._closed = True
            frame = (
                encode_error_end_stream(error)
                if error is not None
                else encode_end_stream()
            )
            self._history.append(frame)
            for queue in list(self._subscribers):
                await queue.put(frame)
                await queue.put(None)

    def subscribe(self) -> asyncio.Queue[bytes | None]:
        queue: asyncio.Queue[bytes | None] = asyncio.Queue()
        for chunk in self._history:
            queue.put_nowait(chunk)
        if self._closed:
            queue.put_nowait(None)
        else:
            self._subscribers.append(queue)
        return queue


class TransportRegistry(TransportPort):
    def __init__(self) -> None:
        self._handles: dict[str, TransportHandle] = {}
        self._lock = asyncio.Lock()

    async def get_or_create(self, request_id: str) -> TransportHandle:
        async with self._lock:
            handle = self._handles.get(request_id)
            if handle is None:
                handle = TransportHandle(request_id)
                self._handles[request_id] = handle
            return handle

    async def get(self, request_id: str) -> TransportHandle | None:
        async with self._lock:
            return self._handles.get(request_id)

    async def mark_local(self, request_id: str) -> TransportHandle:
        handle = await self.get_or_create(request_id)
        await handle.set_route(TransportRoute.LOCAL)
        return handle

    async def mark_upstream(self, request_id: str) -> TransportHandle:
        handle = await self.get_or_create(request_id)
        await handle.set_route(TransportRoute.UPSTREAM)
        return handle

    async def publish_agent_message(self, request_id: str, message: object) -> None:
        """Publish a serialized AgentServerMessage (or any protobuf Message)."""
        handle = await self.get_or_create(request_id)
        if handle.protocol == "run_inference":
            return
        serialize = getattr(message, "SerializeToString", None)
        if serialize is None:
            raise TypeError("publish_agent_message expects a protobuf Message")
        await handle.publish_payload(serialize())

    async def publish(self, request_id: str, event: ModelEvent) -> None:
        handle = await self.get_or_create(request_id)
        if handle.protocol == "run_inference":
            # RunInference streaming is driven by gateway.invoke path.
            return
        from cursor_switch.adapters.cursor.protocol.events import from_model_event

        message = from_model_event(event, model_call_id=handle.model_id or "")
        if message is None:
            return
        await handle.publish_payload(message.SerializeToString())

    async def ensure_run_ready(self, request_id: str) -> None:
        from cursor_switch.adapters.cursor.run_inference import encode_run_ready

        handle = await self.get_or_create(request_id)
        if handle.protocol != "run_inference" or handle.run_ready_sent:
            return
        model_id = handle.model_id or "default"
        handle.run_ready_sent = True
        await handle.publish_payload(
            encode_run_ready(
                model_id=model_id,
                vendor=handle.prompt_vendor or "anthropic",
                prompt_version="latest",
                reasoning_effort=handle.reasoning_effort or "high",
            )
        )

    async def close(self, request_id: str) -> None:
        handle = await self.get(request_id)
        if handle is not None:
            await handle.close()

    async def close_error(self, request_id: str, message: str) -> None:
        handle = await self.get_or_create(request_id)
        await handle.close(ConnectStreamError(code=ConnectCode.INTERNAL, message=message))
