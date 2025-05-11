from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal

from app.schemas.songwriter import SongwriterCreate, SongwriterResponse, SongwriterUpdate

from app.crud.create import create_songwriter as create_songwriter_crud
from app.crud.read import *
from app.crud.update import update_songwriter as update_songwriter_crud
from app.crud.delete import delete_songwriter as  delete_songwriter_crud

router = APIRouter(prefix="/songwriters", tags=["Songwriters"])

from app.database import SessionLocal
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SongwriterResponse, status_code=201)
def create_songwriter_endpoint(songwriter: SongwriterCreate, db: Session = Depends(get_db)):
    new_songwriter = create_songwriter_crud(db, songwriter)
    if not new_songwriter:
        raise HTTPException(status_code=404, detail="El compositor ya existe")
    return new_songwriter


@router.get("/{songwriter_id}", response_model=SongwriterResponse)
def get_songwriter_by_id(songwriter_id: int, db: Session = Depends(get_db)):
    songwriter = get_songwriter_by_id(db, songwriter_id)
    if not songwriter:
        raise HTTPException(status_code=404, detail="Compositor no encontrado")
    return songwriter


@router.get("/", response_model=list[SongwriterResponse])
def get_songwriters(db: Session = Depends(get_db)):
    return get_all_songwriters(db)


@router.put("/{songwriter_id}", response_model=SongwriterResponse)
def update_songwriter_endpoint(songwriter_id: int, songwriter_data: SongwriterUpdate, db: Session = Depends(get_db)):
    updated = update_songwriter_crud(db, songwriter_id, songwriter_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Compositor no encontrado")
    return updated


@router.delete("/{songwriter_id}", status_code=204)
def delete_songwriter_endpoint(songwriter_id: int, db: Session = Depends(get_db)):
    deleted_songwriter = delete_songwriter_crud(db, songwriter_id)
    if not deleted_songwriter:
        raise HTTPException(status_code=404, detail="Compositor no encontrado")
