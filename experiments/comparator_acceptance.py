import json, math, time
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution, minimize
import cma

OUT=Path(__file__).resolve().parents[1]/"artifacts"/"validation";OUT.mkdir(parents=True,exist_ok=True)
D=5; BUDGET=500; bounds=[(-5.0,5.0)]*D
def sphere(x): return float(np.dot(x,x))
rows=[]

# SciPy DE: explicitly no polish; callback/configuration recorded separately.
t=time.perf_counter()
res=differential_evolution(sphere,bounds,strategy="best1bin",popsize=10,mutation=0.5,recombination=0.9,
 seed=11,polish=False,maxiter=9,tol=0,atol=0,updating="immediate",workers=1)
rows.append({"algorithm":"SciPy-DE","best":float(res.fun),"nfev":int(res.nfev),"runtime":time.perf_counter()-t,"status":"ACCEPTANCE_ONLY"})

# SciPy Nelder-Mead: bounded, hard objective-call guard.
calls=[0]
def guarded(x):
 if calls[0]>=BUDGET: raise RuntimeError("budget")
 calls[0]+=1; return sphere(x)
t=time.perf_counter()
try:
 r=minimize(guarded,np.zeros(D)+3.0,method="Nelder-Mead",bounds=bounds,
  options={"maxfev":BUDGET,"xatol":0.0,"fatol":0.0,"adaptive":False})
 best=float(r.fun)
except RuntimeError:
 best=float("nan")
rows.append({"algorithm":"SciPy-NelderMead","best":best,"nfev":calls[0],"runtime":time.perf_counter()-t,"status":"ACCEPTANCE_ONLY"})

# pycma ask/tell: adapter owns objective-call budget.
opts={"seed":11,"bounds":[-5.0,5.0],"verbose":-9,"verb_disp":0,"popsize":10,"maxfevals":BUDGET}
es=cma.CMAEvolutionStrategy([3.0]*D,2.0,opts); calls=0; best=math.inf;t=time.perf_counter()
while not es.stop() and calls<BUDGET:
 xs=es.ask(); xs=xs[:max(0,BUDGET-calls)]
 if not xs: break
 ys=[sphere(np.asarray(x)) for x in xs]; calls+=len(ys);best=min(best,min(ys));es.tell(xs,ys)
rows.append({"algorithm":"pycma-CMAES","best":best,"nfev":calls,"runtime":time.perf_counter()-t,"status":"ACCEPTANCE_ONLY"})

(OUT/"comparator_acceptance.json").write_text(json.dumps(rows,indent=2)+"\n",encoding="utf-8")
if any(r["nfev"]>BUDGET for r in rows): raise SystemExit("budget exceeded")
if any(not math.isfinite(r["best"]) for r in rows): raise SystemExit("non-finite result")
print(json.dumps(rows,indent=2))
