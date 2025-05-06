from pydantic import BaseModel
from typing import Optional

# PRODUCER SCHEMAS

class ProducerCreate(BaseModel):
    name: str
    specialty: Optional[str] = None

    class Config:
        orm_mode = True


class ProducerUpdate(BaseModel):
    name: Optional[str] = None
    specialty: Optional[str] = None

    class Config:
        orm_mode = True


class ProducerResponse(BaseModel):
    id: int
    name: str
    specialty: Optional[str] = None

    class Config:
        orm_mode = True
