import csv
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"experiments"/"pub_d5_batches.csv"
r=list(csv.DictReader(p.open(encoding="utf-8",newline="")))
assert len(r)==4
assert [x["functions"] for x in r]==["1-6","7-12","13-18","19-24"]
assert all(x["freeze_id"]=="EF002" and x["dimension"]=="5" and x["instances"]=="1-5" and x["seeds"]=="11;23;37" for x in r)
assert all(x["status"]=="AUTHORIZED_NOT_RUN" and x["paper_evidence"]=="NO_UNTIL_PROMOTED" for x in r)
print("PUB-D5 BATCH PLAN VALID",len(r),"batches")
