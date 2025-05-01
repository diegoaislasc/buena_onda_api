from fastapi import FastAPI
from app.routers import artist, album

app = FastAPI()
app.include_router(artist.router)
app.include_router(album.router)