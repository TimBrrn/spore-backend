from typing import List
from fastapi import APIRouter, Depends, status, Query
from sqlmodel import Session
from database import get_session

from services.biosample import create, get_all, get, delete, update
from schemas.biosample import BioSampleRead, BioSampleCreate, BioSampleUpdate

router = APIRouter(prefix="/biosamples")

@router.post("/", response_model=BioSampleRead, status_code=status.HTTP_201_CREATED)
def create_biosample(
    data: BioSampleCreate, 
    session: Session = Depends(get_session)) -> None:
    return create(session, data)

@router.get("/", response_model=List[BioSampleRead])
def get_all_samples(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    session: Session = Depends(get_session)) -> List[BioSampleRead]:
    return get_all(session, page, size)

@router.get("/{sample_id}", response_model=BioSampleRead)
def get_samples(
    sample_id: int, 
    session: Session = Depends(get_session)) -> BioSampleRead:
    return get(session, sample_id)

@router.delete("/{sample_id}")
def delete_sample(
    sample_id: int, 
    session: Session = Depends(get_session)) -> None:
    return delete(session, sample_id)

@router.post("/{sample_id}")
def update_sample(
    sample_id: int,
    data: BioSampleUpdate,
    session: Session = Depends(get_session)) -> BioSampleRead:
    return update(session, sample_id, data)