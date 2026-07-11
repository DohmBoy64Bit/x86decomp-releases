#!/usr/bin/env python3
"""Verify repository and package copies of the ground-truth corpus are identical."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = ROOT / "corpus" / "ground_truth_sources"
PACKAGED = ROOT / "src" / "x86decomp" / "corpus" / "ground_truth_sources"


def inventory(root: Path) -> dict[str, str]:
    """Return relative-path SHA-256 digests for every regular corpus file."""
    return {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def main() -> int:
    """Compare both corpus inventories and return a process status."""
    repository = inventory(REPOSITORY)
    packaged = inventory(PACKAGED)
    missing = sorted(set(repository) - set(packaged))
    extra = sorted(set(packaged) - set(repository))
    mismatched = sorted(
        path for path in set(repository) & set(packaged) if repository[path] != packaged[path]
    )
    report = {
        "repository_file_count": len(repository),
        "packaged_file_count": len(packaged),
        "missing_from_package": missing,
        "extra_in_package": extra,
        "hash_mismatches": mismatched,
        "passed": not missing and not extra and not mismatched,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
