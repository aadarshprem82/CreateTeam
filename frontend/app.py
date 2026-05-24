import streamlit as st

from core.models import Player
from core.team_logic import divide_teams
from core.toss_logic import toss_coin

from state.session import (
    initialize_session_state,
    get_players,
    add_player,
    reset_players,
    set_team_result,
    get_team_result,
    set_toss_result,
    get_toss_result,
    enable_animation,
    should_show_animation,
    disable_animation,
)

from ui.styles import load_global_styles

from ui.components import (
    render_player_list,
    render_teams,
    render_coin_toss_countdown,
    render_toss_result,
)

from utils.constants import (
    PAGE_TITLE,
    LAYOUT,
)

from utils.validators import (
    validate_player_name,
    validate_player_count,
    normalize_player_name,
)


# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title=PAGE_TITLE,
    layout=LAYOUT,
)

# -----------------------------
# INITIALIZATION
# -----------------------------

initialize_session_state()

load_global_styles()

# -----------------------------
# PAGE HEADER
# -----------------------------

st.title("🏏 Create Cricket Team")

st.markdown(
    """
    Add player names one by one.
    When ready, click **Divide Teams**
    to generate balanced random teams.
    """
)

# -----------------------------
# PLAYER FORM
# -----------------------------

with st.form("player_form", clear_on_submit=True):

    player_name = st.text_input(
        "Enter player name"
    )

    submitted = st.form_submit_button(
        "➕ Add Player"
    )

    if submitted:

        players = get_players()

        is_valid, error_message = validate_player_name(
            player_name,
            players,
        )

        if not is_valid:
            st.warning(error_message)

        else:
            normalized_name = normalize_player_name(
                player_name
            )

            player = Player(
                name=normalized_name
            )

            add_player(player)

            st.success(
                f"{normalized_name} added successfully."
            )

# -----------------------------
# PLAYER LIST
# -----------------------------

players = get_players()

render_player_list(players)

# -----------------------------
# DIVIDE TEAMS
# -----------------------------

if st.button("🚀 Divide Teams"):

    is_valid, error_message = validate_player_count(
        players
    )

    if not is_valid:
        st.warning(error_message)

    else:

        team_result = divide_teams(players)

        set_team_result(team_result)

        toss_result = toss_coin(
            team_result.team1,
            team_result.team2,
        )

        set_toss_result(toss_result)

        enable_animation()

# -----------------------------
# DISPLAY RESULTS
# -----------------------------

team_result = get_team_result()

toss_result = get_toss_result()

if team_result:

    print(f"before: show_animation: {should_show_animation()}")

    if should_show_animation():
        render_teams(team_result)

        render_coin_toss_countdown()

        render_toss_result(toss_result)

        disable_animation()

    print(f"after: show_animation: {should_show_animation()}")

# -----------------------------
# RESET BUTTON
# -----------------------------

if st.button("🔄 Reset Players"):
    print("Reset button click!!")
    reset_players()

    st.rerun()
