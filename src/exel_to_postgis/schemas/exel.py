from dataclasses import dataclass


@dataclass(frozen=True)
class ExelRow:
    id: int
    longitude: str
    latitude: str
    speed: int
    gps_time: str
    vehicle_id: int

    @property
    def get_point(self):
        return f"POINT({self.longitude} {self.latitude})"
