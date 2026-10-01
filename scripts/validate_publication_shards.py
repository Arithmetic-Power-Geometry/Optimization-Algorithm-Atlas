import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
with (ROOT/"experiments"/"publication_shards.csv").open(encoding="utf-8",newline="") as f:r=list(csv.DictReader(f))
pub=[x for x in r if x["shard_id"].startswith("PUB-")]
if [int(x["dimension"]) for x in pub]!=[2,5,10,20,40]:raise SystemExit("dimension shards incomplete")
for x in pub:
 if x["freeze_id"]!="EF001" or x["status"]!="AUTHORIZED_NOT_RUN":raise SystemExit("bad publication shard state")
 if x["functions"]!="1-24" or x["instances"]!="1-5" or x["seeds"]!="11;23;37":raise SystemExit("coverage drift")
 if x["max_budget"]!="1000*D" or x["checkpoints"]!="100*D;300*D;1000*D":raise SystemExit("budget drift")
 if x["paper_evidence"]!="NO_UNTIL_PROMOTED":raise SystemExit("premature evidence status")
dry=[x for x in r if x["shard_id"]=="DRY-D2"]
if len(dry)!=1 or dry[0]["paper_evidence"]!="NO":raise SystemExit("dry run evidence leak")
print("PUBBBOB001 SHARD PLAN VALID",len(pub),"publication shards + dry run")
