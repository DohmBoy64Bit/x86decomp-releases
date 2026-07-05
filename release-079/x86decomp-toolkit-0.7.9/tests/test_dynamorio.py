"""Provide tests.test_dynamorio functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from pathlib import Path
import importlib.util
import subprocess
import sys

import pytest

from x86decomp.angr_backend import angr_bounded_compare
from x86decomp.dynamorio import parse_drcov_text
from x86decomp.errors import ExternalToolError


def test_parse_drcov_text(tmp_path: Path) -> None:
    """Verify parse drcov text.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
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
    """Verify angr backend has explicit optional dependency error.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
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
