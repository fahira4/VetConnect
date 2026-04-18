from pydantic import BaseModel
from typing import List, Optional
from schemas.medical import MedicalRecordResponse

class PetBase(BaseModel):
    name: str
    species: str
    breed: str
    owner_name: str

class PetCreate(PetBase):
    pass

class PetResponse(PetBase):
    id: int
    records: List[MedicalRecordResponse] = []

    class Config:
        from_attributes = True

class PetUpdate(BaseModel):
    name: Optional[str] = None
    species: Optional[str] = None
    breed: Optional[str] = None
    owner_name: Optional[str] = None