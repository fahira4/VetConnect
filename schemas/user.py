from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    # Perhatikan: Kita TIDAK mengembalikan password di Response demi keamanan!

    class Config:
        from_attributes = True