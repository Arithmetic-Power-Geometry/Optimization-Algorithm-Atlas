import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
dims=[5,10,20,40]
out=ROOT/"artifacts"/"publication"/"CROSS-DIMENSIONAL";out.mkdir(parents=True,exist_ok=True)
rows=[]
for D in dims:
 p=ROOT/"artifacts"/"publication"/f"PUB-D{D}"/f"PUB-D{D}_function_checkpoint_summary.csv"
 with p.open(encoding="utf-8",newline="") as f:
  for r in csv.DictReader(f):
   rows.append({"dimension":D,"algorithm":r["algorithm"],"function_id":r["function_id"],"checkpoint":r["checkpoint"],"fe_per_dimension":int(r["checkpoint"])/D,"n":r["n"],"cell_status":r["cell_status"],"median_best":r["median_best"],"mean_best":r["mean_best"],"min_best":r["min_best"],"max_best":r["max_best"],"evidence_state":"DESCRIPTIVE_SCALING_NOT_TARGET_ECDF"})
p=out/"checkpoint_scaling_cells.csv"
with p.open("w",encoding="utf-8",newline="") as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
assert len(rows)==1152,len(rows)
assert {float(r["fe_per_dimension"]) for r in rows}=={100.0,300.0,1000.0}
print("CROSS-DIMENSIONAL CHECKPOINT CELLS",len(rows),"unobserved",sum(r["cell_status"]=="UNOBSERVED" for r in rows))
