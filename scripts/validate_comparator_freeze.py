import csv
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"experiments"/"comparator_freeze.csv"
with p.open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
roles=[r["role"] for r in rows]
if len(roles)!=len(set(roles)): raise SystemExit("duplicate comparator role")
if any(not r["information_regime"] for r in rows): raise SystemExit("missing information regime")
if any(r["configuration_regime"] not in {"REFERENCE","TUNED","ABLATION"} for r in rows): raise SystemExit("invalid configuration regime")
print("COMPARATOR FREEZE LEDGER VALID",len(rows),"roles")
