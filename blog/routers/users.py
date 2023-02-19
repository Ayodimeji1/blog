from fastapi import APIRouter, Depends, status, HTTPException
from ..routers import users
from .. import database, schemas, models
from sqlalchemy.orm import Session
from ..hashing import Hash 



router = APIRouter(
    prefix='/user',
    tags=['Users'],
)
get_db = database.get_db



@router.get('/')
def get_users(db:Session = Depends(get_db)):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No user found')
    return users



@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db:Session = Depends(get_db)):   
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user 



@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User not found')
    return user

