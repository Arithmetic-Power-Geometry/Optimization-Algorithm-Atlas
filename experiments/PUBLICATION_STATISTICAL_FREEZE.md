# Publication Statistical Freeze — Pre-Result Protocol

This protocol must be frozen before any experiment is promoted to PROJECT-VALIDATED.

## Experimental unit
The atomic unit is:
algorithm/configuration × benchmark function × instance × dimension × independent seed × budget.

No run is discarded because of poor performance. Crashes, invalid outputs, infeasibility and timeouts are retained under predeclared coding rules.

## Primary performance views
1. target attainment / success probability at declared targets;
2. evaluations-to-target for successful runs;
3. best-so-far value at declared budgets;
4. anytime/ECDF-style performance across declared targets where suite semantics support it;
5. optimizer wall-clock/overhead as a separate cost view.

Aggregate ranks are descriptive only and never establish universal superiority.

## Pairing
Algorithms are compared on matched function × instance × dimension × seed conditions whenever possible.

## Uncertainty
Report distributional summaries and confidence intervals. For paired contrasts, use paired effect estimates with bootstrap confidence intervals where appropriate.

## Hypothesis testing
For multi-algorithm comparisons, use a predeclared omnibus procedure followed, when justified, by multiplicity-controlled post-hoc paired comparisons. P-values are not interpreted without effect magnitude and uncertainty.

## Multiplicity
The family of confirmatory comparisons is declared before analysis. Holm-type family-wise error control is the default for planned post-hoc pairwise tests unless the final endpoint structure requires a different predeclared procedure.

## Failure frontier
A failure frontier is estimated only for a predeclared success criterion. For a condition axis theta, the frontier is the transition region where the estimated probability of satisfying the criterion crosses the declared reliability threshold. Boundary uncertainty is reported and conditions near the transition receive additional replication when predeclared.

## Discovery vs confirmation
Conditions used to discover a candidate mechanism/failure relationship cannot serve as the sole confirmatory evidence for that same relationship. Confirmation uses held-out conditions or a separately frozen experiment.

## No result-dependent changes
After PROJECT-VALIDATED runs begin, changes to primary endpoints, exclusions, comparator configurations, targets, statistical families or frontier criteria require a versioned amendment and cannot silently replace the original analysis.
