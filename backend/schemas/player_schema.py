from datetime import datetime

from pydantic import BaseModel, ConfigDict

class PlayerCreate(BaseModel):
    name : str

class PlayerResponse(BaseModel):
    id : int
    name : str
    created_at : datetime

    model_config = ConfigDict(from_attributes=True)