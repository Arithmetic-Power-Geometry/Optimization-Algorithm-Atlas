import streamlit as st
from app_utils.data import load_fingerprints

st.title("Mechanism Atlas")
df=load_fingerprints()
if df.empty:
    st.info("Mechanism fingerprints are still being populated.")
    st.stop()

st.markdown("Compare algorithms by normalized computational structure rather than inspiration labels.")
ids=st.multiselect("Algorithms", sorted(df["algorithm_id"].unique()), default=list(df["algorithm_id"].unique())[:5])
cols=["algorithm_id","state_type","information_source","proposal_geometry","memory","adaptation","selection","diversity_control","derivative_order","model_type","dominant_overhead"]
st.dataframe(df[df["algorithm_id"].isin(ids)][cols],use_container_width=True,hide_index=True)
st.caption("Structural proximity is a novelty-audit signal, not proof of identity or equivalent empirical behavior.")
