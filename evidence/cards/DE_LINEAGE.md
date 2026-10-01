# Batch 1 — DE Lineage Evidence Card

## Mechanism genealogy

DE (1997)
→ JADE (2009): current-to-pbest + optional archive + adaptive control parameters
→ SHADE (2013): success-history memory for parameter adaptation
→ L-SHADE (2014): SHADE + linear population-size reduction

## Evidence-supported interpretation

Canonical DE established a compact population-based mechanism for continuous optimization. JADE directly addressed control-parameter dependence and introduced adaptive parameter control together with current-to-pbest and archive mechanisms. SHADE retained the adaptive DE lineage but replaced short-memory adaptation with success-history memory. L-SHADE then added deterministic linear population-size reduction.

## Candidate persistent weakness

Subsequent studies report that SHADE-family adaptation can still overemphasize exploitation, with premature convergence particularly relevant in higher-dimensional settings. A 2026 study independently frames conventional SHADE-family adaptation as having exploration-exploitation limitations on multimodal problems.

This is **candidate gap G-DE-001**, not a project finding.

## What must be established experimentally

1. Does the failure reproduce under canonical implementations?
2. Is it caused primarily by parameter-memory dynamics, population-size reduction, mutation strategy, or their interaction?
3. Does rotation/nonseparability move the failure boundary?
4. Is diversity loss predictive or merely correlated?
5. Do existing distance/neighborhood/adaptive-exploration repairs already resolve it?
6. Does any residual gap generalize beyond the benchmark suite used to discover it?

## Required ablations if the gap survives

- DE baseline
- JADE
- SHADE
- L-SHADE
- SHADE without history memory
- L-SHADE without population reduction
- established exploration-preserving SHADE variants
- any proposed mechanism M as parent vs parent+M

No new algorithm should be designed before these questions are resolved.
