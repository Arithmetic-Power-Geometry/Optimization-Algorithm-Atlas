import csv
from pathlib import Path
R=Path(__file__).resolve().parents[1]
fp=list(csv.DictReader(open(R/"evidence/mechanism_fingerprints.csv",encoding="utf-8")))
src=list(csv.DictReader(open(R/"evidence/sources.csv",encoding="utf-8")))
ids={x["source_id"] for x in src}
missing=sorted({x["source_id"] for x in fp if x["source_id"] not in ids})
assert not missing,missing
assert len({x["algorithm_id"] for x in fp})==len(fp),"duplicate algorithm fingerprints"
bad=[x["source_id"] for x in src if x["status"]!="verified"]
assert not bad,("unverified source rows",bad)
print("R13 STRUCTURAL AUDIT PASS",len(fp),"fingerprints",len(src),"verified source rows")
