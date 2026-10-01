import csv
from pathlib import Path
R=Path(__file__).resolve().parents[1]
g=list(csv.DictReader(open(R/"publication/PAPER_REMAINING_GATES.csv",encoding="utf-8")))
state={x["gate_id"]:x["status"] for x in g}
for k in ["R10","R11","R12","R13","R14"]:
 assert state[k] not in {"TODO","BLOCKED",""},(k,state[k])
# literature structural integrity
fp=list(csv.DictReader(open(R/"evidence/mechanism_fingerprints.csv",encoding="utf-8")))
src=list(csv.DictReader(open(R/"evidence/sources.csv",encoding="utf-8")))
ids={x["source_id"] for x in src}
assert all(x["source_id"] in ids for x in fp)
assert all(x["status"]=="verified" for x in src)
# execution freezes required
fr=list(csv.DictReader(open(R/"experiments/execution_freeze.csv",encoding="utf-8")))
fids={x["freeze_id"] for x in fr}
assert {"EF001","EF002","EF003","EF004","EF005"}<=fids,fids
# required integrity records
for p in [
 "experiments/R10_COMPLETION.md","experiments/R11_INTERPRETATION.md",
 "experiments/R12_DECISION.md","evidence/R13_COMPLETION.md",
 "publication/R15_FINAL_REPLAY_GATE.md","publication/JOURNAL_DECISION_GATE.md",
 "publication/TEVC_WRITING_STANDARD.md","publication/LATEX_TEMPLATE_POLICY.md"]:
 assert (R/p).exists(),p
print("R15 STATIC PRE-FREEZE AUDIT PASS",state)
