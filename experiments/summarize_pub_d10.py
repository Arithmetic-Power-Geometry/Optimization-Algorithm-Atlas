import csv,statistics
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];src=ROOT/"artifacts"/"publication"/"PUB-D10"/"PUB-D10_merged_checkpoints.csv";out=ROOT/"artifacts"/"publication"/"PUB-D10"
rows=list(csv.DictReader(src.open(encoding="utf-8",newline="")))
g=defaultdict(list)
for r in rows:
 if r["checkpoint_observed"].lower() in {"true","1","yes"} and r["best_at_checkpoint"] not in {"","NA","None"}:
  g[(r["algorithm"],int(r["function_id"]),int(r["checkpoint"]))].append(float(r["best_at_checkpoint"]))
algs=["RandomSearch","SciPy-DE","SciPy-NelderMead","pycma-CMAES"];cps=[1000,3000,10000]
p=out/"PUB-D10_function_checkpoint_summary.csv"
with p.open("w",encoding="utf-8",newline="") as f:
 w=csv.writer(f);w.writerow(["algorithm","function_id","checkpoint","n","median_best","mean_best","min_best","max_best","cell_status","status"])
 for alg in algs:
  for fn in range(1,25):
   for cp in cps:
    v=g.get((alg,fn,cp),[])
    if v:w.writerow([alg,fn,cp,len(v),statistics.median(v),statistics.fmean(v),min(v),max(v),"OBSERVED","DESCRIPTIVE_RUN_COMPLETE_UNVERIFIED"])
    else:w.writerow([alg,fn,cp,0,"NA","NA","NA","NA","UNOBSERVED","DESCRIPTIVE_RUN_COMPLETE_UNVERIFIED"])
print("D10 DESCRIPTIVE SUMMARY",len(algs)*24*len(cps),"cells","unobserved",sum(1 for alg in algs for fn in range(1,25) for cp in cps if not g.get((alg,fn,cp))))
