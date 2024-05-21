from fastapi import FastAPI 
from typing import Optional
from .database import Base , get_db , engine
from . import models , schemas
from .Routers import posts_router  , user_router

app = FastAPI() 
models.Base.metadata.create_all(bind=engine)
get_db()  

app.include_router(posts_router)
app.include_router(user_router)





