from fastapi import APIRouter , Depends ,  status
from typing import List
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models , schemas



user_router = APIRouter(
    prefix="/users" ,
    tags = ['Users']
) 