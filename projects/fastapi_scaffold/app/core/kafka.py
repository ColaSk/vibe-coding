import asyncio
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from aiokafka import AIOKafkaProducer

from app.core.config import KafkaSettings


class KafkaConnection:
    def __init__(self, name: str, settings: KafkaSettings) -> None:
        self.name = name
        self.enabled = settings.enabled
        self.settings = settings
        self._lock = asyncio.Lock()
        self._producer: AIOKafkaProducer | None = None

    async def startup(self) -> None:
        producer = AIOKafkaProducer(bootstrap_servers=self.settings.bootstrap_servers)
        await producer.start()
        self._producer = producer

    async def shutdown(self) -> None:
        producer = self._producer
        self._producer = None
        if producer is not None:
            await producer.stop()

    async def ping(self) -> None:
        async with self.open() as producer:
            await producer.client.force_metadata_update()
            if not producer.client.cluster.brokers():
                raise RuntimeError(f"{self.name} unavailable")

    @asynccontextmanager
    async def open(self) -> AsyncIterator[AIOKafkaProducer]:
        if self._producer is None:
            async with self._lock:
                if self._producer is None:
                    await self.startup()
        if self._producer is None:
            raise RuntimeError(f"{self.name} unavailable")
        yield self._producer


_connections: dict[str, KafkaConnection] = {}


def kafka_connection(name: str, settings: KafkaSettings) -> KafkaConnection:
    current = _connections.get(name)
    if current is None or current.settings != settings:
        current = KafkaConnection(name, settings)
        _connections[name] = current
    return current
