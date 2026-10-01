import cocoex,random
from pathlib import Path
algs=["RS-A","RS-B"]
for alg in algs:
 suite=cocoex.Suite("bbob","","function_indices:1 dimensions:2 instance_indices:1")
 obs=cocoex.Observer("bbob",f"result_folder: R10-PROBE-{alg} algorithm_name: {alg}")
 p=suite[0];p.observe_with(obs);rng=random.Random(11 if alg=="RS-A" else 23)
 for _ in range(100):p([rng.uniform(-5,5),rng.uniform(-5,5)])
 print(alg,p.id,p.evaluations,p.final_target_hit)
 p.free();suite.free()
print("SEPARATE OBSERVER PROBE PASS")
