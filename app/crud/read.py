from sqlalchemy.orm import Session
from app.models.models import Artist, Album, Song, Songwriter, Producer, Service
from typing import List, Optional, Type


# READ ARTISTs
def get_artist_by_id(db: Session, artist_id: int) -> Optional[Artist]:
    return db.query(Artist).filter(Artist.id == artist_id).first()

def get_all_artists(db: Session) -> list[Type[Artist]]:
    return db.query(Artist).all()

def get_artist_by_name(db: Session, artist_name: str) -> Optional[Artist]:
    return db.query(Artist).filter(Artist.stage_name == artist_name).first()

# READ ALBUM
def get_album_by_name(db: Session, album_name: str) -> Optional[Album]:
    return db.query(Album).filter(Album.id == album_name).first()

def get_album_by_id(db: Session, album_id: int) -> Optional[Album]:
    return db.query(Album).filter(Album.id == album_id).first()

def get_all_albums(db: Session) -> list[Type[Album]]:
    return db.query(Album).all()

# READ songs
def get_all_songs(db: Session) -> list[Type[Song]]:
    return db.query(Song).all()

def get_song_by_id(db: Session, song_id: int) -> Optional[Song]:
    return db.query(Song).filter(Song.id == song_id).first()

def get_song_by_title(db: Session, title: str) -> Optional[Song]:
    return db.query(Song).filter(Song.title.ilike(f"%{title}%")).first()


# READ songwriter
def get_songwriter_by_id(db: Session, songwriter_id: int) -> Optional[Songwriter]:
    return db.query(Songwriter).filter(Songwriter.id == songwriter_id).first()
def get_all_songwriters(db: Session) -> list[Type[Songwriter]]:
    return db.query(Songwriter).all()

# READ producer
def get_producer_by_id(db: Session, producer_id: int) -> Producer | None:
    return db.query(Producer).filter(Producer.id == producer_id).first()

def get_all_producers(db: Session) -> list[Type[Producer]]:
    return db.query(Producer).all()

def get_producer_by_name(db: Session, name: str) -> Producer | None:
    return db.query(Producer).filter(Producer.name == name).first()

# READ service
def get_service_by_id(db: Session, service_id: int) -> Service | None:
    return db.query(Service).filter(Service.id == service_id).first()

def get_all_services(db: Session) -> list[Type[Service]]:
    return db.query(Service).all()

def get_service_by_name(db: Session, name: str) -> Service | None:
    return db.query(Service).filter(Service.name == name).first()

