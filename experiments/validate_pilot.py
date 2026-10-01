import csv, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(ROOT/"experiments"/"run_pilot.py")],check=True)
p=ROOT/"artifacts"/"validation"/"pilot_raw.csv"
with p.open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
if len(rows)!=270: raise SystemExit(f"expected 270 runs got {len(rows)}")
for r in rows:
    if r["status"]!="PILOT_ONLY": raise SystemExit("status guard failed")
    if int(r["evaluations_used"])!=int(r["budget_evals"]): raise SystemExit("budget enforcement failed")
print("PILOT VALIDATION PASSED",len(rows))
