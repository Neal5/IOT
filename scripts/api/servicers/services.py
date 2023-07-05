from scripts.api.handlers.handlers import handling
from scripts.api.schemas.response_schema import DefaultFailureResponse, DefaultResponse
from fastapi import FastAPI, Request,File, UploadFile,APIRouter
from fastapi.responses import FileResponse
import os
import logging

# user = APIRouter()

class service:
    def create_an_item(item):
        """ A function that calls the newentry function from handling which takes one entry and inserts it into the database
        params: one item according to the format of the table
        returns:success and the entry that has just been inserted else Failed and exception
        """
        try:
            # new_item = handling.newentry(item)

            # return handling.newentry(item)
            return DefaultResponse(message="Success", data=handling.newentry(item))
        except Exception as e:
            # print(e)
            return DefaultFailureResponse(
                message="Failed", error=str(e)
            ).dict()
        

    """File upload,download"""
    # async def download(name: str):
    #     try:
    #         file_path = "C:\\Users\\nealparas.mehta\\Desktop\\IOT" + name + "csv"
    #         if os.path.exists(file_path):
    #             return FileResponse(path=file_path, filename=file_path, media_type='application/csv')
    #         return {"message": "File not found"}
    #     except Exception as e:
    #         logging.exception(e)
        
    # async def upload(name: str, file: UploadFile = File(...)):
    #     try:
    #         filename = "C:\Users\nealparas.mehta\Desktop\IOT" + name + ".csv"
    #         with open(filename, 'wb') as f:
    #             while contents := file.file.read(1024 * 1024):
    #                 f.write(contents)
    #     except Exception as e:
    #         logging.exception(e)
    #     finally:
    #         file.file.close()
    

    