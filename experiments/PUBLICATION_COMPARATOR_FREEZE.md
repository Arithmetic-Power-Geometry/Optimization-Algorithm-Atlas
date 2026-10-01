# Publication Comparator Freeze — Draft Gate

The comparator panel is selected by scientific role, not expected rank.

## Continuous black-box core
- Random Search — reference/calibration baseline.
- Nelder-Mead or another justified direct-search representative — classical derivative-free role.
- Differential Evolution — canonical population/difference-vector role.
- CMA-ES — adaptive distribution/covariance role.
- Particle Swarm Optimization — social/velocity population role.
- one evolutionary recombination/selection representative where implementation comparability is adequate.

## Conditional comparators
Bayesian/surrogate optimization is included only for an expensive-objective/sample-efficiency question with a scientifically compatible budget model. Gradient/quasi-Newton methods are analyzed in their appropriate information regime and are not treated as interchangeable black-box competitors.

## Configuration regimes
For each publication algorithm:
1. REFERENCE — canonical/default settings justified by source or maintained implementation;
2. TUNED — only if a predeclared equal tuning budget is available;
3. ABLATION — only for a tested mechanism component.

Reference and tuned results must never be pooled.

## Fairness
- same objective-evaluation budget within a compatible comparison;
- identical benchmark instances;
- predeclared seeds/run counts;
- boundary handling recorded;
- initialization distribution recorded;
- failures retained;
- optimizer overhead recorded separately;
- no algorithm removed because its results are poor.

This file is a draft gate until exact implementation IDs and versions are attached.
