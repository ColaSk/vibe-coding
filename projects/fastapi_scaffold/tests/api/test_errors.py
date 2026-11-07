from fastapi.testclient import TestClient

from app.core.exceptions import AppError
from app.main import create_app


def test_app_error_returns_envelope() -> None:
    application = create_app()

    @application.get("/boom")
    async def boom() -> None:
        raise AppError(status_code=409, msg="already exists")

    with TestClient(application) as client:
        response = client.get("/boom")

    assert response.status_code == 409
    assert response.json() == {
        "success": False,
        "code": 409,
        "msg": "already exists",
        "data": None,
    }


def test_unhandled_exception_returns_generic_envelope() -> None:
    application = create_app()

    @application.get("/crash")
    async def crash() -> None:
        raise RuntimeError("secret")

    with TestClient(application, raise_server_exceptions=False) as client:
        response = client.get("/crash")

    assert response.status_code == 500
    body = response.json()
    assert body == {
        "success": False,
        "code": 500,
        "msg": "internal server error",
        "data": None,
    }
    assert "secret" not in response.text


def test_validation_error_returns_envelope() -> None:
    application = create_app()

    @application.get("/items/{item_id}")
    async def read_item(item_id: int) -> dict[str, int]:
        return {"item_id": item_id}

    with TestClient(application) as client:
        response = client.get("/items/not-a-number")

    assert response.status_code == 422
    body = response.json()
    assert body["success"] is False
    assert body["code"] == 422
    assert body["data"] is None
    assert body["msg"]
