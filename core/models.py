from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Player:
    name: str
    rating: int = 50


@dataclass
class Team:
    name: str
    icon: str
    players: list[Player] = field(default_factory=list)

    @property
    def player_count(self) -> int:
        return len(self.players)

    @property
    def total_rating(self) -> int:
        return sum(player.rating for player in self.players)


@dataclass
class TeamResult:
    team1: Team
    team2: Team
    common_player: Optional[Player] = None


@dataclass
class TossResult:
    winner: str