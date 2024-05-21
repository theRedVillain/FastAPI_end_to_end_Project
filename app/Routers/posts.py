from fastapi import APIRouter , Depends , status , HTTPException
from typing import List
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models , schemas



posts_router = APIRouter(
    prefix="/posts" ,
    tags = ['Posts']
) 

@posts_router.get("/all_posts" , response_model = List[schemas.posts_response])
def get_all_post(db: Session = Depends(get_db)):
    result = db.query(models.Posts).all()
    return result 

@posts_router.post("/make_a_post" , status_code=status.HTTP_201_CREATED , response_model=schemas.posts_response)
def make_a_post_func(posts_data : schemas.posts_data , db: Session = Depends(get_db)):
    new_post = models.Posts(**posts_data.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post 

@posts_router.get("/get_one_post/{id}" , status_code=status.HTTP_200_OK ,response_model=schemas.posts_response)
def get_one_post(id : int , db: Session = Depends(get_db)):
    response = db.query(models.Posts).filter(models.Posts.id == id).first() 

    if response == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail = "Post not found") 
    return response

@posts_router.delete("/delete_post/{id}" , status_code = status.HTTP_204_NO_CONTENT)
def delete_post_func(id : int , db: Session = Depends(get_db)):
    response = db.query(models.Posts).filter(models.Posts.id == id).first()
    if response == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail = "No Such Post") 
    db.delete(response)
    db.commit()  

@posts_router.put("/update_post/{id}" , status_code=status.HTTP_200_OK , response_model=schemas.posts_response) 
def update_function(id : int, update_data : schemas.posts_data , db: Session = Depends(get_db)):
    post = db.query(models.Posts).filter(models.Posts.id == id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail = "No Such Post")
    post.update(update_data.dict())
    db.commit() 
    # db.refresh(post)
    return post.first()
