from fastapi import FastAPI

from src.api.routers import main_router
from src.core.configs import api_settings

app = FastAPI(title=api_settings.title, description=api_settings.description)

app.include_router(main_router)
