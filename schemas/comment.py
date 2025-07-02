from datetime import datetime
from pydantic import BaseModel

class CommentCreate(BaseModel):
    text: str

class CommentRead(BaseModel):
    id: int
    sample_id: int
    text: str
    created_at: datetime

    class Config:
        orm_mode = True