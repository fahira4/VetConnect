from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    species = Column(String) 
    breed = Column(String)   
    owner_name = Column(String) 

    records = relationship("MedicalRecord", back_populates="pet")