from fastapi.testclient import TestClient

from app.main import create_app


def test_read_hello() -> None:
    with TestClient(create_app()) as client:
        response = client.get("/api/v1/hello")

    assert response.status_code == 200
    assert response.json() == {"message": "hello from {{title}}"}
