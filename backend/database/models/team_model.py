from datetime import datetime, timezone

from sqlalchemy import (DateTime, ForeignKey, Integer, String, Table, Column,)

from sqlalchemy.orm import (Mapped, mapped_column, relationship,)

from database.base import Base


team_players = Table("team_players", Base.metadata, Column("team_id", ForeignKey("teams.id"), primary_key=True,), Column("player_id", ForeignKey("players.id"), primary_key=True), )

class Team(Base):
    __tablename__ = "teams"

    id : Mapped[int] = mapped_column(Integer, primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))

    players = relationship("Player", secondary=team_players, back_populates="teams")