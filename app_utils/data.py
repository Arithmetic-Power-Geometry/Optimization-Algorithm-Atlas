from pathlib import Path
import pandas as pd
import streamlit as st

ROOT=Path(__file__).resolve().parents[1]

@st.cache_data
def _csv(path):
    p=ROOT/path
    return pd.read_csv(p).fillna("") if p.exists() else pd.DataFrame()

def load_census(): return _csv("census/master_census.csv")
def load_sources(): return _csv("evidence/sources.csv")
def load_fingerprints(): return _csv("evidence/mechanism_fingerprints.csv")
def load_status(): return _csv("evidence/status_matrix.csv")
def load_gaps():
    p=ROOT/"gap_registry"/"CROSS_FAMILY_GAPS.csv"
    return pd.read_csv(p).fillna("") if p.exists() else pd.DataFrame()
