import streamlit as st


def render_metrics(
    risk,
    total_findings,
    document_type,
    score,
):
    """
    Render dashboard metric cards.
    """

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        with st.container(border=True):

            st.caption("🟢 Risk Level")

            st.markdown(f"## {risk}")

    with c2:

        st.info("🔍 Total Findings")

        st.markdown(f"## {total_findings}")

    with c3:

        st.info("📄 Document Type")

        st.markdown(f"## {document_type}")

    with c4:

        st.info("🛡 Compliance Score")

        st.markdown(f"## {score}/100")