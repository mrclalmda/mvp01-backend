from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Astro
from schemas import AstroCreate, AstroRead
from typing import List


Astro.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["http://localhost",    "http://localhost:5500",
           "http://127.0.0.1",    "http://127.0.0.1:5500"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_model=List[AstroRead])
def read_astro(db: Session = Depends(get_db)):
    astros = db.query(Astro).all()
    return astros


@app.post("/astro/", response_model=AstroRead)
def create_astro(astro: AstroCreate, db: Session = Depends(get_db)):
    db_astro = Astro(name=astro.name, distance=astro.distance,
                     type=astro.type)
    db.add(db_astro)
    db.commit()
    db.refresh(db_astro)
    return {
        "id": db_astro.id,
        "name": db_astro.name,
        "distance": db_astro.distance,
        "type": db_astro.type
    }


@app.delete("/astro/{astro_id}")
def delete_astro(astro_id: int, db: Session = Depends(get_db)):
    db_astro = db.query(Astro).filter(Astro.id == astro_id).first()
    if db_astro is None:
        raise HTTPException(status_code=404, detail="Astro not found")
    db.delete(db_astro)
    db.commit()
    return {"message": "Astro deleted"}
