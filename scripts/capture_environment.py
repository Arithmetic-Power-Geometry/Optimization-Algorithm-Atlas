import json, platform, sys, importlib.metadata as md
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
pkgs={}
for p in ("coco-experiment","ioh","numpy","pandas","streamlit"):
    try: pkgs[p]=md.version(p)
    except md.PackageNotFoundError: pkgs[p]="NOT_INSTALLED"
data={
 "python":sys.version,
 "platform":platform.platform(),
 "machine":platform.machine(),
 "processor":platform.processor(),
 "packages":pkgs,
}
out=ROOT/"artifacts"/"validation";out.mkdir(parents=True,exist_ok=True)
(out/"environment_snapshot.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
print(json.dumps(data,indent=2))
