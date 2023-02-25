from passlib.context import CryptContext
from passlib.exc import UnknownHashError
from passlib.hash import bcrypt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str) -> str:
        hashedPassword = pwd_context.hash(password)
        return hashedPassword
    

    def verify(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password,hashed_password) 