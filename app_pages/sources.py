import streamlit as st
from app_utils.data import load_sources

st.title("Sources & Provenance")
df=load_sources()
if df.empty:
    st.info("Source ledger is empty.")
    st.stop()

q=st.text_input("Search title, author, algorithm, venue or DOI")
view=df.copy()
if q:
    x=q.lower()
    view=view[view.astype(str).apply(lambda r:r.str.lower().str.contains(x,regex=False).any(),axis=1)]
st.dataframe(view,use_container_width=True,hide_index=True)
st.caption("A verified bibliographic record does not by itself validate every empirical claim made in that source. Claim-level evidence is audited separately.")
