# Target Recorder Policy

TARGET001 target attainment is recorded at the objective-call layer.

For each actual objective evaluation, the recorder:
1. increments the evaluation count exactly once;
2. updates best-so-far;
3. records exact fixed-budget checkpoints when encountered;
4. records the first evaluation satisfying f_best <= f_opt + delta_f for every frozen TARGET001 delta.

The target recorder must satisfy recorder.evaluations == COCO problem.evaluations on real BBOB problems.

Target hits are monotone: once hit, first-hit evaluation is immutable. Unreached targets remain explicit missing runtimes and are not imputed.

This recorder is prospective for higher-dimensional publication runs. D2 checkpoint evidence remains valid but is not retroactively represented as exact evaluations-to-target.
