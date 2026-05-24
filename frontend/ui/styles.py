import streamlit as st


def load_global_styles() -> None:
    """
    Load custom global CSS styles.
    """

    st.markdown(
        """
        <style>

        /* -----------------------------
           Main App Styling
        ----------------------------- */

        .main {
            padding-top: 1rem;
        }

        /* -----------------------------
           Team Box
        ----------------------------- */

        .team-box {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 12px;
            border: 1px solid #d9d9d9;
        }

        /* -----------------------------
           Player Text
        ----------------------------- */

        .player {
            font-size: 18px;
            margin: 6px 0;
            color: #111111;
            font-weight: 500;
        }

        /* -----------------------------
           Section Headers
        ----------------------------- */

        .section-title {
            margin-top: 1rem;
            margin-bottom: 0.5rem;
        }

        /* -----------------------------
           Toss Result
        ----------------------------- */

        .toss-result {
            font-size: 22px;
            font-weight: bold;
            color: #1f77b4;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )