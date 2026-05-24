from core.models import Player
from utils.constants import (
    MAX_PLAYER_NAME_LENGTH,
    MIN_PLAYERS_REQUIRED,
)


def normalize_player_name(name: str) -> str:
    """
    Clean and normalize player name.
    """

    return " ".join(name.strip().title().split())


def validate_player_name(
    name: str,
    existing_players: list[Player],
) -> tuple[bool, str]:
    """
    Validate player name.

    Returns:
        (is_valid, error_message)
    """

    normalized_name = normalize_player_name(name)

    if not normalized_name:
        return False, "Player name cannot be empty."

    if len(normalized_name) > MAX_PLAYER_NAME_LENGTH:
        return (
            False,
            f"Player name cannot exceed {MAX_PLAYER_NAME_LENGTH} characters.",
        )

    existing_names = {
        player.name.lower()
        for player in existing_players
    }

    if normalized_name.lower() in existing_names:
        return False, "Player already added."

    return True, ""


def validate_player_count(players: list[Player]) -> tuple[bool, str]:
    """
    Ensure enough players exist for team generation.
    """

    if len(players) < MIN_PLAYERS_REQUIRED:
        return (
            False,
            f"At least {MIN_PLAYERS_REQUIRED} players are required.",
        )

    return True, ""