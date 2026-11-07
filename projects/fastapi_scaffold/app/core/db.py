from dataclasses import dataclass
from urllib.parse import quote_plus

from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config import Settings


@dataclass
class Database:
    engine: AsyncEngine
    session_factory: async_sessionmaker[AsyncSession]


def mysql_url(settings: Settings) -> str:
    user = quote_plus(settings.mysql_user)
    password = quote_plus(settings.mysql_password)
    return (
        f"mysql+asyncmy://{user}:{password}@{settings.mysql_server}:"
        f"{settings.mysql_port}/{settings.mysql_db}"
    )


async def connect(settings: Settings) -> Database:
    engine = create_async_engine(mysql_url(settings), pool_pre_ping=True)
    session_factory = async_sessionmaker(engine, expire_on_commit=False)
    return Database(engine=engine, session_factory=session_factory)


async def disconnect(database: Database) -> None:
    await database.engine.dispose()


async def ping(database: Database) -> None:
    async with database.session_factory() as session:
        await session.execute(text("SELECT 1"))
