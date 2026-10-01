import csv,sys
from pathlib import Path
import cocoex

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"experiments"))
from target_recorder import TargetRecorder

with (ROOT/"experiments"/"bbob_targets.csv").open(encoding="utf-8",newline="") as fh:
    deltas=[float(x["delta_f"]) for x in csv.DictReader(fh)]

selector="function_indices:1 dimensions:2 instance_indices:1"
probe_suite=cocoex.Suite("bbob","",selector)
probe=probe_suite[0]
fopt=float(probe(probe.best_parameter))
probe.free()
probe_suite.free()

suite=cocoex.Suite("bbob","",selector)
problem=suite[0]
rec=TargetRecorder(problem,[2,5,10],fopt,deltas)
rec(list(problem.best_parameter))

if rec.evaluations!=problem.evaluations:
    raise SystemExit("recorder/COCO count mismatch")
hits=rec.target_snapshot()
if not all(x["hit"] and x["evals_to_target"]==1 for x in hits):
    raise SystemExit("known optimum did not hit all targets on first evaluation")
if hits[-1]["delta_f"]!=1e-8:
    raise SystemExit("final target drift")

print("TARGET RECORDER COCO INVARIANT VALID",problem.id,"fopt",fopt,"targets",len(hits))
problem.free()
suite.free()
