import sys
from pathlib import Path
import numpy as np,cocoex,cma
from scipy.optimize import differential_evolution,minimize
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"experiments"))
from objective_recorder import ObjectiveRecorder
D=2;MAX=1000*D;CHECK=(100*D,300*D,1000*D)

def getp():
 s=cocoex.Suite("bbob","",f"function_indices:1 dimensions:{D} instance_indices:1");return s,s[0]
def verify(name,rec,p):
 if rec.evaluations!=p.evaluations:raise AssertionError(f"{name}: recorder={rec.evaluations}, coco={p.evaluations}")
 if rec.evaluations>MAX:raise AssertionError(f"{name}: budget exceeded")
 print(name,"COUNTS MATCH",rec.evaluations,"checkpoints",rec.snapshot())

# DE: objective recorder observes every SciPy call. maxiter selected not to exceed hard cap.
s,p=getp();r=ObjectiveRecorder(p,CHECK)
differential_evolution(r,[(-5,5)]*D,strategy="best1bin",popsize=10,mutation=.5,recombination=.9,
 seed=11,polish=False,maxiter=99,tol=0,atol=0,workers=1,updating="immediate")
verify("SciPy-DE",r,p);p.free();s.free()

# Nelder-Mead: maxfev is the hard objective-call cap.
s,p=getp();r=ObjectiveRecorder(p,CHECK)
minimize(r,np.zeros(D)+3,method="Nelder-Mead",bounds=[(-5,5)]*D,
 options={"maxfev":MAX,"xatol":0.0,"fatol":0.0,"adaptive":False})
verify("SciPy-NelderMead",r,p);p.free();s.free()

# CMA-ES: ask/tell; recorder owns every objective call.
s,p=getp();r=ObjectiveRecorder(p,CHECK)
es=cma.CMAEvolutionStrategy([3.0]*D,2.0,{"seed":11,"bounds":[-5,5],"verbose":-9,"verb_disp":0,"popsize":10,
 "maxfevals":MAX,"tolfun":0,"tolfunhist":0,"tolx":0,"tolstagnation":0})
while r.evaluations<MAX:
 xs=es.ask()[:MAX-r.evaluations]
 if not xs:break
 ys=[r(x) for x in xs];es.tell(xs,ys)
verify("pycma-CMAES",r,p);p.free();s.free()
print("RECORDER-COCO INVARIANT PASSED")
