import streamlit as st

st.set_page_config(
    page_title="Optimization Evidence Atlas",
    page_icon="📚",
    layout="wide",
)

pages = {
    "Explore": [
        st.Page("app_pages/home.py", title="Home", icon=":material/home:", default=True),
        st.Page("app_pages/algorithms.py", title="Algorithm Explorer", icon=":material/search:"),
        st.Page("app_pages/mechanisms.py", title="Mechanism Atlas", icon=":material/account_tree:"),
        st.Page("app_pages/evidence.py", title="Evidence Atlas", icon=":material/grid_on:"),
    ],
    "Research": [
        st.Page("app_pages/gaps.py", title="Gap & Frontier Explorer", icon=":material/biotech:"),
        st.Page("app_pages/sources.py", title="Sources & Provenance", icon=":material/library_books:"),
        st.Page("app_pages/about.py", title="Methods", icon=":material/info:"),
    ],
}
pg = st.navigation(pages)
pg.run()
