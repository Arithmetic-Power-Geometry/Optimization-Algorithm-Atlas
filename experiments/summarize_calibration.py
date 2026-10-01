import csv, statistics
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
raw=ROOT/"artifacts"/"validation"/"calibration_raw.csv"
out=ROOT/"artifacts"/"validation"/"calibration_summary.md"
with raw.open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
g=defaultdict(list)
for r in rows:
    g[(r["function"],r["dimension"],r["algorithm"])].append(float(r["best_objective"]))
lines=["# Calibration Summary","","**CALIBRATION_ONLY — NOT PUBLICATION EVIDENCE.**","",
"All algorithms receive the same objective-evaluation budget. Five fixed seeds test deterministic replay and result plumbing.","",
"| Function | D | Algorithm | Median best | Min | Max |","|---|---:|---|---:|---:|---:|"]
for (fn,d,a),v in sorted(g.items()):
    lines.append(f"| {fn} | {d} | {a} | {statistics.median(v):.6g} | {min(v):.6g} | {max(v):.6g} |")
lines += ["","No inferential or superiority claim may be drawn from this calibration run."]
out.write_text("\n".join(lines)+"\n",encoding="utf-8")
print(f"wrote {out}")
