from sqlalchemy.orm import Session

from . import models, schemas


def get_astros(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Astro).offset(skip).limit(limit).all()

def create_astro(db: Session, astro: schemas.AstroCreate):
    db_astro = models.Astro(name=astro.name, distance=astro.distance, type=astro.type)
    print(db_astro)
    # db.add(dict(db_astro))
    # db.commit()
    # db.refresh(db_astro)
    # return db_astro