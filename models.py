from typing import List, Optional
from datetime import datetime, timezone
from datetime import date
from sqlalchemy import Column, ForeignKey
from sqlmodel import Relationship, SQLModel, Field

class BioSample(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sampling_location: str
    sample_type: str
    sampling_date: date
    sampling_operator: str

    comments: List["Comment"] = Relationship(
        back_populates="biosample",
        sa_relationship_kwargs={"passive_deletes": True}
    )


class Comment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    sample_id: int = Field(
        sa_column=Column(
            ForeignKey("biosample.id", ondelete="CASCADE"),
            nullable=False
        )
    )
    biosample: Optional["BioSample"] = Relationship(back_populates="comments")