from sqlalchemy import func, select

from src.core.db.database import Database
from src.core.db.models import Vehicles
from src.core.db.repositories.base import BaseRepository


class VehiclesRepository(BaseRepository):
    def __init__(self, database: Database):
        super().__init__(database, Vehicles)

    async def get_all_vehicles_with_last_geometry(
        self,
    ) -> list[Vehicles]:
        async with self._database.get_session() as session:
            sq = select(self._model).subquery()
            q = (
                select(
                    func.max(self._model.gps_time).label("gps_time"),
                    self._model.vehicle_id,
                )
                .group_by(self._model.vehicle_id)
                .join(
                    sq,
                    Vehicles.vehicle_id == sq.c.vehicle_id,
                )
            )

            db_objs = await session.execute(q)
            db_objs = db_objs.all()
            for db_obj in db_objs:
                print(db_obj)
                db_obj.geom = self.get_correct_geom_field(db_obj.geom)
            return db_objs

    async def get_vehicles_with_last_geometry_by_id(
        self, vehicle_id: int
    ) -> Vehicles:
        pass
