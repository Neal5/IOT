from pydantic import BaseModel
from passlib.hash import bcrypt
class ItemPydantic(BaseModel): #serializer
    kW: float
    kWh: float
    Current: float
    Voltage: float

    class Config:
        orm_mode=True

class PydanticOauth(BaseModel):
    id: int
    username: str
    password_hash: str

    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)
    
    class Config:
        orm_mode=True