from fastapi import FastAPI
from blog import models
from blog.routers import users, blog, authentication
from .database import engine



app = FastAPI()


app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(blog.router)


models.Base.metadata.create_all(bind=engine)






# @app.post('/user', response_model=schemas.ShowUser, tags=['users'])
# def create_user(request: schemas.User, db:Session = Depends(get_db)):   
#     new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user 



# @app.get('/user/{id}', response_model=schemas.ShowUser, tags=['users'])
# def get_user(id:int, db:Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id==id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User not found')
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'detail':f'Blog with id {id} not available'}
#     return user


# @app.get('/users', tags=['users'])
# def get_users(db:Session = Depends(get_db)):
#     users = db.query(models.User).all()
#     if not users:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No user found')
#     return users