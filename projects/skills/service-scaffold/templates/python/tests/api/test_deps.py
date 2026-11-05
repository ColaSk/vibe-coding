from fastapi import Depends
from fastapi.testclient import TestClient

from app.api.deps import get_db, get_kafka, get_rabbitmq, get_redis
from app.main import create_app


def test_dependencies_return_503_when_disabled() -> None:
    application = create_app()

    @application.get("/deps/db")
    async def read_db(session: object = Depends(get_db)) -> dict[str, object]:
        return {"session": session is not None}

    @application.get("/deps/redis")
    async def read_redis(client: object = Depends(get_redis)) -> dict[str, object]:
        return {"client": client is not None}

    @application.get("/deps/kafka")
    async def read_kafka(producer: object = Depends(get_kafka)) -> dict[str, object]:
        return {"producer": producer is not None}

    @application.get("/deps/rabbitmq")
    async def read_rabbitmq(connection: object = Depends(get_rabbitmq)) -> dict[str, object]:
        return {"connection": connection is not None}

    with TestClient(application) as client:
        for path in ("/deps/db", "/deps/redis", "/deps/kafka", "/deps/rabbitmq"):
            response = client.get(path)
            assert response.status_code == 503, path
