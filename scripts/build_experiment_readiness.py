import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
with (ROOT/"experiments"/"publication_matrix.csv").open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
with (ROOT/"experiments"/"implementations.csv").open(encoding="utf-8",newline="") as f: impl=list(csv.DictReader(f))
out=ROOT/"artifacts"/"tables";out.mkdir(parents=True,exist_ok=True)
lines=["# Publication Experiment Readiness","","**PROJECT-VALIDATED runs are not yet authorized.**","","## Planned experiment questions","",
"| ID | Question | Suite | Status |","|---|---|---|---|"]
for r in rows: lines.append(f"| {r['matrix_id']} | {r['question']} | {r['suite']} | {r['status']} |")
lines += ["","## Current implementation ledger","",
"| Algorithm | Role | Version/commit | Publication status |","|---|---|---|---|"]
for r in impl: lines.append(f"| {r['algorithm']} | {r['role']} | {r['version_or_commit']} | {r['publication_status']} |")
lines += ["","## Blocking conditions","",
"- exact benchmark package versions and suite options not frozen;",
"- publication implementations/commits not yet pinned for the full comparator panel;",
"- parameter/tuning policy not yet frozen;",
"- final run-count/statistical-power rationale not yet frozen;",
"- environment snapshot not yet generated.",
"",
"Pilot success validates infrastructure only; it does not remove these publication gates."]
(out/"experiment_readiness.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
