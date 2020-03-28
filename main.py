
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn
from fastapi.exceptions import HTTPException


app = FastAPI()


class Movie(BaseModel):
    film: str
    description: str
    casts: List[str]
    year: str


fake_result = [
    {
        'film': 'Star Wars',
        'description': 'SW description',
        'casts': ['MWM', 'EOG'],
        'year': '2019'
    },
    {
        'film': 'Tower',
        'description': 'Tower description',
        'casts': ['MWM', 'EOG'],
        'year': '2013'
    },
    {
        'film': 'New Age',
        'description': 'NA description',
        'casts': ['MWM', 'EOG'],
        'year': '2011'
    },
    {
        'film': 'Home',
        'description': 'Home description',
        'casts': ['MWM', 'EOG'],
        'year': '2011'
    },
]


@app.get('/movies', response_model=List[Movie])
async def movies():
    return fake_result


@app.post('/movies/', response_model=Movie, status_code=201)
async def add_movie(payload: Movie):
    movie = payload.dict()
    fake_result.append(movie)
    movie['id'] = len(fake_result) - 1
    return movie


@app.put('/movies/{movie_id}', response_model=Movie)
async def update_movie(movie_id: int, payload: Movie):
    movie = payload.dict()
    movies_length = len(fake_result)
    if not (0 <= movie_id <= movies_length - 1):
        raise HTTPException(
            status_code=404,
            detail='Movie with given id not found'
        )
    fake_result[movie_id] = movie
    return movie


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)


