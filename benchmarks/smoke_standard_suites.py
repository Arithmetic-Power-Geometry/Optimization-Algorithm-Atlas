from pathlib import Path
import json

report={"status":"PASS","checks":[]}

try:
 import cocoex
 suite=cocoex.Suite("bbob","","dimensions: 2 instance_indices: 1")
 problem=next(iter(suite))
 x=[0.0]*problem.dimension
 y=float(problem(x))
 report["checks"].append({"suite":"COCO BBOB","dimension":problem.dimension,"evaluation_finite":y==y})
except Exception as e:
 report["status"]="FAIL";report["checks"].append({"suite":"COCO BBOB","error":repr(e)})

try:
 import ioh
 p=ioh.get_problem(1,instance=1,dimension=10,problem_class=ioh.ProblemClass.PBO)
 y=float(p([0]*10))
 report["checks"].append({"suite":"IOH PBO","dimension":10,"evaluation_finite":y==y})
except Exception as e:
 report["status"]="FAIL";report["checks"].append({"suite":"IOH PBO","error":repr(e)})

out=Path(__file__).resolve().parents[1]/"artifacts"/"validation"
out.mkdir(parents=True,exist_ok=True)
(out/"standard_suite_smoke.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
if report["status"]!="PASS": raise SystemExit(json.dumps(report))
print(json.dumps(report,indent=2))
