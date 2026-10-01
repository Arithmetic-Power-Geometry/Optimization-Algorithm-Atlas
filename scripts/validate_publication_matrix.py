import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
suite=ROOT/"benchmarks"/"suite_registry.csv"
matrix=ROOT/"experiments"/"publication_matrix.csv"
with suite.open(encoding="utf-8",newline="") as f: suites={r["suite_id"] for r in csv.DictReader(f)}
with matrix.open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
bad=[r["matrix_id"] for r in rows if r["suite"] not in suites]
if bad: raise SystemExit("unknown benchmark suite: "+",".join(bad))
if any(r["status"]!="PLANNED" for r in rows): raise SystemExit("publication matrix must remain PLANNED before implementation/environment freeze")
print("PUBLICATION MATRIX VALID",len(rows),"rows",len(suites),"registered suites")
