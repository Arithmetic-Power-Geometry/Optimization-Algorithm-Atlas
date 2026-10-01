# Publication Benchmark Adapter Contract

A benchmark adapter must expose:
- stable suite/function/instance identifiers;
- dimension and variable domain;
- optimum/target metadata when legitimately known;
- objective-evaluation counter owned by the adapter;
- deterministic instance construction;
- explicit constraint/noise metadata;
- no optimizer-side access to hidden optimum information;
- raw evaluation budget enforcement;
- target-hit logging;
- suite/version provenance.

## Preferred publication ecosystems
COCO/BBOB and IOHprofiler/IOHexperimenter are preferred where the research question fits their supported problem classes.

## Local analytic functions
Sphere, Rastrigin and Rosenbrock in this repository are calibration/pilot functions only unless a later protocol explicitly promotes a defined, versioned suite.

## Boundary handling
Boundary policy is an algorithm/configuration property and must be recorded. Comparisons with materially different boundary behavior require sensitivity analysis.

## Fairness
Equal objective-evaluation budgets do not imply equal computational cost. Wall-clock and optimizer overhead are recorded separately where relevant.
