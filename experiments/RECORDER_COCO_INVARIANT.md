# Recorder–COCO Evaluation Invariant

Before publication-scale execution, every maintained optimizer adapter must satisfy:

recorder objective-call count = COCO problem evaluation count

on an integration test.

This detects hidden or bypassed objective evaluations.

Exact checkpoint observation is optimizer dependent:
- a checkpoint is exact when the wrapped objective reaches that call number;
- early native termination leaves later checkpoints unobserved;
- publication execution must never copy a later best value backward to an earlier checkpoint.

The invariant test currently covers SciPy DE, SciPy Nelder–Mead and pycma CMA-ES on BBOB f1, D=2, instance 1. It is infrastructure validation only and not paper evidence.
