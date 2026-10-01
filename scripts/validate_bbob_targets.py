import csv
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"experiments"/"bbob_targets.csv"
with P.open(encoding="utf-8",newline="") as f:r=list(csv.DictReader(f))
vals=[float(x["delta_f"]) for x in r]
exp=[10.0**k for k in range(2,-9,-1)]
if vals!=exp:raise SystemExit(f"target grid drift {vals}")
if any(x["status"]!="FROZEN" for x in r):raise SystemExit("target status drift")
if r[-1]["role"]!="ECDF_FINAL" or float(r[-1]["delta_f"])!=1e-8:raise SystemExit("final target drift")
print("TARGET001 VALID",len(r),"targets",vals[0],"to",vals[-1])
