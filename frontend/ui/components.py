import time

import streamlit as st

from core.models import Player, Team, TeamResult, TossResult
from ui.audio import autoplay_audio
from utils.constants import (
    PLAYER_ICON_TEAM_1,
    PLAYER_ICON_TEAM_2,
    PLAYER_REVEAL_DELAY,
    COIN_TOSS_COUNTDOWN,
    COIN_DROP_DELAY,
    POP_SOUND,
    DRUM_SOUND,
    COIN_FLIP_SOUND,
    COIN_DROP_SOUND,
)


# -----------------------------
# PLAYER DISPLAY
# -----------------------------

def render_player_list(players: list[Player]) -> None:
    """
    Display all added players.
    """

    if not players:
        st.info("No players added yet.")
        return

    st.markdown("### 👥 Player List")

    formatted_players = ", ".join(
        f"`{player.name}`"
        for player in players
    )

    st.markdown(formatted_players)


# -----------------------------
# TEAM DISPLAY
# -----------------------------

def display_players_with_animation(
    players: list[Player],
    prefix: str,
) -> None:
    """
    Reveal players one-by-one with sound effect.
    """

    for player in players:
        player_placeholder = st.empty()

        player_placeholder.markdown(
            f"""
            <div class="player">
                {prefix} {player.name}
            </div>
            """,
            unsafe_allow_html=True,
        )

        autoplay_audio(POP_SOUND)

        time.sleep(PLAYER_REVEAL_DELAY)


def render_team(team: Team, player_icon: str) -> None:
    """
    Render a single team section.
    """

    st.markdown(f"### {team.icon} {team.name}")

    with st.container(border=True):
        display_players_with_animation(
            team.players,
            player_icon,
        )


def render_teams(team_result: TeamResult) -> None:
    """
    Render both teams side-by-side.
    """

    st.markdown("## 🏏 Teams")

    col1, col2 = st.columns(2)

    with col1:
        render_team(
            team_result.team1,
            PLAYER_ICON_TEAM_1,
        )

    with col2:
        render_team(
            team_result.team2,
            PLAYER_ICON_TEAM_2,
        )

    if team_result.common_player:
        autoplay_audio(DRUM_SOUND)

        st.markdown(
            f"""
            ### 🧢 Common Player:
            `{team_result.common_player.name}`
            plays for both teams!
            """
        )


# -----------------------------
# COIN TOSS DISPLAY
# -----------------------------

def render_coin_toss_countdown() -> None:
    """
    Display toss countdown animation.
    """

    countdown_placeholder = st.empty()

    for seconds in range(COIN_TOSS_COUNTDOWN, 0, -1):

        countdown_placeholder.markdown(
            f"## 🥎 Tossing coin in {seconds}..."
        )

        time.sleep(1)

    countdown_placeholder.empty()


def render_toss_result(toss_result: TossResult) -> None:
    """
    Display toss result with audio effects.
    """

    st.markdown("---")

    st.subheader("🥎 Coin Toss")

    autoplay_audio(COIN_FLIP_SOUND)

    time.sleep(1)

    autoplay_audio(COIN_DROP_SOUND)

    time.sleep(COIN_DROP_DELAY)

    st.success(
        f"🎉 {toss_result.winner} won the toss!"
    )