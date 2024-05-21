from .database import Base 
from sqlalchemy import Column , String , Integer , func , TIMESTAMP


class Posts(Base):
    __tablename__ = "Posts" 

    id = Column(Integer, primary_key=True , autoincrement=True) 
    title = Column(String , nullable = False) 
    description = Column(String , nullable = False) 
    created_at = Column(TIMESTAMP(timezone=True) , nullable = False , server_default=func.now())

class Users(Base):
    __tablename__ = "Users" 

    id = Column(Integer , primary_key=True, autoincrement=True) 
    email = Column(String , nullable = False , unique=True) 
    password = Column(String , nullable = False) 
    onboarding_date = Column(TIMESTAMP(timezone=True) , server_default=func.now() , nullable = False) 

    