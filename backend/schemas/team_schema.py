from datetime import datetime

from pydantic import BaseModel, ConfigDict

from schemas.player_schema import PlayerResponse


class TeamCreate(BaseModel):
    name : str


class TeamResponse(BaseModel):
    id : int
    name : str
    created_at : datetime

    players : list[PlayerResponse] = []

    model_config = ConfigDict(from_attributes=True)