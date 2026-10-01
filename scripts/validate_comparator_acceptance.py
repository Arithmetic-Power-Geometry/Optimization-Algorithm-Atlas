import json,csv,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
raw=ROOT/"artifacts"/"validation"/"comparator_acceptance.json"
manifest=ROOT/"experiments"/"comparator_acceptance_manifest.csv"
with manifest.open(encoding="utf-8",newline="") as f:m=list(csv.DictReader(f))
if len(m)!=3 or any(r["paper_evidence"]!="NO" or r["status"]!="ACCEPTANCE_ONLY" for r in m):
 raise SystemExit("acceptance manifest guard failed")
rows=json.loads(raw.read_text(encoding="utf-8"))
if {r["algorithm"] for r in rows}!={"SciPy-DE","SciPy-NelderMead","pycma-CMAES"}:
 raise SystemExit("acceptance result panel mismatch")
for r in rows:
 if r["status"]!="ACCEPTANCE_ONLY":raise SystemExit("status guard failed")
 if int(r["nfev"])>500:raise SystemExit("budget exceeded")
 if not math.isfinite(float(r["best"])):raise SystemExit("non-finite result")
print("COMPARATOR ACCEPTANCE VALID",len(rows),"implementations")
