# Fast API docs - https://fastapi.tiangolo.com/
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.models import Artist
from app.schemas.schemas import ArtistCreate, ArtistResponse
from typing import List

router = APIRouter(prefix="/artists", tags=["Artists"])


# Dependency para obtener la sesión de la BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ArtistResponse)
def create_artist(artist: ArtistCreate, db: Session = Depends(get_db)):
    # Verificar si el artista ya existe (por stage_name o email)
    existing = db.query(Artist).filter(
        (Artist.stage_name == artist.stage_name) |
        (Artist.email == artist.email)
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="El artista ya existe")

    # Crear nuevo artista
    new_artist = Artist(**artist.dict())
    db.add(new_artist)
    db.commit()
    db.refresh(new_artist)

    return new_artist
