# R11 Failure-Frontier Discovery and Held-Out Confirmation Protocol

Status: PREDECLARED BEFORE FRONTIER SELECTION

## Purpose
Identify dimension-conditioned failure regions from the completed EF003 discovery campaign, then test those regions on held-out benchmark instances without changing algorithms or configurations.

## Discovery data
EF003 BBOB functions 1–24, dimensions 5/10/20/40, instances 1–5, frozen algorithms and 100/300/1000 FE/D checkpoints. Discovery may nominate candidate failure regions but cannot itself confirm them.

## Held-out confirmation
- BBOB functions: same 1–24 so mechanism/property interpretation remains matched.
- Dimensions: 5, 10, 20, 40.
- Held-out instances: 6, 7, 8, 9, 10; none appeared in discovery.
- Algorithms/configurations: identical to EF003.
- Stochastic seeds: 11, 23, 37, unchanged.
- Budgets: 100D, 300D, 1000D, unchanged.
- Primary target-runtime analysis uses COCO-authoritative target data after R10 attribution validation.
- Checkpoint scaling is supporting/descriptive only.

## Frontier definition
A candidate failure frontier is a transition across ordered dimension/budget conditions where a predeclared target-attainment reliability criterion changes from satisfied to unsatisfied. The exact reliability threshold and target subset must be fixed from the R10 target protocol before held-out outcomes are inspected.

## Confirmation rule
A frontier is PROJECT-VALIDATED only if the direction and condition boundary are supported on held-out instances with uncertainty reported. Discovery-only boundaries remain exploratory.

## Integrity
No algorithm may be removed because of poor performance. No seed, instance, budget, target or threshold may be changed after confirmation execution begins. Any amendment is versioned and cannot be motivated by confirmation outcomes.
