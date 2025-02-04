from pydantic import BaseModel


class HoleReport(BaseModel):
    lon: float
    lat: float
    locname: str

