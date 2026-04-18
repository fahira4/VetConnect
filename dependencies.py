from fastapi.security import OAuth2PasswordBearer

# Letakkan gembok di sini agar bisa dipakai semua file tanpa tabrakan
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")