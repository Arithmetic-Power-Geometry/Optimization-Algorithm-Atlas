import sys
from pathlib import Path
import cocoex

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"experiments"))
from target_recorder import TargetRecorder

selector="function_indices:1 dimensions:2 instance_indices:1"
suite=cocoex.Suite("bbob","",selector)
problem=suite[0]

# Use a deterministic point and an auditable synthetic target threshold for the
# recorder/COCO counting invariant. This test does not infer BBOB f_opt.
x=[0.0]*problem.dimension
probe=float(problem(x))
problem.free()
suite.free()

suite=cocoex.Suite("bbob","",selector)
problem=suite[0]
# f_opt=probe-1 makes delta_f=1 exactly equal to the first observed value.
rec=TargetRecorder(problem,[1,2,5],probe-1.0,[1.0,0.1])
rec(x)

if rec.evaluations!=problem.evaluations:
    raise SystemExit("recorder/COCO count mismatch")
hits=rec.target_snapshot()
if not hits[0]["hit"] or hits[0]["evals_to_target"]!=1:
    raise SystemExit("guaranteed first target was not hit at evaluation 1")
if hits[1]["hit"]:
    raise SystemExit("stricter synthetic target unexpectedly hit at evaluation 1")
if rec.checkpoint_snapshot()[0]["best"]!=probe:
    raise SystemExit("checkpoint best mismatch")

print("TARGET RECORDER COCO COUNT/FIRST-HIT INVARIANT VALID",problem.id,"evaluations",rec.evaluations)
problem.free()
suite.free()
