# Optimization Algorithm Atlas

Research software, evidence registries, benchmark protocols, and frozen computational artifacts supporting the study **From Algorithm Names to Evidence: A Mechanism-First Framework for Reproducible Optimization Research**.

## Scope

The atlas represents optimization methods at two complementary levels:

- a cross-paradigm census of **90 algorithm identities** for coverage and provenance;
- **42 source-backed mechanism fingerprints** for comparison by computational structure rather than by name or metaphor.

The fingerprint representation records state, information source, proposal geometry, memory, adaptation, selection, diversity control, constraint handling, derivative order, and model type. Evidence completeness is tracked separately from provenance so that missing evidence is not interpreted as algorithmic failure.

## Controlled computational characterization

The frozen continuous black-box study evaluates:

- Random Search;
- differential evolution;
- Nelder--Mead;
- CMA-ES.

The computational campaign uses all **24 noiseless COCO BBOB functions** at dimensions **5, 10, 20, and 40**, with normalized objective-evaluation budgets of **100D, 300D, and 1000D**.

Discovery uses BBOB instances **1--5** and held-out characterization uses disjoint instances **6--10**. Objective-call accounting is recorded independently and cross-checked against COCO. Official `cocopp` outputs provide target-runtime and ECDF views.

The promoted execution artifacts include:

- **EF003**: corrected fixed-budget cross-dimensional campaign;
- **EF004**: algorithm-separated COCO target-runtime campaign on discovery instances;
- **EF005**: held-out target-runtime campaign on instances 6--10;
- **P031**: frozen evidence manifest.

The fixed-budget product contains **1,152 algorithm-function-dimension-budget cells**. EF004 and EF005 each retain **14,400 validated checkpoint rows** and **64 algorithm-labelled COCO result roots**.

## Interpretation boundary

The computational evidence supports condition-level characterization under the declared BBOB settings. It does not establish a universal optimizer ranking.

The exact numerical reliability threshold and target subset required for a confirmatory binary failure frontier were not fully frozen before held-out execution. Accordingly, the repository does not promote a post-hoc exact frontier or a mechanism-repair claim from those results.

## Repository structure

- `census/` — algorithm identity and coverage records
- `evidence/` — source ledger, mechanism fingerprints, evidence records, and evidence cards
- `benchmarks/` — benchmark-property mappings and adapter contracts
- `experiments/` — frozen configurations, execution records, interpretation notes, and validation policies
- `artifacts/` — generated research artifacts used for inspection and reproduction
- `gap_registry/` — unresolved evidence conditions and resolving-study records
- `protocol/` — review, statistical, similarity, status, and gap-validation protocols
- `schemas/` — machine-readable record schemas
- `scripts/` — reproducibility and validation utilities
- `.github/workflows/` — executable benchmark and evidence-validation workflows

## Reproducibility

The repository preserves configuration, execution, validation, and interpretation boundaries needed to reproduce the reported computational characterization. Historical or superseded execution records are retained when they are necessary for provenance but are not promoted as scientific evidence.

## Research record

Akhtar, M. A. K. (2026). *From Algorithm Names to Evidence: A Mechanism-First Framework for Reproducible Optimization Research* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23085104

## License

Repository-authored software and documentation are licensed under the Apache License, Version 2.0, unless a file states otherwise.

Copyright © 2026 Mohammad Amir Khusru Akhtar.

The Zenodo research article and third-party materials retain their own stated rights and licenses.
