import csv, random, time
from pathlib import Path
import cocoex

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"artifacts"/"validation";OUT.mkdir(parents=True,exist_ok=True)
FUNCTIONS=(1,5,10,15); DIMS=(2,5,10); INST=(1,2,3); SEEDS=(11,23,37)

def rs(p,lo,hi,d,budget,rng):
 best=float("inf")
 while p.evaluations<budget:
  y=float(p([rng.uniform(lo,hi) for _ in range(d)]));best=min(best,y)
 return best

def de(p,lo,hi,d,budget,rng,npop=20,F=.5,CR=.9):
 n=min(npop,max(4,budget)); pop=[[rng.uniform(lo,hi) for _ in range(d)] for _ in range(n)]
 fit=[float(p(x)) for x in pop]
 while p.evaluations<budget:
  for i in range(n):
   if p.evaluations>=budget:break
   ids=list(range(n));ids.remove(i);a,b,c=rng.sample(ids,3);jr=rng.randrange(d);z=[]
   for j in range(d):
    q=max(lo,min(hi,pop[a][j]+F*(pop[b][j]-pop[c][j])))
    z.append(q if rng.random()<CR or j==jr else pop[i][j])
   y=float(p(z))
   if y<=fit[i]:pop[i],fit[i]=z,y
 return min(fit)

def pso(p,lo,hi,d,budget,rng,npop=20,w=.7298,c1=1.49618,c2=1.49618):
 n=min(npop,budget);x=[[rng.uniform(lo,hi) for _ in range(d)] for _ in range(n)];v=[[0.]*d for _ in range(n)]
 pb=[z[:] for z in x];pf=[float(p(z)) for z in x];gi=min(range(n),key=lambda i:pf[i]);g=pb[gi][:];gf=pf[gi]
 while p.evaluations<budget:
  for i in range(n):
   if p.evaluations>=budget:break
   for j in range(d):
    v[i][j]=w*v[i][j]+c1*rng.random()*(pb[i][j]-x[i][j])+c2*rng.random()*(g[j]-x[i][j])
    x[i][j]=max(lo,min(hi,x[i][j]+v[i][j]))
   y=float(p(x[i]))
   if y<pf[i]:
    pb[i],pf[i]=x[i][:],y
    if y<gf:g=x[i][:];gf=y
 return min(pf)

ALGS={"RandomSearch":rs,"DE":de,"PSO":pso}
rows=[]
for f in FUNCTIONS:
 for d in DIMS:
  budget=500*d
  for ins in INST:
   for seed in SEEDS:
    for an,alg in ALGS.items():
     suite=cocoex.Suite("bbob","","function_indices:%d dimensions:%d instance_indices:%d"%(f,d,ins))
     p=suite[0]; lo,hi=-5.0,5.0; rng=random.Random(seed); t=time.perf_counter()
     best=alg(p,lo,hi,d,budget,rng); elapsed=time.perf_counter()-t
     rows.append({"validation_id":"BBOBVAL001","status":"STANDARD_SUITE_VALIDATION","function_id":f,"dimension":d,"instance":ins,"algorithm":an,"seed":seed,"budget_evals":budget,"evaluations_used":p.evaluations,"best_observed":f"{best:.17g}","runtime_seconds":f"{elapsed:.9g}","problem_id":p.id})
     p.free();suite.free()
with (OUT/"bbob_validation_raw.csv").open("w",newline="",encoding="utf-8") as fh:
 wri=csv.DictWriter(fh,fieldnames=rows[0].keys());wri.writeheader();wri.writerows(rows)
print("BBOB validation runs",len(rows))
