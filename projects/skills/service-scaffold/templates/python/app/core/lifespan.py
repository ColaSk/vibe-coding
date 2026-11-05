from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from types import ModuleType

from fastapi import FastAPI

from app.core import db, kafka, rabbitmq, redis
from app.core.config import Settings, get_settings


def enabled_backends(settings: Settings | None = None) -> list[tuple[str, ModuleType]]:
    current = settings if settings is not None else get_settings()
    catalog = (
        ("db", current.mysql_enabled, db),
        ("redis", current.redis_enabled, redis),
        ("kafka", current.kafka_enabled, kafka),
        ("rabbitmq", current.rabbitmq_enabled, rabbitmq),
    )
    return [(name, module) for name, enabled, module in catalog if enabled]


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Startup order is the catalog order. Shutdown reverses it."""

    started: list[tuple[str, ModuleType, object]] = []
    try:
        for name, module in enabled_backends():
            client = await module.connect(get_settings())
            setattr(app.state, name, client)
            started.append((name, module, client))
        yield
    finally:
        for name, module, client in reversed(started):
            await module.disconnect(client)
