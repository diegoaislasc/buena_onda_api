from pydantic import BaseModel, constr
from typing import Optional

# Crea un nuevo estudio que hereda
class StudioCreate(BaseModel):
    name: constr(min_length=1, max_length=255)
    address :Optional[str] = None

    class Config:
        orm_mode = True

# Respuesta al cliente con la ID incluida
class StudioResponse(BaseModel):
    id: int
    name: str
    address: Optional[str] = None

    class Config:
        orm_mode = True  # FastAPI puede convertir objetos SQLAlchemy a JSON


# Actualiza un estudio pero es opcional las dos cosas
class StudioUpdate(BaseModel):
    name: Optional[constr(min_length=1, max_length=255)] = None
    address: Optional[constr(min_length=1, max_length=255)] = None

    class Config:
        orm_mode = True
