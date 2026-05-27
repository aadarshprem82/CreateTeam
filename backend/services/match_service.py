import random

from sqlalchemy.orm import Session

from database.models.match_model import Match

from repositories.match_repository import MatchRepository


class MatchService:
    @staticmethod
    def create_match(db: Session, team1_id: int, team2_id: int) -> Match:
        if team1_id == team2_id:
            raise ValueError("A team cannot play against itself")
        
        team1 = MatchRepository.get_team_by_id(db, team1_id)

        if not team1:
            raise ValueError("Team1 not found")
        
        team2 = MatchRepository.get_team_by_id(db, team2_id)

        if not team2:
            raise ValueError("Team2 not found")
        
        toss_winner_team_id = random.choice([team1_id, team2_id])

        return MatchRepository.create_match(db, team1_id, team2_id, toss_winner_team_id)
    
    @staticmethod
    def get_all_matches(db: Session) -> list[Match]:
        return MatchRepository.get_all_matches(db)