from fastapi import FastAPI

from api.players import router as player_router

from database.base import Base
from database.connection import engine

from database.models.player_model import Player

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Cricket Management API",
    version="1.0.0",
)

app.include_router(player_router)


@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "message": "Cricket API is running",
    }

