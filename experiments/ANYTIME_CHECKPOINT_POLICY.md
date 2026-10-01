# Anytime Checkpoint Policy

Publication budgets 100D, 300D and 1000D are checkpoints on a single trajectory when the optimizer supports a checkpoint-safe execution adapter.

A checkpoint records the best value available after the declared number of objective evaluations. Population/batch optimizers require special care: a library callback that fires only after a generation may cross a checkpoint.

Therefore:
- exact per-evaluation checkpoints are preferred;
- if a batch crosses a checkpoint, the adapter must record the actual evaluation count and must not attribute later evaluations to an earlier budget;
- an optimizer without a checkpoint-safe adapter is not promoted to the nested-budget publication run;
- separate reruns are allowed only if predeclared and are analyzed as separate stochastic trajectories.

The engine smoke test currently validates Random Search and pycma CMA-ES. SciPy DE remains excluded from the nested-checkpoint engine until its generation/evaluation accounting is made checkpoint-safe.

## Termination semantics
The publication runner must distinguish an optimizer's native early termination from infrastructure failure. For the engine-accounting smoke test, the adapter is deliberately exercised to the hard evaluation cap so every checkpoint can be validated. In publication runs, native termination is retained and later checkpoints are recorded as terminated/no-additional-evaluation states rather than silently imputed.
