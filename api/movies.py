from fastapi.exceptions import HTTPException
from typing import List

from api.models import Movieзш
from fastapi import APIRouter

movies_router = APIRouter()


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


@movies_router.get('/movies', response_model=List[Movie])
async def movies():
    return fake_result


@movies_router.post('/movies/', response_model=Movie, status_code=201)
async def add_movie(payload: Movie):
    movie = payload.dict()
    fake_result.append(movie)
    movie['id'] = len(fake_result) - 1
    return movie


@movies_router.put('/movies/{movie_id}', response_model=Movie)
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


@movies_router.delete('/movies/{movie_id}')
async def delete_movie(movie_id: int):
    movies_length = len(fake_result)
    if not (0 <= movie_id <= movies_length):
        raise HTTPException(status_code=404, detail='Movie with given id not found')
    del fake_result[movie_id]
    return None
