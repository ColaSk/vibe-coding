from collections.abc import AsyncIterator

from aio_pika.abc import AbstractRobustConnection
from aiokafka import AIOKafkaProducer
from fastapi import HTTPException, Request
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import get_settings
from app.core.db import Database


async def get_db(request: Request) -> AsyncIterator[AsyncSession]:
    if not get_settings().mysql_enabled:
        raise HTTPException(status_code=503, detail="db disabled")
    database: Database | None = getattr(request.app.state, "db", None)
    if database is None:
        raise HTTPException(status_code=503, detail="db unavailable")
    async with database.session_factory() as session:
        yield session


async def get_redis(request: Request) -> Redis:
    if not get_settings().redis_enabled:
        raise HTTPException(status_code=503, detail="redis disabled")
    client: Redis | None = getattr(request.app.state, "redis", None)
    if client is None:
        raise HTTPException(status_code=503, detail="redis unavailable")
    return client


async def get_kafka(request: Request) -> AIOKafkaProducer:
    if not get_settings().kafka_enabled:
        raise HTTPException(status_code=503, detail="kafka disabled")
    producer: AIOKafkaProducer | None = getattr(request.app.state, "kafka", None)
    if producer is None:
        raise HTTPException(status_code=503, detail="kafka unavailable")
    return producer


async def get_rabbitmq(request: Request) -> AbstractRobustConnection:
    if not get_settings().rabbitmq_enabled:
        raise HTTPException(status_code=503, detail="rabbitmq disabled")
    connection: AbstractRobustConnection | None = getattr(request.app.state, "rabbitmq", None)
    if connection is None:
        raise HTTPException(status_code=503, detail="rabbitmq unavailable")
    return connection
