"""Model CRUD control-plane API."""

from pathlib import Path

from fastapi.testclient import TestClient

from cursor_switch.control.app import create_app


def _client(tmp_path: Path) -> TestClient:
    db = tmp_path / "test.db"
    app = create_app(f"sqlite+aiosqlite:///{db}", ca_dir=tmp_path / "ca")
    return TestClient(app)


def test_model_crud_and_reorder(tmp_path: Path) -> None:
    with _client(tmp_path) as client:
        created = client.post(
            "/api/models",
            json={
                "display_name": "GPT Test",
                "provider_type": "openai_responses",
                "base_url": "https://api.openai.com/v1",
                "api_key": "sk-test",
                "model_name": "gpt-4.1",
                "sort_order": 1,
            },
        )
        assert created.status_code == 201
        model = created.json()
        assert model["display_name"] == "GPT Test"
        model_id = model["id"]

        listed = client.get("/api/models")
        assert listed.status_code == 200
        assert len(listed.json()) == 1

        second = client.post(
            "/api/models",
            json={
                "display_name": "Claude",
                "provider_type": "anthropic",
                "base_url": "https://api.anthropic.com",
                "api_key": "sk-ant",
                "model_name": "claude-sonnet-4",
                "sort_order": 2,
            },
        ).json()

        reordered = client.put(
            "/api/models/order",
            json={"ordered_ids": [second["id"], model_id]},
        )
        assert reordered.status_code == 200
        names = [item["display_name"] for item in reordered.json()]
        assert names == ["Claude", "GPT Test"]

        updated = client.put(
            f"/api/models/{model_id}",
            json={
                "display_name": "GPT Renamed",
                "provider_type": "openai_responses",
                "base_url": "https://api.openai.com/v1",
                "api_key": "sk-test",
                "model_name": "gpt-4.1",
                "sort_order": 2,
            },
        )
        assert updated.status_code == 200
        assert updated.json()["display_name"] == "GPT Renamed"

        deleted = client.delete(f"/api/models/{model_id}")
        assert deleted.status_code == 204
        assert len(client.get("/api/models").json()) == 1
