from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
headers = {"Access-Control-Allow-Origin": "*"}
# Configure CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_astros(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    astros = crud.get_astros(db, skip=skip, limit=limit)
    return JSONResponse(content=astros, headers=headers)

@app.post("/astro/")
def create_astro(astro: schemas.AstroCreate, db: Session = Depends(get_db)):
    db_astro = crud.create_astro(db, astro)
    return JSONResponse(content=db_astro, headers=headers)