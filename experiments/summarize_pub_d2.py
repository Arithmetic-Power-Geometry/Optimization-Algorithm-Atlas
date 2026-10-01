import csv,statistics,math
from collections import defaultdict,Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];P=ROOT/"artifacts"/"publication"/"PUB-D2";src=P/"PUB-D2_merged_raw.csv"
with src.open(encoding="utf-8",newline="") as f:r=list(csv.DictReader(f))
g=defaultdict(list);rt=defaultdict(list);obs=Counter();tot=Counter();term=Counter()
for x in r:
 k=(x["algorithm"],int(x["function_id"]),int(x["checkpoint"]))
 tot[k]+=1
 if x["checkpoint_observed"]=="True" and x["best_at_checkpoint"] not in ("","None"):
  obs[k]+=1;g[k].append(float(x["best_at_checkpoint"]))
 rt[(x["algorithm"],int(x["function_id"]))].append(float(x["runtime_seconds"]))
 term[(x["algorithm"],x["termination_status"])]+=1
out=P/"PUB-D2_function_checkpoint_summary.csv"
with out.open("w",newline="",encoding="utf-8") as f:
 w=csv.writer(f);w.writerow(["algorithm","function_id","checkpoint","records","observed","median_best","q25_best","q75_best","status"])
 for k in sorted(tot,key=lambda z:(z[1],z[2],z[0])):
  v=sorted(g[k]);q=lambda p:v[min(len(v)-1,max(0,round((len(v)-1)*p)))] if v else ""
  w.writerow([*k,tot[k],obs[k],statistics.median(v) if v else "",q(.25),q(.75),"DESCRIPTIVE_RUN_COMPLETE_UNVERIFIED"])
out=P/"PUB-D2_runtime_summary.csv"
with out.open("w",newline="",encoding="utf-8") as f:
 w=csv.writer(f);w.writerow(["algorithm","function_id","checkpoint_rows","median_runtime_seconds","status"])
 for k,v in sorted(rt.items(),key=lambda z:(z[0][1],z[0][0])):
  w.writerow([*k,len(v),statistics.median(v),"DESCRIPTIVE_RUN_COMPLETE_UNVERIFIED"])
out=P/"PUB-D2_termination_summary.csv"
with out.open("w",newline="",encoding="utf-8") as f:
 w=csv.writer(f);w.writerow(["algorithm","termination_status","checkpoint_rows","status"])
 for k,n in sorted(term.items()):w.writerow([*k,n,"DESCRIPTIVE_RUN_COMPLETE_UNVERIFIED"])
print("PUB-D2 DESCRIPTIVE COMPARISON BUILT",len(g),"function-checkpoint groups")
