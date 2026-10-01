import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];d=ROOT/"artifacts"/"publication"/"PUB-D20"
rows=list(csv.DictReader((d/"PUB-D20_merged_checkpoints.csv").open(encoding="utf-8",newline="")))
if len(rows)!=3600:raise SystemExit(f"expected 3600 rows, got {len(rows)}")
if {int(r["function_id"]) for r in rows}!=set(range(1,25)):raise SystemExit("function coverage drift")
if {int(r["instance"]) for r in rows}!={1,2,3,4,5}:raise SystemExit("instance coverage drift")
if {int(r["checkpoint"]) for r in rows}!={2000,6000,20000}:raise SystemExit("checkpoint drift")
if any(r["freeze_id"]!="EF002" or int(r["final_recorder_evals"])!=int(r["final_coco_evals"]) for r in rows):raise SystemExit("freeze/count mismatch")
keys=[(r["algorithm"],r["function_id"],r["instance"],r["seed"],r["checkpoint"]) for r in rows]
if len(keys)!=len(set(keys)):raise SystemExit("duplicate atomic checkpoint key")
p=json.load((d/"PUB-D20_merged_provenance.json").open())
if p["rows"]!=3600 or p["paper_evidence"]!="NO_UNTIL_PROMOTED":raise SystemExit("provenance drift")
print("PUB-D20 MERGED VALID",len(rows),"rows")
