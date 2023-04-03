from fastapi import APIRouter, Depends, status, HTTPException

from blog import oauth2
from ..routers import users
from .. import database, schemas, models
from sqlalchemy.orm import Session
# from ..hashing import Hash 
from typing import List
from ..repositories import blog
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm



router = APIRouter(
    prefix='/blog',
    tags=['Blogs'],
)


get_db = database.get_db


@router.post('/')
def create(request: schemas.Blog, db:Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
    return blog.create(request, db) 


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id:int, db:Session = Depends(get_db)):
    return blog.delete(id, db)



@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)



@router.get('/', response_model = List[schemas.ShowBlog])
def get_all(db: Session = Depends(get_db)):
    return blog.get_all(db)




@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show_blog(id: int, db: Session = Depends(get_db)):
    return blog.show(id, db)

