import asyncio

import pytest

from app.core.config import MySQLSettings
from app.core.db import Database


def test_open_starts_once_and_borrows_distinct_sessions(monkeypatch: pytest.MonkeyPatch) -> None:
    database = Database("db", MySQLSettings(enabled=True))
    starts = 0
    startup = Database.startup

    async def counted_startup(self: Database) -> None:
        nonlocal starts
        starts += 1
        await startup(self)

    monkeypatch.setattr(Database, "startup", counted_startup)

    async def borrow() -> tuple[int, object]:
        async with database.open() as session:
            assert session.bind is not None
            return id(session), session.bind

    async def run() -> None:
        try:
            first, second = await asyncio.gather(borrow(), borrow())
        finally:
            await database.shutdown()
        assert starts == 1
        assert first[0] != second[0]
        assert first[1] is second[1]

    asyncio.run(run())
