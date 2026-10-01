import csv
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"experiments"/"implementation_candidates.csv"
with p.open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
required={"RandomSearch","Nelder-Mead","DE","CMA-ES","PSO","GA"}
seen={r["algorithm"] for r in rows}
if seen!=required: raise SystemExit("candidate panel mismatch: "+repr(required-seen)+" extra="+repr(seen-required))
if any(not r["reason"] for r in rows): raise SystemExit("candidate without rationale")
print("IMPLEMENTATION CANDIDATE PANEL VALID",len(rows))
