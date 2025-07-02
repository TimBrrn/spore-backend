from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select

from database import create_db_and_tables, engine
from models import BioSample
from services.biosample import create_samples
from routes import biosample, comment

def create_app() -> FastAPI:
    app = FastAPI(title="BioSample API")
    app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"]
    )
    app.include_router(biosample.router)
    app.include_router(comment.router)
    return app

app = create_app()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    with Session(engine) as session:
        already_seeded = session.exec(
            select(BioSample.id).limit(1)
        ).first()

        if not already_seeded:
            create_samples(session) 