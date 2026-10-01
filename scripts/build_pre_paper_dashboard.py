import csv
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
src=ROOT/"publication"/"PRE_PAPER_BACKLOG.csv"
out=ROOT/"artifacts"/"tables"
out.mkdir(parents=True,exist_ok=True)

with src.open(encoding="utf-8",newline="") as f:
    rows=list(csv.DictReader(f))

states=Counter(r["state"] for r in rows)
critical_open=[r for r in rows if r["priority"]=="critical" and r["state"]!="complete"]
paper=next(r for r in rows if r["id"]=="P032")
ready=(len(critical_open)==0 and paper["state"]!="blocked")

lines=["# Pre-Paper Completion Dashboard","",
f"**Paper-ready: {'YES' if ready else 'NO'}**","",
f"Total tracked tasks: **{len(rows)}**  ",
f"Open critical tasks: **{len(critical_open)}**","",
"## State summary",""]
for k,v in sorted(states.items()): lines.append(f"- {k}: {v}")

lines += ["","## Open critical path","","| ID | Workstream | Task | State |","|---|---|---|---|"]
for r in critical_open:
    lines.append(f"| {r['id']} | {r['workstream']} | {r['task']} | {r['state']} |")

lines += ["","## Rule","",
"Paper drafting remains blocked until the evidence-freeze gate is complete. This dashboard measures process completion, not journal acceptance probability."]
(out/"pre_paper_dashboard.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
print(f"paper_ready={ready}; open_critical={len(critical_open)}")
