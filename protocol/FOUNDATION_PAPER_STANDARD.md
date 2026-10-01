# Foundation-Paper Standard

## Goal
Create a reusable status atlas rather than another narrative catalogue or leaderboard.

## Five status layers
Every included algorithm/family should be readable through five linked layers:

1. **Identity status** — canonical source, aliases, lineage, variants.
2. **Mechanism status** — what information the method uses and how search state changes.
3. **Evidence status** — DOCUMENTED / PARTIAL / CONTRADICTORY / UNTESTED / PROJECT-VALIDATED for each declared condition.
4. **Reproducibility status** — source/code/specification/independent reproduction.
5. **Frontier status** — unresolved question and the minimal experiment/theorem required to resolve it.

## Required researcher views
The final atlas should answer:
- What should I compare my new method against?
- Which benchmark properties have actually tested this method?
- What is known versus merely repeated?
- Which mechanism is closest to my proposed contribution?
- Is my proposed novelty structurally redundant?
- Where does this method fail or become inefficient?
- Which gaps are still untested?
- Which existing remedies must be checked before proposing a new method?
- What experiment would resolve the gap?

## Evidence density, not citation density
A highly cited claim is not automatically strong evidence. Store the experimental conditions supporting it.

## No universal ranking
Performance conclusions are conditional on problem properties, budget, implementation, tuning and metric.

## Publication presentation
The eventual paper should have a compact main narrative supported by a machine-readable atlas. The main paper presents maps and synthesis; exhaustive algorithm cards and evidence rows remain reproducible supplementary artifacts.

## Evidence-freeze gate
No final paper claim is written until its supporting source rows or project-generated artifacts are frozen and traceable.
