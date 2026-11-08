from fastapi.testclient import TestClient

from app.core.context import RequestContext, get_context
from app.main import create_app


def test_read_hello() -> None:
    with TestClient(create_app()) as client:
        response = client.get("/api/v1/hello")

    assert response.status_code == 200
    assert response.json() == {
        "success": True,
        "code": 200,
        "msg": "ok",
        "data": {"message": "hello from {{title}}"},
    }
    assert response.headers["x-request-id"]


def test_request_id_is_echoed() -> None:
    with TestClient(create_app()) as client:
        response = client.get("/api/v1/hello", headers={"X-Request-ID": "req-123"})

    assert response.headers["x-request-id"] == "req-123"


def test_route_can_read_request_context() -> None:
    application = create_app()
    seen: list[RequestContext] = []

    @application.get("/context")
    async def read_context() -> dict[str, object]:
        ctx = get_context()
        assert ctx is not None
        seen.append(ctx)
        return {
            "request_id": ctx.request_id,
            "method": ctx.method,
            "path": ctx.path,
            "client_ip": ctx.client.ip,
            "client_port": ctx.client.port,
            "server_ip": ctx.server.ip,
            "server_port": ctx.server.port,
            "started_at": ctx.started_at.isoformat(),
            "ended_at": None if ctx.ended_at is None else ctx.ended_at.isoformat(),
            "duration": None if ctx.duration is None else ctx.duration.total_seconds(),
        }

    with TestClient(application) as client:
        response = client.get("/context", headers={"X-Request-ID": "req-456"})

    assert response.status_code == 200
    assert response.json() == {
        "request_id": "req-456",
        "method": "GET",
        "path": "/context",
        "client_ip": "testclient",
        "client_port": 50000,
        "server_ip": "testserver",
        "server_port": 80,
        "started_at": response.json()["started_at"],
        "ended_at": None,
        "duration": None,
    }
    ctx = seen[0]
    assert ctx.ended_at is not None
    assert ctx.started_at <= ctx.ended_at
    assert ctx.duration == ctx.ended_at - ctx.started_at
    assert get_context() is None
