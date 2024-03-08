from datetime import datetime
from typing import Annotated

from geoalchemy2.types import WKBElement
from pydantic import BaseModel, ConfigDict, Field


class VehiclesBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True, arbitrary_types_allowed=True
    )
    geom: Annotated[str, WKBElement] = Field(description="Координаты")
    speed: int = Field(description="Скорость")
    gps_time: datetime = Field(description="Метка времени")
    vehicle_id: int = Field(description="Идентификатор авто")


class VehiclesDB(VehiclesBase):
    id: int
