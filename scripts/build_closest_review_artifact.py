import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
src=ROOT/"evidence"/"closest_review_matrix.csv"
out=ROOT/"artifacts"/"tables"
out.mkdir(parents=True,exist_ok=True)
with src.open(encoding="utf-8",newline="") as f:
    rows=list(csv.DictReader(f))
cols=["review_id","year","scope","mechanism_taxonomy","benchmark_properties","performance_analysis","structural_similarity","structural_bias","reproducibility_status","condition_level_evidence_status","failure_frontiers","resolving_experiment_links","living_machine_readable_atlas"]
lines=["# Closest-Review Differentiation Matrix","",
"This matrix is used to constrain—not exaggerate—the eventual novelty claim.","",
"| Work | Year | Scope | Mechanism | Benchmark properties | Performance | Similarity | Structural bias | Reproducibility | Cell status | Failure frontiers | Resolving experiments | Living atlas |",
"|---|---:|---|---|---|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    lines.append("| "+" | ".join(str(r[c]) for c in cols)+" |")
lines += ["","The OAA_TARGET row is a design target until the corresponding artifacts are completed and validated."]
(out/"closest_review_matrix.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
print("wrote artifacts/tables/closest_review_matrix.md")
