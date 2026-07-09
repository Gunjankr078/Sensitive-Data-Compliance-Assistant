import streamlit as st
import plotly.express as px

# Note: keep imports aligned; the app does not currently use `px`, `generate_summary`, or `mask_value`. 
from pathlib import Path
from components.sidebar import render_sidebar
from utils.extractor import extract_text
from utils.detector import detect_sensitive_data
from utils.classifier import classify_risk
from utils.scorer import calculate_score
from utils.summarizer import generate_summary
from utils.chatbot import ask_question
from utils.masker import mask_value
from components.chat_ui import render_chat
from components.floating_button import floating_button
from components.metrics import render_metrics
from components.detection import render_detection
from components.charts import render_chart
from components.summary import render_summary


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Sensitive Data Detection & Compliance Assistant",
    page_icon="🛡️",
    layout="wide"
)


css_path = Path(__file__).parent / "assets" / "style.css"

with open(css_path, encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


if "messages" not in st.session_state:
    st.session_state.messages = []

if "summary" not in st.session_state:
    st.session_state.summary = None

if "last_file" not in st.session_state:
    st.session_state.last_file = ""

if "chat_open" not in st.session_state:
    st.session_state.chat_open = False


if "summary_generated" not in st.session_state:
    st.session_state.summary_generated = False

if "gemini_api_key" not in st.session_state:
    st.session_state.gemini_api_key = ""


# ---------------- HEADER ---------------- #

st.title("🛡️ Sensitive Data Detection & Compliance Assistant")

st.write(
    "Upload a document to detect sensitive information and generate compliance insights."
)

st.divider()



# ---------------- UPLOAD ---------------- #

st.subheader("📤 Upload Document")

uploaded_file = st.file_uploader(
    "Choose a PDF, TXT or CSV file",
    type=["pdf", "txt", "csv"],
)

# Reset when a new file is uploaded
if uploaded_file:

    if (
        "last_uploaded" not in st.session_state
        or st.session_state.last_uploaded != uploaded_file.name
    ):

        st.session_state.last_uploaded = uploaded_file.name

        st.session_state.summary = None
        st.session_state.summary_generated = False
        st.session_state.messages = []
        st.session_state.processed_file = ""

def handle_chat(question):
    api_key = st.session_state.get("gemini_api_key", "")


    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.spinner("Thinking..."):

        if not api_key:
            answer = "⚠️ Please enter your Gemini API Key first."
        else:
            answer = ask_question(
                api_key,
                st.session_state.extracted_text,
                st.session_state.detected_data,
                question,
            )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )

    st.rerun()

# ---------------- SHOW DASHBOARD ONLY AFTER UPLOAD ---------------- #
selected = render_sidebar()

if uploaded_file:

    # Keep a single main container to avoid nested column/layout constraints.
    # Chat UI is handled by an overlay (floating panel) so it shouldn't affect layout width.
    main_area = st.container()

    with main_area:

        st.success(f"Uploaded Successfully : {uploaded_file.name}")

        if (
            "processed_file" not in st.session_state
            or st.session_state.processed_file != uploaded_file.name
        ):

            with st.spinner("Analyzing document..."):

                st.session_state.extracted_text = extract_text(uploaded_file)

                st.session_state.detected_data = detect_sensitive_data(
                st.session_state.extracted_text
            )

                st.session_state.processed_file = uploaded_file.name
            

        extracted_text = st.session_state.extracted_text

        detected_data = st.session_state.detected_data

        risk = classify_risk(detected_data)

        score = calculate_score(detected_data)

        total_findings = sum(len(v) for v in detected_data.values())

        # ---------------- METRIC CARDS ---------------- #

        render_metrics(
            risk=risk,
            total_findings=total_findings,
            document_type=uploaded_file.name.split(".")[-1].upper(),
            score=score,
        )

        # ---------------- TWO COLUMN LAYOUT ---------------- #

        left, right = st.columns([1.3, 1])

                        # LEFT

        with left:
            render_detection(detected_data)

                        # RIGHT

        with right:

            render_chart(detected_data)

            st.divider()

            st.subheader("🔑 Gemini API")

            api_key = st.text_input(
            "Enter Gemini API Key",
            type="password",
            key="gemini_api_key"
        )
        
        st.divider()

        render_summary(
            api_key,
            extracted_text,
            detected_data
        )

# ---------------- ABOUT ---------------- #

    if selected == "About":

        st.divider()

        st.subheader("About This Project")

        st.write(
            """

            This application detects sensitive information from documents
            such as PDF, TXT and CSV files.

            Features:

           • Sensitive Data Detection

           • Risk Classification

           • AI Generated Compliance Summary

           • AI Question Answering

           Developed using:

           - Streamlit

           - Python

           - Google Gemini
           """
        )

    # ---------------- FLOATING AI BUTTON ---------------- #

    if not st.session_state.chat_open:

        clicked = floating_button()

        if clicked:
            st.session_state.chat_open = True
            st.rerun()

    st.divider()

    render_chat(
        st.session_state.messages,
        handle_chat
    )


st.divider()

st.markdown(
    """
    <div style="text-align:center; padding:15px 0 25px 0;">
        <h2 style="margin-bottom:8px;">
            About Sensitive Data Detection & Compliance Assistant
        </h2>
        <p style="font-size:16px; color:#6B7280; max-width:900px; margin:auto;">
            An AI-powered document analysis platform designed to identify sensitive
            information, assess compliance risks, and generate intelligent security
            recommendations for uploaded documents.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True, height=340):
        st.markdown("### Features")
        st.markdown("""
        - PDF, TXT & CSV Support
        - Sensitive Data Detection
        - Interactive Dashboard
        - AI Compliance Summary
        - AI Document Chat
        - Risk Classification
        """)

with col2:
    with st.container(border=True, height=340):
        st.markdown("### Detects")
        st.markdown("""
        - Email Addresses
        - Phone Numbers
        - Aadhaar Numbers
        - PAN Numbers
        - Credit Cards
        - Bank Accounts
        - API Keys
        - Employee IDs
        """)

# st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    with st.container(border=True, height=220):
        st.markdown("### Technology")
        st.markdown("""
        - **Frontend:** Streamlit
        - **Language:** Python
        - **Charts:** Plotly
        - **AI:** Google Gemini
        - **Parsing:** PDF • TXT • CSV
        """)

with col4:
    with st.container(border=True, height=220):
        st.markdown("### Purpose")
        st.markdown("""
        The Sensitive Data Detection & Compliance Assistant is designed to help organizations identify confidential and sensitive information within documents before they are shared or stored. By leveraging automated detection, AI-driven compliance analysis, and intelligent risk assessment, the application enhances data security, supports regulatory compliance, and assists organizations in making informed decisions to reduce potential security and privacy risks.
        """)

st.success("✅ AI-powered Compliance & Security Assistant")

st.markdown(
    """
    <div style="text-align:center; color:gray; padding-top:15px;">
        Version 1.0 • Built with Streamlit, Python, Plotly and Google Gemini
    </div>
    """,
    unsafe_allow_html=True,
)