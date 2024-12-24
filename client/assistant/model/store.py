from pydantic import BaseModel


class Coordinates(BaseModel):
    lat: float
    lon: float

class Store(BaseModel):
    guid: str
    name: str
    address: str
    division: str
    coordinates: Coordinates


class StoreResponse(BaseModel):
    stores: list[Store]
