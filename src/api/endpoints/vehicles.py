from fastapi import APIRouter

from src.api.schemas.vehicles import VehiclesDB
from src.core.configs import postgres_settings
from src.core.db.database import Database
from src.core.db.repositories.vehicles import VehiclesRepository

router = APIRouter()

database = Database(postgres_settings)
vehicles_repository = VehiclesRepository(database)


@router.get(
    "/",
    response_model=list[VehiclesDB],
)
async def get_all_vehicles_with_last_geometry():
    db_objs = vehicles_repository.get_all_vehicles_with_last_geometry()
    return await db_objs


# @router.get(
#     "/{vehicle_id}",
#     response_model=VehiclesDB,
# )
# async def get_all_vehicles_with_last_geometry(vehicle_id: int):
#     db_obj = vehicles_repository.get_vehicles_with_last_geometry_by_id(
#         vehicle_id
#     )
#     return await db_obj
