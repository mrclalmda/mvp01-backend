from sqlalchemy import Column, Integer, String
from database import Base

class Astro(Base):
    __tablename__ = "astro"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    distance = Column(Integer)
    type = Column(String)

    