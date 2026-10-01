class TargetRecorder:
    """Objective-call recorder for exact checkpoints and first target hits."""
    def __init__(self, objective, checkpoints, f_opt, deltas):
        self.objective=objective
        self.checkpoints=tuple(sorted(set(int(x) for x in checkpoints)))
        self.f_opt=float(f_opt)
        self.deltas=tuple(sorted(set(float(x) for x in deltas), reverse=True))
        self.evaluations=0
        self.best=float("inf")
        self.checkpoint_best={}
        self.target_hits={d:None for d in self.deltas}
    def __call__(self,x):
        y=float(self.objective(x));self.evaluations+=1
        if y<self.best:self.best=y
        if self.evaluations in self.checkpoints:self.checkpoint_best[self.evaluations]=self.best
        for d in self.deltas:
            if self.target_hits[d] is None and self.best<=self.f_opt+d:self.target_hits[d]=self.evaluations
        return y
    def checkpoint_snapshot(self):
        return [{"checkpoint":c,"observed":c in self.checkpoint_best,"best":self.checkpoint_best.get(c)} for c in self.checkpoints]
    def target_snapshot(self):
        return [{"delta_f":d,"target_value":self.f_opt+d,"hit":self.target_hits[d] is not None,"evals_to_target":self.target_hits[d]} for d in self.deltas]
