import csv,sys,time,random,hashlib,json
from pathlib import Path
import numpy as np,cocoex,cma
from scipy.optimize import differential_evolution,minimize
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"experiments"))
from objective_recorder import ObjectiveRecorder
OUT=ROOT/"artifacts"/"validation";OUT.mkdir(parents=True,exist_ok=True)
FUN=(1,10,15);DIMS=(2,5);INS=1;SEED=11;rows=[]

def getp(f,d):
 s=cocoex.Suite("bbob","",f"function_indices:{f} dimensions:{d} instance_indices:{INS}");return s,s[0]
def add(alg,f,d,p,r,t,status):
 for q in r.snapshot():
  rows.append([alg,f,d,INS,SEED,q["checkpoint"],q["observed"],q["best"],r.evaluations,p.evaluations,
               time.perf_counter()-t,p.id,status,"ENGINE_REHEARSAL_ONLY"])
def check(name,r,p,maxb):
 if r.evaluations!=p.evaluations:raise RuntimeError(f"{name} recorder/COCO mismatch")
 if r.evaluations>maxb:raise RuntimeError(f"{name} budget exceeded")

for f in FUN:
 for d in DIMS:
  maxb=300*d; cps=(100*d,300*d)
  s,p=getp(f,d);rng=random.Random(SEED);r=ObjectiveRecorder(p,cps);t=time.perf_counter()
  while r.evaluations<maxb:r([rng.uniform(-5,5) for _ in range(d)])
  check("RandomSearch",r,p,maxb);add("RandomSearch",f,d,p,r,t,"BUDGET_EXHAUSTED");p.free();s.free()

  s,p=getp(f,d);r=ObjectiveRecorder(p,cps);t=time.perf_counter();pop=10*d
  # init population consumes pop evaluations; each complete generation consumes pop.
  maxiter=max(0,maxb//pop-1)
  differential_evolution(r,[(-5,5)]*d,strategy="best1bin",popsize=10,mutation=.5,recombination=.9,
    seed=SEED,polish=False,maxiter=maxiter,tol=0,atol=0,workers=1,updating="immediate")
  check("SciPy-DE",r,p,maxb);add("SciPy-DE",f,d,p,r,t,"COMPLETED_LIBRARY_RUN");p.free();s.free()

  s,p=getp(f,d);r=ObjectiveRecorder(p,cps);t=time.perf_counter()
  nm=minimize(r,np.zeros(d)+3,method="Nelder-Mead",bounds=[(-5,5)]*d,
    options={"maxfev":maxb,"xatol":0.0,"fatol":0.0,"adaptive":False})
  check("SciPy-NelderMead",r,p,maxb);add("SciPy-NelderMead",f,d,p,r,t,"BUDGET_EXHAUSTED" if r.evaluations==maxb else "NATIVE_TERMINATION");p.free();s.free()

  s,p=getp(f,d);r=ObjectiveRecorder(p,cps);t=time.perf_counter()
  es=cma.CMAEvolutionStrategy([3.0]*d,2.0,{"seed":SEED,"bounds":[-5,5],"verbose":-9,"verb_disp":0,"popsize":10,
    "maxfevals":maxb,"tolfun":0,"tolfunhist":0,"tolx":0,"tolstagnation":0})
  while r.evaluations<maxb:
   xs=es.ask()[:maxb-r.evaluations]
   if not xs:break
   ys=[r(x) for x in xs];es.tell(xs,ys)
  check("pycma-CMAES",r,p,maxb);add("pycma-CMAES",f,d,p,r,t,"BUDGET_EXHAUSTED" if r.evaluations==maxb else "NATIVE_TERMINATION");p.free();s.free()

cols=["algorithm","function_id","dimension","instance","seed","checkpoint","checkpoint_observed","best_at_checkpoint","final_recorder_evals","final_coco_evals","runtime_seconds","problem_id","termination_status","evidence_status"]
out=OUT/"publication_engine_rehearsal.csv"
with out.open("w",newline="",encoding="utf-8") as fh:w=csv.writer(fh);w.writerow(cols);w.writerows(rows)
manifest=ROOT/"experiments"/"publication_engine_rehearsal_manifest.csv"
prov={"rows":len(rows),"result_sha256":hashlib.sha256(out.read_bytes()).hexdigest(),"manifest_sha256":hashlib.sha256(manifest.read_bytes()).hexdigest()}
(OUT/"publication_engine_rehearsal_provenance.json").write_text(json.dumps(prov,indent=2)+"\n")
print(prov)
