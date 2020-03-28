from pydantic import BaseModel
from typing import List, Optional


class MovieIn(BaseModel):
    name: str
    description: str
    year: str
    casts_id: List[int]


class MovieOut(MovieIn):
    id: int


class MovieUpdate(MovieIn):
    name: Optional[str] = None
    description: Optional[str] = None
    year: Optional[str] = None
    casts_id: Optional[List[int]] = None
