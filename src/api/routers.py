from fastapi import APIRouter

from src.api.endpoints import vehicles_router

main_router = APIRouter()

main_router.include_router(
    vehicles_router,
    prefix="/vehicles",
    tags=["vehicles"],
)
