import csv
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"experiments"/"bbob_core_freeze.csv"
with p.open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
if len(rows)!=1:raise SystemExit("expected one core BBOB design")
r=rows[0]
checks={
 "experiment_id":"PUBBBOB001","status":"PREDECLARED_NOT_RUN","suite":"BBOB",
 "functions":"1-24","dimensions":"2;5;10;20;40","instances":"1;2;3;4;5",
 "seeds":"11;23;37","budget_multipliers":"100;300;1000","paper_evidence":"NO_UNTIL_PROMOTED"}
for k,v in checks.items():
 if r[k]!=v:raise SystemExit(f"freeze mismatch {k}: {r[k]!r}")
required={"RandomSearch","SciPy-DE","SciPy-NelderMead","pycma-CMAES"}
if set(r["algorithms"].split(";"))!=required:raise SystemExit("comparator panel mismatch")
print("BBOB CORE PREDECLARATION VALID")
