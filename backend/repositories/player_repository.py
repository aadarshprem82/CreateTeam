from sqlalchemy.orm import Session

from database.models.player_model import Player

class PlayerRepository:
    @staticmethod
    def create_player(db:Session, name : str) -> Player:
        player = Player(name=name)
        
        db.add(player)
        db.commit()
        db.refresh(player)

        return player
    
    @staticmethod
    def get_all_players(db:Session) -> list[Player]:
        return db.query(Player).all()

    @staticmethod
    def get_player_by_id(db:Session, id:int) -> Player | None:
        return (db.query(Player).filter(Player.id == id).first())
