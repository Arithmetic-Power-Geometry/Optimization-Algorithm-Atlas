import ast
from pathlib import Path
p=Path(__file__).with_name("run_bbob_publication_ef003.py")
s=p.read_text()
assert 'choices=["rehearsal","publication"]' in s
assert '("REHEARSAL_ONLY","NO")' in s
assert '("RUN_COMPLETE_UNVERIFIED","NO_UNTIL_PROMOTED")' in s
assert '"freeze_id":"EF003"' in s
assert '"parent_freeze":"EF002"' in s
ast.parse(s)
print("EF003 METADATA MODE STATIC TEST PASS")
