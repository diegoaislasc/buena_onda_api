from pydantic import BaseModel, constr
from typing import Optional
from datetime import date

# ARTIST SCHEMAS
class AlbumCreate(BaseModel):
    title: constr(min_length=1, max_length=255)
    release_date: Optional[date] = None
    artist_id: int

    class Config:
        orm_mode = True

class AlbumResponse(BaseModel):
    id: int
    title: constr(min_length=1, max_length=255)
    release_date: Optional[date] = None
    artist_id: int

    class Config:
        orm_mode = True

class AlbumUpdate(BaseModel):
    title: Optional[constr(min_length=1, max_length=255)] = None
    release_date: Optional[date] = None
    artist_id: Optional[int]

    class Config:
        orm_mode = True