import csv,sys
from pathlib import Path
import cocoex
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"experiments"))
from target_recorder import TargetRecorder
with (ROOT/"experiments"/"bbob_targets.csv").open(encoding="utf-8",newline="") as f:deltas=[float(x["delta_f"]) for x in csv.DictReader(f)]
s=cocoex.Suite("bbob","","function_indices:1 dimensions:2 instance_indices:1");p=s[0]
# COCO exposes the instance optimum through best_value in cocoex.
fopt=float(p.best_value)
r=TargetRecorder(p,[2,5,10],fopt,deltas)
# Evaluate optimum if exposed; otherwise use the documented best parameter.
x=list(p.best_parameter)
r(x)
if r.evaluations!=p.evaluations:raise SystemExit("recorder/COCO count mismatch")
hits=r.target_snapshot()
if not all(x["hit"] and x["evals_to_target"]==1 for x in hits):raise SystemExit("known optimum did not hit all targets on first evaluation")
if hits[-1]["delta_f"]!=1e-8:raise SystemExit("final target drift")
print("TARGET RECORDER COCO INVARIANT VALID",p.id,"fopt",fopt,"targets",len(hits))
p.free();s.free()
