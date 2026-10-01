import streamlit as st

st.title("Methods and Interpretation")
st.markdown("""
The Optimization Evidence Atlas is a read-only scholarly interface over version-controlled evidence.

### Core analytical unit
**algorithm / variant × problem condition × budget × metric × evidence state**

### Interpretation rules
- Algorithm names are not assumed to represent distinct mechanisms.
- Missing evidence is not interpreted as algorithm failure.
- Structural similarity does not establish identity, plagiarism or equal performance.
- Benchmark ranks do not establish universal superiority.
- Literature-derived evidence and project-generated validation are distinguished.
- Final publication claims will cite a frozen release rather than the evolving live application.

### Paper relationship
The repository and application are research infrastructure. They do not generate the manuscript. The paper will synthesize evidence and artifacts only after the evidence-freeze gate has passed.
""")
