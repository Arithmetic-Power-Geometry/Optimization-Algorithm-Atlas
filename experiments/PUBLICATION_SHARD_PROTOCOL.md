# PUBBBOB001 Shard Protocol

Freeze: EF001.

The full BBOB core is partitioned by dimension: D2, D5, D10, D20 and D40. Scientific conditions are unchanged by sharding.

Each publication shard must:
- use all BBOB functions 1–24;
- use instances 1–5;
- use seeds 11, 23 and 37 for stochastic algorithms;
- execute to a maximum of 1000D objective evaluations;
- obtain 100D and 300D as checkpoints from the same trajectory when observed;
- retain exact BBOB problem IDs and objective-call counts;
- retain native termination/failure status;
- record freeze ID EF001 and environment provenance;
- preserve raw run-level results before aggregation.

A shard initially has paper_evidence=NO_UNTIL_PROMOTED. Completion changes status only to RUN_COMPLETE_UNVERIFIED. Promotion requires integrity, provenance and statistical validation.

DRY-D2 is infrastructure-only and can never become paper evidence.
