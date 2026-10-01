# EF002 COCO Observer Lifecycle

Pinned environment: coco-experiment==2.8.2.

The EF002 rehearsal showed that explicit cocoex.Observer.free() raises an internal AttributeError involving __dealloc__ in the pinned binding.

Policy:
- Problem.free() remains explicit.
- Suite.free() remains explicit.
- Observer.free() is not called by project runners.
- Observer lifetime is left to Python/Cython object ownership after the observed problem and suite are released.
- This is an infrastructure/lifecycle correction only. It changes no algorithm, benchmark, seed, budget, checkpoint, target declaration, or statistical rule.

The production rehearsal must pass after this correction before EF002 is frozen.
