from fastapi import APIRouter, Depends, status, HTTPException
from ..routers import users
from .. import database, schemas, models
from sqlalchemy.orm import Session
from ..hashing import Hash 
from ..repositories import user



router = APIRouter(
    prefix='/user',
    tags=['Users'],
)
get_db = database.get_db



@router.get('/')
def get_users(db:Session = Depends(get_db)):
    return user.get_all(db)



@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db:Session = Depends(get_db)):   
    return user.create(request, db)



@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db:Session = Depends(get_db)):
    return user.get_one(id, db)

