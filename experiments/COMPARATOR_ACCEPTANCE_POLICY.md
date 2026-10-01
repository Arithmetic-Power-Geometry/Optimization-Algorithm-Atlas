# Comparator Acceptance Test

This test is infrastructure validation only and is never paper evidence.

It verifies that maintained comparator implementations can be executed under explicit configurations with observable objective-evaluation counts and finite outputs.

Current acceptance algorithms:
- SciPy Differential Evolution — polishing disabled;
- SciPy Nelder–Mead — explicit bounds and objective-call cap;
- pycma CMA-ES — ask/tell with adapter-owned evaluation budget.

Passing this test does not make a configuration canonical. Canonical/reference parameter provenance remains a separate publication gate.
