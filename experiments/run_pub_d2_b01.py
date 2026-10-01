import csv,sys,time,random,hashlib,json,os
from pathlib import Path
import numpy as np,cocoex,cma
from scipy.optimize import differential_evolution,minimize
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"experiments"))
from objective_recorder import ObjectiveRecorder
OUT=ROOT/"artifacts"/"publication"/"PUB-D2";OUT.mkdir(parents=True,exist_ok=True)
FUN=range(1,7);D=2;INST=range(1,6);SEEDS=(11,23,37);MAX=1000*D;CPS=(100*D,300*D,1000*D);rows=[]
def getp(f,ins):
 s=cocoex.Suite("bbob","",f"function_indices:{f} dimensions:{D} instance_indices:{ins}");return s,s[0]
def finish(alg,f,ins,seed,p,r,t,status):
 if r.evaluations!=p.evaluations:raise RuntimeError(f"{alg} counter mismatch")
 for q in r.snapshot():
  rows.append(["D2-B01","PUB-D2","PUBBBOB001","EF001",alg,f,D,ins,seed,q["checkpoint"],q["observed"],q["best"],r.evaluations,p.evaluations,time.perf_counter()-t,p.id,status,"RUN_COMPLETE_UNVERIFIED","NO_UNTIL_PROMOTED"])
for f in FUN:
 for ins in INST:
  for seed in SEEDS:
   s,p=getp(f,ins);rng=random.Random(seed);r=ObjectiveRecorder(p,CPS);t=time.perf_counter()
   while r.evaluations<MAX:r([rng.uniform(-5,5) for _ in range(D)])
   finish("RandomSearch",f,ins,seed,p,r,t,"BUDGET_EXHAUSTED");p.free();s.free()
   s,p=getp(f,ins);r=ObjectiveRecorder(p,CPS);t=time.perf_counter();pop=10*D;mi=max(0,MAX//pop-1)
   differential_evolution(r,[(-5,5)]*D,strategy="best1bin",popsize=10,mutation=.5,recombination=.9,seed=seed,polish=False,maxiter=mi,tol=0,atol=0,workers=1,updating="immediate")
   finish("SciPy-DE",f,ins,seed,p,r,t,"COMPLETED_LIBRARY_RUN");p.free();s.free()
   s,p=getp(f,ins);r=ObjectiveRecorder(p,CPS);t=time.perf_counter()
   es=cma.CMAEvolutionStrategy([3.0]*D,2.0,{"seed":seed,"bounds":[-5,5],"verbose":-9,"verb_disp":0,"popsize":10,"maxfevals":MAX,"tolfun":0,"tolfunhist":0,"tolx":0,"tolstagnation":0})
   while r.evaluations<MAX:
    xs=es.ask()[:MAX-r.evaluations]
    if not xs:break
    es.tell(xs,[r(x) for x in xs])
   finish("pycma-CMAES",f,ins,seed,p,r,t,"BUDGET_EXHAUSTED" if r.evaluations==MAX else "NATIVE_TERMINATION");p.free();s.free()
  # deterministic NM once per function-instance block; seed=NA avoids false replication
  s,p=getp(f,ins);r=ObjectiveRecorder(p,CPS);t=time.perf_counter()
  minimize(r,np.zeros(D)+3,method="Nelder-Mead",bounds=[(-5,5)]*D,options={"maxfev":MAX,"xatol":0.0,"fatol":0.0,"adaptive":False})
  finish("SciPy-NelderMead",f,ins,"NA",p,r,t,"BUDGET_EXHAUSTED" if r.evaluations==MAX else "NATIVE_TERMINATION");p.free();s.free()
cols=["batch_id","shard_id","experiment_id","freeze_id","algorithm","function_id","dimension","instance","seed","checkpoint","checkpoint_observed","best_at_checkpoint","final_recorder_evals","final_coco_evals","runtime_seconds","problem_id","termination_status","run_status","paper_evidence"]
out=OUT/"D2-B01_raw.csv"
with out.open("w",newline="",encoding="utf-8") as fh:w=csv.writer(fh);w.writerow(cols);w.writerows(rows)
prov={"batch_id":"D2-B01","freeze_id":"EF001","rows":len(rows),"sha256":hashlib.sha256(out.read_bytes()).hexdigest()}
(OUT/"D2-B01_provenance.json").write_text(json.dumps(prov,indent=2)+"\n")
print(prov)
