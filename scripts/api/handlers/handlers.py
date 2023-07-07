import logging
from scripts.api.DB.pysql.pysql import ItemSqlalchemy
from scripts.api.DB.database import SessionLocal
import json
import os 
from fastapi.responses import FileResponse
from scripts.Device.reports.report_generator import GenerateReports

db=SessionLocal()
class Handling:
        def new_entry(item):
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
                
                new_item=ItemSqlalchemy(
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
                logging.exception(e)
            
        def report():
            """ A function to check if the given path exists and to return that file
            params: NA
            returns: A CSV file containing the reports else Failed and the exception
            """
            file_path = 'C:\\Users\\nealparas.mehta\\Desktop\\IOT\\scripts\\reports\\report.csv'
            try:    
                GenerateReports.create_report()
                if os.path.exists(file_path):
                    return FileResponse(path=file_path, filename=file_path, media_type='application/csv')
                return {"message": "File not found"}
            except Exception as e:
                logging.exception(e)
