from fastapi import APIRouter, Depends, HTTPException, status

from blog.hashing import Hash
from .. import database, schemas, models
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from passlib.hash import bcrypt


router = APIRouter(
    prefix='/login',
    tags=['Authentication'],
)
 


@router.post('/')
async def login(request: schemas.Login, db: Session = Depends(database.get_db)):
        user = db.query(models.User).filter(models.User.email == request.username).first()

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid username')
        
        if not Hash.verify_password(user.password, request.password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'incorrect password')
        return user 