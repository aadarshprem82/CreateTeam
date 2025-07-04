import streamlit as st
import random
import base64
import time

st.set_page_config(page_title="Create Cricket Team", layout="centered")

st.markdown("""
    <style>
        .team-box {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .player {
            font-size: 18px;
            margin: 5px 0;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🏏 Create Cricket Team")

st.markdown("Add player names one by one. When ready, click **Divide Teams** to get balanced teams!")

# ---- SESSION STATE ----
if 'players' not in st.session_state:
    st.session_state.players = []

with st.form("player_form", clear_on_submit=True):
    name = st.text_input("Enter player name:")
    submitted = st.form_submit_button("➕ Add Player")
    if submitted and name.strip():
        st.session_state.players.append(name.strip().title())

if st.session_state.players:
    st.markdown("### 👥 Player List:")
    st.markdown(", ".join(f"`{p}`" for p in st.session_state.players))
else:
    st.info("No players added yet.")

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio style="display:none;" controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )
        
def display_players_with_delay(team, prefix):
    for player in team:
        # Create a placeholder for each player (it will be updated one by one)
        player_placeholder = st.empty()
        
        player = f"{prefix} {player}" 
        # Display player with a delay
        player_placeholder.text(player)
        
        autoplay_audio("./pop.mp3")
        
        # Introduce a delay (you can adjust this value to control the speed)
        time.sleep(0.5)


if st.button("🚀 Divide Teams") and st.session_state.players:
    players = st.session_state.players.copy()
    random.shuffle(players)

    common_player = None
    if len(players) % 2 == 1:
        common_player = players.pop()

    mid = len(players) // 2
    team1 = players[:mid]
    team2 = players[mid:]

    if 'team1' not in st.session_state:
        st.session_state.team1 = team1

    if 'team2' not in st.session_state:
        st.session_state.team2 = team2

    st.markdown("## 🏏 Teams")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🟦 Team 1")
        # st.markdown('<div class="team-box">' + "<br>".join(f'🔹 <span class="player">{p}</span>' for p in team1) + "</div>", unsafe_allow_html=True)
        display_players_with_delay(team1, "🔹")

    with col2:
        st.markdown("### 🟥 Team 2")
        # st.markdown('<div class="team-box">' + "<br>".join(f'🔸 <span class="player">{p}</span>' for p in team2) + "</div>", unsafe_allow_html=True)
        display_players_with_delay(team2,"🔸")

    if common_player:
        autoplay_audio("./drum.mp3")
        time.sleep(0.4)
        st.markdown(f"### 🧢 Common Player: `{common_player}` plays for **both teams**!")
    
    countdown_placeholder = st.empty()
    coin_toss_delay = 5
    for i in range(coin_toss_delay, 0, -1):
        countdown_placeholder.markdown(f"**Tossing the 🥎Coin in {i} seconds...**")
        time.sleep(1)
        countdown_placeholder.empty()
    
    st.markdown("---")
    st.subheader("🥎Coin Tossed!")

    # if 'coin_toss_result' not in st.session_state:
    # toss_button = st.button("Toss Coin")

    if st.session_state.team1 and st.session_state.team2:
        autoplay_audio("./coin_flip.mp3")
        
        toss_dict = {"team1":0,"team2":0}
        for _ in range(100):    
            if random.choice(["team1", "team2"]) == "team1":
                toss_dict["team1"] += 1 
            else:
                toss_dict["team2"] += 1
        
        toss_result = "🟦 Team 1" if toss_dict["team1"] > toss_dict["team2"] else "🟥 Team 2"

        st.session_state.coin_toss_result = toss_result

        time.sleep(1)
        autoplay_audio("./coin_drop.mp3")
        time.sleep(3.2)
        st.success(f"🎉 {toss_result} won the toss.")
        # else:
        #     st.write(f"The coin toss result was: **{st.session_state.coin_toss_result}**")


if st.button("🔄 Reset Players"):
    st.session_state.players = []
    st.rerun()
