from pydantic import BaseModel
from typing import List

class AstroBase(BaseModel):
    name: str
    distance: str
    type: str


class AstroCreate(AstroBase):
    pass


class Astro(AstroBase):
    id: int

    class Config:
        orm_mode = True


class AstroList(BaseModel):
    __root__: List[Astro] = []