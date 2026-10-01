from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
lic=(ROOT/"LICENSE").read_text(encoding="utf-8")
notice=(ROOT/"NOTICE").read_text(encoding="utf-8")
checks=[
    ("Apache License", "Version 2.0" in lic and "TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION" in lic),
    ("copyright", "Copyright (C) 2026 Mohammad Amir Khusru Akhtar" in notice),
    ("notice license", "Apache License, Version 2.0" in notice),
]
bad=[name for name,ok in checks if not ok]
if bad: raise SystemExit("LICENSE VALIDATION FAILED: "+", ".join(bad))
print("LICENSE VALIDATION PASSED")
