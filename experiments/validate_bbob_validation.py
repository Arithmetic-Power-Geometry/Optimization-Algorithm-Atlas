import csv, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(ROOT/"experiments"/"run_bbob_validation.py")],check=True)
p=ROOT/"artifacts"/"validation"/"bbob_validation_raw.csv"
with p.open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
expected=4*3*3*3*3
if len(rows)!=expected: raise SystemExit(f"expected {expected}, got {len(rows)}")
for r in rows:
 if r["status"]!="STANDARD_SUITE_VALIDATION":raise SystemExit("status guard failed")
 if int(r["evaluations_used"])!=int(r["budget_evals"]):raise SystemExit("evaluation-budget mismatch")
 if not r["problem_id"].startswith("bbob_"):raise SystemExit("invalid BBOB id")
print("BBOB STANDARD-SUITE VALIDATION PASSED",len(rows))
