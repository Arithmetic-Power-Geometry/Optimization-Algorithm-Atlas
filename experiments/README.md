# Experimental Program

Experiments begin after the review evidence identifies the conditions that require resolution.

## Stage A — calibration

Use small subsets to validate:
- implementations;
- objective-evaluation accounting;
- seeds;
- stopping criteria;
- expected optima;
- result serialization.

## Stage B — standardized baselines

Where compatible, use established benchmark infrastructure such as COCO/BBOB for continuous black-box optimization, supplemented by problem-class-specific suites.

## Stage C — stress dimensions

Evaluate selected algorithms across controlled changes in:
- dimension;
- conditioning;
- separability/non-separability;
- modality;
- noise;
- constraints;
- dynamics;
- mixed variables;
- evaluation budget.

## Stage D — failure frontiers

Estimate where declared success criteria cease to hold and where comparative ordering changes robustly.

## Stage E — gap repair

Only after a validated gap is identified, test existing remedies first.

If a new mechanism is justified:
- parent vs parent + mechanism;
- component ablations;
- closest-mechanism comparator;
- strong established comparator;
- recent relevant comparator;
- out-of-discovery-regime validation.

## Artifact policy

All publication figures and tables must be regenerated from retained raw results by workflow scripts.
