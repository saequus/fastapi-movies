from fastapi import FastAPI
from api.movies import movies_router

app = FastAPI()

app.include_router(movies_router)
