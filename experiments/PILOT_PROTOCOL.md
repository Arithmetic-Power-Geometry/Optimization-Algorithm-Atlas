# Pre-Publication Pilot Protocol

Status: **PILOT_ONLY — NOT PAPER EVIDENCE**

## Purpose
Stress the experiment plumbing before publication-scale benchmarking.

## Checks
1. equal objective-evaluation budgets;
2. fixed seeds and deterministic replay;
3. raw run preservation;
4. algorithm configuration provenance;
5. boundary policy recording;
6. best-so-far trace support;
7. evaluations-to-target support;
8. failure/timeout representation;
9. runtime measurement schema;
10. no use of pilot results for algorithm superiority claims.

## Promotion rule
No pilot result is promoted into PROJECT-VALIDATED evidence. Publication experiments are rerun under a separately frozen manifest after benchmark adapters and implementations are finalized.
