import streamlit as st
from app_utils.data import load_comparator_rules,load_gaps
st.title("Researcher Decision Guide")
st.write("Use problem conditions and information assumptions before choosing an optimizer. The atlas does not declare a universal winner.")
st.subheader("Comparator roles"); st.dataframe(load_comparator_rules(),use_container_width=True,hide_index=True)
st.subheader("Open evidence gaps"); st.dataframe(load_gaps(),use_container_width=True,hide_index=True)
st.caption("Recommendations remain conditional on representation, derivative access, objective cost, constraints, dimensionality, noise and evaluation budget.")
