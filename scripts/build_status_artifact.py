import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
src=ROOT/"evidence"/"status_matrix.csv"
out=ROOT/"artifacts"/"tables"
out.mkdir(parents=True,exist_ok=True)
with src.open(encoding="utf-8",newline="") as f:
    rows=list(csv.DictReader(f))
lines=["# Optimization Evidence Status — Initial Matrix","","Status is condition-specific. UNTESTED is never interpreted as failure.","","| Algorithm | Condition | Status | Confidence | Resolution needed |","|---|---|---|---|---|"]
for r in rows:
    lines.append(f"| {r['algorithm_id']} | {r['condition']} | {r['status']} | {r['confidence']} | {r['resolution_needed']} |")
lines += ["","Generated from evidence/status_matrix.csv. This artifact is descriptive, not a ranking."]
(out/"evidence_status_matrix.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
print("wrote artifacts/tables/evidence_status_matrix.md")
