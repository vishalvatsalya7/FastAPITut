from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hashing:

    def bcrypt(self,  password: str):
        hashedPassword = pwd_context.hash(password)
        return hashedPassword

    def verify(self, userPassword: str, requestPassword: str):
        return pwd_context.verify(requestPassword, userPassword)