# Optional class from typing module - https://www.geeksforgeeks.org/make-every-field-optional-with-pydantic-in-python/
# pydantic docs - https://docs.pydantic.dev/latest/concepts/models/
# pydantic email validation - https://docs.pydantic.dev/2.0/usage/types/string_types/

from pydantic import BaseModel, EmailStr, constr
from typing import Optional

class ArtistCreate(BaseModel):
    real_name: Optional[str] = None
    stage_name: constr(min_length=2, max_length=255)
    music_genre: Optional[str] = None
    country_of_origin: Optional[str] = None
    email: Optional[EmailStr] = None
    instagram_handle: Optional[constr(min_length=2, max_length=30)] = None

    class Config:
        orm_mode = True
