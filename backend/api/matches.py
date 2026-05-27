from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from database.dependencies import get_db

from schemas.match_schema import MatchCreate, MatchResponse

from services.match_service import MatchService

router = APIRouter(prefix="/matches", tags=["Matches"])

@router.post("/", response_model = MatchResponse)
def create_match(payload: MatchCreate, db: Session = Depends(get_db)):
    try:
        return MatchService.create_match(db, payload.team1_id, payload.team2_id)
    
    except ValueError as error:
        raise HTTPException(status_code=400, detail= str(error))
    
@router.get("/", response_model = list[MatchResponse])
def get_all_matches(db: Session = Depends(get_db)):
    return MatchService.get_all_matches(db)