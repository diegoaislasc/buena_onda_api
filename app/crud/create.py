from sqlalchemy.orm import Session
from app.models.models import *

# ARTIST
from app.schemas.artist import ArtistCreate
from app.schemas.event import EventCreate


def create_artist(db: Session, artist: ArtistCreate):
    existing = db.query(Artist).filter(
        (Artist.stage_name == artist.stage_name) |
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
from app.schemas.album import AlbumCreate
def create_album(db: Session, album: AlbumCreate):
    existing = db.query(Album).filter(
        (Album.title == album.title) |
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
from app.schemas.song import SongCreate
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
from app.schemas.songwriter import SongwriterCreate
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
from app.schemas.producer import ProducerCreate
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
from app.schemas.service import ServiceCreate
def create_service(db: Session, service: ServiceCreate) -> Service | None:
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

# STUDIO
from app.schemas.studio import StudioCreate
def create_studio(db: Session, studio: StudioCreate) -> Studio | None:
    #Revisa si hay un estudio con el mismo nombre
    existing = db.query(Studio).filter(Studio.name == studio.name).first()
    if existing:
        return None
    #Convierte el objeto StudioCreate a un objeto Studio
    new_studio = Studio(**studio.dict())
    #Guarda el nuevo estudio en la bd
    db.add(new_studio)
    db.commit()
    db.refresh(new_studio)

    #Devuelve el estudio creado
    return new_studio

# EVENT
from app.schemas.event import EventCreate
def create_event(db: Session, event: EventCreate) -> Event | None:
    existing = db.query(Event).filter(Event.name == event.name).first()
    if existing:
        return None
    new_event = Event(**event.dict())
    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return new_event


