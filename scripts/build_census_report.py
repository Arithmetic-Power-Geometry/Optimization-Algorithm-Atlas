import csv
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
with (ROOT/"census"/"master_census.csv").open(encoding="utf-8",newline="") as f:
    rows=list(csv.DictReader(f))
lanes=Counter(r["lane"] for r in rows)
roles=Counter(r["role"] for r in rows)
clusters=Counter(r["mechanism_cluster"] for r in rows if r["mechanism_cluster"])

out=ROOT/"artifacts"/"tables"
out.mkdir(parents=True,exist_ok=True)
lines=["# Optimization Census — Coverage Snapshot","",
f"Seed identities: **{len(rows)}**",
f"Mechanism-cluster labels: **{len(clusters)}**","",
"## Coverage by lane","","| Lane | Identities |","|---|---:|"]
for k,v in sorted(lanes.items()): lines.append(f"| {k} | {v} |")
lines += ["","## Roles","","| Role | Identities |","|---|---:|"]
for k,v in sorted(roles.items(),key=lambda x:(-x[1],x[0])): lines.append(f"| {k} | {v} |")
lines += ["","## Largest current mechanism clusters","","| Cluster | Identities |","|---|---:|"]
for k,v in sorted(clusters.items(),key=lambda x:(-x[1],x[0]))[:15]: lines.append(f"| {k} | {v} |")
lines += ["","This is a growing census, not a completeness claim. Identity counts must not be interpreted as mechanism counts."]
(out/"census_coverage.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
print("wrote artifacts/tables/census_coverage.md")
