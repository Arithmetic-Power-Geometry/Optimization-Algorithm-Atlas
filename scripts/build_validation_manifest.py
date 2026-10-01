import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
targets=[
 "experiments/calibration_manifest.csv",
 "experiments/pilot_manifest.csv",
 "experiments/implementations.csv",
 "artifacts/validation/calibration_raw.csv",
 "artifacts/validation/pilot_raw.csv",
 "artifacts/validation/pilot_traces.csv",
]
records=[]
for rel in targets:
 p=ROOT/rel
 if p.exists():
  records.append({"path":rel,"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
out=ROOT/"artifacts"/"validation"/"provenance_manifest.json"
out.write_text(json.dumps({"status":"PRE_PUBLICATION_VALIDATION","artifacts":records},indent=2)+"\n",encoding="utf-8")
print("manifest artifacts",len(records))
