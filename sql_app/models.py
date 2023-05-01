from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base


class Astro(Base):
    __tablename__ = "astros"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    distance = Column(String)
    type = Column(String)