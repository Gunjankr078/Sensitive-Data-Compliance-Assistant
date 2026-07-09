import streamlit as st


def render_chat(messages, ask_callback):
    """Render AI Chat UI"""

    # ---------------- SHOW ONLY WHEN OPEN ---------------- #
    if not st.session_state.chat_open:
        return

    # ---------------- CSS ---------------- #
    st.markdown(
        """
        <style>

        .chat-overlay{
            position:fixed;
            right:25px;
            bottom:110px;
            width:420px;
            height:650px;
            background:white;
            border-radius:22px;
            box-shadow:
                0 20px 60px rgba(0,0,0,.18);
            z-index:999999;
            border:1px solid #E5E7EB;
            overflow:hidden;
        }

        .chat-header{
            background:linear-gradient(
                135deg,
                #6366F1,
                #7C3AED
            );
            color:white;
            padding:18px;
            display:flex;
            justify-content:space-between;
            align-items:center;
        }

        .chat-title{
            font-size:20px;
            font-weight:bold;
        }

        .online{
            color:#BBF7D0;
            font-size:13px;
            margin-top:5px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # ---------------- WINDOW ---------------- #
    with st.container(border=True):
        c1, c2 = st.columns([8, 1])

        with c1:
            st.markdown(
                """
                <div class="chat-header">
                    <div>
                        <div class="chat-title">🤖 Toast Ai</div>
                        <div class="online">🟢 Online</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with c2:
            if st.button("Close", key="close_chat"):
                st.session_state.chat_open = False
                st.rerun()

        chat = st.container(height=420)

        with chat:
            if len(messages) == 0:
                st.markdown(
                    """
                    ## 👋 Welcome

                    Ask me anything about your uploaded document.

                    **Suggested actions**
                    """
                )

                # Use custom HTML buttons (non-round) for better look.
                

                st.markdown("### Suggested Actions")

                col1, col2 = st.columns(2)

                with col1:
                    if st.button("📄 Summarize", key="sum_btn", use_container_width=True):
                        ask_callback("Summarize this document.")

                    if st.button("⚠️ Compliance Risks", key="risk_btn", use_container_width=True):
                        ask_callback("What compliance risks are identified?")

                with col2:
                    if st.button("🔍 Sensitive Data", key="data_btn", use_container_width=True):
                        ask_callback("What sensitive data exists in the document?")

                    if st.button("🛡 Security Recommendations", key="recommend_btn", use_container_width=True):
                        ask_callback("Give me security recommendations.")


            for msg in messages:
                with st.chat_message(msg["role"]):
                    st.markdown(msg["content"])

        question = st.chat_input("Ask anything...")
        if question:
            ask_callback(question)

