"""Verify the current toolkit behavior covered by `tests/test_pdb.py`."""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

from x86decomp.errors import FormatError
from x86decomp.pdb import parse_pdb, parse_pdb_bytes
from x86decomp.test_bundle import create_test_bundle, inspect_test_bundle


def test_invalid_pdb_is_rejected() -> None:
    """Verify invalid pdb is rejected behavior."""
    with pytest.raises(FormatError, match="MSF 7.0"):
        parse_pdb_bytes(b"not a pdb")


@pytest.mark.skipif(
    shutil.which("clang++") is None or shutil.which("lld-link") is None,
    reason="LLVM Windows C++/linker tools unavailable",
)
def test_real_lld_pdb_inventory_identity_and_bundle(tmp_path: Path) -> None:
    """Verify real lld pdb inventory identity and bundle behavior."""
    source = tmp_path / "sample.cpp"
    source.write_text(
        "struct Base { virtual int f(){return 1;} virtual ~Base(){} };\n"
        "struct Derived: Base { int f() override {return 2;} };\n"
        "Derived global_object;\n"
        "extern \"C\" int atexit(void(*)(void)){return 0;}\n"
        "extern \"C\" int entry(){return global_object.f();}\n",
        encoding="utf-8",
    )
    obj = tmp_path / "sample.obj"
    image = tmp_path / "sample.exe"
    pdb = tmp_path / "sample.pdb"
    map_file = tmp_path / "sample.map"
    subprocess.run(
        [
            "clang++", "-target", "x86_64-pc-windows-msvc", "-c", str(source),
            "-O0", "-g", "-gcodeview", "-frtti", "-fexceptions", "-o", str(obj),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    linked = subprocess.run(
        [
            "lld-link", "/nologo", "/machine:x64", "/entry:entry", "/subsystem:console",
            "/nodefaultlib", "/force:unresolved", "/debug", f"/pdb:{pdb}",
            f"/map:{map_file}", f"/out:{image}", str(obj),
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    assert linked.returncode == 0, linked.stderr

    report = parse_pdb(pdb, pe_path=image).to_dict()
    assert report["superblock"]["block_size"] == 4096
    assert report["pdb_info"]["age"] == 1
    assert report["tpi"]["type_record_count"] > 0
    assert report["ipi"]["type_record_count"] > 0
    assert any(module["object_file_name"].endswith("sample.obj") for module in report["dbi"]["modules"])
    assert str(source) in report["dbi"]["source_info"]["unique_files"]
    assert report["pe_match"]["identity_match"]
    assert report["scope"]["codeview_type_records_fully_parsed"] is False

    bundle = tmp_path / "authorized.zip"
    created = create_test_bundle(
        bundle,
        artifacts=[
            ("primary_image", image),
            ("pdb", pdb),
            ("linker_map", map_file),
            ("coff_object", obj),
        ],
        authorization_statement="Synthetic files created and owned by this regression test.",
        expected_architecture="x86_64",
    )
    assert created["static_verification_passed"]
    inspected = inspect_test_bundle(bundle)
    assert inspected["passed"]
    assert inspected["analyses"]["pdb_files"][0]["pdb"]["pe_match"]["identity_match"]
    assert inspected["supplied_code_executed"] is False
