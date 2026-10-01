# Differential Evolution Configuration Audit

Candidate implementation: SciPy `differential_evolution`.

A publication result must identify the actual configuration rather than report only “DE”.

Freeze at minimum:
- strategy;
- population-size rule;
- mutation constant/range;
- recombination probability;
- initialization;
- immediate vs deferred updating;
- worker/parallelism policy;
- boundary behavior;
- polishing on/off;
- stopping tolerances;
- random-number generator;
- evaluation-budget translation.

## Publication baseline rule
Polishing is disabled for a DE-only baseline because otherwise local-search evaluations alter the mechanism and cost. Any hybrid DE+polish result is a separately named configuration.

A canonical-literature DE configuration and a maintained-library reference configuration may both be evaluated, but they remain separate evidence records.
