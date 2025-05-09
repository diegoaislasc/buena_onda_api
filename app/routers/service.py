
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from artist import get_db
from app.schemas.service import ServiceCreate, ServiceResponse, ServiceUpdate
# crud functions
from app.crud.read import *
from app.crud.create import create_service as create_service_crud
from app.crud.update import update_service as update_service_crud
from app.crud.delete import delete_service as delete_service_crud

router = APIRouter(prefix="/services", tags=["Services"])

# POSTs
@router.post("/", response_model=ServiceResponse)
def create_service_endpoint(service: ServiceCreate, db: Session = Depends(get_db)):
    new_service = create_service_crud(db, service)

    if not new_service:
        raise HTTPException(status_code=404, detail="El servicio ya existe.")

    return new_service

# GETs
@router.get("/", response_model=list[ServiceResponse])
def get_services(db: Session = Depends(get_db)):
    return get_all_services(db)

@router.get("/{service_id}", response_model=ServiceResponse)
def get_service_by_id(service_id: int, db: Session = Depends(get_db)):
    service = get_service_by_id(db, service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return service
@router.get("/{service_name}", response_model=ServiceResponse)
def read_artist_by_name(service_name: str, db: Session = Depends(get_db)):
    service = get_service_by_name(db, service_name)

# PUT
@router.put("/{artist_id}", response_model=ServiceResponse)
def update_service_endpoint(service_id: int, service_data: ServiceUpdate, db: Session = Depends(get_db)):
    updated_service = update_service_crud(db, service_id, service_data)

    if not updated_service:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")

    return updated_service

# DELETE
@router.delete("/{artist_id}", response_model=ServiceResponse)
def delete_service_endpoint(service_id: int, db: Session = Depends(get_db)):
    deleted_service = delete_service_crud(db, service_id)

    if not deleted_service:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")

    return deleted_service





