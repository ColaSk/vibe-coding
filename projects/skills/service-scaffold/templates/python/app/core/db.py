import asyncio
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from urllib.parse import quote_plus

from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config import MySQLSettings


def mysql_url(settings: MySQLSettings) -> str:
    user = quote_plus(settings.user)
    password = quote_plus(settings.password)
    return f"mysql+asyncmy://{user}:{password}@{settings.server}:{settings.port}/{settings.db}"


class Database:
    def __init__(self, name: str, settings: MySQLSettings) -> None:
        self.name = name
        self.enabled = settings.enabled
        self.settings = settings
        self._lock = asyncio.Lock()
        self._engine: AsyncEngine | None = None
        self._sessions: async_sessionmaker[AsyncSession] | None = None

    async def startup(self) -> None:
        engine = create_async_engine(mysql_url(self.settings), pool_pre_ping=True)
        self._engine = engine
        self._sessions = async_sessionmaker(engine, expire_on_commit=False)

    async def shutdown(self) -> None:
        engine = self._engine
        self._engine = None
        self._sessions = None
        if engine is not None:
            await engine.dispose()

    async def ping(self) -> None:
        async with self.open() as session:
            await session.execute(text("SELECT 1"))

    @asynccontextmanager
    async def open(self) -> AsyncIterator[AsyncSession]:
        if self._sessions is None:
            async with self._lock:
                if self._sessions is None:
                    await self.startup()
        sessions = self._sessions
        if sessions is None:
            raise RuntimeError(f"{self.name} unavailable")
        async with sessions() as session:
            yield session


_databases: dict[str, Database] = {}


def database(name: str, settings: MySQLSettings) -> Database:
    current = _databases.get(name)
    if current is None or current.settings != settings:
        current = Database(name, settings)
        _databases[name] = current
    return current
