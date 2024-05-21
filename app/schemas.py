from pydantic import BaseModel , EmailStr
from datetime import datetime


class posts_data(BaseModel):
    title : str 
    description : str


class posts_response(BaseModel):
    title : str 
    created_at : datetime 
    class Config:
        orm_mode = True 
class users_data(BaseModel):
    email : EmailStr
    password : str

class users_response(BaseModel):
    email : str
    onboarding_date : datetime 
    class Config:
        orm_mode = True 

class User_Email(BaseModel):
    email : EmailStr 

class update_user_password(users_data):
    pass


