import streamlit as st
from utils.masker import mask_value


def render_detection(detected_data):
    """
    Render sensitive data detection cards.
    """

    st.subheader("🔍 Sensitive Data Detection")

    st.info(
        "Detection results will appear here after processing the document."
    )

    if not detected_data:
        st.warning("No sensitive data patterns were found.")
        return

    for category, matches in detected_data.items():

        with st.container(border=True):

            # IMPORTANT: avoid nested st.columns here.
            # Nested columns inside an outer Streamlit column can cause severe layout squeezing
            # (the UI “shrinks to a thin column” symptom) after reruns.
            st.markdown(f"### {category}")

            if matches:
                st.metric("Count", len(matches))
                for item in matches:
                    st.caption(mask_value(category, item))
            else:
                st.caption("No data found")
                st.metric("Count", 0)
