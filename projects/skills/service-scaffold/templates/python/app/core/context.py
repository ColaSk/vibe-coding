import uuid
from collections.abc import Awaitable, Callable
from contextvars import ContextVar, Token
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from fastapi import Request, Response


@dataclass(frozen=True, slots=True)
class SocketAddress:
    ip: str | None
    port: int | None


@dataclass(slots=True)
class RequestContext:
    request_id: str
    method: str
    path: str
    started_at: datetime
    client: SocketAddress
    server: SocketAddress
    ended_at: datetime | None = None

    @property
    def duration(self) -> timedelta | None:
        if self.ended_at is None:
            return None
        return self.ended_at - self.started_at

    def finish(self) -> None:
        if self.ended_at is None:
            self.ended_at = datetime.now(timezone.utc)


_request_context: ContextVar[RequestContext | None] = ContextVar[RequestContext | None](
    "request_context",
    default=None,
)


def get_context() -> RequestContext | None:
    return _request_context.get()


def set_context(context: RequestContext | None) -> Token[RequestContext | None]:
    return _request_context.set(context)


def reset_context(token: Token[RequestContext | None]) -> None:
    _request_context.reset(token)


def _socket_address(address: object | None) -> SocketAddress:
    if address is None:
        return SocketAddress(ip=None, port=None)
    host = getattr(address, "host", None)
    port = getattr(address, "port", None)
    if host is None and isinstance(address, list | tuple) and len(address) >= 2:
        host, port = address[0], address[1]
    ip = str(host) if host else None
    parsed_port = int(port) if isinstance(port, int) else None
    return SocketAddress(ip=ip, port=parsed_port)


async def request_context_middleware(
    request: Request,
    call_next: Callable[[Request], Awaitable[Response]],
) -> Response:
    request_id = request.headers.get("x-request-id") or str(uuid.uuid4())
    context = RequestContext(
        request_id=request_id,
        method=request.method,
        path=request.url.path,
        started_at=datetime.now(timezone.utc),
        client=_socket_address(request.client),
        server=_socket_address(request.scope.get("server")),
    )
    token = set_context(context)
    try:
        response = await call_next(request)
    finally:
        context.finish()
        reset_context(token)
    response.headers["X-Request-ID"] = request_id
    return response
