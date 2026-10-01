import streamlit as st
from app_utils.data import load_status

st.title("Condition-Level Evidence Atlas")
st.markdown("Evidence is interpreted at the level of **algorithm × condition**, not as a universal algorithm score.")
df=load_status()
if df.empty:
    st.info("Condition-level evidence cells are still being populated.")
    st.stop()

status_col="evidence_status" if "evidence_status" in df.columns else ("status" if "status" in df.columns else None)
if status_col:
    choices=sorted(df[status_col].astype(str).unique())
    selected=st.multiselect("Evidence states", choices, default=choices)
    df=df[df[status_col].astype(str).isin(selected)]
st.dataframe(df,use_container_width=True,hide_index=True)
st.warning("UNTESTED means that adequate evidence has not been identified; it does not mean the algorithm failed.")
