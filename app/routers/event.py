from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.routers.artist import get_db
from app.schemas.event import EventCreate, EventResponse, EventUpdate
from app.crud.create import create_event as create_event_crud
from app.crud.read import *
from app.crud.update import update_event as update_event_crud
from app.crud.delete import delete_event as delete_event_crud

router = APIRouter(
    prefix="/events",
    tags=["Events"]
)

@router.post("/", response_model=EventResponse, status_code=201)
def create_new_event(event: EventCreate, db: Session = Depends(get_db)):
    new_event = create_event_crud(db, event)
    if not new_event:
        raise HTTPException(status_code=404, detail="El evento ya existe")
    return new_event


@router.get("/", response_model=list[EventResponse])
def read_all_events(db: Session = Depends(get_db)):
    return get_all_events(db)

@router.get("/id/{event_id}", response_model=EventResponse)
def read_event_by_id(event_id: int, db: Session = Depends(get_db)):
    event = get_event_by_id(db, event_id)
    if  not event:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return event

@router.get("/{event_name}", response_model=EventResponse)
def read_event_by_name(event_name: str, db: Session = Depends(get_db)):
    event = get_event_by_name(db, event_name)
    if not event:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return event

@router.put("/{event_id}", response_model=EventResponse)
def update_event_endpoint(event_id: int, event_data: EventUpdate, db: Session = Depends(get_db)):
    updated_event = update_event_crud(db, event_id, event_data)
    if updated_event is None:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return updated_event

@router.delete("/{event_id}", response_model=EventResponse)
def delete_existing_event(event_id: int, db: Session = Depends(get_db)):
    deleted_event = delete_event_crud(db, event_id)
    if deleted_event is None:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return deleted_event