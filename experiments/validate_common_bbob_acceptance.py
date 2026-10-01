import csv,subprocess,sys,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(ROOT/"experiments"/"run_common_bbob_acceptance.py")],check=True)
p=ROOT/"artifacts"/"validation"/"common_bbob_acceptance_raw.csv"
with p.open(encoding="utf-8",newline="") as f:rows=list(csv.DictReader(f))
if len(rows)!=3*2*2*2*4:raise SystemExit(f"expected 96 rows, got {len(rows)}")
for r in rows:
 if int(r["evaluations_used"])>int(r["budget_evals"]):raise SystemExit("budget exceeded")
 if not math.isfinite(float(r["best_observed"])):raise SystemExit("non-finite result")
 if not r["problem_id"].startswith("bbob_"):raise SystemExit("invalid BBOB id")
print("COMMON BBOB ACCEPTANCE VALID",len(rows),"runs")
