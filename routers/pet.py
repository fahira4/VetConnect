from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from dependencies import oauth2_scheme
from models import pet as pet_models
from schemas import pet as pet_schemas
from database import get_db

router = APIRouter(
    prefix="/pets",
    tags=["Pets"]
)

@router.post("/", response_model=pet_schemas.PetResponse)
def create_pet(
    pet: pet_schemas.PetCreate, 
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme) 
):
    db_pet = pet_models.Pet(**pet.model_dump())
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

@router.get("/", response_model=List[pet_schemas.PetResponse])
def read_pets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pets = db.query(pet_models.Pet).offset(skip).limit(limit).all()
    return pets

@router.get("/{pet_id}", response_model=pet_schemas.PetResponse)
def read_pet_by_id(pet_id: int, db: Session = Depends(get_db)):
    db_pet = db.query(pet_models.Pet).filter(pet_models.Pet.id == pet_id).first()
    if not db_pet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data hewan tidak ditemukan")
    return db_pet

@router.put("/{pet_id}", response_model=pet_schemas.PetResponse)
def update_pet(
    pet_id: int, 
    pet_data: pet_schemas.PetUpdate, 
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme) 
):
    db_pet = db.query(pet_models.Pet).filter(pet_models.Pet.id == pet_id).first()
    if not db_pet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data hewan tidak ditemukan")

    update_data = pet_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_pet, key, value)
    
    db.commit()
    db.refresh(db_pet)
    return db_pet

@router.delete("/{pet_id}")
def delete_pet(
    pet_id: int, 
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme) 
):
    db_pet = db.query(pet_models.Pet).filter(pet_models.Pet.id == pet_id).first()
    if not db_pet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data hewan tidak ditemukan")
    
    db.delete(db_pet)
    db.commit()
    return {"message": f"Data hewan dengan ID {pet_id} berhasil dihapus"}