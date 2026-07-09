# TODO

- [ ] Refactor `app.py` to store Gemini API key in `st.session_state` and remove fragile local `api_key` dependency from `handle_chat()`.
- [ ] Make CSS loading robust using `pathlib.Path(__file__).parent / "assets" / "style.css"`.
- [ ] Update Gemini API text input to bind to `st.session_state.gemini_api_key`.
- [ ] Sanity test: run `streamlit run app.py`, upload a document, and try chat + summary generation.

