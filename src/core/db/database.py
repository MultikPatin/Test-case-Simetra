import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.core.configs.postgres import PostgresSettings

logger = logging.getLogger(__name__)


def get_async_session_factory(
    settings: PostgresSettings,
) -> async_sessionmaker:
    return async_sessionmaker(
        create_async_engine(settings.postgres_connection_url, echo=True),
        expire_on_commit=False,
    )


class Database:
    def __init__(self, settings: PostgresSettings) -> None:
        self._async_session_factory = get_async_session_factory(settings)

    @asynccontextmanager
    async def get_session(self) -> AsyncIterator[AsyncSession]:
        try:
            session = self._async_session_factory()
            yield session
        except Exception as error:
            logger.exception("Session rollback because of exception", error)
            await session.rollback()
            raise
        finally:
            await session.close()
