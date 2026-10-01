# BFGS / L-BFGS Evidence Card

## Mechanism
Quasi-Newton updates approximate curvature from gradient/displacement pairs. L-BFGS retains only a limited history to reduce memory cost.

## Established strengths and boundaries
BFGS/L-BFGS are central smooth unconstrained methods. Nonconvex curvature can violate positive-definiteness assumptions and motivates damping/cautious/globalized variants. L-BFGS behavior on nonsmooth objectives can differ sharply from full BFGS; published analysis gives explicit failure behavior for scaled limited-memory variants on a nonsmooth convex class.

## Atlas questions
- When does limited memory cease to preserve useful curvature information?
- How do memory size, conditioning, nonconvexity, stochastic gradients and nonsmoothness interact?
- Which failure is due to curvature approximation versus line search?

Status: substantial theory exists; cross-regime evidence map required.
