import csv, math, random
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"artifacts"/"validation"
OUT.mkdir(parents=True,exist_ok=True)

def sphere(x): return sum(v*v for v in x)
def rastrigin(x): return 10*len(x)+sum(v*v-10*math.cos(2*math.pi*v) for v in x)
def rosenbrock(x): return sum(100*(x[i+1]-x[i]*x[i])**2+(1-x[i])**2 for i in range(len(x)-1))
FUNCS={"Sphere":(sphere,-5.12,5.12),"Rastrigin":(rastrigin,-5.12,5.12),"Rosenbrock":(rosenbrock,-5,10)}

def random_search(fn,lo,hi,d,budget,rng):
    best=float("inf")
    for _ in range(budget):
        x=[rng.uniform(lo,hi) for _ in range(d)]
        best=min(best,fn(x))
    return best

def de(fn,lo,hi,d,budget,rng,npop=20,F=.5,CR=.9):
    pop=[[rng.uniform(lo,hi) for _ in range(d)] for _ in range(npop)]
    fit=[fn(x) for x in pop]; used=npop
    while used<budget:
        for i in range(npop):
            if used>=budget: break
            ids=list(range(npop)); ids.remove(i); a,b,c=rng.sample(ids,3)
            jrand=rng.randrange(d)
            trial=[]
            for j in range(d):
                v=pop[a][j]+F*(pop[b][j]-pop[c][j])
                v=max(lo,min(hi,v))
                trial.append(v if rng.random()<CR or j==jrand else pop[i][j])
            f=fn(trial); used+=1
            if f<=fit[i]: pop[i],fit[i]=trial,f
    return min(fit)

def pso(fn,lo,hi,d,budget,rng,npop=20,w=.7298,c1=1.49618,c2=1.49618):
    x=[[rng.uniform(lo,hi) for _ in range(d)] for _ in range(npop)]
    v=[[0.0]*d for _ in range(npop)]
    p=[z[:] for z in x]; pf=[fn(z) for z in x]; used=npop
    gi=min(range(npop),key=lambda i:pf[i]); g=p[gi][:]; gf=pf[gi]
    while used<budget:
        for i in range(npop):
            if used>=budget: break
            for j in range(d):
                v[i][j]=w*v[i][j]+c1*rng.random()*(p[i][j]-x[i][j])+c2*rng.random()*(g[j]-x[i][j])
                x[i][j]=max(lo,min(hi,x[i][j]+v[i][j]))
            f=fn(x[i]); used+=1
            if f<pf[i]:
                p[i],pf[i]=x[i][:],f
                if f<gf: g=x[i][:]; gf=f
    return min(pf)

ALGS={"RandomSearch":random_search,"DE":de,"PSO":pso}
rows=[]
for name,(fn,lo,hi) in FUNCS.items():
  for d in (2,10):
    for seed in (11,23,37,53,71):
      for alg,runner in ALGS.items():
        rng=random.Random(seed)
        val=runner(fn,lo,hi,d,2000,rng)
        rows.append({"experiment_id":"CAL001","status":"CALIBRATION_ONLY","algorithm":alg,"function":name,"dimension":d,"budget_evals":2000,"seed":seed,"best_objective":f"{val:.17g}"})

raw=OUT/"calibration_raw.csv"
with raw.open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
print(f"wrote {raw} rows={len(rows)}")
