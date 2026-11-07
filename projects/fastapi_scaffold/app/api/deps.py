from collections.abc import AsyncIterator, Awaitable, Callable

from aio_pika.abc import AbstractRobustConnection
from aiokafka import AIOKafkaProducer
from fastapi import HTTPException
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import get_settings
from app.core.db import Database, database
from app.core.kafka import kafka_connection
from app.core.rabbitmq import rabbitmq_connection
from app.core.redis import redis_connection


def _database(name: str) -> Database:
    settings = get_settings().mysql.get(name)
    if settings is None or not settings.enabled:
        raise HTTPException(status_code=503, detail=f"{name} disabled")
    return database(name, settings)


def get_db_connection(name: str) -> Callable[[], AsyncIterator[AsyncSession]]:
    async def dependency() -> AsyncIterator[AsyncSession]:
        async with _database(name).open() as session:
            yield session

    return dependency


def get_redis_connection(name: str) -> Callable[[], Awaitable[Redis]]:
    async def dependency() -> Redis:
        settings = get_settings().redis.get(name)
        if settings is None or not settings.enabled:
            raise HTTPException(status_code=503, detail=f"{name} disabled")
        async with redis_connection(name, settings).open() as client:
            return client

    return dependency


def get_kafka_connection(name: str) -> Callable[[], Awaitable[AIOKafkaProducer]]:
    async def dependency() -> AIOKafkaProducer:
        settings = get_settings().kafka.get(name)
        if settings is None or not settings.enabled:
            raise HTTPException(status_code=503, detail=f"{name} disabled")
        async with kafka_connection(name, settings).open() as producer:
            return producer

    return dependency


def get_rabbitmq_connection(name: str) -> Callable[[], Awaitable[AbstractRobustConnection]]:
    async def dependency() -> AbstractRobustConnection:
        settings = get_settings().rabbitmq.get(name)
        if settings is None or not settings.enabled:
            raise HTTPException(status_code=503, detail=f"{name} disabled")
        async with rabbitmq_connection(name, settings).open() as connection:
            return connection

    return dependency


get_db = get_db_connection("db")
get_redis = get_redis_connection("redis")
get_kafka = get_kafka_connection("kafka")
get_rabbitmq = get_rabbitmq_connection("rabbitmq")


__all__ = [
    "get_db",
    "get_db_connection",
    "get_kafka",
    "get_rabbitmq",
    "get_redis",
]
