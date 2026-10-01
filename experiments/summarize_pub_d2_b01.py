import csv,statistics
from collections import defaultdict,Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];P=ROOT/"artifacts"/"publication"/"PUB-D2";src=P/"D2-B01_raw.csv"
with src.open(encoding="utf-8",newline="") as f:r=list(csv.DictReader(f))
grp=defaultdict(list); term=Counter(); observed=Counter(); total=Counter()
for x in r:
 k=(x["algorithm"],int(x["function_id"]),int(x["checkpoint"]))
 total[k]+=1
 if x["checkpoint_observed"]=="True" and x["best_at_checkpoint"] not in ("","None"):
  observed[k]+=1;grp[k].append(float(x["best_at_checkpoint"]))
 term[(x["algorithm"],x["termination_status"])]+=1
out=P/"D2-B01_descriptive_summary.csv"
with out.open("w",newline="",encoding="utf-8") as f:
 w=csv.writer(f);w.writerow(["algorithm","function_id","checkpoint","records","observed","median_best","status"])
 for k in sorted(total,key=lambda z:(z[0],z[1],z[2])):
  vals=grp[k];w.writerow([*k,total[k],observed[k],statistics.median(vals) if vals else "", "DESCRIPTIVE_RUN_COMPLETE_UNVERIFIED"])
tout=P/"D2-B01_termination_summary.csv"
with tout.open("w",newline="",encoding="utf-8") as f:
 w=csv.writer(f);w.writerow(["algorithm","termination_status","checkpoint_rows","status"])
 for k,n in sorted(term.items()):w.writerow([*k,n,"DESCRIPTIVE_RUN_COMPLETE_UNVERIFIED"])
print("B01 DESCRIPTIVE AUDIT",len(r),"raw rows",len(total),"condition-checkpoint groups")
