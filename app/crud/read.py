from sqlalchemy.orm import Session
from app.models.models import Artist, Album
from typing import List, Optional

# READ ARTISTs
def get_artist_by_id(db: Session, artist_id: int) -> Optional[Artist]:
    return db.query(Artist).filter(Artist.id == artist_id).first()

def get_all_artists(db: Session) -> List[Artist]:
    return db.query(Artist).all()

def get_artist_by_name(db: Session, artist_name: str) -> Optional[Artist]:
    return db.query(Artist).filter(Artist.stage_name == artist_name).first()

# READ ALBUM
def get_album_by_name(db: Session, album_name: str) -> Optional[Album]:
    return db.query(Album).filter(Album.id == album_name).first()

def get_album_by_id(db: Session, album_id: int) -> Optional[Album]:
    return db.query(Album).filter(Album.id == album_id).first()

def get_all_albums(db: Session) -> List[Album]:
    return db.query(Album).all()


