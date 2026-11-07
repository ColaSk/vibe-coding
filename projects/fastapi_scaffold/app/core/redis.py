import asyncio
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from redis.asyncio import Redis

from app.core.config import RedisSettings


class RedisConnection:
    def __init__(self, name: str, settings: RedisSettings) -> None:
        self.name = name
        self.enabled = settings.enabled
        self.settings = settings
        self._lock = asyncio.Lock()
        self._client: Redis | None = None

    async def startup(self) -> None:
        self._client = Redis(
            host=self.settings.host,
            port=self.settings.port,
            decode_responses=True,
        )

    async def shutdown(self) -> None:
        client = self._client
        self._client = None
        if client is not None:
            await client.aclose()

    async def ping(self) -> None:
        async with self.open() as client:
            if not await client.ping():
                raise RuntimeError(f"{self.name} unavailable")

    @asynccontextmanager
    async def open(self) -> AsyncIterator[Redis]:
        if self._client is None:
            async with self._lock:
                if self._client is None:
                    await self.startup()
        if self._client is None:
            raise RuntimeError(f"{self.name} unavailable")
        yield self._client


_connections: dict[str, RedisConnection] = {}


def redis_connection(name: str, settings: RedisSettings) -> RedisConnection:
    current = _connections.get(name)
    if current is None or current.settings != settings:
        current = RedisConnection(name, settings)
        _connections[name] = current
    return current
