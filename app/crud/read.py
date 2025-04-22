from sqlalchemy.orm import Session
from app.models.models import Artist
from typing import List, Optional

# READ ARTIST(s)
def get_artist_by_id(db: Session, artist_id: int) -> Optional[Artist]:
    return db.query(Artist).filter(Artist.id == artist_id).first()

def get_all_artists(db: Session) -> List[Artist]:
    return db.query(Artist).all()
