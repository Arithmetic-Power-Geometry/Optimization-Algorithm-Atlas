import csv,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/"experiments"/"execution_freeze.csv"
with p.open(encoding="utf-8",newline="") as f:rows=list(csv.DictReader(f))
if not rows or any(r["freeze_id"]!="EF001" or r["status"]!="FROZEN" for r in rows):raise SystemExit("bad freeze ledger")
for r in rows:
 path=r["path"]
 got=subprocess.check_output(["git","hash-object",path],cwd=ROOT,text=True).strip()
 if got!=r["git_blob_sha"]:raise SystemExit(f"FREEZE HASH MISMATCH {path}: {got} != {r['git_blob_sha']}")
print("EXECUTION FREEZE EF001 VALID",len(rows),"files")
