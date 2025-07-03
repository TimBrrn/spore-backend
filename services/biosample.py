from typing import List
from datetime import date, timedelta

from sqlmodel import Session, select, update as sql_update
from sqlalchemy.orm import selectinload

from models import BioSample
from schemas.biosample import BioSampleCreate, BioSampleUpdate

def create(session: Session, data: BioSampleCreate) -> BioSample:
    sample = BioSample.model_validate(data)
    session.add(sample)
    session.commit()
    session.refresh(sample)
    return sample

def get_all(session: Session, page: int, size: int) -> List[BioSample]:
    stmt = (
        select(BioSample)
        .options(selectinload(BioSample.comments))
        .offset((page - 1) * size)
        .limit(size)
    )
    return session.exec(stmt).all()

def get(session: Session, sample_id: int) -> BioSample:
    sample = session.get(BioSample, sample_id)
    if not sample:
        raise ValueError("Sample not found")
    return sample

def update(session: Session, sample_id: int, data: BioSampleUpdate) -> BioSample:
    update_data = data.model_dump(exclude_unset=True)
    if not update_data:
        return session.get(BioSample, sample_id)
    session.exec(
        sql_update(BioSample)
        .where(BioSample.id == sample_id)
        .values(**update_data)
    )
    session.commit()
    return session.get(BioSample, sample_id)

def delete(session: Session, sample_id) -> None:
    sample = get(session, sample_id)
    session.delete(sample)
    session.commit()

def create_samples(session: Session) -> None:
    locations = [
        "Lab-A", "Lab-B", "Lab-C", "Lab-D",
        "Lab-E", "Lab-F", "Lab-G", "Lab-H",
        "Lab-I", "Lab-J", "Lab-K", "Lab-L",
    ]

    types = [
        "water", "chocolate", "flour", "soil",
        "milk", "air", "yeast", "coffee",
    ]

    operators = [
        "Alice", "Bob", "Charlie", "Diane",
        "Marc", "Nina", "Oscar", "Paul",
        "Quentin", "Rita", "Sophie", "Tom",
    ]

    base_date = date(2023, 1, 1)

    samples = [
        BioSample(
            sampling_location = locations[i % len(locations)],
            sample_type       = types[i % len(types)],
            sampling_date     = base_date + timedelta(days=15 * i),
            sampling_operator = operators[i % len(operators)],
            comments          = [],
        )
        for i in range(20)
    ]

    session.add_all(samples)
    session.commit()