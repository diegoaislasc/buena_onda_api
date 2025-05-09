from sqlalchemy.orm import Session
from app.models.models import Artist, Album, Song, Songwriter, Producer, Service
from typing import Optional, Type, Any


# ARTIST
def delete_artist(db: Session, artist_id: int) -> Type[Artist] | None:
    artist = db.query(Artist).filter(Artist.id == artist_id).first()

    if not artist:
        return None

    db.delete(artist)
    db.commit()
    return artist

# ALBUM
def delete_album(db: Session, album_id: int) -> Type[Album] | None:
    album = db.query(Album).filter(Album.id == album_id).first()

    if not album:
        return None

    db.delete(album)
    db.commit()
    return album

# SONG
def delete_song(db: Session, song_id: int) -> Type[Song] | None:
    song = db.query(Song).filter(Song.id == song_id).first()
    if not song:
        return None

    db.delete(song)
    db.commit()
    return song

# SONGWRITER
def delete_songwriter(db: Session, song_id: int) -> Type[Songwriter] | None:
    songwriter = db.query(Songwriter).filter(Songwriter.id == song_id).first()
    if not songwriter:
        return None

    db.delete(songwriter)
    db.commit()
    return songwriter

# PRODUCER
def delete_producer(db: Session, producer_id: int) -> Type[Producer] | None:
    producer = db.query(Producer).filter(Producer.id == producer_id).first()
    if not producer:
        return None
    db.delete(producer)
    db.commit()
    return producer

# SERVICE
def delete_service(db: Session, service_id: int) -> Type[Service] | None:
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        return None
    db.delete(service)
    db.commit()
    return service
