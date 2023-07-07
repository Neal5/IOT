import logging
from scripts.fastapi.DB.pysql.pysql import Item1
from scripts.fastapi.schemas.db_schema import Item2
from fastapi import status,HTTPException
from scripts.fastapi.DB.database import SessionLocal
import pandas as pd
import uuid
import json
db=SessionLocal()
class handling:
        def newentry(item):
            """ A function that calls the newentry function from handling which takes one entry and inserts it into the database
            params: one item according to the format of the table
            returns:success and the entry that has just been inserted else Failed and exception
            """
            try:
                data = json.loads(item)

                converted_data = {}

                for item in data:
                    parameter = item["Parameter"]
                    value = item["random_values"]
                    converted_data[parameter] = value
                
                new_item=Item1(
                    kW=converted_data["kW"],
                    kWh=converted_data["kWh"],
                    Current=converted_data["Current "],
                    Voltage=converted_data["Voltage"],
                )

                db.add(new_item)
                db.commit()
                return new_item
            except Exception as e:
                logging(e)