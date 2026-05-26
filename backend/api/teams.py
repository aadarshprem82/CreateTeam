from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from database.dependencies import get_db

from schemas.team_schema import TeamCreate, TeamResponse

from services.team_service import TeamService


router = APIRouter(prefix="/teams", tags=["Teams"])

@router.post("/", response_model=TeamResponse)
def create_team(payload: TeamCreate, db: Session = Depends(get_db)):
    try:
        return TeamService.create_team(db, payload.name)
    
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    

@router.get("/", response_model=list[TeamResponse])
def get_all_teams(db: Session = Depends(get_db)):
    return TeamService.get_all_teams(db)


@router.post("/{team_id}/players/{player_id}", response_model=TeamResponse)
def add_player_to_team(team_id: int, player_id:int, db: Session = Depends(get_db)):
    try:
        return TeamService.add_player_to_team(db, team_id, player_id)
    
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))