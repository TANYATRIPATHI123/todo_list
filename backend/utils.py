#import hashlib
from passlib.context import CryptContext
import bcrypt, uuid
bcrypt.__about__ = bcrypt
pwd_context = CryptContext(schemes=['bcrypt'])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def encode(plain_text_password: str) -> str:
    return pwd_context.hash(plain_text_password)

def verify_password(plain_text_password: str, encoded_password: str) -> bool:
    return pwd_context.verify(plain_text_password, encoded_password)

def generate_session_token() -> str:
    return 