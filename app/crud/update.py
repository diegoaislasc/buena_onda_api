from sqlalchemy.orm import Session
from app.models.models import *
from app.schemas.album import AlbumUpdate
from app.schemas.artist import ArtistUpdate
from app.schemas.song import SongUpdate
from typing import Optional, Type, Any

from app.schemas.songwriter import SongwriterUpdate
from app.schemas.producer import ProducerUpdate


# ARTIST
def update_artist(db: Session, artist_id: int, artist_data: ArtistUpdate) -> Type[Artist] | None:
    artist = db.query(Artist).filter(Artist.id == artist_id).first()

    if not artist:
        return None

    for key, value in artist_data.dict(exclude_unset=True).items():
        setattr(artist, key,value)

    db.commit()
    db.refresh(artist)
    return artist

# ALBUM
def update_album(db: Session, album_id: int, album_data: AlbumUpdate) -> Type[Album] | None:
    album = db.query(Album).filter(Album.id == album_id).first()

    if not album:
        return None

    for key, value in album_data.dict(exclude_unset=True).items():
        setattr(album, key,value)

    db.commit()
    db.refresh(album)
    return album

# SONG
def update_song(db: Session, song_id: int, song_data: SongUpdate) -> Type[Song] | None:
    song = db.query(Song).filter(Song.id == song_id).first()
    if not song:
        return None

    for key, value in song_data.dict(exclude_unset=True).items():
        setattr(song, key, value)

    db.commit()
    db.refresh(song)
    return song

# SONGWRITER
def update_songwriter(db: Session, songwriter_id: int, songwriter_data: SongwriterUpdate) -> Type[Songwriter] | None:
    songwriter = db.query(Songwriter).filter(Songwriter.id == songwriter_id).first()
    if not songwriter:
        return None

    for key,value in songwriter_data.dict(exclude_unset=True).items():
        setattr(songwriter, key,value)

        db.commit()
        db.refresh(songwriter)
        return songwriter

# PRODUCER
def update_producer(db: Session, producer_id: int, updates: ProducerUpdate) -> Type[Producer] | None:
    producer = db.query(Producer).filter(Producer.id == producer_id).first()
    if not producer:
        return None
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(producer, key, value)
    db.commit()
    db.refresh(producer)
    return producer
