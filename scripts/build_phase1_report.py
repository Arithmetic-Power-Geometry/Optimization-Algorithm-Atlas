import csv
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"artifacts"/"tables"
OUT.mkdir(parents=True,exist_ok=True)
with (ROOT/"evidence"/"algorithms.csv").open(encoding="utf-8",newline="") as f:
    rows=list(csv.DictReader(f))
families=Counter(r["family"] for r in rows)
roles=Counter(r["scope_role"] for r in rows)
lines=["# Phase-1 Registry Summary","",f"Algorithms/family records: **{len(rows)}**","","## Family coverage","","| Family | Records |","|---|---:|"]
for k,v in sorted(families.items(),key=lambda x:(-x[1],x[0])): lines.append(f"| {k} | {v} |")
lines += ["","## Scope roles","","| Role | Records |","|---|---:|"]
for k,v in sorted(roles.items(),key=lambda x:(-x[1],x[0])): lines.append(f"| {k} | {v} |")
lines += ["","## Interpretation","","This table describes registry coverage only. It is not an algorithm ranking and contains no performance claim.","","Generated automatically from evidence/algorithms.csv."]
(OUT/"phase1_registry_summary.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
print("wrote artifacts/tables/phase1_registry_summary.md")
