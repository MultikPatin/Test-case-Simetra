from datetime import datetime

from geoalchemy2 import Geometry
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.core.db.models import Base


class Vehicles(Base):
    __tablename__ = "vehicles"

    geom: Mapped[Geometry] = mapped_column(Geometry("POINT", srid=4269))
    speed: Mapped[int] = mapped_column()
    gps_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    vehicle_id: Mapped[int] = mapped_column()
