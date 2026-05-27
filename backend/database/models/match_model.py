from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, Integer

from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base

class Match(Base):
    __tablename__ = "matches"

    id : Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    team1_id : Mapped[int] = mapped_column(Integer, ForeignKey("teams.id"), nullable=False)

    team2_id : Mapped[int] = mapped_column(Integer, ForeignKey("teams.id"), nullable=False)

    toss_winner_team_id : Mapped[int] = mapped_column(ForeignKey("teams.id"), nullable=False)

    created_at : Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))

    team1 = relationship("Team", foreign_keys=[team1_id])

    team2 = relationship("Team", foreign_keys=[team2_id])

    toss_winner = relationship("Team", foreign_keys=[toss_winner_team_id])