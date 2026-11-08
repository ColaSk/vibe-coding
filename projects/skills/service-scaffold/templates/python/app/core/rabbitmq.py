import asyncio
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

import aio_pika
from aio_pika.abc import AbstractRobustConnection

from app.core.config import RabbitMQSettings


class RabbitMQConnection:
    def __init__(self, name: str, settings: RabbitMQSettings) -> None:
        self.name = name
        self.enabled = settings.enabled
        self.settings = settings
        self._lock = asyncio.Lock()
        self._connection: AbstractRobustConnection | None = None

    async def startup(self) -> None:
        self._connection = await aio_pika.connect_robust(
            host=self.settings.host,
            port=self.settings.port,
            login=self.settings.user,
            password=self.settings.password,
        )

    async def shutdown(self) -> None:
        connection = self._connection
        self._connection = None
        if connection is not None:
            await connection.close()

    async def ping(self) -> None:
        async with self.open() as connection:
            if connection.is_closed:
                raise RuntimeError(f"{self.name} unavailable")

    @asynccontextmanager
    async def open(self) -> AsyncIterator[AbstractRobustConnection]:
        if self._connection is None:
            async with self._lock:
                if self._connection is None:
                    await self.startup()
        if self._connection is None:
            raise RuntimeError(f"{self.name} unavailable")
        yield self._connection


_connections: dict[str, RabbitMQConnection] = {}


def rabbitmq_connection(name: str, settings: RabbitMQSettings) -> RabbitMQConnection:
    current = _connections.get(name)
    if current is None or current.settings != settings:
        current = RabbitMQConnection(name, settings)
        _connections[name] = current
    return current
