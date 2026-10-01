# Optimization Evidence Status Ontology

## Cell key
A status cell is indexed by:
algorithm × mechanism/version × problem property × dimension × budget × metric.

## Status
- **DOCUMENTED**: direct, adequate evidence exists for the declared cell.
- **PARTIAL**: evidence exists but coverage, controls or replication are incomplete.
- **CONTRADICTORY**: comparable evidence supports materially different conclusions.
- **UNTESTED**: no adequate evidence found after the declared search.
- **PROJECT-VALIDATED**: this repository has produced and validated controlled evidence.

## Confidence
Separate status from confidence:
- HIGH: multiple adequate independent sources or replicated project evidence.
- MEDIUM: one strong source or several weaker consistent sources.
- LOW: limited or indirect evidence.

## Critical distinction
UNTESTED is not evidence of failure.
PARTIAL is not evidence of weakness.
DOCUMENTED is not universal superiority.

## Resolution
Every PARTIAL, CONTRADICTORY or UNTESTED high-priority cell must link to a resolving experiment or theoretical question.
