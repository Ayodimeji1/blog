from passlib.context import CryptContext
from passlib.hash import bcrypt

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def verify_password(plain_password, hashed_password):
        return password_context.verify(plain_password, hashed_password)
    
    def bcrypt(password):
        return password_context.hash(password)

          