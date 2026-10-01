from objective_recorder import ObjectiveRecorder
def f(x):return sum(v*v for v in x)
r=ObjectiveRecorder(f,[2,5,10])
for i in range(10):r([10-i])
assert r.evaluations==10
assert set(r.records)=={2,5,10}
assert r.records[2]==81.0 and r.records[5]==36.0 and r.records[10]==1.0
print("OBJECTIVE RECORDER EXACT CHECKPOINT TEST PASSED",r.snapshot())
