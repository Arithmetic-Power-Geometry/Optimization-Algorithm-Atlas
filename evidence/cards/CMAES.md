# CMA-ES Evidence Card

## Core mechanism
CMA-ES adapts a multivariate search distribution, especially its covariance structure and global step size, using successful search directions accumulated across generations.

## Mechanistic strength
Its covariance adaptation can learn variable scaling and dependencies, giving it a fundamentally different response to nonseparable continuous landscapes than coordinate-wise or simple population-difference mechanisms.

## Current limitations to audit
- covariance representation/decomposition becomes expensive as dimension grows;
- difficult multimodal/noisy tasks remain sensitive to adaptation settings;
- premature local convergence remains relevant in multimodal optimization;
- specialized large-scale, restart, learning-rate and uncertainty-handling variants complicate attribution of gains.

## Candidate research question
Where does full covariance learning stop paying for its computational cost, and can observable search-state evidence predict that transition?

## Required tests
Compare canonical CMA-ES and appropriate scalable variants under matched objective-evaluation and wall-clock views across dimension, conditioning, rotation/nonseparability, modality and noise. Separate objective-call efficiency from optimizer overhead.

Status: literature-derived candidate; not project-validated.
