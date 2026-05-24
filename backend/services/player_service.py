from sqlalchemy.orm import Session

from database.models.player_model import Player
from repositories.player_repository import (PlayerRepository)

class PlayerService:
    @staticmethod
    def create_player(db:Session, name:str) -> Player:
        return PlayerRepository.create_player(db, name)
    
    @staticmethod
    def get_all_players(db:Session) -> list[Player]:
        return PlayerRepository.get_all_players(db)
    
    @staticmethod
    def get_player_by_id(db:Session, id:int) -> Player:
        return PlayerRepository.get_player_by_id(db, id)