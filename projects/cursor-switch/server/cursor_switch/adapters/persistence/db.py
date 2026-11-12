"""SQLite engine and session factory."""

from __future__ import annotations

from collections.abc import AsyncIterator
from pathlib import Path

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from cursor_switch.adapters.persistence.models import Base


def default_database_url() -> str:
    root = Path.home() / ".cursor-switch"
    root.mkdir(parents=True, exist_ok=True)
    return f"sqlite+aiosqlite:///{root / 'cursor-switch.db'}"


def create_engine(database_url: str | None = None) -> AsyncEngine:
    url = database_url or default_database_url()
    return create_async_engine(url, echo=False)


def create_session_factory(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(engine, expire_on_commit=False)


async def init_schema(engine: AsyncEngine) -> None:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


async def session_scope(
    factory: async_sessionmaker[AsyncSession],
) -> AsyncIterator[AsyncSession]:
    session = factory()
    try:
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()
