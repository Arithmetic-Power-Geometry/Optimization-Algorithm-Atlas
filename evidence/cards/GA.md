# Genetic Algorithm Evidence Card

## Core mechanism
Population-based selection combines inherited variation through crossover and mutation, with replacement/elitism controlling survival.

## Persistent issues
Recent long-horizon review literature continues to identify:
- premature convergence;
- parameter dependence;
- scaling difficulty in high-dimensional and dynamic settings;
- computational expense when population/generation counts or fitness evaluations are large.

## Mechanism question
When does selection pressure destroy useful population diversity faster than recombination can exploit building structure?

## Candidate test
Factorial ablations of selection pressure, crossover, mutation and elitism while tracking genotypic/phenotypic diversity, takeover behavior, success probability and evaluations-to-target.

Status: candidate; the large existing diversity-preservation literature must be treated as prior remedies rather than ignored.
