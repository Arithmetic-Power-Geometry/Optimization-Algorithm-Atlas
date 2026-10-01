import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
src=ROOT/"evidence"/"mechanism_fingerprints.csv"
out=ROOT/"artifacts"/"tables"
out.mkdir(parents=True,exist_ok=True)
with src.open(encoding="utf-8",newline="") as f:
    rows=list(csv.DictReader(f))
features=[c for c in rows[0] if c not in {"algorithm_id","source_id","primary_failure_signal"}]
def tok(v): return {x.strip() for x in v.split(";") if x.strip()}
def sim(a,b):
    vals=[]
    for c in features:
        A,B=tok(a[c]),tok(b[c])
        vals.append(1.0 if not A and not B else 0.0 if not A or not B else len(A&B)/len(A|B))
    return sum(vals)/len(vals)
pairs=sorted(((sim(a,b),a["algorithm_id"],b["algorithm_id"]) for i,a in enumerate(rows) for b in rows[i+1:]),reverse=True)
lines=["# Initial Mechanism-Similarity Audit","","Exploratory unweighted fingerprint similarity; not a novelty verdict.","","| A | B | Similarity |","|---|---|---:|"]
for s,a,b in pairs[:25]: lines.append(f"| {a} | {b} | {s:.3f} |")
lines += ["","Similarity indicates overlap under the current schema only. It does not establish identity, priority, plagiarism, or equivalent empirical behavior."]
(out/"mechanism_similarity_initial.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
print(f"fingerprints={len(rows)} pairs={len(pairs)}")
