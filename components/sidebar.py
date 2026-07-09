import streamlit as st
from streamlit_option_menu import option_menu


def render_sidebar():
    """
    Render application sidebar.
    Returns selected menu item.
    """

    with st.sidebar:

        st.markdown(
            """
            <h2 style='text-align:center;'>🛡️</h2>
            <h3 style='text-align:center;'>Compliance Assistant</h3>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        selected = option_menu(
            menu_title=None,
            options=[
                "Dashboard",
                "Upload",
                "Detection",
                "AI Summary",
                "Chat",
                "About",
            ],
            icons=[
                "house",
                "cloud-upload",
                "shield-lock",
                "robot",
                "chat-dots",
                "info-circle",
            ],
            default_index=0,
        )

    return selected