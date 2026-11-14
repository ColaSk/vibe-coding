"""Overview buckets, calls, tab routing, and model discovery."""

from pathlib import Path

import httpx
from fastapi.testclient import TestClient

from cursor_switch.adapters.local_access.routing import upstream_url
from cursor_switch.control.app import create_app


def test_overview_buckets_and_call_detail(tmp_path: Path) -> None:
    app = create_app(f"sqlite+aiosqlite:///{tmp_path / 'calls.db'}", ca_dir=tmp_path / "ca")
    with TestClient(app) as client:
        client.put("/api/settings/observation", json={"detailed": True})
        client.put(
            "/api/settings/pricing",
            json={
                "input_per_million": 1,
                "output_per_million": 2,
                "cache_read_per_million": 0.1,
                "cache_write_per_million": 0.2,
            },
        )
        created = client.post(
            "/api/calls",
            json={
                "model_id": "m1",
                "display_name": "Demo",
                "status": "ok",
                "created_at_ms": 1_700_000_000_000,
                "first_token_ms": 40,
                "duration_ms": 100,
                "input_tokens": 1_000_000,
                "output_tokens": 1_000_000,
                "cache_read_tokens": 0,
                "cache_write_tokens": 0,
                "request_json": "{\"n\":1}",
                "response_text": "hello",
            },
        )
        assert created.status_code == 201
        call_id = created.json()["id"]
        detail = client.get(f"/api/calls/{call_id}")
        assert detail.json()["response_text"] == "hello"
        overview = client.get(
            "/api/overview",
            params={"start_ms": 1_700_000_000_000, "end_ms": 1_700_000_060_000},
        )
        body = overview.json()
        assert body["call_count"] == 1
        assert body["token_usage_granularity"] == "minute"
        assert body["estimated_value"] == 3
        assert body["token_usage_series"][0]["input_tokens"] == 1_000_000
        cleared = client.delete("/api/storage", params={"scope": "details"})
        assert cleared.json()["trace_count"] == 0
        assert client.get(f"/api/calls/{call_id}").json()["response_text"] == ""


def test_tab_upstream_modes() -> None:
    path = "/aiserver.v1.AiService/StreamCpp"
    direct = upstream_url(
        path, "api3.cursor.sh", local=False, backend_host="127.0.0.1", backend_port=8787, tab_mode="direct"
    )
    custom = upstream_url(
        path,
        "api3.cursor.sh",
        local=False,
        backend_host="127.0.0.1",
        backend_port=8787,
        tab_mode="custom",
        tab_address="https://tab.example",
    )
    assert direct.startswith("https://api3.cursor.sh")
    assert custom.startswith("https://tab.example")


def test_discover_models(tmp_path: Path, monkeypatch) -> None:
    app = create_app(f"sqlite+aiosqlite:///{tmp_path / 'disc.db'}", ca_dir=tmp_path / "ca")

    class FakeResponse:
        def raise_for_status(self) -> None:
            return None

        def json(self) -> dict:
            return {"data": [{"id": "gpt-4.1"}, {"id": "gpt-4.1-mini"}]}

    class FakeClient:
        def __init__(self, *args, **kwargs) -> None:
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, *args) -> None:
            return None

        async def get(self, url, headers=None):
            assert url.endswith("/v1/models")
            return FakeResponse()

    monkeypatch.setattr(httpx, "AsyncClient", FakeClient)
    with TestClient(app) as client:
        found = client.post(
            "/api/models/discover",
            json={"provider_type": "openai_chat", "base_url": "https://api.example/v1", "api_key": "k"},
        )
        assert found.status_code == 200
        assert found.json()["model_ids"] == ["gpt-4.1", "gpt-4.1-mini"]
        created = client.post(
            "/api/models",
            json={
                "display_name": "A",
                "provider_type": "openai_chat",
                "base_url": "https://old",
                "api_key": "old",
                "model_name": "a",
                "group_name": "work",
            },
        )
        assert created.status_code == 201
        updated = client.put(
            "/api/models/group",
            json={"group_name": "work", "base_url": "https://new", "api_key": "new"},
        )
        assert updated.json()[0]["base_url"] == "https://new"
        saved = client.put("/api/settings/tab", json={"mode": "direct", "address": ""})
        assert saved.json()["mode"] == "direct"
        cursor_path = client.get("/api/settings/cursor-path")
        assert cursor_path.status_code == 200
        assert cursor_path.json()["path"] == ""
        assert cursor_path.json()["effective_path"]
        custom = tmp_path / "alt-settings.json"
        updated = client.put("/api/settings/cursor-path", json={"path": str(custom)})
        assert updated.status_code == 200
        assert updated.json()["path"] == str(custom)
        assert updated.json()["effective_path"] == str(custom)
