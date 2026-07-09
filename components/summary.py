import streamlit as st
from utils.summarizer import generate_summary


def render_summary(api_key, extracted_text, detected_data):

    st.subheader("🤖 AI Compliance Summary")

    if "summary" not in st.session_state:
        st.session_state.summary = ""

    clicked = st.button(
        "✨ Generate AI Summary",
        key="generate_summary_btn",
        type="primary"
    )


    if clicked:

        if not api_key:
            st.warning("Please enter your Gemini API Key first.")
        else:
            with st.spinner("Generating summary..."):
                st.session_state.summary = generate_summary(
                    api_key,
                    extracted_text,
                    detected_data
                )

    if st.session_state.summary:
        st.success("Summary Generated Successfully!")
        st.markdown(st.session_state.summary)