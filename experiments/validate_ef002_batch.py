import argparse,csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument("--label",required=True);ap.add_argument("--lo",type=int,required=True);ap.add_argument("--hi",type=int,required=True);a=ap.parse_args()
d=ROOT/"artifacts"/"publication"/a.label
rows=list(csv.DictReader((d/"checkpoints.csv").open(encoding="utf-8",newline="")))
expected_funcs=set(range(a.lo,a.hi+1))
if len(rows)!=900: raise SystemExit(f"expected 900 checkpoint rows, got {len(rows)}")
if {int(r["function_id"]) for r in rows}!=expected_funcs: raise SystemExit("function coverage drift")
if {int(r["instance"]) for r in rows}!={1,2,3,4,5}: raise SystemExit("instance coverage drift")
if {r["algorithm"] for r in rows}!={"RandomSearch","SciPy-DE","pycma-CMAES","SciPy-NelderMead"}: raise SystemExit("algorithm drift")
if any(r["freeze_id"]!="EF002" or r["paper_evidence"]!="NO" for r in rows): raise SystemExit("freeze/evidence drift")
if any(int(r["final_recorder_evals"])!=int(r["final_coco_evals"]) for r in rows): raise SystemExit("recorder/COCO mismatch")
for r in rows:
 if r["algorithm"]=="SciPy-NelderMead" and r["seed"]!="NA": raise SystemExit("NM false seed replication")
 if r["algorithm"]!="SciPy-NelderMead" and r["seed"] not in {"11","23","37"}: raise SystemExit("stochastic seed drift")
p=json.load((d/"provenance.json").open())
files=p.get("coco_observer_files",[])
if not files or not any(x.endswith(".info") for x in files) or not any(x.endswith(".tdat") for x in files): raise SystemExit("COCO provenance incomplete")
print("EF002 BATCH VALID",a.label,len(rows),"rows",len(files),"COCO files")
