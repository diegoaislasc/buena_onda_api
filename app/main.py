from fastapi import FastAPI
from app.routers import artist, album, song, songwriter, producer, service, event

app = FastAPI()
app.include_router(artist.router)
app.include_router(album.router)
app.include_router(song.router)
app.include_router(songwriter.router)
app.include_router(producer.router)
app.include_router(service.router)
app.include_router(event.router)


# uvicorn app.main:app --reload