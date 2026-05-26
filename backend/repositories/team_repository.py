from sqlalchemy.orm import Session

from database.models.player_model import Player
from database.models.team_model import Team


class TeamRepository:
    @staticmethod
    def create_team(db: Session, name: str) -> Team:
        team = Team(name=name)

        db.add(team)

        db.commit()

        db.refresh(team)

        return team

    @staticmethod
    def get_all_teams(db: Session) -> list[Team]:
        return db.query(Team).all()
    
    @staticmethod
    def get_team_by_name(db: Session, name: str) -> Team|None:
        return db.query(Team).filter(Team.name == name).first()
    
    @staticmethod
    def get_team_by_id(db: Session, team_id: int ) -> Team | None:
        return db.query(Team).filter(Team.id == team_id).first()
    
    @staticmethod
    def get_player_by_id(db: Session, player_id: int) -> Player| None:
        return db.query(Player).filter(Player.id == player_id).first()
    
    @staticmethod
    def add_player_to_team(db: Session, team: Team, player: Player) -> Team:
        team.players.append(player)

        db.commit()
        db.refresh(team)

        return team