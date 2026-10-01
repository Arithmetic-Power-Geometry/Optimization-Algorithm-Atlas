class ObjectiveRecorder:
    """Optimizer-independent exact objective-evaluation checkpoint recorder."""
    def __init__(self, objective, checkpoints):
        self.objective=objective
        self.checkpoints=tuple(sorted(int(x) for x in checkpoints))
        self.evaluations=0
        self.best=float("inf")
        self.records={}
    def __call__(self,x):
        y=float(self.objective(x))
        self.evaluations+=1
        if y<self.best:self.best=y
        if self.evaluations in self.checkpoints:
            self.records[self.evaluations]=self.best
        return y
    def snapshot(self):
        return [{"checkpoint":c,"best":self.records.get(c),"observed":c in self.records}
                for c in self.checkpoints]
