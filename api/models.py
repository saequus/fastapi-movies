from pydantic import BaseModel
from typing import List


class Movie(BaseModel):
    film: str
    description: str
    casts: List[str]
    year: str
