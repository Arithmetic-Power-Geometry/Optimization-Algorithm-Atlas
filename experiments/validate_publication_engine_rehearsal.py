import csv,json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/"artifacts"/"validation"
p=OUT/"publication_engine_rehearsal.csv"
with p.open(encoding="utf-8",newline="") as f:r=list(csv.DictReader(f))
if len(r)!=3*2*4*2:raise SystemExit(f"expected 48 rows got {len(r)}")
allowed={"BUDGET_EXHAUSTED","NATIVE_TERMINATION","COMPLETED_LIBRARY_RUN"}
for x in r:
 if x["evidence_status"]!="ENGINE_REHEARSAL_ONLY":raise SystemExit("evidence status leak")
 if int(x["final_recorder_evals"])!=int(x["final_coco_evals"]):raise SystemExit("counter mismatch")
 if x["termination_status"] not in allowed:raise SystemExit("bad termination code")
 if not x["problem_id"].startswith("bbob_"):raise SystemExit("bad problem id")
prov=json.loads((OUT/"publication_engine_rehearsal_provenance.json").read_text())
if prov["result_sha256"]!=hashlib.sha256(p.read_bytes()).hexdigest():raise SystemExit("result hash mismatch")
print("PUBLICATION ENGINE REHEARSAL VALID",len(r),"rows")
