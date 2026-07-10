---
title: tests/test_pe64_patch_hybrid.py
description: Test source page for tests/test_pe64_patch_hybrid.py.
---

# `tests/test_pe64_patch_hybrid.py`

- SHA-256: `1c4c7817684d2149bfa82bb3c91f820ae79e81f0f5ea8b82835cb876e8985fba`
- Size: `2488` bytes
- Test functions: `3`

```python
"""Verify the current toolkit behavior covered by `tests/test_pe64_patch_hybrid.py`."""
import json
import subprocess
from pathlib import Path

from pe_fixture import build_minimal_pe32, build_minimal_pe64
from x86decomp.hybrid import generate_hybrid_project
from x86decomp.patching import patch_pe_function
from x86decomp.pe import parse_pe
from x86decomp.project import initialize_project, verify_project


def test_pe64_project(tmp_path: Path) -> None:
    """Verify pe64 project behavior."""
    binary = build_minimal_pe64(tmp_path / "a64.exe")
    image = parse_pe(binary)
    assert image.to_dict()["architecture"] == "x86_64"
    project = tmp_path / "p64"
    manifest = initialize_project(binary, project)
    assert manifest["architecture"] == "x86_64"
    assert verify_project(project)["valid"]


def test_patch_image(tmp_path: Path) -> None:
    """Verify patch image behavior."""
    original = build_minimal_pe32(tmp_path / "a.exe")
    candidate = tmp_path / "candidate.bin"
    candidate.write_bytes(b"\x90\x90\xc3")
    output = tmp_path / "patched.exe"
    report = patch_pe_function(original, candidate, output, function_rva=0x1000)
    assert report["patch_size"] == 3
    assert output.read_bytes()[0x200:0x203] == candidate.read_bytes()
    assert parse_pe(output).checksum == report["pe_checksum"]


def test_hybrid_project_builds_assembly_objects(tmp_path: Path) -> None:
    """Verify hybrid project builds assembly objects behavior."""
    binary = build_minimal_pe32(tmp_path / "a.exe")
    project = tmp_path / "project"
    initialize_project(binary, project)
    artifact = project / "functions" / "pe-rva_00001000"
    (artifact / "ranges").mkdir(parents=True)
    (artifact / "ranges" / "00.bin").write_bytes(b"\x31\xc0\xc3")
    (artifact / "decompiler.c").write_text("int f(void){return 0;}\n")
    (artifact / "context.h").write_text("#pragma once\n")
    (artifact / "function.json").write_text(json.dumps({
        "schema_version": 2, "id": "pe-rva:00001000", "entry_rva": 0x1000,
        "body_ranges": [{"file": "ranges/00.bin", "start_rva": 0x1000, "end_rva": 0x1003}]
    }))
    out = tmp_path / "hybrid"
    result = generate_hybrid_project(project, out)
    assert len(result["functions"]) == 1
    assert (out / "Makefile").is_file()
    completed = subprocess.run(["make"], cwd=out, capture_output=True, text=True, check=False)
    assert completed.returncode == 0, completed.stderr
    assert (out / "build" / "sub_00001000.o").is_file()
```
