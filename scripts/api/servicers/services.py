from scripts.api.handlers.handlers import Handling
from scripts.api.schemas.response_schema import DefaultFailureResponse, DefaultResponse
from fastapi import FastAPI,Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from scripts.Device.data_generator.Data_Genrator import GenerateData
from scripts.api.DB.database import SessionLocal
import logging
from scripts.Device.data_generator.Data_Genrator import GenerateData

user = FastAPI()
db=SessionLocal()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

class Service:
    def create_an_item(item):
        """ A function that calls the newentry function from handling which takes one entry and inserts it into the database
        params: one item according to the format of the table
        returns:success and the entry that has just been inserted else Failed and exception
        """
        try:
            return DefaultResponse(message="Success", data=Handling.new_entry(item))
        except Exception as e:
            return DefaultFailureResponse(
                message="Failed", error=str(e)
            ).dict()

    @user.get("/")
    async def download_file(device_name,token: str = Depends(oauth2_scheme)):
        """ A function that calls the report function from handling which return a json file containing the report
        params: NA
        returns: A json file containing the reports else Failed and the exception
        """
        try:
            return Handling.report(device_name)
        except Exception as e:
            return DefaultFailureResponse(
                    message="Failed", error=str(e)
                ).dict()
        
    @user.post('/token')
    async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
        """ A function that takes the form data that contains the username and if it matches the details stored in the database it returns a jwt token
        params: form_data
        returns: A success if a token has been genrated
        """
        try:
            return(Handling.token_genration)
        except Exception as e:
            logging.exception(e)

    @user.post("/simdata")
    async def sim_devices(no,token: str = Depends(oauth2_scheme)):
        """ A function that calls the report function from handling which return a json file containing the report
        params: NA
        returns: A json file containing the reports else Failed and the exception
        """
        try:
            GenerateData.simulate_data_fastapi(no)
            return Handling.report("m")
        except Exception as e:
            return DefaultFailureResponse(
                    message="Failed", error=str(e)
                ).dict()
    # @user.post('/users')
    # async def create_user(user: PydanticOauth):
    #     try:
    #         db_item = db.query(SqlAlchemyOauth).filter(SqlAlchemyOauth.id==user.id).first()
            
    #         if db_item is not None:
    #             return HTTPException(status_code=400,detail="Item already exists")
    #         new_item=SqlAlchemyOauth(
    #             id=user.id,
    #             username=user.username,
    #             password_hash=bcrypt.hash(user.password_hash)
    #         )
    #         db.add(new_item)
    #         db.commit()
    #         return new_item
    #     except Exception as e:
    #         logging.exception(e)

    @user.post('/create-data-a')
    async def sim_data(ttl,token: str = Depends(oauth2_scheme)):
        """ A function that takes in the ttl(time to live in minutes) and generates data for device a every 10 second for that amount of time
        params: time to live
        returns: generates the data and writes it into a the json file for device a
        """
        try:
            GenerateData.simulate_data_a(ttl)
        except Exception as e:
            logging.exception(e)

        

    