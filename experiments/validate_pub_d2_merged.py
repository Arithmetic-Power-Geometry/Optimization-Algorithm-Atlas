import csv,json,hashlib,math
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];P=ROOT/"artifacts"/"publication"/"PUB-D2";p=P/"PUB-D2_merged_raw.csv"
with p.open(encoding="utf-8",newline="") as f:r=list(csv.DictReader(f))
if len(r)!=3600:raise SystemExit("row count")
if set(map(lambda x:int(x["function_id"]),r))!=set(range(1,25)):raise SystemExit("function coverage")
keys=set();traj=defaultdict(list)
for x in r:
 if x["shard_id"]!="PUB-D2" or x["freeze_id"]!="EF001" or x["run_status"]!="RUN_COMPLETE_UNVERIFIED" or x["paper_evidence"]!="NO_UNTIL_PROMOTED":raise SystemExit("state drift")
 if int(x["final_recorder_evals"])!=int(x["final_coco_evals"]):raise SystemExit("counter mismatch")
 if x["algorithm"]=="SciPy-NelderMead":
  if x["seed"]!="NA":raise SystemExit("NM false replication")
 elif x["seed"] not in {"11","23","37"}:raise SystemExit("stochastic seed drift")
 k=(x["algorithm"],x["function_id"],x["dimension"],x["instance"],x["seed"],x["checkpoint"])
 if k in keys:raise SystemExit("duplicate atomic key")
 keys.add(k)
 traj[(x["algorithm"],x["function_id"],x["instance"],x["seed"])].append(x)
for k,rr in traj.items():
 rr.sort(key=lambda z:int(z["checkpoint"]));vals=[float(z["best_at_checkpoint"]) for z in rr if z["checkpoint_observed"]=="True" and z["best_at_checkpoint"] not in ("","None")]
 if any(vals[i]>vals[i-1] for i in range(1,len(vals))):raise SystemExit(f"best-so-far worsened {k}")
prov=json.loads((P/"PUB-D2_merged_provenance.json").read_text())
if prov["sha256"]!=hashlib.sha256(p.read_bytes()).hexdigest():raise SystemExit("merged hash mismatch")
print("PUB-D2 MERGED INTEGRITY VALID",len(r),"rows",len(keys),"unique keys",len(traj),"trajectories")
