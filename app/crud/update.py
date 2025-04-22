from sqlalchemy.orm import Session
from app.models.models import Artist
from app.schemas.schemas import ArtistUpdate
from typing import Optional

def update_artist(db: Session, artist_id: int, artist_data: ArtistUpdate) -> Optional[Artist]:
    artist = db.query(Artist).filter(Artist.id == artist_id).first()

    if not artist:
        return None

    for key, value in artist_data.dict(exclude_unset=True).items():
        setattr(artist, key,value)

    db.commit()
    db.refresh(artist)
    return artist