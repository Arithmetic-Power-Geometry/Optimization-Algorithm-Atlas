import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];P=ROOT/"artifacts"/"publication"/"PUB-D2"
for name in ["D2-B01_descriptive_summary.csv","D2-B01_termination_summary.csv"]:
 p=P/name
 if not p.exists():raise SystemExit(f"missing {name}")
 with p.open(encoding="utf-8",newline="") as f:r=list(csv.DictReader(f))
 if not r:raise SystemExit(f"empty {name}")
 if any(x["status"]!="DESCRIPTIVE_RUN_COMPLETE_UNVERIFIED" for x in r):raise SystemExit("premature interpretive status")
print("B01 DESCRIPTIVE AUDIT VALID")
