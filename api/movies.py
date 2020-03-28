from fastapi.exceptions import HTTPException
from typing import List

from api.models import MovieIn, MovieOut
from fastapi import APIRouter
from api.db import get_all_movies, add_movie

movies_router = APIRouter()


fake_result = [
    {
        'name': 'Star Wars',
        'description': 'SW description',
        'casts': ['MWM', 'EOG'],
        'year': '2019'
    },
    {
        'name': 'Tower',
        'description': 'Tower description',
        'casts': ['MWM', 'EOG'],
        'year': '2013'
    },
    {
        'name': 'New Age',
        'description': 'NA description',
        'casts': ['MWM', 'EOG'],
        'year': '2011'
    },
    {
        
        'name': 'Home',
        'description': 'Home description',
        'casts': ['MWM', 'EOG'],
        'year': '2011'
    },
]


@movies_router.get('/movies', response_model=List[MovieOut])
async def index():
    return await get_all_movies()


@movies_router.post('/movies', response_model=MovieIn, status_code=201)
async def api_add_movie(payload: MovieIn):
    movie_id = await add_movie(payload)
    response = {
        'id': movie_id,
        **payload.dict()
    }
    return response


@movies_router.put('/movies/{movie_id}', response_model=MovieIn)
async def update_movie(movie_id: int, payload: MovieIn):
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
