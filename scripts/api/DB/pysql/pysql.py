from scripts.api.DB.database import postgres_base
from sqlalchemy import Column,Float,TIMESTAMP,Integer,String

class ItemSqlalchemy(postgres_base):
    __tablename__='timescale_iot'
    datetime=Column(TIMESTAMP,nullable=False)
    kw=Column(Float,nullable=False,primary_key=True)
    kwh=Column(Float,nullable=False)
    current=Column(Float,nullable=False)
    voltage=Column(Float,nullable=False)

class SqlAlchemyOauth(postgres_base):
    __tablename__='users'
    id = Column(Integer,primary_key=True)
    username = Column(String(50), unique=True)
    password_hash = Column(String(128))