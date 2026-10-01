import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
with (ROOT/"experiments"/"pub_d2_batches.csv").open(encoding="utf-8",newline="") as f:r=list(csv.DictReader(f))
if len(r)!=4:raise SystemExit("expected four D2 batches")
expected=["1-6","7-12","13-18","19-24"]
if [x["functions"] for x in r]!=expected:raise SystemExit("function partition drift")
for x in r:
 if x["shard_id"]!="PUB-D2" or x["freeze_id"]!="EF001" or x["dimension"]!="2":raise SystemExit("identity drift")
 if x["instances"]!="1-5" or x["seeds"]!="11;23;37":raise SystemExit("block design drift")
 if x["status"]!="AUTHORIZED_NOT_RUN" or x["paper_evidence"]!="NO_UNTIL_PROMOTED":raise SystemExit("premature state")
print("PUB-D2 BATCH PLAN VALID",len(r),"batches")
