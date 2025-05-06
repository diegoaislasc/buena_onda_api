# SONG SCHEMAS
from pydantic import BaseModel, constr
from typing import Optional


class SongCreate(BaseModel):
    title: constr(min_length=1, max_length=255)
    duration: int  # duración en segundos
    album_id: int

    class Config:
        orm_mode = True

class SongUpdate(BaseModel):
    title: Optional[constr(min_length=1, max_length=255)] = None
    duration: Optional[int] = None
    album_id: Optional[int] = None

    class Config:
        orm_mode = True

class SongResponse(BaseModel):
    id: int
    title: str
    duration: int
    album_id: int

    class Config:
        orm_mode = True
