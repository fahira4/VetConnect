from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# Import gembok keamanan dari dependencies
from dependencies import oauth2_scheme

from models import medical as medical_models
from models import pet as pet_models
from schemas import medical as medical_schemas
from database import get_db

router = APIRouter(
    prefix="/medical",
    tags=["Medical Records"]
)

# Menambahkan gembok (token) agar hanya admin yang bisa tambah rekam medis
@router.post("/{pet_id}", response_model=medical_schemas.MedicalRecordResponse)
def create_medical_record(
    pet_id: int, 
    record: medical_schemas.MedicalRecordCreate, 
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme) # <--- Gembok dipasang di sini
):
    # Cek apakah hewan dengan ID tersebut ada
    db_pet = db.query(pet_models.Pet).filter(pet_models.Pet.id == pet_id).first()
    if not db_pet:
        raise HTTPException(status_code=404, detail="Data hewan tidak ditemukan")
    
    db_record = medical_models.MedicalRecord(**record.model_dump(), pet_id=pet_id)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

@router.get("/", response_model=List[medical_schemas.MedicalRecordResponse])
def read_all_medical_records(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    records = db.query(medical_models.MedicalRecord).offset(skip).limit(limit).all()
    return records

# ==========================================
# TAMBAHAN FITUR: READ BY ID, UPDATE, DELETE
# ==========================================

# 1. READ BY ID (Melihat detail 1 rekam medis saja)
@router.get("/{record_id}", response_model=medical_schemas.MedicalRecordResponse)
def read_medical_record_by_id(record_id: int, db: Session = Depends(get_db)):
    db_record = db.query(medical_models.MedicalRecord).filter(medical_models.MedicalRecord.id == record_id).first()
    if not db_record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rekam medis tidak ditemukan")
    return db_record

# 2. UPDATE (Mengubah rekam medis - Dilindungi Token)
@router.put("/{record_id}", response_model=medical_schemas.MedicalRecordResponse)
def update_medical_record(
    record_id: int, 
    record_data: medical_schemas.MedicalUpdate, 
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme) # Gembok
):
    db_record = db.query(medical_models.MedicalRecord).filter(medical_models.MedicalRecord.id == record_id).first()
    if not db_record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rekam medis tidak ditemukan")
    
    # Menggunakan model_dump khusus Pydantic v2
    update_data = record_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_record, key, value)
    
    db.commit()
    db.refresh(db_record)
    return db_record

# 3. DELETE (Menghapus rekam medis - Dilindungi Token)
@router.delete("/{record_id}")
def delete_medical_record(
    record_id: int, 
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme) # Gembok
):
    db_record = db.query(medical_models.MedicalRecord).filter(medical_models.MedicalRecord.id == record_id).first()
    if not db_record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rekam medis tidak ditemukan")
    
    db.delete(db_record)
    db.commit()
    return {"message": f"Rekam medis dengan ID {record_id} berhasil dihapus"}