import streamlit as st
from app_utils.data import load_fingerprints
st.title("Mechanism Similarity Explorer")
df=load_fingerprints(); st.metric("Source-backed fingerprints",len(df)); st.dataframe(df,use_container_width=True,hide_index=True)
st.caption("Structural similarity is exploratory: it does not imply algorithm identity, plagiarism, or equal performance. Weighting and distance sensitivity must be audited before inferential use.")
