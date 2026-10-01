# Publication Run Authorization

Freeze: EF001

PUBBBOB001 may enter execution only when all conditions below are true:

1. final-style publication engine rehearsal is green;
2. recorder–COCO evaluation invariant is green;
3. BBOB core predeclaration validator is green;
4. statistical-design validator is green;
5. all EF001 file hashes match;
6. environment/dependency snapshot is captured;
7. output location preserves raw run-level evidence and provenance;
8. the run status begins as RUN_COMPLETE_UNVERIFIED, never directly PROJECT-VALIDATED.

## Change control
Any modification to an EF001 file after authorization creates a new freeze ID. Previous publication results remain associated with the freeze under which they were generated.

No silent overwrite of a frozen experimental definition is permitted.

## Paper gate
Only results promoted from RUN_COMPLETE_UNVERIFIED to PROJECT-VALIDATED may support project-generated empirical claims in the paper.
