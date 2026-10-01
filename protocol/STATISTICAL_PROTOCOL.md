# Statistical Analysis Protocol

## Principle
No optimizer is declared universally superior from finite benchmark samples.

## Primary reporting
For each declared condition report:
- raw per-run outcomes;
- median and distributional summaries;
- confidence intervals where appropriate;
- evaluations-to-target / success probability for target-based tasks;
- anytime/convergence behavior when meaningful;
- wall-clock and optimizer overhead when computational cost matters;
- failures/timeouts without deletion.

## Comparisons
Use paired designs when algorithms share instances/seeds. Report effect magnitude in addition to significance. For multiple algorithms/functions, control multiplicity or use an appropriate omnibus/post-hoc procedure. Rank summaries may be descriptive but cannot replace magnitude and uncertainty.

## Seeds and instances
Predeclare seeds or deterministic seed-generation rule. Distinguish stochastic runs from distinct problem instances.

## Tuning
Separate default/reference configuration from tuned configuration. Equalize tuning opportunity where tuned comparisons are made. Report tuning cost separately from evaluation cost.

## Stopping
Predeclare objective-evaluation and/or time budgets. Do not stop individual methods opportunistically after observing results.

## Missing/failure outcomes
Preserve crashes, infeasible outcomes and timeouts as outcomes with explicit handling rules.

## Failure-frontier estimation
Define the success criterion before examining frontier results. Report uncertainty around transition location and replicate near the estimated boundary.

## New mechanism
Require parent-vs-parent+mechanism comparison, component ablations, cost accounting and validation conditions not used to discover the mechanism.
