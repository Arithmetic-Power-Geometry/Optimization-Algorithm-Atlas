# Publication Implementation Acceptance

An implementation may enter a PROJECT-VALIDATED experiment only after:

1. algorithm identity and role are fixed;
2. package/repository and exact version or commit are recorded;
3. license permits the intended use/redistribution arrangement;
4. parameter defaults are traced to maintained documentation or canonical literature;
5. initialization and boundary handling are explicit;
6. stopping conditions do not violate the common evaluation budget;
7. hidden objective evaluations are ruled out or counted;
8. randomness is controllable by recorded seeds;
9. a deterministic/sanity test passes;
10. a small standard-suite run produces complete raw provenance.

Internal reference code may remain useful for calibration, but it is not silently presented as a canonical external implementation.
