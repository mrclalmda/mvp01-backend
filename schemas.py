from typing import List
from pydantic import BaseModel

class AstroBase(BaseModel):
    name: str
    distance: int
    type: str

class AstroCreate(AstroBase):
    pass

class AstroRead(AstroBase):
    id: int

    class Config:
        orm_mode = True
