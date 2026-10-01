import streamlit as st
from app_utils.data import load_suite_registry,load_publication_design
st.title("Benchmark Atlas")
st.caption("Declared benchmark ecosystems, scope, budgets and evidence boundaries.")
a=load_suite_registry(); b=load_publication_design()
st.subheader("Suite registry"); st.dataframe(a,use_container_width=True,hide_index=True)
st.subheader("Publication design"); st.dataframe(b,use_container_width=True,hide_index=True)
st.info("Benchmark inclusion is evidence-led. Calibration and rehearsal outputs are not publication evidence.")
