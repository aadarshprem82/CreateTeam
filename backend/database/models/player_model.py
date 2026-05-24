from datetime import datetime
from datetime import timezone

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base


class Player(Base):
    __tablename__ = "players"

    id : Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name : Mapped[str] = mapped_column(String, nullable=False)
    created_at : Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
