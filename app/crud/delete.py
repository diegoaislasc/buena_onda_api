from sqlalchemy.orm import Session
from app.models.models import Artist
from typing import Optional

def delete_artist(db: Session, artist_id: int) -> Optional[Artist]:
    artist = db.query(Artist).filter(Artist.id == artist_id).first()

    if not artist:
        return None

    db.delete(artist)
    db.commit()
    return artist

