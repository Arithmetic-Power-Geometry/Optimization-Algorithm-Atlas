import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
src=ROOT/"publication"/"completeness_requirements.csv"
out=ROOT/"artifacts"/"tables"
out.mkdir(parents=True,exist_ok=True)
with src.open(encoding="utf-8",newline="") as f:
    rows=list(csv.DictReader(f))
counts={}
for r in rows:
    counts[r["current_state"]]=counts.get(r["current_state"],0)+1
lines=["# Publication Readiness Dashboard","",
"Readiness is based on evidence-layer completion, not manuscript length.","",
"| Layer | Required artifact | Completion rule | State |","|---|---|---|---|"]
for r in rows:
    lines.append(f"| {r['layer']} | {r['required_artifact']} | {r['completion_rule']} | {r['current_state']} |")
lines += ["","## State counts",""]
for k,v in sorted(counts.items()):
    lines.append(f"- {k}: {v}")
lines += ["","The paper remains blocked until evidence freeze criteria are met."]
(out/"publication_readiness.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
print("wrote artifacts/tables/publication_readiness.md")
