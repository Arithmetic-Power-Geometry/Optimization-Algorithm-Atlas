import csv,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];P=ROOT/"artifacts"/"publication"/"PUB-D2";rows=[]
for i in range(1,5):
 p=P/f"D2-B0{i}_raw.csv"
 with p.open(encoding="utf-8",newline="") as f:
  rr=list(csv.DictReader(f));rows.extend(rr)
if len(rows)!=3600:raise SystemExit(f"expected 3600 rows got {len(rows)}")
cols=list(rows[0]);out=P/"PUB-D2_merged_raw.csv"
with out.open("w",encoding="utf-8",newline="") as f:
 w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(rows)
prov={"shard_id":"PUB-D2","freeze_id":"EF001","rows":len(rows),"source_batches":["D2-B01","D2-B02","D2-B03","D2-B04"],"sha256":hashlib.sha256(out.read_bytes()).hexdigest(),"status":"RUN_COMPLETE_UNVERIFIED"}
(P/"PUB-D2_merged_provenance.json").write_text(json.dumps(prov,indent=2)+"\n")
print(prov)
