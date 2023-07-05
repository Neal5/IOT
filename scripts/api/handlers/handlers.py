import logging
from scripts.api.DB.pysql.pysql import Item1
from scripts.api.DB.database import SessionLocal
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
                    datetime="now()",
                    kw=converted_data["kW"],
                    kwh=converted_data["kWh"],
                    current=converted_data["Current "],
                    voltage=converted_data["Voltage"],
                )

                db.add(new_item)
                db.commit()
                return new_item
            except Exception as e:
                logging(e)