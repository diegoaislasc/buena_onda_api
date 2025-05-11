# REST
from fastapi import APIRouter, Depends, HTTPException


from app.database import SessionLocal
# CRUD
from app.schemas.album import AlbumCreate, AlbumUpdate, AlbumResponse

from app.crud.create import create_album as create_album_crud
from app.crud.update import update_album as update_album_crud
from app.crud.delete import delete_album as delete_album_crud
from app.crud.read import *

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/albums", tags=["Albums"])

# POST - crear albums
@router.post("/", response_model=AlbumResponse)
def create_album_endpoint(album: AlbumCreate, db: Session = Depends(get_db)):
    new_album = create_album_crud(db, album)
    if not new_album:
        raise HTTPException(status_code=400, detail="El álbum ya existe")
    return new_album

# GETs - obtener albums
@router.get("/", response_model=List[AlbumResponse])
def get_albums(db: Session = Depends(get_db)):
    return get_all_albums(db)

@router.get("/{album_id}", response_model=AlbumResponse)
def get_album_by_id(album_id: int, db: Session = Depends(get_db)):
    album = get_album_by_id(db, album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Álbum no encontrado")
    return album

@router.get("/search/{title}", response_model=AlbumResponse)
def get_album_by_name(title: str, db: Session = Depends(get_db)):
    album = get_album_by_name(db, title)
    if not album:
        raise HTTPException(status_code=404, detail="Álbum no encontrado")
    return album

# PUT - actualizar albums
@router.put("/{album_id}", response_model=AlbumResponse)
def update_album_endpoint(album_id: int, album_data: AlbumUpdate, db: Session = Depends(get_db)):
    updated_album = update_album_crud(db, album_id, album_data)
    if not updated_album:
        raise HTTPException(status_code=404, detail="Álbum no encontrado")
    return updated_album

# DELETE - eliminar álbums
@router.delete("/{album_id}", response_model=AlbumResponse)
def delete_album_endpoint(album_id: int, db: Session = Depends(get_db)):
    deleted_album = delete_album_crud(db, album_id)
    if not deleted_album:
        raise HTTPException(status_code=404, detail="Álbum no encontrado")
    return deleted_album