import pytest
from fastapi.testclient import TestClient

from app.core import db
from app.main import create_app


def test_lifespan_calls_mysql_hooks(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[str] = []

    async def connect(settings: object) -> object:
        calls.append("connect")
        assert settings.mysql_enabled is True
        return object()

    async def ping(client: object) -> None:
        calls.append("ping")
        assert client is not None

    async def disconnect(client: object) -> None:
        calls.append("disconnect")
        assert client is not None

    monkeypatch.setattr(db, "connect", connect)
    monkeypatch.setattr(db, "ping", ping)
    monkeypatch.setattr(db, "disconnect", disconnect)
    monkeypatch.setenv("MYSQL_ENABLED", "true")

    with TestClient(create_app()) as client:
        response = client.get("/ready")
        assert response.status_code == 200
        assert calls == ["connect", "ping"]

    assert calls == ["connect", "ping", "disconnect"]


def test_ready_returns_503_when_ping_fails(monkeypatch: pytest.MonkeyPatch) -> None:
    async def connect(settings: object) -> object:
        return object()

    async def ping(client: object) -> None:
        raise RuntimeError("down")

    async def disconnect(client: object) -> None:
        return None

    monkeypatch.setattr(db, "connect", connect)
    monkeypatch.setattr(db, "ping", ping)
    monkeypatch.setattr(db, "disconnect", disconnect)
    monkeypatch.setenv("MYSQL_ENABLED", "true")

    with TestClient(create_app()) as client:
        response = client.get("/ready")

    assert response.status_code == 503
    assert response.json() == {"status": "unavailable", "failed": ["db"]}
