from pydantic import BaseModel, constr
from typing import Optional

# SERVICE SCHEMAS

class ServiceCreate(BaseModel):
    name: constr(min_length=2,max_length=255)
    description: Optional[str] = None
    price: float

    class Config:
        orm_mode = True


class ServiceResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

    class Config:
        orm_mode = True


class ServiceUpdate(BaseModel):
    name: Optional[constr(min_length=2,max_length=255)] = None
    description: Optional[str] = None
    price: Optional[float] = None

    class Config:
        orm_mode = True

