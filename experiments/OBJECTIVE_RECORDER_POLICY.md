# Objective Recorder Policy

All publication optimizers should be evaluated through the same objective-level recorder whenever the library API permits it.

The recorder increments only when the benchmark objective is actually called. It stores best-so-far exactly when the objective-call count equals a declared checkpoint.

This avoids dependence on:
- generation counters;
- iteration counters;
- optimizer callbacks;
- population-size assumptions;
- post-generation reporting.

If an implementation performs hidden objective calls outside the wrapped objective, it fails implementation acceptance.

For an optimizer that terminates before a checkpoint, the checkpoint remains explicitly unobserved. Publication analysis must distinguish this from a completed checkpoint and from infrastructure failure.
