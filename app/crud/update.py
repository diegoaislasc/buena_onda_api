from sqlalchemy.orm import Session
from app.models.models import *
from app.schemas.album import AlbumUpdate
from app.schemas.artist import ArtistUpdate
from typing import Optional

# ARTIST
def update_artist(db: Session, artist_id: int, artist_data: ArtistUpdate) -> Optional[Artist]:
    artist = db.query(Artist).filter(Artist.id == artist_id).first()

    if not artist:
        return None

    for key, value in artist_data.dict(exclude_unset=True).items():
        setattr(artist, key,value)

    db.commit()
    db.refresh(artist)
    return artist

# ALBUM
def update_album(db: Session, album_id: int, album_data: AlbumUpdate) -> Optional[Album]:
    album = db.query(Album).filter(Album.id == album_id).first()

    if not album:
        return None

    for key, value in album_data.dict(exclude_unset=True).items():
        setattr(album, key,value)

    db.commit()
    db.refresh(album)
    return album