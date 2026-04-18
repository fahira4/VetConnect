from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True) # Username tidak boleh kembar
    password = Column(String) # Nanti akan kita simpan dalam bentuk sandi acak (Hash)