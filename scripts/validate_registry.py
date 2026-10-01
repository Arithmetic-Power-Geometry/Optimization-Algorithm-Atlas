import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = {
    "algorithms.csv": ["algorithm_id","canonical_name","family","scope_role","agent_id","status"],
    "search_log.csv": ["search_id","database_or_source","search_date","query"],
    "claims.csv": ["claim_id","claim_type","claim_text","source_id","status"],
    "gaps.csv": ["gap_id","title","gap_type","evidence_status","status"],
}
errors=[]
for name, cols in required.items():
    path=ROOT/"evidence"/name
    if not path.exists():
        errors.append(f"missing: {path}")
        continue
    with path.open(encoding="utf-8", newline="") as f:
        reader=csv.DictReader(f)
        missing=[c for c in cols if c not in (reader.fieldnames or [])]
        if missing: errors.append(f"{name}: missing columns {missing}")
        if not list(reader): errors.append(f"{name}: no data rows")
path=ROOT/"evidence"/"algorithms.csv"
if path.exists():
    with path.open(encoding="utf-8", newline="") as f: rows=list(csv.DictReader(f))
    ids=[r["algorithm_id"].strip() for r in rows]
    dup=sorted({x for x in ids if ids.count(x)>1})
    if dup: errors.append(f"duplicate algorithm_id: {dup}")
if errors:
    print("VALIDATION FAILED")
    for e in errors: print("-",e)
    raise SystemExit(1)
print("VALIDATION PASSED")
print("Evidence ledgers and algorithm registry have the required structure.")
