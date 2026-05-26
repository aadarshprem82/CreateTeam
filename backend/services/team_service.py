from sqlalchemy.orm import Session

from database.models.team_model import Team

from repositories.team_repository import TeamRepository


class TeamService:
    @staticmethod
    def create_team(db: Session, name: str) -> Team:
        existing_team = TeamRepository.get_team_by_name(db, name)

        if existing_team:
            raise ValueError("Team already exists.")
        
        return TeamRepository.create_team(db, name)
    
    @staticmethod
    def get_all_teams(db: Session) -> list[Team]:
        return TeamRepository.get_all_teams(db)
    
    @staticmethod
    def add_player_to_team(db: Session, team_id: int, player_id: int):
        team = TeamRepository.get_team_by_id(db, team_id)

        if not team:
            raise ValueError("Team not found.")
        
        player = TeamRepository.get_player_by_id(db, player_id)
        
        if not player:
            raise ValueError("Player not found.")
        
        if player in team.players:
            raise ValueError("Player already in team.")
        
        return TeamRepository.add_player_to_team(db, team, player)