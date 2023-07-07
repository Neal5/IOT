from scripts.fastapi.DB.database import postgres_base,engine
from sqlalchemy import String,Boolean,Integer,Column,Text,Float
from sqlalchemy import create_engine
class Item1(postgres_base):
    __tablename__='Data'
    kW=Column(Float,nullable=False,primary_key=True)
    kWh=Column(Float,nullable=False)
    Current=Column(Float,nullable=False)
    Voltage=Column(Float,nullable=False)