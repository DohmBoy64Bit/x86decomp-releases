from __future__ import annotations
import hashlib, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MANIFEST = ROOT / "DOCSITE_MARKDOWN_HASHES.json"

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    expected = {item["path"]: item["sha256"] for item in data["files"]}
    actual_paths = sorted(p.relative_to(ROOT).as_posix() for p in DOCS.rglob("*.md"))
    errors = []
    for path in actual_paths:
        if path not in expected:
            errors.append(f"untracked Markdown file: {path}")
        elif sha256_file(ROOT / path) != expected[path]:
            errors.append(f"Markdown hash mismatch: {path}")
    for path in expected:
        if path not in actual_paths:
            errors.append(f"missing Markdown file: {path}")
    if errors:
        print("FAIL")
        for error in errors[:200]:
            print(f"- {error}")
        if len(errors) > 200:
            print(f"... {len(errors) - 200} additional errors omitted")
        return 1
    print("PASS")
    print(f"Markdown hashes verified: {len(actual_paths)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
