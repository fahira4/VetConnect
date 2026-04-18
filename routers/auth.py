from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from database import get_db
from models import user as user_models
from schemas import user as user_schemas
from auth import utils, jwt_handler

router = APIRouter(tags=["Authentication"])

# 1. Endpoint Registrasi Dokter Baru
@router.post("/register", response_model=user_schemas.UserResponse)
def register(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    # Cek apakah username sudah dipakai
    db_user = db.query(user_models.User).filter(user_models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username sudah terdaftar")
    
    # Simpan dengan password yang sudah di-hash (diacak)
    new_user = user_models.User(
        username=user.username,
        password=utils.hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# 2. Endpoint Login untuk dapat Token
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(user_models.User).filter(user_models.User.username == form_data.username).first()
    
    if not user or not utils.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Username atau password salah")
    
    # Buat token kartu akses
    access_token = jwt_handler.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}