# PUB-D2 Execution Plan

PUB-D2 is the first real PUBBBOB001 publication shard under EF001.

To reduce CI timeout/retry risk, the 24 BBOB functions are split into four execution batches of six functions each. This is an execution partition only; it does not alter the predeclared scientific design.

For stochastic algorithms, each batch covers 6 functions x 5 instances x 3 seeds = 90 trajectories per algorithm. At D=2 and 1000D maximum budget, this is at most 180,000 objective evaluations per stochastic algorithm per batch before native termination. Nelder–Mead is deterministic under the frozen configuration and must not be treated as gaining independent stochastic replication from seed labels.

All raw outputs remain RUN_COMPLETE_UNVERIFIED until batch integrity and merged-shard validation pass. No batch-level winner or paper claim is permitted.
