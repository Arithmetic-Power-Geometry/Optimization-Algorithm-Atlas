# COCO Target Authority Decision

Decision ID: CTA001
Status: FROZEN BEFORE EF002

The pinned coco-experiment 2.8.2 public Python Problem interface was probed in CI. It exposes public fields including best_observed_fvalue1 and final_target_hit, but does not expose a public f_opt or best_parameter field.

Therefore publication execution MUST NOT depend on private attributes such as _best_parameter and MUST NOT maintain a hand-copied table of BBOB optima.

Authority split:
- COCO observer/logger: official benchmark target attainment and COCO-compatible postprocessing.
- Project objective recorder: exact objective-call accounting, best-so-far fixed-budget checkpoints, runtime, failures, and optimizer-independent traces.
- TARGET001: project reporting grid and analysis declaration; where exact per-target runtimes are needed, they must be derived from official COCO logged/postprocessed data or another separately verified public metadata path.
- final_target_hit may be recorded as a supported public COCO field but does not replace the full target-runtime analysis.

This decision preserves EF001 history. EF002 will freeze the observer configuration, recorder, comparator configuration, dependency lock, runner, and validators together.

No publication claim may infer f_opt from undocumented cocoex internals.
