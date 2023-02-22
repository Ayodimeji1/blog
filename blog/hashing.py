from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def verify(plain_password, hashed_password):
        return pwd_context.verify(plain_password,hashed_password)
    
    def bcrypt(password:str):
        # hashedPassword = pwd_context.hash(password)
        return pwd_context.hash(password)
    

    # def verify(plain_password, hashed_password):
    #     return pwd_context.verify(plain_password,hashed_password)