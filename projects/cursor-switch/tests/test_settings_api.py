"""Settings and harness control-plane API."""

from pathlib import Path

from fastapi.testclient import TestClient

from cursor_switch.adapters.local_access.ca import CaState
from cursor_switch.control.app import create_app


def test_ports_proxy_and_harness(tmp_path: Path, monkeypatch) -> None:
    settings_file = tmp_path / "cursor-settings.json"
    app = create_app(
        f"sqlite+aiosqlite:///{tmp_path / 'settings.db'}",
        ca_dir=tmp_path / "ca",
        cursor_settings_path=settings_file,
    )
    with TestClient(app) as client:
        ports = client.put(
            "/api/settings/ports",
            json={"proxy_port": 8788, "service_port": 8787},
        )
        assert ports.status_code == 200
        assert ports.json()["proxy_port"] == 8788
        assert client.get("/api/settings/ports").json()["service_port"] == 8787

        proxy = client.put(
            "/api/settings/proxy",
            json={
                "mode": "custom",
                "address": "http://127.0.0.1:7890",
                "auth_enabled": False,
                "username": "",
                "password": "",
            },
        )
        assert proxy.status_code == 200
        assert client.get("/api/settings/proxy").json()["mode"] == "custom"

        status = client.get("/api/harness/cursor/status")
        assert status.status_code == 200
        assert status.json()["enabled"] is False
        assert status.json()["ca"] == "missing"

        initialized = client.post("/api/harness/cursor/ca/initialize")
        assert initialized.status_code == 200
        assert initialized.json()["ca"] in {"untrusted", "ready"}
        assert initialized.json()["ca_install_command"]

        # Default mode is passthrough: enable without trusted CA.
        status = client.get("/api/harness/cursor/status")
        assert status.json()["mode"] == "passthrough"

        enabled = client.put("/api/harness/cursor/enabled", json={"enabled": True})
        assert enabled.status_code == 200
        body = enabled.json()
        assert body["enabled"] is True
        assert body["integration"] == "enabled"
        assert body["mode"] == "passthrough"
        assert body["proxy_url"] and body["proxy_url"].startswith("http://127.0.0.1:")
        assert body["proxy_port"]
        assert settings_file.exists()
        written = settings_file.read_text(encoding="utf-8")
        assert "http.proxy" in written
        assert body["proxy_url"] in written

        # Switching to intercept while enabled is blocked.
        blocked = client.put("/api/harness/cursor/mode", json={"mode": "intercept"})
        assert blocked.status_code == 400

        disabled = client.put("/api/harness/cursor/enabled", json={"enabled": False})
        assert disabled.status_code == 200
        assert disabled.json()["enabled"] is False
        assert disabled.json()["proxy_url"] is None
        assert "http.proxy" not in settings_file.read_text(encoding="utf-8")

        # Intercept requires a trusted CA.
        mode = client.put("/api/harness/cursor/mode", json={"mode": "intercept"})
        assert mode.status_code == 200
        assert mode.json()["mode"] == "intercept"
        rejected = client.put("/api/harness/cursor/enabled", json={"enabled": True})
        assert rejected.status_code == 400

        ca = client.app.state.services.local_access.ca
        monkeypatch.setattr(ca, "state", lambda: CaState.READY)
        intercept_on = client.put("/api/harness/cursor/enabled", json={"enabled": True})
        assert intercept_on.status_code == 200
        assert intercept_on.json()["mode"] == "intercept"
        client.put("/api/harness/cursor/enabled", json={"enabled": False})
