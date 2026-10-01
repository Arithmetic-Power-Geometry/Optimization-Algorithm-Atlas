import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
out=ROOT/"artifacts"/"tables"
out.mkdir(parents=True,exist_ok=True)

paths=[ROOT/"gap_registry"/"CROSS_FAMILY_GAPS.csv", ROOT/"gap_registry"/"G-DE-001.csv"]
rows=[]
for p in paths:
    if not p.exists():
        continue
    with p.open(encoding="utf-8",newline="") as f:
        rows.extend(list(csv.DictReader(f)))

lines=["# Candidate Gap Atlas","","These are literature-derived candidate gaps. None is a project-validated failure unless explicitly marked PROJECT-VALIDATED.",""]
for r in rows:
    gid=r.get("gap_id","")
    fam=r.get("family") or r.get("algorithm_or_family","")
    typ=r.get("gap_type","")
    state=r.get("evidence_status","")
    q=r.get("question") or r.get("title","")
    lines += [f"## {gid} — {fam}",f"- Type: {typ}",f"- Evidence: {state}",f"- Question: {q}",""]
(out/"candidate_gap_atlas.md").write_text("\n".join(lines),encoding="utf-8")
print(f"wrote {out/'candidate_gap_atlas.md'}")
