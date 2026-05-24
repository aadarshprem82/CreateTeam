import random

from core.models import Player, Team, TeamResult
from utils.constants import (
    TEAM_1_NAME,
    TEAM_2_NAME,
    TEAM_1_ICON,
    TEAM_2_ICON,
)


def shuffle_players(players: list[Player]) -> list[Player]:
    """
    Return a shuffled copy of players list.
    """
    shuffled = players.copy()
    random.shuffle(shuffled)
    return shuffled


def divide_teams(players: list[Player]) -> TeamResult:
    """
    Divide players into two balanced random teams.

    If odd number of players exists,
    one player becomes the common player.
    """

    if len(players) < 2:
        raise ValueError("At least 2 players are required.")

    shuffled_players = shuffle_players(players)

    common_player = None

    # Handle odd player count
    if len(shuffled_players) % 2 != 0:
        common_player = shuffled_players.pop()

    midpoint = len(shuffled_players) // 2

    team1_players = shuffled_players[:midpoint]
    team2_players = shuffled_players[midpoint:]

    team1 = Team(
        name=TEAM_1_NAME,
        icon=TEAM_1_ICON,
        players=team1_players,
    )

    team2 = Team(
        name=TEAM_2_NAME,
        icon=TEAM_2_ICON,
        players=team2_players,
    )

    return TeamResult(
        team1=team1,
        team2=team2,
        common_player=common_player,
    )