import csv,json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
stage=ROOT/"artifacts"/"publication"/"D40-STAGE";out=ROOT/"artifacts"/"publication"/"PUB-D40";out.mkdir(parents=True,exist_ok=True)
labels=["PUB-D40-B01","PUB-D40-B02","PUB-D40-B03","PUB-D40-B04"];rows=[];header=None
for label in labels:
 p=stage/label/"checkpoints.csv"
 with p.open(encoding="utf-8",newline="") as fh:
  rr=list(csv.DictReader(fh))
  if len(rr)!=900:raise SystemExit(f"{label}: expected 900 rows, got {len(rr)}")
  if header is None:header=list(rr[0].keys())
  rows.extend(rr)
raw=out/"PUB-D40_merged_checkpoints.csv"
with raw.open("w",encoding="utf-8",newline="") as fh:
 w=csv.DictWriter(fh,fieldnames=header);w.writeheader();w.writerows(rows)
prov={"freeze_id":"EF002","dimension":40,"batches":labels,"rows":len(rows),"sha256":hashlib.sha256(raw.read_bytes()).hexdigest(),"status":"RUN_COMPLETE_UNVERIFIED","paper_evidence":"NO_UNTIL_PROMOTED"}
(out/"PUB-D40_merged_provenance.json").write_text(json.dumps(prov,indent=2)+"\n")
print(prov)
