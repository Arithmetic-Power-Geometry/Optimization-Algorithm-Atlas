# EF004 Amendment — Algorithm-Separable COCO Target Runtime

EF004 exists solely to complete the R10 target-runtime/ECDF measurement path.

The EF003 scientific design is unchanged: BBOB functions, dimensions, instances, seeds, algorithms, algorithm configurations, 100D/300D/1000D checkpoints, 1000D maximum budget, ObjectiveRecorder accounting, target protocol, and statistical protocol are identical.

The only execution change is that each algorithm writes to a distinct COCO observer result folder with its own algorithm_name. This permits authoritative algorithm-attributed target-runtime processing by official cocopp.

EF004 was rehearsed on real BBOB and passed:
- four distinct algorithm observer folders;
- ObjectiveRecorder evaluation count equals COCO evaluation count;
- required COCO .info/.dat logs exist;
- official cocopp joint postprocessing succeeds.

EF004 results remain RUN_COMPLETE_UNVERIFIED until downstream integrity/statistical/reproducibility promotion.
