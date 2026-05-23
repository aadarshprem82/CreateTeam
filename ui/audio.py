import base64
from pathlib import Path

import streamlit as st


def autoplay_audio(file_path: Path) -> None:
    """
    Play audio automatically in Streamlit.

    Safely skips playback if file does not exist.
    """

    if not file_path.exists():
        st.warning(f"Audio file not found: {file_path.name}")
        return

    with open(file_path, "rb") as audio_file:
        audio_bytes = audio_file.read()

    encoded_audio = base64.b64encode(audio_bytes).decode()

    audio_html = f"""
        <audio autoplay style="display:none;">
            <source
                src="data:audio/mp3;base64,{encoded_audio}"
                type="audio/mp3"
            >
        </audio>
    """

    st.markdown(
        audio_html,
        unsafe_allow_html=True,
    )