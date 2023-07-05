from pydantic import BaseModel

class Item2(BaseModel): #serializer
    kW: float
    kWh: float
    Current: float
    Voltage: float

    class Config:
        orm_mode=True