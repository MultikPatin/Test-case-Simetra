from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.database import Database
from src.core.db.models import Base


class BaseRepository:
    """Абстрактный класс, для реализации паттерна Repository."""

    _database: Database
    _model: Base

    def __init__(self, database: Database, model: Base) -> None:
        self._database = database
        self._model = model

    async def get_all(self, session: AsyncSession = None) -> list[Base]:
        async with self._database.get_session(session) as session:
            objects = await session.execute(select(self._model))
            return objects.scalars().all()

    async def get_or_none(
        self, instance_id: int, session: AsyncSession = None
    ) -> Base | None:
        async with self._database.get_session(session) as session:
            db_obj = await session.execute(
                select(self._model).where(self._model.id == instance_id)
            )
            return db_obj.scalars().first()
