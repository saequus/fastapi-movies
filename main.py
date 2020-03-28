from fastapi import FastAPI
from api.movies import movies_router
from api.db import metadata, database, engine

app = FastAPI()


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


app.include_router(movies_router)
