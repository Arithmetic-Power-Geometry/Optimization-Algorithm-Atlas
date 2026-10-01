import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
with (ROOT/"publication"/"PRE_PAPER_BACKLOG.csv").open(encoding="utf-8",newline="") as f:
    rows={r["id"]:r for r in csv.DictReader(f)}

required=[f"P{i:03d}" for i in range(1,34)]
missing=[x for x in required if x not in rows]
if missing:
    print("PRE-PAPER GATE INVALID: missing task IDs",missing)
    raise SystemExit(1)

if rows["P032"]["state"]!="blocked" and rows["P031"]["state"]!="complete":
    print("PRE-PAPER GATE INVALID: paper unblocked before evidence freeze")
    raise SystemExit(1)

if rows["P031"]["state"]=="complete" and rows["P030"]["state"]!="complete":
    print("PRE-PAPER GATE INVALID: evidence freeze completed before clean artifact audit")
    raise SystemExit(1)

print("PRE-PAPER GATE VALID")
