# EF003 Amendment — Evidence-State Metadata Correction

## Reason
EF002 was frozen with output rows hard-coded as `REHEARSAL_ONLY` and `paper_evidence=NO`. The D5, D10, D20, and D40 executions therefore remain validated infrastructure/descriptive runs and are not promoted to publication evidence.

The inconsistency was detected before P031 Evidence Freeze and before manuscript drafting.

## Scope of EF003
EF003 changes evidence-state metadata only. It does not change:
- BBOB suite, functions, dimensions, instances, or domains;
- algorithms or algorithm configurations;
- seeds;
- 100D, 300D, and 1000D checkpoints;
- maximum 1000D budget;
- ObjectiveRecorder accounting;
- COCO observer use;
- statistical protocol.

## Modes
- `rehearsal`: `REHEARSAL_ONLY / NO`
- `publication`: `RUN_COMPLETE_UNVERIFIED / NO_UNTIL_PROMOTED`

Publication-mode output is still not PROJECT-VALIDATED. Promotion requires all downstream integrity, statistical, provenance, and reproducibility gates.

## Scientific integrity
No EF002 comparative outcome is used to alter EF003 algorithms, configurations, budgets, seeds, instances, targets, or analysis rules. EF002 remains immutable historical evidence of infrastructure validation.
