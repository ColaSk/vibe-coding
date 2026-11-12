"""Control plane health route."""

from pathlib import Path

from fastapi.testclient import TestClient

from cursor_switch.control.app import create_app


def test_healthz_returns_ok(tmp_path: Path) -> None:
    app = create_app(f"sqlite+aiosqlite:///{tmp_path / 'health.db'}", ca_dir=tmp_path / "ca")
    with TestClient(app) as client:
        response = client.get("/healthz")
        assert response.status_code == 200
        assert response.json() == {"status": "ok", "service": "cursor-switch"}
