from sqlalchemy.orm import Session
from app.models.models import Artist
from app.schemas.schemas import ArtistCreate

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