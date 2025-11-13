import json
from pathlib import Path
import tempfile
import os

def load(path):
    """Load JSON from path. Accepts Path or str. Returns dict.
    If file missing, returns empty dict {"cards": []} by default.
    """
    p = Path(path)
    if not p.exists():
        return {"cards": []}
    with p.open('r', encoding='utf-8') as f:
        return json.load(f)


def save(path, data):
    """Save JSON atomically to path."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    # write to temp file then replace
    fd, tmp = tempfile.mkstemp(dir=str(p.parent))
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        os.replace(tmp, str(p))
    finally:
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except Exception:
                pass

# convenience aliases
load = load
save = save
