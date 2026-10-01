import csv,random,time,hashlib,json
from pathlib import Path
import numpy as np,cocoex,cma
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/"artifacts"/"validation";OUT.mkdir(parents=True,exist_ok=True)
FUN=(1,10);D=2;INS=1;SEED=11;CHECK=(100*D,300*D,1000*D);rows=[]

def problem(f):
 s=cocoex.Suite("bbob","",f"function_indices:{f} dimensions:{D} instance_indices:{INS}")
 return s,s[0]
def emit(alg,f,p,best,t0,next_cp):
 while next_cp and p.evaluations>=next_cp[0]:
  cp=next_cp.pop(0);rows.append([alg,f,D,INS,SEED,cp,p.evaluations,best,time.perf_counter()-t0,p.id,"ENGINE_VALIDATION_ONLY"])

for f in FUN:
 # Random search: exact one-evaluation steps.
 s,p=problem(f);rng=random.Random(SEED);best=float("inf");t=time.perf_counter();cp=list(CHECK)
 while p.evaluations<CHECK[-1]:
  best=min(best,float(p([rng.uniform(-5,5) for _ in range(D)])));emit("RandomSearch",f,p,best,t,cp)
 p.free();s.free()

 # DE implemented generation-by-generation through SciPy's solver is not used here because public callback checkpoints
 # are generation-level and may cross an exact checkpoint. Keep DE out of engine smoke until a checkpoint-safe adapter is verified.

 # CMA-ES: ask/tell batches; checkpoint records may occur after a batch crossing and preserve actual evaluation count.
 s,p=problem(f);es=cma.CMAEvolutionStrategy([3.0]*D,2.0,{"seed":SEED,"bounds":[-5,5],"verbose":-9,"verb_disp":0,"popsize":10,"maxfevals":CHECK[-1]});best=float("inf");t=time.perf_counter();cp=list(CHECK)
 while p.evaluations<CHECK[-1]:
  # For accounting validation, disable early-stop semantics and exercise the adapter to the hard evaluation cap.\n  xs=es.ask()[:CHECK[-1]-p.evaluations]
  if not xs:break
  ys=[]
  for x in xs:
   y=float(p(x));ys.append(y);best=min(best,y);emit("pycma-CMAES",f,p,best,t,cp)
  es.tell(xs,ys)
 p.free();s.free()

cols=["algorithm","function_id","dimension","instance","seed","checkpoint","evaluations_observed","best_observed","runtime_seconds","problem_id","status"]
out=OUT/"anytime_engine_smoke.csv"
with out.open("w",newline="",encoding="utf-8") as fh:w=csv.writer(fh);w.writerow(cols);w.writerows(rows)
manifest=ROOT/"experiments"/"anytime_engine_smoke_manifest.csv"
meta={"result_sha256":hashlib.sha256(out.read_bytes()).hexdigest(),"manifest_sha256":hashlib.sha256(manifest.read_bytes()).hexdigest(),"rows":len(rows)}
(OUT/"anytime_engine_smoke_provenance.json").write_text(json.dumps(meta,indent=2)+"\n")
print(meta)
