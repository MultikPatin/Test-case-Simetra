from src.core.db.database import Database
from src.core.db.models import Vehicles
from src.core.db.repositories.base import BaseRepository


class VehiclesRepository(BaseRepository):
    def __init__(self, database: Database):
        super().__init__(database, Vehicles)
