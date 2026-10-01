import csv,statistics
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];p=ROOT/"artifacts"/"validation"/"bbob_validation_raw.csv"
with p.open(encoding="utf-8",newline="") as f:rows=list(csv.DictReader(f))
g=defaultdict(list)
for r in rows:g[(r["function_id"],r["dimension"],r["algorithm"])].append(float(r["best_observed"]))
lines=["# Standard-Suite BBOB Validation","","**STANDARD_SUITE_VALIDATION — NOT PAPER EVIDENCE.**","",
"Values below are descriptive medians across validation instances/seeds. No superiority claim is authorized.","",
"| f | D | Algorithm | Median best observed | n |","|---:|---:|---|---:|---:|"]
for (fn,d,a),v in sorted(g.items()):lines.append(f"| {fn} | {d} | {a} | {statistics.median(v):.6g} | {len(v)} |")
lines+=["","This stage validates real BBOB identifiers, instance handling, dimension-scaled budgets and cross-algorithm result plumbing."]
(ROOT/"artifacts"/"validation"/"bbob_validation_summary.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
