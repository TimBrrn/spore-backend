from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from database import get_session
from schemas.comment import CommentCreate
from services.comment import create


router = APIRouter()

@router.post("/biosamples/{sample_id}/comments", response_model=CommentCreate, status_code=status.HTTP_201_CREATED)
def add_comment(
    sample_id: int,
    data: CommentCreate,
    session: Session = Depends(get_session),
):
    return create(session, sample_id, data)
