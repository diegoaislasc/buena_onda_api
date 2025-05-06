# SONGWRITER SCHEMAS
from pydantic import BaseModel, constr
from typing import Optional

class SongwriterCreate(BaseModel):
    name: str
    country_of_origin: Optional[str] = None
    music_genre: Optional[str] = None

    class Config:
        orm_mode = True

class SongwriterResponse(BaseModel):
    id: int
    name: str
    country_of_origin: Optional[str] = None
    music_genre: Optional[str] = None

    class Config:
        orm_mode = True

class SongwriterUpdate(BaseModel):
    name: Optional[str] = None
    country_of_origin: Optional[str] = None
    music_genre: Optional[str] = None

    class Config:
        orm_mode = True