import os
from pathlib import Path
import cocoex
root=Path.cwd()
before={p.resolve() for p in root.rglob("*") if p.is_file()}
s=cocoex.Suite("bbob","","function_indices:1 dimensions:2 instance_indices:1")
o=cocoex.Observer("bbob","result_folder: EF002_COCO_PROBE algorithm_name: EF002_PROBE")
p=s[0];p.observe_with(o)
p([0.0]*p.dimension)
print("PROBLEM",p.id,"EVALS",p.evaluations,"FINAL",p.final_target_hit)
p.free();s.free()
after={p.resolve() for p in root.rglob("*") if p.is_file()}
new=sorted(str(p.relative_to(root)) for p in after-before)
print("NEW_FILES_COUNT",len(new))
for x in new: print("NEW_FILE",x)
print("CWD",root)
