import argparse,csv,sys,time,random,hashlib,json
from pathlib import Path
import numpy as np,cocoex,cma
from scipy.optimize import differential_evolution,minimize
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"experiments"))
from objective_recorder import ObjectiveRecorder

def main():
 ap=argparse.ArgumentParser()
 ap.add_argument("--dimension",type=int,required=True,choices=[2,5,10,20,40])
 ap.add_argument("--functions",required=True,help="inclusive range, e.g. 1-3")
 ap.add_argument("--instances",default="1",help="comma-separated")
 ap.add_argument("--seeds",default="11",help="comma-separated")
 ap.add_argument("--label",default="EF002-REHEARSAL")
 a=ap.parse_args(); D=a.dimension
 lo,hi=map(int,a.functions.split("-")); fun=range(lo,hi+1)
 inst=[int(x) for x in a.instances.split(",")];seeds=[int(x) for x in a.seeds.split(",")]
 MAX=1000*D;CPS=(100*D,300*D,1000*D)
 outdir=ROOT/"artifacts"/"publication"/a.label;outdir.mkdir(parents=True,exist_ok=True)
 observer_dir=outdir/"coco";observer_dir.mkdir(parents=True,exist_ok=True)
 rows=[]
 def getp(f,i):
  s=cocoex.Suite("bbob","",f"function_indices:{f} dimensions:{D} instance_indices:{i}")
  obs=cocoex.Observer("bbob",f"result_folder: {observer_dir.resolve().as_posix()} algorithm_name: EF002")
  p=s[0];p.observe_with(obs);return s,obs,p
 def finish(alg,f,i,seed,p,r,t,status):
  if r.evaluations!=p.evaluations:raise RuntimeError(f"{alg} counter mismatch {r.evaluations}!={p.evaluations}")
  for q in r.snapshot():
   rows.append([a.label,"PUBBBOB001","EF002",alg,f,D,i,seed,q["checkpoint"],q["observed"],q["best"],r.evaluations,p.evaluations,time.perf_counter()-t,p.id,bool(p.final_target_hit),status,"REHEARSAL_ONLY","NO"])
 for f in fun:
  for i in inst:
   for seed in seeds:
    s,o,p=getp(f,i);rng=random.Random(seed);r=ObjectiveRecorder(p,CPS);t=time.perf_counter()
    while r.evaluations<MAX:r([rng.uniform(-5,5) for _ in range(D)])
    finish("RandomSearch",f,i,seed,p,r,t,"BUDGET_EXHAUSTED");p.free();s.free()
    s,o,p=getp(f,i);r=ObjectiveRecorder(p,CPS);t=time.perf_counter();pop=10*D;mi=max(0,MAX//pop-1)
    differential_evolution(r,[(-5,5)]*D,strategy="best1bin",popsize=10,mutation=.5,recombination=.9,seed=seed,polish=False,maxiter=mi,tol=0,atol=0,workers=1,updating="immediate")
    finish("SciPy-DE",f,i,seed,p,r,t,"COMPLETED_LIBRARY_RUN");p.free();s.free()
    s,o,p=getp(f,i);r=ObjectiveRecorder(p,CPS);t=time.perf_counter()
    es=cma.CMAEvolutionStrategy([3.0]*D,2.0,{"seed":seed,"bounds":[-5,5],"verbose":-9,"verb_disp":0,"popsize":10,"maxfevals":MAX,"tolfun":0,"tolfunhist":0,"tolx":0,"tolstagnation":0})
    while r.evaluations<MAX:
     xs=es.ask()[:MAX-r.evaluations]
     if not xs:break
     es.tell(xs,[r(x) for x in xs])
    finish("pycma-CMAES",f,i,seed,p,r,t,"BUDGET_EXHAUSTED" if r.evaluations==MAX else "NATIVE_TERMINATION");p.free();s.free()
   s,o,p=getp(f,i);r=ObjectiveRecorder(p,CPS);t=time.perf_counter()
   minimize(r,np.zeros(D)+3,method="Nelder-Mead",bounds=[(-5,5)]*D,options={"maxfev":MAX,"xatol":0.0,"fatol":0.0,"adaptive":False})
   finish("SciPy-NelderMead",f,i,"NA",p,r,t,"BUDGET_EXHAUSTED" if r.evaluations==MAX else "NATIVE_TERMINATION");p.free();s.free()
 cols=["run_label","experiment_id","freeze_id","algorithm","function_id","dimension","instance","seed","checkpoint","checkpoint_observed","best_at_checkpoint","final_recorder_evals","final_coco_evals","runtime_seconds","problem_id","coco_final_target_hit","termination_status","run_status","paper_evidence"]
 raw=outdir/"checkpoints.csv"
 with raw.open("w",newline="",encoding="utf-8") as fh:w=csv.writer(fh);w.writerow(cols);w.writerows(rows)
 files=sorted(str(p.relative_to(outdir)) for p in observer_dir.rglob("*") if p.is_file())
 prov={"label":a.label,"freeze_id":"EF002","dimension":D,"functions":[lo,hi],"instances":inst,"seeds":seeds,"rows":len(rows),"checkpoint_sha256":hashlib.sha256(raw.read_bytes()).hexdigest(),"coco_observer_files":files}
 (outdir/"provenance.json").write_text(json.dumps(prov,indent=2)+"\n")
 print(json.dumps(prov,indent=2))
if __name__=="__main__":main()
