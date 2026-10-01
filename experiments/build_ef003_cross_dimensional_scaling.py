import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
dims=[5,10,20,40]; out=ROOT/"artifacts"/"publication"/"EF003-CROSS-DIMENSIONAL";out.mkdir(parents=True,exist_ok=True)
rows=[]
for D in dims:
 p=ROOT/"artifacts"/"publication"/f"EF003-PUB-D{D}"/"function_checkpoint_summary.csv"
 rr=list(csv.DictReader(p.open()))
 assert len(rr)==288,(D,len(rr))
 assert {r["evidence_state"] for r in rr}=={"RUN_COMPLETE_UNVERIFIED"}
 for r in rr:
  rows.append({"freeze_id":"EF003","dimension":D,"algorithm":r["algorithm"],"function_id":r["function_id"],"checkpoint":r["checkpoint"],"fe_per_dimension":int(r["checkpoint"])/D,"n":r["n"],"cell_status":r["cell_status"],"median_best":r["median_best"],"evidence_state":"RUN_COMPLETE_UNVERIFIED_DESCRIPTIVE_SCALING"})
assert len(rows)==1152
assert {float(r["fe_per_dimension"]) for r in rows}=={100.,300.,1000.}
p=out/"checkpoint_scaling_cells.csv"
with p.open("w",newline="",encoding="utf-8") as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print("EF003 CROSS-DIMENSIONAL",len(rows),"cells","unobserved",sum(r["cell_status"]=="UNOBSERVED" for r in rows))
