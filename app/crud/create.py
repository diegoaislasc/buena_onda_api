from sqlalchemy.orm import Session
from app.models.models import *
from app.schemas.album import *
from app.schemas.artist import *
from app.schemas.song import *
from app.schemas.songwriter import *
from app.schemas.producer import *


# ARTIST
def create_artist(db: Session, artist: ArtistCreate):
    existing = db.query(Artist).filter(
        (Artist.stage_name == artist.artist.stage_name) |
        (Artist.email == artist.email)
    ).first()
    if existing:
        return None # evitar artistas duplicados
    # new artist
    new_artist = Artist(**artist.dict())
    db.add(new_artist)
    db.commit()
    db.refresh(new_artist)
    return new_artist

# ALBUM
def create_album(db: Session, album: AlbumCreate):
    existing = db.query(Album).filter(
        (Album.title == album.album.title) |
        (Album.id == album.id.id)
    ).first()

    if existing:
        return None # evitar albumes duplicados

    # new album
    new_album = Album(**album.dict())
    db.add(new_album)
    db.commit()
    db.refresh(new_album)
    return new_album

# SONG
def create_song(db: Session, song: SongCreate):
    # Evitar canciones duplicadas dentro del mismo álbum
    existing = db.query(Song).filter(
        (Song.title == song.title) |
        (Song.id == song.id.id)
    ).first()

    if existing:
        return None

    new_song = Song(**song.dict())
    db.add(new_song)
    db.commit()
    db.refresh(new_song)
    return new_song

# SONGWRITER
def create_songwriter(db: Session, songwriter: SongwriterCreate) -> Songwriter:
    existing = db.query(Songwriter).filter(
        Songwriter.id == songwriter.id
    ).first()

    if existing:
        return None

    new_songwriter = Songwriter(**songwriter.dict())
    db.add(new_songwriter)
    db.commit()
    db.refresh(new_songwriter)
    return new_songwriter


# PRODUCER
def create_producer(db: Session, producer: ProducerCreate) -> Producer:
    existing = db.query(Producer).filter(
        Producer.id == producer.id
    ).first()

    if existing:
        return None

    new_producer = Producer(**producer.dict())
    db.add(new_producer)
    db.commit()
    db.refresh(new_producer)
    return new_producer

# SERVICE
def create_service(db: Session, service: ServiceCreate) -> Service:
    existing = db.query(Service).filter(
        Service.id == service.id
    ).first()

    if existing:
        return None

    new_service = Service(**service.dict())
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service

