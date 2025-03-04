import hashlib

def encode(plain_text_password: str) -> str:
    return hashlib.md5(plain_text_password.encode('utf-8'), usedforsecurity=True).hexdigest()

