from fastapi import FastAPI

from app.api.routes import router
from app.db.session import engine
from app.models.base import Base
from app.models import entities  # noqa: F401

app = FastAPI(title="NBA Legacy Universe Tracker API", version="0.1.0")


@app.on_event("startup")
def startup() -> None:
    Base.metadata.create_all(bind=engine)


app.include_router(router, prefix="/api")
