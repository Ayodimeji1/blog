from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import database, schemas, models, oauth2, utils
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/login',
    tags=['Authentication'],
)
# schemas.Login

@router.post('/')
async def login(request: OAuth2PasswordRequestForm = Depends() , db: Session = Depends(database.get_db)):
        user = db.query(models.User).filter(models.User.email == request.username).first()

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid credentials')
        
        if not utils.verify(request.password, user.password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid credentials')    
        
        access_token = oauth2.create_access_token(data={"user_id": user.id})

        return {"access_token": access_token, "token_type": "bearer"}
        