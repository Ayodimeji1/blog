from fastapi import APIRouter, Depends, status, HTTPException
from ..routers import users
from .. import database, schemas, models
from sqlalchemy.orm import Session
from ..hashing import Hash 
from typing import List



router = APIRouter()
get_db = database.get_db


@router.post('/blog', tags=['blogs'])
def create(request: schemas.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 


@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
def destroy(id, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f'Blog with id {id} notfound')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'deleted'


@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f'Blog with id {id} notfound')
    blog.update({'title':request.title, 'body':request.body})
    db.commit()
    return 'updated'



@router.get('/blog', response_model = List[schemas.ShowBlog], tags=['blogs'])
def get_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No blogs found')
    return blogs

@router.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=['blogs'])
def show_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not available')
    return blog

