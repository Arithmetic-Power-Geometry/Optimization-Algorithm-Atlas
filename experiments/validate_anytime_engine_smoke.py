import csv,json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/"artifacts"/"validation"
with (OUT/"anytime_engine_smoke.csv").open(encoding="utf-8",newline="") as f:r=list(csv.DictReader(f))
if len(r)!=2*2*3:raise SystemExit(f"expected 12 checkpoint rows, got {len(r)}")
for x in r:
 if x["status"]!="ENGINE_VALIDATION_ONLY":raise SystemExit("status leak")
 if not x["problem_id"].startswith("bbob_"):raise SystemExit("bad problem id")
 if int(x["evaluations_observed"])<int(x["checkpoint"]):raise SystemExit("checkpoint recorded early")
 if int(x["evaluations_observed"])>2000:raise SystemExit("max budget exceeded")
m=json.loads((OUT/"anytime_engine_smoke_provenance.json").read_text())
if m["result_sha256"]!=hashlib.sha256((OUT/"anytime_engine_smoke.csv").read_bytes()).hexdigest():raise SystemExit("result hash mismatch")
print("ANYTIME ENGINE SMOKE VALID",len(r),"checkpoint rows")
