from fastapi import FastAPI, Depends, Request # Tambahkan Request
from fastapi.responses import HTMLResponse # Tambahkan HTMLResponse
from fastapi.templating import Jinja2Templates # Tambahkan Jinja2Templates
from sqlalchemy.orm import Session # Tambahkan Session untuk query database
from database import engine, Base, get_db # Tambahkan get_db
from models import pet, medical, user
from routers import pet as pet_router, medical as medical_router, auth as auth_router
from dependencies import oauth2_scheme

# 1. Inisialisasi folder templates
templates = Jinja2Templates(directory="templates")

# Membuat tabel database
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="VetConnect API",
    description="Centralized Pet Medical Record API",
    version="1.0.0"
)

# Daftarkan router
app.include_router(auth_router.router)
app.include_router(pet_router.router)
app.include_router(medical_router.router)

# 2. Ubah fungsi ini untuk menampilkan UI
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, db: Session = Depends(get_db)):
    pets = db.query(pet.Pet).all()
    
    # Gunakan format ini agar tidak tertukar parameternya
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"pets": pets}
    )