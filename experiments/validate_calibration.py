import csv, hashlib, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
runner=ROOT/"experiments"/"run_calibration.py"
raw=ROOT/"artifacts"/"validation"/"calibration_raw.csv"

def digest():
    return hashlib.sha256(raw.read_bytes()).hexdigest()

subprocess.run([sys.executable,str(runner)],check=True)
d1=digest()
subprocess.run([sys.executable,str(runner)],check=True)
d2=digest()
if d1!=d2: raise SystemExit("deterministic replay failed")
with raw.open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
if len(rows)!=90: raise SystemExit(f"expected 90 rows, got {len(rows)}")
if {int(r["budget_evals"]) for r in rows}!={2000}: raise SystemExit("budget mismatch")
if {r["status"] for r in rows}!={"CALIBRATION_ONLY"}: raise SystemExit("publication-status guard failed")
print("CALIBRATION VALIDATION PASSED",d1)
