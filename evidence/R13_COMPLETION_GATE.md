# R13 Literature Evidence Completion Gate

R13 is complete only when the literature layer is adequate for the claims actually made by the atlas; algorithm census size alone is not a completion criterion.

Required checks:
1. Every mechanism fingerprint has a source_id present in evidence/sources.csv.
2. Every source used as canonical evidence has stable bibliographic identity (DOI, archival proceedings/journal identifier, or explicitly recorded archival URL/arXiv identifier).
3. Algorithm names are normalized to mechanisms; metaphor names are not treated as evidence of distinct mechanisms.
4. Negative/contradictory evidence is retained where found.
5. Closest-review matrix covers the review's claimed differentiation.
6. No claim of universal superiority, exhaustive coverage of all optimizers, or unsupported novelty is permitted.
7. Publication references must be re-verified at R15 immediately before evidence freeze.

Current fingerprint/source counts are descriptive coverage indicators, not evidence of completeness by themselves.
