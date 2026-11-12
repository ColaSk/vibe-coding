"""Overview control-plane API."""

from pathlib import Path

from fastapi.testclient import TestClient

from cursor_switch.control.app import create_app


def test_overview_counts_models(tmp_path: Path) -> None:
    app = create_app(
        f"sqlite+aiosqlite:///{tmp_path / 'ov.db'}",
        ca_dir=tmp_path / "ca",
    )
    with TestClient(app) as client:
        empty = client.get("/api/overview")
        assert empty.status_code == 200
        assert empty.json()["model_count"] == 0

        created = client.post(
            "/api/models",
            json={
                "display_name": "Demo",
                "provider_type": "openai_chat",
                "base_url": "https://example.com",
                "api_key": "",
                "model_name": "demo",
                "notes": "",
                "context_tokens": 128000,
                "max_output_tokens": 8192,
                "enabled": True,
                "sort_order": 1,
                "extra": {},
                "headers": {},
            },
        )
        assert created.status_code in {200, 201}
        overview = client.get("/api/overview")
        assert overview.json()["model_count"] == 1
        assert overview.json()["enabled_model_count"] == 1
        assert client.get("/api/calls").json() == []
