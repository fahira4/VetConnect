from pydantic import BaseModel
from typing import Optional 

class MedicalRecordBase(BaseModel):
    diagnosis: str
    treatment: str
    date: str 

class MedicalRecordCreate(MedicalRecordBase):
    pass

class MedicalRecordResponse(MedicalRecordBase):
    id: int
    pet_id: int

    class Config:
        from_attributes = True

class MedicalUpdate(BaseModel):
    diagnosis: Optional[str] = None
    treatment: Optional[str] = None
    date: Optional[str] = None