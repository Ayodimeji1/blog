from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def get_all(db: Session):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No user found')
    return users


def create(request: schemas.User, db:Session):   
    hashed_password = pwd_context.hash(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user 


def get_one(id:int, db:Session):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User not found')
    return user


def delete_user(id:int, db:Session):
    user = db.query(models.User).filter(models.User.id==id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f'Blog with id {id} notfound')
    user.delete(synchronize_session=False)
    db.commit()
    return 'user deleted'    