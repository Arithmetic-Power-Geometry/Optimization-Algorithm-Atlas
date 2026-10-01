import csv, random, time
from pathlib import Path
import numpy as np, cocoex, cma
from scipy.optimize import differential_evolution, minimize
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/"artifacts"/"validation";OUT.mkdir(parents=True,exist_ok=True)
FUN=(1,10,15);DIMS=(2,5);INST=(1,2);SEEDS=(11,23);rows=[]

def make_problem(f,d,i):
 s=cocoex.Suite("bbob","",f"function_indices:{f} dimensions:{d} instance_indices:{i}")
 return s,s[0]

for f in FUN:
 for d in DIMS:
  budget=300*d
  for ins in INST:
   for seed in SEEDS:
    # Random Search
    s,p=make_problem(f,d,ins);rng=random.Random(seed);best=float("inf");t=time.perf_counter()
    while p.evaluations<budget:best=min(best,float(p([rng.uniform(-5,5) for _ in range(d)])))
    rows.append(["RandomSearch",f,d,ins,seed,budget,p.evaluations,best,time.perf_counter()-t,p.id]);p.free();s.free()

    # SciPy DE with objective guard; population/init accounting is retained in nfev.
    s,p=make_problem(f,d,ins);t=time.perf_counter()
    r=differential_evolution(lambda x:float(p(x)),[(-5,5)]*d,strategy="best1bin",popsize=10,mutation=.5,recombination=.9,
       seed=seed,polish=False,maxiter=max(0,budget//(10*d)-1),tol=0,atol=0,workers=1,updating="immediate")
    rows.append(["SciPy-DE",f,d,ins,seed,budget,p.evaluations,float(r.fun),time.perf_counter()-t,p.id]);p.free();s.free()

    # Nelder-Mead: maxfev enforces cap.
    s,p=make_problem(f,d,ins);t=time.perf_counter()
    r=minimize(lambda x:float(p(x)),np.zeros(d)+3,method="Nelder-Mead",bounds=[(-5,5)]*d,
      options={"maxfev":budget,"xatol":0.0,"fatol":0.0,"adaptive":False})
    rows.append(["SciPy-NelderMead",f,d,ins,seed,budget,p.evaluations,float(r.fun),time.perf_counter()-t,p.id]);p.free();s.free()

    # CMA-ES ask/tell with strict remaining-budget truncation.
    s,p=make_problem(f,d,ins);es=cma.CMAEvolutionStrategy([3.0]*d,2.0,{"seed":seed,"bounds":[-5,5],"verbose":-9,"verb_disp":0,"popsize":10,"maxfevals":budget});best=float("inf");t=time.perf_counter()
    while not es.stop() and p.evaluations<budget:
     xs=es.ask()[:budget-p.evaluations]
     if not xs:break
     ys=[float(p(x)) for x in xs];best=min(best,min(ys));es.tell(xs,ys)
    rows.append(["pycma-CMAES",f,d,ins,seed,budget,p.evaluations,best,time.perf_counter()-t,p.id]);p.free();s.free()

cols=["algorithm","function_id","dimension","instance","seed","budget_evals","evaluations_used","best_observed","runtime_seconds","problem_id"]
with (OUT/"common_bbob_acceptance_raw.csv").open("w",newline="",encoding="utf-8") as fh:
 w=csv.writer(fh);w.writerow(cols);w.writerows(rows)
print("COMMON BBOB ACCEPTANCE",len(rows),"runs")
