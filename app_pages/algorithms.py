import streamlit as st
from app_utils.data import load_census, load_sources, load_fingerprints

st.title("Algorithm Explorer")
census=load_census()
if census.empty:
    st.info("Census not yet available.")
    st.stop()

query=st.text_input("Search algorithm, abbreviation, lane or mechanism")
view=census.copy()
if query:
    q=query.lower()
    view=view[view.astype(str).apply(lambda r: r.str.lower().str.contains(q,regex=False).any(),axis=1)]
st.dataframe(view, use_container_width=True, hide_index=True)

names=sorted(census["canonical_name"].dropna().unique())
selected=st.selectbox("Inspect one algorithm", names)
row=census[census["canonical_name"]==selected].iloc[0]
st.subheader(selected)
st.write(f"**Role:** {row['role']} · **Lane:** {row['lane']} · **Census status:** {row['status']}")

fp=load_fingerprints()
abbr=str(row["abbreviation"])
f=fp[fp["algorithm_id"].astype(str)==abbr]
if not f.empty:
    st.markdown("#### Normalized mechanism fingerprint")
    st.dataframe(f.T.rename(columns={f.index[0]:"Value"}), use_container_width=True)

sources=load_sources()
s=sources[sources["algorithm_id"].astype(str)==abbr]
st.markdown("#### Source records")
if s.empty: st.info("No linked source record yet.")
else: st.dataframe(s, use_container_width=True, hide_index=True)
