from sqlalchemy.orm import Session
from app.models.models import *
from app.schemas.album import *
from app.schemas.artist import *

# ARTIST
def create_artist(db: Session, artist: ArtistCreate):
    existing = db.query(Artist).filter(
        (Artist.stage_name == artist.artist.stage_name) |
        (Artist.email == artist.email)
    ).first()
    if existing:
        return None # if existing, we manage in router

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
        return None # handled in router

    # new album
    new_album = Album(**album.dict())
    db.add(new_album)
    db.commit()
    db.refresh(new_album)
    return new_album
