# CMA-ES Configuration Audit

Candidate implementation: `pycma`.

Use the ask-and-tell interface for publication experiments so the benchmark adapter owns objective evaluation counting.

Freeze at minimum:
- pycma version/commit;
- initial mean generation;
- initial sigma;
- population size;
- bound handling;
- restart policy;
- termination options;
- seed/randomness policy;
- active covariance/default options;
- integer/mixed-variable options disabled for continuous BBOB unless explicitly studied.

Default CMA-ES and restarted CMA-ES are separate configurations and must not be pooled.
