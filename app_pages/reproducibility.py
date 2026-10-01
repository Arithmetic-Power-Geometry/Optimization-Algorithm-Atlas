import streamlit as st
from app_utils.data import load_freezes,load_gates
st.title("Reproducibility")
st.subheader("Execution freezes"); st.dataframe(load_freezes(),use_container_width=True,hide_index=True)
st.subheader("Paper gates"); st.dataframe(load_gates(),use_container_width=True,hide_index=True)
st.info("PROJECT-VALIDATED evidence requires frozen design, provenance, integrity, statistics and clean regeneration. RUN_COMPLETE_UNVERIFIED is not publication promotion.")
