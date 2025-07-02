from typing import List, Optional
from datetime import datetime
from datetime import date
from sqlmodel import Relationship, SQLModel, Field

class BioSample(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sampling_location: str
    sample_type: str
    sampling_date: date
    sampling_operator: str

    comments: Optional[List["Comment"]] = Relationship(back_populates="biosample")


class Comment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sample_id: int = Field(foreign_key="biosample.id")
    text: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    biosample: Optional["BioSample"] = Relationship(back_populates="comments")