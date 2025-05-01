from sqlalchemy.orm import Session
from app.models.models import Artist, Album
from typing import Optional

# ARTIST
def delete_artist(db: Session, artist_id: int) -> Optional[Artist]:
    artist = db.query(Artist).filter(Artist.id == artist_id).first()

    if not artist:
        return None

    db.delete(artist)
    db.commit()
    return artist

# ALBUM
def delete_album(db: Session, album_id: int) -> Optional[Album]:
    album = db.query(Album).filter(Album.id == album_id).first()

    if not album:
        return None

    db.delete(album)
    db.commit()
    return album
