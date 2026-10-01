import csv, statistics
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/"artifacts"/"validation"/"pilot_raw.csv"; out=ROOT/"artifacts"/"validation"/"pilot_summary.md"
with p.open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
g=defaultdict(list)
for r in rows:g[(r["function"],r["dimension"],r["budget_evals"],r["algorithm"])].append(float(r["best_objective"]))
lines=["# Pre-Publication Pilot Summary","","**PILOT_ONLY — NOT PAPER EVIDENCE.**","","| Function | D | Budget | Algorithm | Median best |","|---|---:|---:|---|---:|"]
for (fn,d,b,a),v in sorted(g.items()):lines.append(f"| {fn} | {d} | {b} | {a} | {statistics.median(v):.6g} |")
lines += ["","The pilot validates data capture and budget scaling. It is not a basis for algorithm ranking or manuscript claims."]
out.write_text("\n".join(lines)+"\n",encoding="utf-8")
