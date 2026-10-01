import csv,json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];P=ROOT/"artifacts"/"publication"/"PUB-D2";p=P/"D2-B04_raw.csv"
with p.open(encoding="utf-8",newline="") as f:r=list(csv.DictReader(f))
# stochastic: 6*5*3*3 algorithms*3 checkpoints=810; deterministic NM: 6*5*3 checkpoints=90
if len(r)!=900:raise SystemExit(f"expected 900 rows got {len(r)}")
keys=set()
for x in r:
 if x["batch_id"]!="D2-B04" or x["freeze_id"]!="EF001" or x["run_status"]!="RUN_COMPLETE_UNVERIFIED" or x["paper_evidence"]!="NO_UNTIL_PROMOTED":raise SystemExit("state leak")
 if int(x["final_recorder_evals"])!=int(x["final_coco_evals"]):raise SystemExit("counter mismatch")
 if x["algorithm"]=="SciPy-NelderMead" and x["seed"]!="NA":raise SystemExit("false deterministic replication")
 k=(x["algorithm"],x["function_id"],x["dimension"],x["instance"],x["seed"],x["checkpoint"])
 if k in keys:raise SystemExit("duplicate key")
 keys.add(k)
prov=json.loads((P/"D2-B04_provenance.json").read_text())
if prov["sha256"]!=hashlib.sha256(p.read_bytes()).hexdigest():raise SystemExit("hash mismatch")
print("PUB-D2 B04 RAW INTEGRITY VALID",len(r),"rows")
