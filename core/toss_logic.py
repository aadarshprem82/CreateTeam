import random

from core.models import Team, TossResult


def toss_coin(team1: Team, team2: Team) -> TossResult:
    """
    Randomly select one team as toss winner.
    """

    winning_team = random.choice([team1.name, team2.name])

    return TossResult(
        winner=winning_team
    )