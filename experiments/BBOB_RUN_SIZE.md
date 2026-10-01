# PUBBBOB001 Run-Size Accounting

The full Cartesian design is intentionally explicit before execution.

For stochastic algorithms, the maximum scheduled unit count under the current manifest is:

24 functions × 5 dimensions × 5 instances × 3 seeds × 3 budget levels.

This equals 5,400 condition-budget-seed units per stochastic algorithm before accounting for trace checkpoints.

The final execution engine may reuse a single 1000D anytime trajectory to derive the nested 100D and 300D checkpoints when this is scientifically and technically valid. If so, those budgets are repeated observations from one trajectory, not falsely reported as independent runs.

This distinction must be preserved in statistical analysis and provenance.
