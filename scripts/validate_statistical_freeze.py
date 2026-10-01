import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/"experiments"/"publication_design.csv"
with p.open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
ids=[r["design_id"] for r in rows]
if len(ids)!=len(set(ids)):raise SystemExit("duplicate design id")
if any(r["status"]!="DRAFT_FREEZE" for r in rows):raise SystemExit("design cannot be promoted before comparator/environment freeze")
required={"PD-CONT-01","PD-FRONTIER-01","PD-NOISE-01","PD-PBO-01"}
if set(ids)!=required:raise SystemExit("publication design set mismatch")
for r in rows:
 if not r["primary_endpoint"] or not r["budget_levels"]:raise SystemExit("incomplete design row "+r["design_id"])
print("STATISTICAL DESIGN DRAFT VALID",len(rows),"domains")
