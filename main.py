from fastapi import FastAPI, Depends, Request 
from fastapi.responses import HTMLResponse 
from fastapi.templating import Jinja2Templates 
from sqlalchemy.orm import Session 
from database import engine, Base, get_db 
from models import pet, medical, user
from routers import pet as pet_router, medical as medical_router, auth as auth_router
from dependencies import oauth2_scheme

templates = Jinja2Templates(directory="templates")

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="VetConnect API",
    description="Centralized Pet Medical Record API",
    version="1.0.0"
)

app.include_router(auth_router.router)
app.include_router(pet_router.router)
app.include_router(medical_router.router)

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, db: Session = Depends(get_db)):
    pets = db.query(pet.Pet).all()
    
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"pets": pets}
    )