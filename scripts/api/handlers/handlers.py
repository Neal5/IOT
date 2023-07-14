import logging
from scripts.api.DB.pysql.pysql import ItemSqlalchemy,SqlAlchemyOauth
from scripts.api.DB.database import SessionLocal
import json
import os
import jwt
from fastapi.responses import FileResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt
from fastapi import Depends, HTTPException,status
from scripts.api.schemas.db_schema import PydanticOauth
JWT_SECRET = 'qI6yeXKBzAi8SqQ7gFWfmk2hm39vdTOT55MpcEMAN3Ms48wtwP-NOiwIAWk-7ph-iKEv_zUO3hrKFt0KCF5iCyFV0cDBnDbZrCAe1_C72803vQ9yii3gGN3N8AztO6EZgMCGwmqCIvYS4uhYO2zENgc-0MH_KP0qENalavOSa9M'
db=SessionLocal()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
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
    
    async def authenticate_user(username: str, password: str):
        """ A function that checks whether or not the username and password entered match the entry in the database
        params: username,password
        returns: User if the credentials match and false if they dont 
        """
        try:
            user = db.query(SqlAlchemyOauth).filter(SqlAlchemyOauth.username==username).first()
            if not user:
                return False 
            if not bcrypt.verify(password, user.password_hash):
                return False
            return user
        except Exception as e:
            logging.exception(e) 
    
    async def get_current_user(token: str = Depends(oauth2_scheme)):
        """ A function to return the current user given their token 
        params: jwt token
        returns:Current user their id and their hashed password
        """
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
            user = await SqlAlchemyOauth.get(id=payload.get('id'))
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail='Invalid username or password'
            )
                

        return await PydanticOauth(user)
    def report(device):
        """ A function to check if the given path exists convert it to the correct json format and return that file
        params: The device for which the user wants a report
        returns: A json file containing the report
        """
        try:    
            input_file = 'C:\\Users\\nealparas.mehta\\Desktop\\IOT_proj\\scripts\\Device\\reports\\device_'+device+'.json'
            output_file =  'C:\\Users\\nealparas.mehta\\Desktop\\IOT_proj\\scripts\\Device\\reports\\formatted_report.json'

            data = []
            with open(input_file, 'r') as f:
                for line in f:
                    record = json.loads(line)
                    data.append(record)

            with open(output_file, 'w') as f:
                json.dump(data, f, indent=4)

            print("JSON conversion complete. Output file: {}".format(output_file))
            if os.path.exists(output_file):
                return FileResponse(path=output_file, filename="device_"+device+".json", media_type='file/json')
            return {"message": "File not found"}
        except Exception as e:
            logging.exception(e)
 
    async def token_genration(form_data):
        """ A function that takes the form data that contains the username and if it matches the details stored in the database it returns a jwt token
        params: form_data
        returns: A success if a token has been genrated
        """
        try:
            user = await Handling.authenticate_user(form_data.username, form_data.password)

            if not user:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, 
                    detail='Invalid username or password'
                )
            user_obj = PydanticOauth.from_orm(user)
            token = jwt.encode(user_obj.dict(), JWT_SECRET)
            return "success"
        except Exception as e:
            logging.exception(e)
