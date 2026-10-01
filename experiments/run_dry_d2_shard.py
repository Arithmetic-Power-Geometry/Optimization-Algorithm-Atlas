import csv,sys,time,random,hashlib,json
from pathlib import Path
import numpy as np,cocoex,cma
from scipy.optimize import differential_evolution,minimize
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"experiments"))
from objective_recorder import ObjectiveRecorder
OUT=ROOT/"artifacts"/"validation";OUT.mkdir(parents=True,exist_ok=True)
FUN=(1,10,15);D=2;INS=1;SEED=11;MAX=1000*D;CPS=(100*D,300*D,1000*D);rows=[]
def getp(f):
 s=cocoex.Suite("bbob","",f"function_indices:{f} dimensions:{D} instance_indices:{INS}");return s,s[0]
def finish(alg,f,p,r,t,status):
 if r.evaluations!=p.evaluations:raise RuntimeError(f"{alg} counter mismatch")
 for q in r.snapshot():
  rows.append(["DRY-D2","PUBBBOB001","EF001",alg,f,D,INS,SEED,q["checkpoint"],q["observed"],q["best"],
   r.evaluations,p.evaluations,time.perf_counter()-t,p.id,status,"DRY_RUN_ONLY","NO"])
for f in FUN:
 s,p=getp(f);rng=random.Random(SEED);r=ObjectiveRecorder(p,CPS);t=time.perf_counter()
 while r.evaluations<MAX:r([rng.uniform(-5,5) for _ in range(D)])
 finish("RandomSearch",f,p,r,t,"BUDGET_EXHAUSTED");p.free();s.free()
 s,p=getp(f);r=ObjectiveRecorder(p,CPS);t=time.perf_counter();pop=10*D;mi=max(0,MAX//pop-1)
 differential_evolution(r,[(-5,5)]*D,strategy="best1bin",popsize=10,mutation=.5,recombination=.9,seed=SEED,
  polish=False,maxiter=mi,tol=0,atol=0,workers=1,updating="immediate")
 finish("SciPy-DE",f,p,r,t,"COMPLETED_LIBRARY_RUN");p.free();s.free()
 s,p=getp(f);r=ObjectiveRecorder(p,CPS);t=time.perf_counter()
 minimize(r,np.zeros(D)+3,method="Nelder-Mead",bounds=[(-5,5)]*D,options={"maxfev":MAX,"xatol":0.0,"fatol":0.0,"adaptive":False})
 finish("SciPy-NelderMead",f,p,r,t,"BUDGET_EXHAUSTED" if r.evaluations==MAX else "NATIVE_TERMINATION");p.free();s.free()
 s,p=getp(f);r=ObjectiveRecorder(p,CPS);t=time.perf_counter()
 es=cma.CMAEvolutionStrategy([3.0]*D,2.0,{"seed":SEED,"bounds":[-5,5],"verbose":-9,"verb_disp":0,"popsize":10,"maxfevals":MAX,"tolfun":0,"tolfunhist":0,"tolx":0,"tolstagnation":0})
 while r.evaluations<MAX:
  xs=es.ask()[:MAX-r.evaluations]
  if not xs:break
  es.tell(xs,[r(x) for x in xs])
 finish("pycma-CMAES",f,p,r,t,"BUDGET_EXHAUSTED" if r.evaluations==MAX else "NATIVE_TERMINATION");p.free();s.free()
cols=["shard_id","experiment_id","freeze_id","algorithm","function_id","dimension","instance","seed","checkpoint","checkpoint_observed","best_at_checkpoint","final_recorder_evals","final_coco_evals","runtime_seconds","problem_id","termination_status","run_status","paper_evidence"]
out=OUT/"dry_d2_raw.csv"
with out.open("w",newline="",encoding="utf-8") as fh:w=csv.writer(fh);w.writerow(cols);w.writerows(rows)
prov={"shard_id":"DRY-D2","freeze_id":"EF001","rows":len(rows),"sha256":hashlib.sha256(out.read_bytes()).hexdigest()}
(OUT/"dry_d2_provenance.json").write_text(json.dumps(prov,indent=2)+"\n")
print(prov)
