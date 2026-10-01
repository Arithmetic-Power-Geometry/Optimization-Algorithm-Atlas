# Optimization Evidence Atlas — Academic Web App

## Purpose
A read-only scholarly interface to the verified evidence, mechanisms, benchmark coverage, reproducibility records, failure frontiers and research gaps produced by this repository.

## Scientific rule
The application does not create evidence. It renders versioned repository evidence and labels incomplete records explicitly.

## Primary user questions
1. What is this optimization algorithm and where did it originate?
2. What computational mechanism does it actually use?
3. Which algorithms are structurally closest?
4. Under which conditions is evidence documented, partial, contradictory, untested or project-validated?
5. Which benchmark properties have actually been tested?
6. What theoretical guarantees and counterexamples exist?
7. How reproducible is the published evidence?
8. What limitations/failure regimes are documented?
9. Which gaps remain and what experiment would resolve them?
10. Which comparator roles are appropriate for a new study?

## Planned navigation
### Explore
- Home
- Algorithm Explorer
- Mechanism Atlas
- Evidence Atlas
- Benchmark Atlas
### Analyze
- Similarity Explorer
- Reproducibility
- Gap & Frontier Explorer
### Research
- Researcher Decision Guide
- Sources & Provenance
- About / Methods

## Integrity
Every evidence-bearing display should expose source IDs and evidence status. UNTESTED must never be rendered as failure. Project-generated findings must be distinguishable from literature-derived evidence.

## Versioning
The app reads the repository's current evidence release. The paper will cite a frozen release/archival identifier rather than an evolving live state.
