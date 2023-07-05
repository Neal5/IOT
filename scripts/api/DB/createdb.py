from database import postgres_base,engine
from sqlalchemy import Column,Float,TIMESTAMP

# from models import Item

print("Creating database ....")


class Item(postgres_base):
    __tablename__='timescale_iot'
    datetime=Column(TIMESTAMP,nullable=False)
    kW=Column(Float,nullable=False,primary_key=True)
    kWh=Column(Float,nullable=False)
    Current=Column(Float,nullable=False)
    Voltage=Column(Float,nullable=False)

postgres_base.metadata.create_all(engine)