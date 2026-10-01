# Multiobjective Lineage: NSGA-II → MOEA/D / NSGA-III

## NSGA-II
Uses elitist nondominated sorting plus crowding distance. It remains a canonical multiobjective baseline. Crowding distance becomes less effective as objective count grows.

## MOEA/D
Decomposes a multiobjective problem into scalar subproblems and exploits neighborhood relations among subproblems.

## NSGA-III
Retains nondominated sorting but replaces crowding-distance diversity pressure with reference-direction/reference-point niching designed for many objectives.

## Diagnostic evidence
Recent diagnostic benchmarking emphasizes that these mechanisms respond differently to Pareto-front geometry and many-objective difficulty. Challenging benchmark studies have shown that both MOEA/D and NSGA-III can struggle on fronts with degeneracy, disconnection, bias and other difficult geometry.

## Atlas question
Instead of asking which MOEA wins, map:
objective count × Pareto-front geometry × decision-space structure × constraint structure × reference-direction/decomposition assumptions.

Status: mechanism-conditioned evidence map required.
