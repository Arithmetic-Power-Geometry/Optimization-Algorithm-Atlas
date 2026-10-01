import csv, math, random, time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"artifacts"/"validation"; OUT.mkdir(parents=True,exist_ok=True)
CHECK={100,500,1000,2000,5000}
TARGETS=(1e-2,1e-6)

def sphere(x): return sum(v*v for v in x)
def rastrigin(x): return 10*len(x)+sum(v*v-10*math.cos(2*math.pi*v) for v in x)
def rosenbrock(x): return sum(100*(x[i+1]-x[i]*x[i])**2+(1-x[i])**2 for i in range(len(x)-1))
FUNCS={"Sphere":(sphere,-5.12,5.12,0.0),"Rastrigin":(rastrigin,-5.12,5.12,0.0),"Rosenbrock":(rosenbrock,-5,10,0.0)}

class Recorder:
    def __init__(self,fn,opt,budget):
        self.fn,self.opt,self.budget=fn,opt,budget; self.n=0; self.best=float("inf"); self.trace=[]; self.hit={t:"" for t in TARGETS}
    def __call__(self,x):
        if self.n>=self.budget: raise RuntimeError("evaluation budget exceeded")
        y=self.fn(x); self.n+=1; self.best=min(self.best,y)
        err=max(0.0,self.best-self.opt)
        for t in TARGETS:
            if self.hit[t]=="" and err<=t:self.hit[t]=self.n
        if self.n in CHECK or self.n==self.budget:self.trace.append((self.n,self.best))
        return y

def rs(ev,lo,hi,d,rng):
    while ev.n<ev.budget: ev([rng.uniform(lo,hi) for _ in range(d)])

def de(ev,lo,hi,d,rng,npop=20,F=.5,CR=.9):
    pop=[[rng.uniform(lo,hi) for _ in range(d)] for _ in range(npop)]; fit=[ev(x) for x in pop]
    while ev.n<ev.budget:
      for i in range(npop):
        if ev.n>=ev.budget: break
        ids=list(range(npop)); ids.remove(i); a,b,c=rng.sample(ids,3); jr=rng.randrange(d)
        z=[]
        for j in range(d):
          q=pop[a][j]+F*(pop[b][j]-pop[c][j]); q=max(lo,min(hi,q))
          z.append(q if rng.random()<CR or j==jr else pop[i][j])
        f=ev(z)
        if f<=fit[i]:pop[i],fit[i]=z,f

def pso(ev,lo,hi,d,rng,npop=20,w=.7298,c1=1.49618,c2=1.49618):
    x=[[rng.uniform(lo,hi) for _ in range(d)] for _ in range(npop)]; v=[[0.]*d for _ in range(npop)]
    p=[z[:] for z in x]; pf=[ev(z) for z in x]; gi=min(range(npop),key=lambda i:pf[i]); g=p[gi][:]; gf=pf[gi]
    while ev.n<ev.budget:
      for i in range(npop):
        if ev.n>=ev.budget:break
        for j in range(d):
          v[i][j]=w*v[i][j]+c1*rng.random()*(p[i][j]-x[i][j])+c2*rng.random()*(g[j]-x[i][j])
          x[i][j]=max(lo,min(hi,x[i][j]+v[i][j]))
        f=ev(x[i])
        if f<pf[i]:
          p[i],pf[i]=x[i][:],f
          if f<gf:g=x[i][:];gf=f

ALGS={"RandomSearch":rs,"DE":de,"PSO":pso}
raw=[]; traces=[]
for fnm,(fn,lo,hi,opt) in FUNCS.items():
 for d in (2,10):
  for budget in (500,2000,5000):
   for seed in (11,23,37,53,71):
    for an,alg in ALGS.items():
     rng=random.Random(seed); ev=Recorder(fn,opt,budget); t0=time.perf_counter(); alg(ev,lo,hi,d,rng); elapsed=time.perf_counter()-t0
     raw.append({"experiment_id":"PIL001","status":"PILOT_ONLY","algorithm":an,"function":fnm,"dimension":d,"budget_evals":budget,"seed":seed,"evaluations_used":ev.n,"best_objective":f"{ev.best:.17g}","evals_to_1e-2":ev.hit[1e-2],"evals_to_1e-6":ev.hit[1e-6],"runtime_seconds":f"{elapsed:.9g}"})
     for n,b in ev.trace: traces.append({"experiment_id":"PIL001","algorithm":an,"function":fnm,"dimension":d,"budget_evals":budget,"seed":seed,"checkpoint_eval":n,"best_objective":f"{b:.17g}"})
for name,rows in [("pilot_raw.csv",raw),("pilot_traces.csv",traces)]:
 with (OUT/name).open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
print("pilot runs",len(raw),"trace rows",len(traces))
