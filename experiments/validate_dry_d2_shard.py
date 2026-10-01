import csv,json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/"artifacts"/"validation";p=OUT/"dry_d2_raw.csv"
with p.open(encoding="utf-8",newline="") as f:r=list(csv.DictReader(f))
if len(r)!=3*4*3:raise SystemExit(f"expected 36 rows got {len(r)}")
keys=set()
for x in r:
 if x["shard_id"]!="DRY-D2" or x["freeze_id"]!="EF001" or x["run_status"]!="DRY_RUN_ONLY" or x["paper_evidence"]!="NO":raise SystemExit("status/evidence leak")
 if int(x["final_recorder_evals"])!=int(x["final_coco_evals"]):raise SystemExit("counter mismatch")
 k=(x["algorithm"],x["function_id"],x["dimension"],x["instance"],x["seed"],x["checkpoint"])
 if k in keys:raise SystemExit("duplicate merge key")
 keys.add(k)
 if not x["problem_id"].startswith("bbob_"):raise SystemExit("bad BBOB id")
prov=json.loads((OUT/"dry_d2_provenance.json").read_text())
if prov["sha256"]!=hashlib.sha256(p.read_bytes()).hexdigest():raise SystemExit("hash mismatch")
print("DRY-D2 VALID",len(r),"rows",len(keys),"unique merge keys")
