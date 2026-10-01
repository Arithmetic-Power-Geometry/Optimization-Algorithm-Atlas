import csv,statistics
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];src=ROOT/"artifacts"/"publication"/"PUB-D5"/"PUB-D5_merged_checkpoints.csv";out=ROOT/"artifacts"/"publication"/"PUB-D5"
rows=list(csv.DictReader(src.open(encoding="utf-8",newline="")))
g=defaultdict(list)
for r in rows:
 if r["observed"].lower() in {"true","1","yes"}:
  g[(r["algorithm"],int(r["function_id"]),int(r["checkpoint"]))].append(float(r["best_at_checkpoint"]))
p=out/"PUB-D5_function_checkpoint_summary.csv"
with p.open("w",encoding="utf-8",newline="") as f:
 w=csv.writer(f);w.writerow(["algorithm","function_id","checkpoint","n","median_best","mean_best","min_best","max_best","status"])
 for k,v in sorted(g.items()):
  w.writerow([*k,len(v),statistics.median(v),statistics.fmean(v),min(v),max(v),"DESCRIPTIVE_RUN_COMPLETE_UNVERIFIED"])
print("D5 DESCRIPTIVE SUMMARY",len(g),"cells")
