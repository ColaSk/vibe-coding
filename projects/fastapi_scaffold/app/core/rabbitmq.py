import aio_pika
from aio_pika.abc import AbstractRobustConnection

from app.core.config import Settings


async def connect(settings: Settings) -> AbstractRobustConnection:
    return await aio_pika.connect_robust(
        host=settings.rabbitmq_host,
        port=settings.rabbitmq_port,
        login=settings.rabbitmq_user,
        password=settings.rabbitmq_password,
    )


async def disconnect(connection: AbstractRobustConnection) -> None:
    await connection.close()


async def ping(connection: AbstractRobustConnection) -> None:
    if connection.is_closed:
        raise RuntimeError("rabbitmq unavailable")
