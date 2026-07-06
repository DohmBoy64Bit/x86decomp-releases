"""Verify the current toolkit behavior covered by `tests/test_relink.py`."""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest

from x86decomp.coff import IMAGE_FILE_MACHINE_AMD64, write_synthetic_coff
from x86decomp.relink import run_full_relink


@pytest.mark.skipif(shutil.which("lld-link") is None, reason="lld-link unavailable")
def test_manifest_driven_full_relink(tmp_path: Path) -> None:
    """Verify manifest driven full relink behavior."""
    obj = tmp_path / "entry.obj"
    write_synthetic_coff(obj, code=b"\x31\xc0\xc3", symbol_name="entry", machine=IMAGE_FILE_MACHINE_AMD64)
    manifest = tmp_path / "relink.json"
    manifest.write_text(json.dumps({
        "schema_version": 1,
        "linker": "lld-link",
        "objects": ["entry.obj"],
        "output": "linked.exe",
        "arguments": ["/nologo", "/machine:x64", "/entry:entry", "/subsystem:console", "/nodefaultlib", "/out:{output}", "{objects}"],
        "environment": {},
        "timeout_seconds": 60
    }), encoding="utf-8")
    result = run_full_relink(manifest)
    assert result["success"]
    assert (tmp_path / "linked.exe").read_bytes()[:2] == b"MZ"
