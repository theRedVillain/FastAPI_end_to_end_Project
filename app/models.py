from .database import Base 
from sqlalchemy import Column , String , Integer , func , TIMESTAMP


class Posts(Base):
    __tablename__ = "Posts" 

    id = Column(Integer, primary_key=True , autoincrement=True) 
    title = Column(String , nullable = False) 
    description = Column(String , nullable = False) 
    created_at = Column(String , nullable = False , server_default=func.now())

