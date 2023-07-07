from sqlalchemy.sql.expression import null
# from scripts.db.database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text
from pydantic import BaseModel



class Item2(BaseModel): #serializer
    kW: float
    kWh: float
    Current: float
    Voltage: float

    class Config:
        orm_mode=True