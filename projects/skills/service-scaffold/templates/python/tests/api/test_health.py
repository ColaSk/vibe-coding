from fastapi.testclient import TestClient

from app.main import create_app


def test_health_and_ready_when_backends_disabled() -> None:
    with TestClient(create_app()) as client:
        health = client.get("/health")
        ready = client.get("/ready")

    assert health.status_code == 200
    assert health.json() == {"status": "ok"}
    assert ready.status_code == 200
    assert ready.json() == {"status": "ready"}
