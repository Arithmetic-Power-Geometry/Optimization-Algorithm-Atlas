# PUB-D5 Comparison Policy

PUB-D5 is a complete D=5 checkpoint layer under EF002.

## Permitted now
- within-function, within-checkpoint descriptive summaries;
- condition-level inspection of failures and termination;
- runtime/accounting diagnostics;
- preservation of COCO observer logs for later official target-runtime post-processing.

## Not permitted now
- averaging raw BBOB objective values across heterogeneous functions;
- declaring an overall winner from raw objective magnitudes;
- treating checkpoint rows as independent repeated experiments;
- reconstructing exact evaluations-to-target from checkpoint values;
- promoting RUN_COMPLETE_UNVERIFIED outputs to PROJECT-VALIDATED before the promotion gate.

Cross-function runtime/ECDF claims will use official COCO-compatible target semantics and a separately validated post-processing path.
