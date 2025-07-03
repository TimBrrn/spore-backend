from datetime import date
from typing import List, Optional
from pydantic import BaseModel

from schemas.comment import CommentRead

class BioSampleBase(BaseModel):
    sampling_location: str
    sample_type: str
    sampling_date: date
    sampling_operator: str

class BioSampleCreate(BioSampleBase):
    pass

class BioSampleUpdate(BaseModel):
    sampling_location: Optional[str] = None
    sample_type:      Optional[str] = None
    sampling_date:    Optional[date]  = None
    sampling_operator:Optional[str]   = None

class BioSampleRead(BioSampleBase):
    id: int
    comments: List[CommentRead] = []

    class Config:
        orm_mode = True
