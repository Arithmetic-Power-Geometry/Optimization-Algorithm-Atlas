import csv
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"experiments"/"implementation_verification_queue.csv"
with p.open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
ids=[r["verification_id"] for r in rows];algs=[r["algorithm"] for r in rows]
if len(ids)!=len(set(ids)):raise SystemExit("duplicate verification id")
if len(algs)!=len(set(algs)):raise SystemExit("duplicate algorithm")
allowed={"READY","PENDING","VERIFIED","REJECTED"}
bad=[r["verification_id"] for r in rows if r["status"] not in allowed]
if bad:raise SystemExit("invalid verification status: "+",".join(bad))
print("IMPLEMENTATION VERIFICATION QUEUE VALID",len(rows),"comparators")
