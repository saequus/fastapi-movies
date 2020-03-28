from pydantic import BaseModel
from typing import List, Optional


class MovieIn(BaseModel):
    name: str
    description: str
    year: str
    casts: List[str]


class MovieOut(MovieIn):
    id: int


class MovieUpdate(MovieIn):
    name: Optional[str] = None
    description: Optional[str] = None
    year: Optional[str] = None
    casts: Optional[List[str]] = None
