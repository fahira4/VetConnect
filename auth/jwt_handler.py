from datetime import datetime, timedelta
from jose import jwt
from typing import Optional

# Kunci rahasia (bebas kamu ubah, tapi jangan kasih tahu siapa-siapa)
SECRET_KEY = "RAHASIA_UTSPEMWEBLANJUTAN_FAKHIRA"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # Token hangus dalam 30 menit

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt