# PSO Evidence Card

## Core mechanism
PSO updates particle velocities and positions using inertia plus information from personal and social best positions.

## Persistent issues in recent reviews
- premature convergence / diversity collapse;
- sensitivity to inertia, cognitive/social coefficients and velocity control;
- reduced effectiveness as dimension increases;
- difficulty on complex multimodal and changing environments;
- large variant space with uneven reproducibility and cross-domain generalization.

## Mechanism question
Can swarm-state observables distinguish healthy convergence from irreversible information collapse before final fitness reveals failure?

## Candidate test
Track diversity, velocity contraction, personal-best dispersion, global-best stagnation and improvement rate under dimension × modality × rotation × budget perturbations.

Status: candidate; existing adaptive/multiswarm remedies must be tested before claiming a new mechanism is required.
