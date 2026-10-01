import csv,subprocess
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/"experiments"/"execution_freeze.csv"
with p.open(encoding="utf-8",newline="") as fh: rows=list(csv.DictReader(fh))
if not rows: raise SystemExit("empty freeze ledger")
allowed={"EF001","EF002","EF003"}
if {r["freeze_id"] for r in rows}!=allowed: raise SystemExit("unexpected freeze IDs")
if any(r["status"]!="FROZEN" for r in rows): raise SystemExit("non-frozen row in execution freeze")
counts=Counter(r["freeze_id"] for r in rows)
if counts["EF001"]!=5 or counts["EF002"]!=9 or counts["EF003"]!=9: raise SystemExit(f"freeze row-count drift {dict(counts)}")
for r in rows:
 path=r["path"]
 got=subprocess.check_output(["git","hash-object",path],cwd=ROOT,text=True).strip()
 if got!=r["git_blob_sha"]: raise SystemExit(f"FREEZE HASH MISMATCH {r['freeze_id']} {path}: {got} != {r['git_blob_sha']}")
print("EXECUTION FREEZES VALID",dict(counts))
