import streamlit as st
from app_utils.data import load_gaps

st.title("Gap & Frontier Explorer")
st.markdown("Open questions are shown with their evidence state and proposed resolving experiment where available.")
df=load_gaps()
if df.empty:
    st.info("The validated gap registry is still under construction.")
else:
    st.dataframe(df,use_container_width=True,hide_index=True)

st.markdown("""
### Gap validation ladder
**G0** mentioned absence → **G1** evidence absence → **G2** evidence conflict → **G3** failure boundary → **G4** mechanistic gap → **G5** repair opportunity.

A new optimization mechanism is considered only after established remedies have been evaluated for a surviving G4/G5 gap.
""")
