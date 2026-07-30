import json
from pathlib import Path

p = Path("config.json")
cfg = json.loads(p.read_text(encoding="utf-8"))

print("Before:", cfg["threshold"])

cfg["threshold"] = 95
cfg["regions"].append("EU-North")

p.write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding="utf-8")

overene = json.loads(p.read_text(encoding="utf-8"))
print("After:", overene["threshold"], overene["regions"])