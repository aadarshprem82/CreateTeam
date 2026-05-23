from pathlib import Path

# -----------------------------
# PROJECT PATHS
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

ASSETS_DIR = BASE_DIR / "assets"

# -----------------------------
# AUDIO FILES
# -----------------------------

POP_SOUND = ASSETS_DIR / "pop.mp3"
DRUM_SOUND = ASSETS_DIR / "drum.mp3"
COIN_FLIP_SOUND = ASSETS_DIR / "coin_flip.mp3"
COIN_DROP_SOUND = ASSETS_DIR / "coin_drop.mp3"

# -----------------------------
# UI SETTINGS
# -----------------------------

PAGE_TITLE = "Create Cricket Team"
LAYOUT = "centered"

# -----------------------------
# ANIMATION / DELAYS
# -----------------------------

PLAYER_REVEAL_DELAY = 0.4
COIN_TOSS_COUNTDOWN = 5
COIN_DROP_DELAY = 3

# -----------------------------
# TEAM SETTINGS
# -----------------------------

TEAM_1_NAME = "Team 1"
TEAM_2_NAME = "Team 2"

TEAM_1_ICON = "🟦"
TEAM_2_ICON = "🟥"

PLAYER_ICON_TEAM_1 = "🔹"
PLAYER_ICON_TEAM_2 = "🔸"

# -----------------------------
# VALIDATION
# -----------------------------

MAX_PLAYER_NAME_LENGTH = 25
MIN_PLAYERS_REQUIRED = 2