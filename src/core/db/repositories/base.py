from typing import TypeVar

from geoalchemy2.shape import to_shape
from geoalchemy2.types import WKBElement
from sqlalchemy import select

from src.core.db.database import Database
from src.core.db.models import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository:
    """Абстрактный класс, для реализации паттерна Repository."""

    _database: Database
    _model: Base

    def __init__(self, database: Database, model: ModelType) -> None:
        self._database = database
        self._model = model

    async def get_all(self) -> list[ModelType]:
        async with self._database.get_session() as session:
            db_objs = await session.execute(select(self._model))
            db_objs = db_objs.scalars().all()[:10]
            for db_obj in db_objs:
                db_obj.geom = self.get_correct_geom_field(db_obj.geom)
            return db_objs

    async def get_or_none(self, instance_id: int) -> ModelType | None:
        async with self._database.get_session() as session:
            db_obj = await session.execute(
                select(self._model).where(self._model.id == instance_id)
            )
            db_obj = db_obj.scalars().first()
            db_obj.geom = self.get_correct_geom_field(db_obj.geom)
            return db_obj

    @staticmethod
    def get_correct_geom_field(geom):
        if isinstance(geom, str):
            geom = WKBElement(geom)
        return to_shape(geom).wkt
