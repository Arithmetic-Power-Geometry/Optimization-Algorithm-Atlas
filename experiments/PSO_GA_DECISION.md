# PSO and GA Publication Implementation Decision

## PSO
A maintained external PSO package is not accepted merely because it is convenient. The publication configuration must expose topology, inertia/weighting, cognitive/social coefficients, velocity handling, boundary handling, seed control and objective-call accounting.

Until a maintained implementation passes those checks, the existing transparent repository PSO remains PILOT_ONLY and PSO publication status remains PENDING.

## GA
“GA” is not a single sufficiently specified algorithm. Publication use requires an explicit representation and operator configuration:
- parent selection;
- crossover operator and probability;
- mutation operator and probability;
- replacement/elitism;
- population-size rule;
- initialization;
- boundary/repair policy;
- stopping rule.

A library default called “GA” is not accepted without operator-level provenance.

## Scientific consequence
The publication panel may proceed with fewer verified comparators rather than include a weakly specified implementation. Missing PSO/GA is a panel-completeness issue, not a reason to relax provenance standards.
