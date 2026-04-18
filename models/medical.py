from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import datetime

class MedicalRecord(Base):
    __tablename__ = "medical_records"

    id = Column(Integer, primary_key=True, index=True)
    diagnosis = Column(String)
    treatment = Column(String)
    date = Column(String)
    
    pet_id = Column(Integer, ForeignKey("pets.id"))

    pet = relationship("Pet", back_populates="records")