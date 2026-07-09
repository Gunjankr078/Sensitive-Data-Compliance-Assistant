import streamlit as st

def floating_button():
    st.markdown("""
    <style>
    div[data-testid="stButton"] > button[kind="secondary"]{
        position: fixed;
        bottom: 22px;
        right: 22px;
        width: 90px;
        height: 90px;
        border-radius: 50%;
        background: linear-gradient(135deg,#6366F1,#7C3AED);
        color: white;
        border: none;
        font-size: 16px;
        font-weight: bold;
        z-index: 999999;
        box-shadow: 0 10px 30px rgba(124,58,237,.45);
    }

    div[data-testid="stButton"] > button[kind="secondary"]:hover{
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

    return st.button(
        "Toast Ai",
        key="floating_ai",
        type="secondary",
    )