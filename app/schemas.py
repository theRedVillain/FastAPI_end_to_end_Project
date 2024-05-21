from pydantic import BaseModel 
from datetime import datetime


class posts_data(BaseModel):
    title : str 
    description : str


class posts_response(BaseModel):
    title : str 
    created_at : datetime 
    class Config:
        orm_mode = True 

