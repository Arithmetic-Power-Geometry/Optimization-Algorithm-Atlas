# Optimization Algorithm Atlas

A reproducible research infrastructure for mapping optimization algorithms by mechanism, evidence, benchmark coverage, failure regimes, structural overlap, and unresolved research gaps.

## Research objective

The project does **not** begin by proposing a new optimizer and does not treat optimization benchmarking as a leaderboard exercise. Its first objective is to establish a defensible evidence map of the optimization literature and then use controlled computational experiments to determine:

1. which mechanisms are genuinely distinct;
2. which problem regimes have adequate evidence;
3. where published evidence is contradictory, incomplete, or irreproducible;
4. where algorithm performance changes qualitatively;
5. which gaps justify new theory, a new transferable mechanism, or—only if warranted—a new algorithm.

## Study sequence

```text
systematic evidence mining
        ↓
algorithm registry
        ↓
mechanism-first taxonomy
        ↓
algorithm-specific evidence audits
        ↓
benchmark-suite audit
        ↓
structural-similarity analysis
        ↓
standardized reproducible experiments
        ↓
failure-frontier mapping
        ↓
gap registry
        ↓
gap-derived hypotheses
        ↓
optional new mechanism / algorithm
        ↓
ablation + fair comparison
        ↓
verified figures, tables, algorithms, and data
        ↓
paper
```

The paper is written only after the evidence and computational artifacts are complete.

## Core principle

Different names or metaphors are not treated as evidence of algorithmic novelty. Algorithms are compared through their operators, information flow, state, memory, adaptation, selection pressure, variation mechanisms, constraint handling, and termination behavior.

## Planned evidence classes

- classical and mathematical optimization
- first- and second-order methods
- derivative-free optimization
- evolutionary computation
- differential-evolution families
- swarm intelligence
- estimation-of-distribution methods
- surrogate and Bayesian optimization
- multiobjective and many-objective optimization
- constrained optimization
- robust and stochastic optimization
- dynamic optimization
- mixed-variable optimization
- large-scale optimization
- learning-assisted and adaptive optimization

## Outputs

The repository will progressively generate:

- algorithm registry;
- mechanism/DNA matrix;
- historical and mechanism genealogy;
- source-level evidence ledger;
- benchmark coverage matrix;
- structural-overlap network;
- reproducibility audit;
- algorithm × condition evidence map;
- performance profiles and convergence diagnostics;
- sensitivity and robustness analyses;
- failure-frontier maps;
- gap registry;
- gap-to-experiment cards;
- optional gap-derived algorithm/mechanism;
- final publication-grade figures and tables.

## Repository status

**Phase 1 — evidence mining and review protocol.**

No manuscript is generated from this repository. The repository is the computational and evidentiary laboratory supporting the later paper.
