from fastapi.exceptions import HTTPException
from typing import List

from api.models import MovieIn, MovieOut
from fastapi import APIRouter
from api.db import get_all_movies, get_movie, add_movie, update_movie, delete_movie

movies_router = APIRouter()


@movies_router.get('/movies', response_model=List[MovieOut])
async def api_get_movie():
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
async def api_update_movie(movie_id: int, payload: MovieIn):
    movie = await get_movie(movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail='Movie not found')
    
    update_data = payload.dict(exclude_unset=True)
    movie_in_db = MovieIn(**movie)

    updated_movie = movie_in_db.copy(update=update_data)
    return await update_movie(movie_id, updated_movie)


@movies_router.delete('/movies/{movie_id}')
async def api_delete_movie(movie_id: int):
    movie = await get_movie(movie_id)
    if not movie:
        return HTTPException(status_code=404, detail='Movie not found')
    return await delete_movie(movie_id)
