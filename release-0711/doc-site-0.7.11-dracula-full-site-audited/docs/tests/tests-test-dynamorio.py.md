---
title: tests/test_dynamorio.py
description: Test source page for tests/test_dynamorio.py.
---

# `tests/test_dynamorio.py`

- SHA-256: `41d1f65aeefadb38e4b937899e801f20a93e495c7933427a2c483d7a6d554fcc`
- Size: `1670` bytes
- Test functions: `2`

```python
"""Verify the current toolkit behavior covered by `tests/test_dynamorio.py`."""
from pathlib import Path
import importlib.util
import subprocess
import sys

import pytest

from x86decomp.angr_backend import angr_bounded_compare
from x86decomp.dynamorio import parse_drcov_text
from x86decomp.errors import ExternalToolError


def test_parse_drcov_text(tmp_path: Path) -> None:
    """Verify parse drcov text behavior."""
    log = tmp_path / "sample.log"
    log.write_text(
        "DRCOV VERSION: 2\n"
        "DRCOV FLAVOR: drcov\n"
        "Module Table: version 2, count 1\n"
        "Columns: id, base, end, entry, checksum, timestamp, path\n"
        "0, 0x00400000, 0x00402000, 0x00401000, 0x00000000, 0x00000000, C:\\\\sample.exe\n"
        "BB Table: 2 bbs\n"
        "module[ 0]: 0x00001000, 3\n"
        "module[ 0]: 0x00001003, 2\n",
        encoding="utf-8",
    )
    result = parse_drcov_text(log)
    assert result["drcov_version"] == "2"
    assert result["unique_basic_blocks"] == 2
    assert result["modules"][0]["path"].endswith("sample.exe")


def test_angr_backend_has_explicit_optional_dependency_error() -> None:
    """Verify angr backend has explicit optional dependency error behavior."""
    if importlib.util.find_spec("angr") is None:
        with pytest.raises(ExternalToolError):
            angr_bounded_compare(b"\x31\xc0\xc3", b"\x31\xc0\xc3")
        return
    completed = subprocess.run(
        [sys.executable, "-c", "import angr"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=60,
        check=False,
    )
    assert completed.returncode == 0, completed.stdout[-4000:]
```
