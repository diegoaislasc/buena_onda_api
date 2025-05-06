from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.schemas.song import SongCreate, SongUpdate, SongResponse
from app.crud.read import get_all_songs, get_song_by_id, get_song_by_title
from app.crud.update import update_song as update_song_crud
from app.crud.delete import delete_song as delete_song_crud
from app.crud.create import create_song as create_song_crud

router = APIRouter(prefix="/songs", tags=["Songs"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST (Crear canción)
@router.post("/", response_model=SongResponse)
def create_song_endpoint(song: SongCreate, db: Session = Depends(get_db)):
    new_song = create_song_crud(db, song)
    if not new_song:
        raise HTTPException(status_code=400, detail="Ya existe una canción con ese título en el mismo álbum")
    return new_song

# GETs ( Obtener canciones)
@router.get("/", response_model=List[SongResponse])
def get_songs(db: Session = Depends(get_db)):
    return get_all_songs(db)

@router.get("/{song_id}", response_model=SongResponse)
def get_song(song_id: int, db: Session = Depends(get_db)):
    song = get_song_by_id(db, song_id)
    if not song:
        raise HTTPException(status_code=404, detail="Canción no encontrada")
    return song

@router.get("/search/title/{title}", response_model=SongResponse)
def search_song(title: str, db: Session = Depends(get_db)):
    song = get_song_by_title(db, title)
    if not song:
        raise HTTPException(status_code=404, detail="Canción no encontrada")
    return song

# PUT (actualizar cancion)
@router.put("/{song_id}", response_model=SongResponse)
def update_song_endpoint(song_id: int, song_data: SongUpdate, db: Session = Depends(get_db)):
    updated_song = update_song_crud(db, song_id, song_data)
    if not updated_song:
        raise HTTPException(status_code=404, detail="Canción no encontrada")
    return updated_song

# DELETE (eliminar cancion)
@router.delete("/{song_id}", response_model=SongResponse)
def delete_song_endpoint(song_id: int, db: Session = Depends(get_db)):
    deleted_song = delete_song_crud(db, song_id)
    if not deleted_song:
        raise HTTPException(status_code=404, detail="Canción no encontrada")
    return deleted_song
