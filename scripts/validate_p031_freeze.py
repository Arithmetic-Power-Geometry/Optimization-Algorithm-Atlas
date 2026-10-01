import csv,hashlib,subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader(open(R/"publication/P031_EVIDENCE_FREEZE_MANIFEST.csv",encoding="utf-8")))
assert rows
for x in rows:
 p=R/x["artifact_path"]; assert p.exists(),p
 got=subprocess.check_output(["git","hash-object",str(p)],text=True).strip()
 assert got==x["git_blob_sha"],(x["artifact_path"],got,x["git_blob_sha"])
print("P031 EVIDENCE FREEZE MANIFEST VALID",len(rows),"artifacts")
