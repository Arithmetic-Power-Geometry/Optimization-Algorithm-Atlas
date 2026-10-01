import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
path=ROOT/"census"/"master_census.csv"
with path.open(encoding="utf-8",newline="") as f:
    rows=list(csv.DictReader(f))

errors=[]
ids=[r["census_id"].strip() for r in rows]
names=[r["canonical_name"].strip().lower() for r in rows]
for label,vals in [("census_id",ids),("canonical_name",names)]:
    dup=sorted({x for x in vals if x and vals.count(x)>1})
    if dup: errors.append(f"duplicate {label}: {dup}")

allowed={"FOUNDATION","CANONICAL","MAJOR_VARIANT","SPECIALIST","REDUNDANCY_AUDIT","EMERGING","CATALOG_ONLY"}
bad=sorted({r["role"] for r in rows if r["role"] not in allowed})
if bad: errors.append(f"invalid roles: {bad}")

missing=[r["census_id"] for r in rows if not r["canonical_name"].strip() or not r["lane"].strip() or not r["role"].strip()]
if missing: errors.append(f"missing required fields: {missing}")

if errors:
    print("CENSUS VALIDATION FAILED")
    for e in errors: print("-",e)
    raise SystemExit(1)
print(f"CENSUS VALIDATION PASSED: {len(rows)} identities")
