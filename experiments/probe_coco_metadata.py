import cocoex
s=cocoex.Suite("bbob","","function_indices:1 dimensions:2 instance_indices:1")
p=s[0]
names=[n for n in dir(p) if not n.startswith("_")]
print("PUBLIC ATTRIBUTES",names)
for n in names:
    if any(k in n.lower() for k in ("best","opt","target","final")):
        try: print("CANDIDATE",n,repr(getattr(p,n)))
        except Exception as e: print("CANDIDATE_ERROR",n,type(e).__name__)
p.free();s.free()
