from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session  # es la forma en la que nos conectamos a la bd
from typing import List
from app.database import SessionLocal  # funcion que crea sesiones de bd
from app.routers.artist import get_db  # funcion que maneja abrir y cerrar esa conexion
from app.schemas.studio import StudioCreate, StudioUpdate, StudioResponse  # importamos los schemas
# importamos las funciones del crud
from app.crud.create import create_studio as create_studio_crud
from app.crud.update import update_studio as update_studio_crud
from app.crud.delete import delete_studio as delete_studio_crud
from app.crud.read import get_all_studios, get_studio_by_id, get_studio_by_name

router = APIRouter(prefix="/studios", tags=["Studios"])


@router.post("/", response_model=StudioResponse)
# devuelve el estudi creado
def create_studio_endpoint(studio: StudioCreate, db: Session = Depends(get_db)):
    new_studio = create_studio_crud(db, studio)  # llama a la funcion crud para crear un estudio
    if not new_studio:
        raise HTTPException(status_code=400, detail="El estudio ya existe")
    return new_studio


# devuelve lista de todos los estudios
@router.get("/", response_model=List[StudioResponse])
def get_studios(db: Session = Depends(get_db)):
    return get_all_studios(db)


# busca el estudio por su id
@router.get("/{studio_id}", response_model=StudioResponse)
def get_studio_by_id_endpoint(studio_id: int, db: Session = Depends(get_db)):
    studio = get_studio_by_id(db, studio_id)
    if not studio:
        raise HTTPException(status_code=404, detail="Estudio no encontrado")
    return studio


# busca por nombre
@router.get("/search/{name}", response_model=StudioResponse)
def get_studio_by_name_endpoint(name: str, db: Session = Depends(get_db)):
    studio = get_studio_by_name(db, name)
    if not studio:
        raise HTTPException(status_code=404, detail="Estudio no encontrado")
    return studio


# actualiza el estudio con una id
@router.put("/{studio_id}", response_model=StudioResponse)
def update_studio_endpoint(studio_id: int, studio_data: StudioUpdate, db: Session = Depends(get_db)):
    updated_studio = update_studio_crud(db, studio_id, studio_data)
    if not updated_studio:
        raise HTTPException(status_code=404, detail="Estudio no encontrado")
    return updated_studio


# elimina el estudio con una id
@router.delete("/{studio_id}", response_model=StudioResponse)
def delete_studio_endpoint(studio_id: int, db: Session = Depends(get_db)):
    deleted_studio = delete_studio_crud(db, studio_id)
    if not deleted_studio:
        raise HTTPException(status_code=404, detail="Estudio no encontrado")
    return deleted_studio
