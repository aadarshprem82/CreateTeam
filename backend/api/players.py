from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.dependencies import get_db

from schemas.player_schema import (PlayerCreate, PlayerResponse)

from services.player_service import (PlayerService)

router = APIRouter(prefix="/players", tags=["Players"])

@router.post("/", response_model = PlayerResponse)
def create_player(payload:PlayerCreate, db:Session = Depends(get_db)):
    try:
        player = PlayerService.create_player(db, payload.name)

        return player
    
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

@router.get("/", response_model = list[PlayerResponse])
def get_all_players(db:Session = Depends(get_db)):
    return PlayerService.get_all_players(db)

@router.get("/{player_id}", response_model = PlayerResponse)
def get_player_by_id(player_id, db:Session = Depends(get_db)):
    return PlayerService.get_player_by_id(db, player_id)