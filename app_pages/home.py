import streamlit as st
from app_utils.data import load_census, load_sources, load_fingerprints

st.title("Optimization Evidence Atlas")
st.caption("Mechanisms · Evidence · Reproducibility · Failure Frontiers · Open Questions")

census=load_census(); sources=load_sources(); fp=load_fingerprints()
a,b,c=st.columns(3)
a.metric("Algorithm identities", len(census))
b.metric("Verified source records", int((sources["status"]=="verified").sum()) if not sources.empty else 0)
c.metric("Mechanism fingerprints", len(fp))

st.markdown("""
### What this atlas is
A scholarly navigation layer over a reproducible optimization review. It separates **algorithm names** from **computational mechanisms**, and **absence of evidence** from **evidence of failure**.

### Evidence vocabulary
- **DOCUMENTED** — adequate direct evidence exists for the declared condition.
- **PARTIAL** — evidence exists but coverage or controls remain incomplete.
- **CONTRADICTORY** — materially different conclusions are supported.
- **UNTESTED** — adequate evidence has not been identified.
- **PROJECT-VALIDATED** — a controlled repository experiment has passed validation.

The live atlas evolves with the evidence repository. Publication claims will use a frozen version.
""")
