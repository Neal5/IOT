from database import postgres_base,engine
from sqlalchemy import Column,Float,TIMESTAMP,Integer,String

print("Creating database ....")


class Item(postgres_base):
    __tablename__='timescale_iot'
    datetime=Column(TIMESTAMP,nullable=False)
    kW=Column(Float,nullable=False,primary_key=True)
    kWh=Column(Float,nullable=False)
    Current=Column(Float,nullable=False)
    Voltage=Column(Float,nullable=False)

class SqlAlchemyOauth(postgres_base):
    __tablename__='users'
    id = Column(Integer,primary_key=True)
    username = Column(String(50), unique=True)
    password_hash = Column(String(128))

postgres_base.metadata.create_all(engine)