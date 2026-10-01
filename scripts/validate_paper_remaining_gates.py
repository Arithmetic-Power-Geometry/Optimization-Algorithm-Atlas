import csv
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"publication"/"PAPER_REMAINING_GATES.csv"
with p.open(encoding="utf-8",newline="") as f:r=list(csv.DictReader(f))
assert [x["gate_id"] for x in r]==[f"R{i:02d}" for i in range(1,19)]
done=sum(x["status"] in ("PASS","FROZEN") for x in r)
todo=sum(x["status"]=="TODO" for x in r)
assert done+todo==18
print("PAPER GATE REGISTER VALID","complete",done,"remaining",todo)
