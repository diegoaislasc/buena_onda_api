from pydantic import BaseModel, constr
from typing import Optional
from datetime import date

# Properties to receive on item creation
class EventCreate(BaseModel):
    name: Optional[str] = None
    event_date: Optional[date] = None
    location: Optional[str] = None
    address: Optional[str] = None
    class Config:
        orm_mode = True

# Properties to receive on item update
class EventUpdate(BaseModel):
    name: Optional[constr(min_length=1)] = None
    event_date: Optional[date] = None
    location: Optional[constr(min_length=3, max_length=255)] = None
    address: Optional[str] = None
    class Config:
        orm_mode = True

# Properties to return to client
class EventResponse(BaseModel):
    id: int
    name: Optional[str] = None
    event_date: date = None
    location: Optional[str] = None
    address: Optional[str] = None

    class Config:
        orm_mode = True