# BBOB Target-Attainment Freeze

Freeze ID: TARGET001

For single-objective BBOB, target attainment is defined by

`f(x) <= f_opt + delta_f`.

The frozen project reporting grid is delta_f in {1e2, 1e1, ..., 1e-8}. This is a deliberately sparse logarithmic reporting grid compatible with COCO's target-based performance framework; it is not presented as the full internal COCO logger target set.

Primary runtime unit for cross-function comparison is objective evaluations divided by dimension (FE/D). Missing target runtimes remain unsuccessful observations and stay in the denominator of ECDF-style summaries.

The final target precision is 1e-8. Checkpoint budgets remain 100D, 300D, and 1000D.

No target may be added, removed, or moved after observing later-dimensional results without a versioned amendment. TARGET001 applies prospectively to D5, D10, D20, and D40. Existing D2 raw checkpoint data are not retroactively claimed to contain exact evaluations-to-target unless the raw trajectory data support reconstruction.

Status: FROZEN BEFORE D5.
