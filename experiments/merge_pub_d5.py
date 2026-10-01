import csv,json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
stage=ROOT/"artifacts"/"publication"/"D5-STAGE";out=ROOT/"artifacts"/"publication"/"PUB-D5";out.mkdir(parents=True,exist_ok=True)
labels=["PUB-D5-B01","PUB-D5-B02","PUB-D5-B03","PUB-D5-B04"];rows=[];header=None
for label in labels:
 p=stage/label/"checkpoints.csv"
 with p.open(encoding="utf-8",newline="") as fh:
  rr=list(csv.DictReader(fh))
  if len(rr)!=900:raise SystemExit(f"{label}: expected 900 rows, got {len(rr)}")
  if header is None:header=list(rr[0].keys())
  rows.extend(rr)
raw=out/"PUB-D5_merged_checkpoints.csv"
with raw.open("w",encoding="utf-8",newline="") as fh:
 w=csv.DictWriter(fh,fieldnames=header);w.writeheader();w.writerows(rows)
prov={"freeze_id":"EF002","dimension":5,"batches":labels,"rows":len(rows),"sha256":hashlib.sha256(raw.read_bytes()).hexdigest(),"status":"RUN_COMPLETE_UNVERIFIED","paper_evidence":"NO_UNTIL_PROMOTED"}
(out/"PUB-D5_merged_provenance.json").write_text(json.dumps(prov,indent=2)+"\n")
print(prov)
