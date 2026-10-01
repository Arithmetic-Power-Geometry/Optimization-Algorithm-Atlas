# Publication Environment Lock

Before the first PROJECT-VALIDATED run, record and freeze:

- operating system image;
- Python version;
- benchmark package versions;
- optimizer package versions/commit hashes;
- numerical library versions;
- CPU model / allocated cores;
- parallel execution policy;
- wall-clock measurement policy;
- environment variables that affect numerical parallelism;
- repository commit;
- experiment manifest hash.

The workflow must export a machine-readable environment snapshot with each publication experiment batch.

## Separation of costs
Objective evaluations, optimizer overhead and wall-clock time are separate quantities. An expensive objective can mask optimizer overhead; a cheap benchmark can expose it. Both interpretations must be retained.
