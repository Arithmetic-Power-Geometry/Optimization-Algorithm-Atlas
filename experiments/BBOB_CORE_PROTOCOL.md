# BBOB Core Publication Protocol

Experiment: PUBBBOB001

Status: PREDECLARED_NOT_RUN.

## Coverage
Use all 24 noiseless BBOB functions. This avoids selecting functions after observing results.

Dimensions:
2, 5, 10, 20, 40.

Instances:
1–5, matched across algorithms.

Independent algorithm seeds:
11, 23, 37 for stochastic algorithms. Deterministic configurations are not artificially replicated as if seeds created independent algorithmic randomness; instance variation remains a matched block.

Budget multipliers:
100D, 300D and 1000D objective evaluations.

## Current comparator panel
- Random Search — transparent reference baseline;
- SciPy DE — maintained implementation, explicit configuration, no polishing;
- SciPy Nelder–Mead — maintained direct-search comparator;
- pycma CMA-ES — maintained ask/tell implementation.

PSO and GA are added only if their publication implementation/configuration provenance passes the same acceptance gate before the manifest is frozen for execution.

## Outputs
Retain raw run-level outcomes, best-so-far traces/checkpoints, evaluations-to-target, failures, runtime/optimizer overhead, exact problem IDs, implementation/environment provenance and manifest hash.

## Interpretation
The primary scientific unit is algorithm/configuration × problem condition × budget, not an overall winner. Function-level evidence is retained. Property-group synthesis is allowed only through an independently documented BBOB property mapping.

## Promotion
PREDECLARED_NOT_RUN → RUN_COMPLETE_UNVERIFIED → PROJECT-VALIDATED only after schema, budget, provenance, statistical and reproducibility checks pass.

No manuscript claim may cite PREDECLARED_NOT_RUN or RUN_COMPLETE_UNVERIFIED as project evidence.
