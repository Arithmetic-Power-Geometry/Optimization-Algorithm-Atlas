import csv,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
d=ROOT/"artifacts"/"publication"/"EF002-REHEARSAL"
raw=d/"checkpoints.csv";prov=d/"provenance.json"
if not raw.exists() or not prov.exists():raise SystemExit("missing rehearsal outputs")
rows=list(csv.DictReader(raw.open(encoding="utf-8",newline="")))
if len(rows)!=36:raise SystemExit(f"expected 36 checkpoint rows, got {len(rows)}")
if {r["algorithm"] for r in rows}!={"RandomSearch","SciPy-DE","pycma-CMAES","SciPy-NelderMead"}:raise SystemExit("algorithm set drift")
if any(r["freeze_id"]!="EF002" or r["paper_evidence"]!="NO" or r["run_status"]!="REHEARSAL_ONLY" for r in rows):raise SystemExit("evidence/status drift")
if any(int(r["final_recorder_evals"])!=int(r["final_coco_evals"]) for r in rows):raise SystemExit("recorder/COCO mismatch")
if {int(r["checkpoint"]) for r in rows}!={200,600,2000}:raise SystemExit("checkpoint drift")
p=json.load(prov.open())
if not p["coco_observer_files"]:raise SystemExit("COCO observer produced no files")
print("EF002 REHEARSAL VALID",len(rows),"rows",len(p["coco_observer_files"]),"COCO files")
