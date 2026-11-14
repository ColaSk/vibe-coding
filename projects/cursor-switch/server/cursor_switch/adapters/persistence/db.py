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


def _ensure_columns(connection) -> None:
    from sqlalchemy import inspect, text

    inspector = inspect(connection)
    if "models" not in inspector.get_table_names():
        return
    columns = {column["name"] for column in inspector.get_columns("models")}
    if "group_name" not in columns:
        connection.execute(text("ALTER TABLE models ADD COLUMN group_name VARCHAR(200) DEFAULT ''"))


async def init_schema(engine: AsyncEngine) -> None:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
        await connection.run_sync(_ensure_columns)


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
