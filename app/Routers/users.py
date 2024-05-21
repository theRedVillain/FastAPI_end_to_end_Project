from fastapi import APIRouter , Depends ,  status , HTTPException
from typing import List
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models , schemas , utils



user_router = APIRouter(
    prefix="/users" ,
    tags = ['Users']
) 

@user_router.get("/get_all_users" , status_code=status.HTTP_200_OK , response_model= List[schemas.users_response])
def get_all_users(db: Session = Depends(get_db)):
    result = db.query(models.Users).all()  
    return result  

@user_router.post("/create_a_user" , status_code=status.HTTP_201_CREATED , response_model= schemas.users_response)
def user_create_func(user_data:schemas.users_data ,db: Session = Depends(get_db)):
    data = user_data.dict() 
    data['password'] = utils.get_password_hash(data['password']) 
    new_data = models.Users(**data)
    db.add(new_data)
    db.commit() 
    db.refresh(new_data) 
    return new_data 

@user_router.get("/get_one_user" , response_model= schemas.users_response , status_code = status.HTTP_200_OK)
def get_one_user_func(user_email : schemas.User_Email , db: Session = Depends(get_db)):
    response = db.query(models.Users).filter(models.Users.email == user_email.email).first()

    if response == None : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail = "No Such User")

    return response 

@user_router.delete("/delete_user" , status_code = status.HTTP_204_NO_CONTENT)
def delete_function(user_email : schemas.User_Email , db: Session = Depends(get_db)):
    response = db.query(models.Users).filter(models.Users.email == user_email.email)
    if response.first() == None : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail = "No Such User")
    response.delete(synchronize_session=False)
    db.commit()

@user_router.put("/update_user", status_code = status.HTTP_200_OK)
def update_user_func(user_data : schemas.update_user_password , db: Session = Depends(get_db)):
    response = db.query(models.Users).filter(models.Users.email == user_data.email) 
    if response.first() == None : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail = "No Such User")
    data = user_data.dict() 
    data['password']  = utils.get_password_hash(data['password']) 
    response.update(data)
    db.commit()
    return {"Message" : "Updated Successfully"}