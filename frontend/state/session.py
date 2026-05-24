import streamlit as st

from core.models import Player, TeamResult


def initialize_session_state() -> None:
    """
    Initialize all required session state variables.
    """

    defaults = {
        "players": [],
        "team_result": None,
        "toss_result": None,
        "show_animation": False,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


# -----------------------------
# PLAYER STATE
# -----------------------------

def get_players() -> list[Player]:
    return st.session_state.players


def add_player(player: Player) -> None:
    st.session_state.players.append(player)


def reset_players() -> None:
    print("Resetting players!!")
    st.session_state.team_result = None
    st.session_state.toss_result = None
    st.session_state.players = []


# -----------------------------
# TEAM RESULT STATE
# -----------------------------

def set_team_result(team_result: TeamResult) -> None:
    st.session_state.team_result = team_result


def get_team_result() -> TeamResult | None:
    return st.session_state.team_result


# -----------------------------
# TOSS RESULT STATE
# -----------------------------

def set_toss_result(toss_result) -> None:
    st.session_state.toss_result = toss_result


def get_toss_result():
    return st.session_state.toss_result

# -----------------------------
# SHOW ANIMATION STATE
# -----------------------------

def enable_animation():
    st.session_state.show_animation = True

def disable_animation():
    st.session_state.show_animation = False

def should_show_animation():
    return st.session_state.show_animation