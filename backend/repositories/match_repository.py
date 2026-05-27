import random

from sqlalchemy.orm import Session

from database.models.match_model import Match
from database.models.team_model import Team


class MatchRepository:
    @staticmethod
    def get_team_by_id(db: Session, team_id: int) -> Team | None:
        return db.query(Team).filter(Team.id == team_id).first()
    
    @staticmethod
    def create_match(db: Session, team1_id: int, team2_id: int, toss_winner_team_id: int) -> Match:
        match = Match(team1_id = team1_id, team2_id = team2_id, toss_winner_team_id = toss_winner_team_id)

        db.add(match)
        db.commit()
        db.refresh(match)

        return match

    @staticmethod
    def get_all_matches(db: Session) -> list[Match]:
        return db.query(Match).all()