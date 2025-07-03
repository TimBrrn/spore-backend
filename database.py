import os
from sqlmodel import Session, SQLModel, create_engine
from sqlalchemy import event
from dotenv import load_dotenv

load_dotenv() 

sqlite_url = os.getenv("DATABASE_URL", "sqlite:///database.db")

engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

@event.listens_for(engine, "connect")
def _enable_sqlite_fk(dbapi_connection, _):
    dbapi_connection.execute("PRAGMA foreign_keys = ON")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session