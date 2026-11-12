"""Unit of work wrapping one AsyncSession."""

from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from cursor_switch.adapters.persistence.repositories import ModelRepository, SettingsRepository


@dataclass
class UnitOfWork:
    session: AsyncSession

    @property
    def models(self) -> ModelRepository:
        return ModelRepository(self.session)

    @property
    def settings(self) -> SettingsRepository:
        return SettingsRepository(self.session)


class UnitOfWorkFactory:
    def __init__(self, factory: async_sessionmaker[AsyncSession]) -> None:
        self._factory = factory

    @asynccontextmanager
    async def begin(self) -> AsyncIterator[UnitOfWork]:
        session = self._factory()
        try:
            yield UnitOfWork(session)
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
