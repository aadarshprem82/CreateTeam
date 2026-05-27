from datetime import datetime

from pydantic import BaseModel, ConfigDict

from schemas.team_schema import TeamResponse


class MatchCreate(BaseModel):
    team1_id : int
    team2_id : int

class MatchResponse(BaseModel):
    id : int

    team1 : TeamResponse
    team2 : TeamResponse
    toss_winner : TeamResponse

    created_at : datetime

    model_config = ConfigDict(from_attributes=True)