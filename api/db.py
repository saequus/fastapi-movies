import os

from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
    ARRAY
)

from api.models import MovieIn, MovieOut, MovieUpdate
from databases import Database


db_username = os.environ['DB_USERNAME']
db_password = os.environ['DB_PASSWORD']
db_host = os.environ['DB_HOST']
db_port = os.environ['DB_PORT']
db_name = os.environ['DB_NAME']

DATABASE_URL = f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'


engine = create_engine(DATABASE_URL)
metadata = MetaData()

movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(128)),
    Column('description', String(256)),
    Column('year', String(8)),
    Column('casts', ARRAY(String))
)

database = Database(DATABASE_URL)


async def add_movie(payload: MovieIn):
    query = movies.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_all_movies():
    query = movies.select()
    return await database.fetch_all(query=query)

