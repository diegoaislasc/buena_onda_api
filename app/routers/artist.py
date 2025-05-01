# Fast API docs - https://fastapi.tiangolo.com/

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from typing import List

from app.schemas.artist import ArtistCreate, ArtistResponse, ArtistUpdate
# crud functions
from app.crud.read import *
from app.crud.create import create_artist as create_artist_crud
from app.crud.update import update_artist as update_artist_crud
from app.crud.delete import delete_artist as delete_artist_crud

router = APIRouter(prefix="/artists", tags=["Artists"])

# Dependency para obtener la sesión de la BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POSTs
@router.post("/", response_model=ArtistResponse)
def create_artist(artist: ArtistCreate, db: Session = Depends(get_db)):
    new_artist = create_artist_crud(db, artist)

    if not new_artist:
        raise HTTPException(status_code=404, detail="El artista ya existe.")

    return new_artist

# GETs
@router.get("/", response_model=List[ArtistResponse])
def read_artists(db: Session = Depends(get_db)):
    return get_all_artists(db)
@router.get("/{artist_id}", response_model=ArtistResponse)
def read_artist_by_id(artist_id: int, db: Session = Depends(get_db)):
    artist = get_artist_by_id(db, artist_id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artista no encontrado")
    return artist
@router.get("/{artist_name}", response_model=ArtistResponse)
def read_artist_by_name(artist_name: str, db: Session = Depends(get_db)):
    artist = get_artist_by_name(db, artist_name)

# PUT
@router.put("/{artist_id}", response_model=ArtistResponse)
def update_artist_endpoint(artist_id: int, artist_data: ArtistUpdate, db: Session = Depends(get_db)):
    updated_artist = update_artist_crud(db, artist_id, artist_data)

    if not updated_artist:
        raise HTTPException(status_code=404, detail="Artista no encontrado")

    return updated_artist

# DELETE
@router.delete("/{artist_id}", response_model=ArtistResponse)
def delete_artist_endpoint(artist_id: int, db: Session = Depends(get_db)):
    deleted_artist = delete_artist_crud(db, artist_id)

    if not deleted_artist:
        raise HTTPException(status_code=404, detail="Artista no encontrado")

    return deleted_artist




