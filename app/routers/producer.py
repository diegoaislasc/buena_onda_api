from fastapi import APIRouter, HTTPException, Depends


from app.schemas.producer import ProducerCreate, ProducerUpdate, ProducerResponse
from app.crud.create import create_producer as create_producer_crud
from app.crud.read import *
from app.crud.update import update_producer as update_producer_crud
from app.crud.delete import delete_producer as delete_producer_crud

router = APIRouter(prefix="/producers", tags=["Producers"])

from app.database import SessionLocal
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProducerResponse)
def create_producer_endpoint(producer: ProducerCreate, db: Session = Depends(get_db)):
    new_producer = create_producer_crud(producer)
    if not new_producer:
        raise HTTPException(status_code=404, detail="El productor ya existe.")

    return new_producer

@router.get("/", response_model=list[ProducerResponse])
def get_producers(db: Session = Depends(get_db)):
    return get_all_producers(db)

@router.get("/{producer_id}", response_model=ProducerResponse)
def get_producer_by_id(producer_id: int, db: Session = Depends(get_db)):
    producer = get_producer_by_id(db, producer_id)
    if not producer:
        raise HTTPException(status_code=404, detail="Productor no encontrado.")
    return producer

@router.put("/{producer_id}", response_model=ProducerResponse)
def update_producer_endpoint(producer_id: int, updates: ProducerUpdate, db: Session = Depends(get_db)):
    updated_producer = update_producer_crud(db, producer_id, updates)
    if not updated_producer:
        raise HTTPException(status_code=404, detail="Productor no encontrado.")
    return updated_producer

@router.delete("/{producer_id}")
def delete_producer_endpoint(producer_id: int, db: Session = Depends(get_db)):
    deleted_producer = delete_producer_crud(db, producer_id)
    if not deleted_producer:
        raise HTTPException(status_code=404, detail="Productor no encontrado.")
    return deleted_producer

