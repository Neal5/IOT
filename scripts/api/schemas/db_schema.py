from pydantic import BaseModel

class ItemPydantic(BaseModel): #serializer
    kW: float
    kWh: float
    Current: float
    Voltage: float

    class Config:
        orm_mode=True