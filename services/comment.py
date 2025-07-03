from sqlmodel import Session

from models import Comment
from schemas.comment import CommentCreate

def create(session: Session, sample_id: int, data: CommentCreate) -> Comment:
    comment = Comment(sample_id=sample_id, **data.model_dump())
    session.add(comment)
    session.commit()
    session.refresh(comment)
    return comment

