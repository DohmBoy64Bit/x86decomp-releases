"""Verify the current toolkit behavior covered by `tests/test_coff_archive.py`."""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

from x86decomp.coff_archive import parse_coff_archive
from x86decomp.test_bundle import create_test_bundle, inspect_test_bundle


@pytest.mark.skipif(shutil.which("clang") is None or shutil.which("llvm-ar") is None, reason="LLVM tools unavailable")
def test_real_coff_archive_members_symbols_and_comdat(tmp_path: Path) -> None:
    """Verify real coff archive members symbols and comdat behavior."""
    first_source = tmp_path / "first.c"
    first_source.write_text("int add(int a,int b){return a+b;}\n", encoding="utf-8")
    second_source = tmp_path / "second.c"
    second_source.write_text(
        "__declspec(selectany) int shared_value=7;\n"
        "int get_shared(void){return shared_value;}\n",
        encoding="utf-8",
    )
    first_object = tmp_path / "first.obj"
    second_object = tmp_path / "second.obj"
    archive = tmp_path / "sample.lib"
    for source, output in ((first_source, first_object), (second_source, second_object)):
        subprocess.run(
            ["clang", "--target=i686-pc-windows-msvc", "-c", str(source), "-o", str(output)],
            check=True,
            capture_output=True,
            text=True,
        )
    subprocess.run(
        ["llvm-ar", "rc", str(archive), str(first_object), str(second_object)],
        check=True,
        capture_output=True,
        text=True,
    )

    report = parse_coff_archive(archive).to_dict()
    object_members = [member for member in report["members"] if member["kind"] == "coff_object"]
    assert [member["name"] for member in object_members] == ["first.obj", "second.obj"]
    assert all(member["coff"]["architecture"] == "x86" for member in object_members)
    symbols = {entry["name"] for entry in report["linker_symbols"]}
    assert {"_add", "_get_shared", "_shared_value"}.issubset(symbols)
    assert any(
        section.get("comdat") is not None
        for member in object_members
        for section in member["coff"]["sections"]
    )


@pytest.mark.skipif(shutil.which("clang") is None or shutil.which("llvm-ar") is None, reason="LLVM tools unavailable")
def test_static_library_is_inspected_in_safe_bundle(tmp_path: Path) -> None:
    """Verify static library is inspected in safe bundle behavior."""
    source = tmp_path / "library.c"
    source.write_text("int library_value(void){return 19;}\n", encoding="utf-8")
    obj = tmp_path / "library.obj"
    archive = tmp_path / "library.lib"
    subprocess.run(
        ["clang", "--target=i686-pc-windows-msvc", "-c", str(source), "-o", str(obj)],
        check=True,
        capture_output=True,
        text=True,
    )
    subprocess.run(["llvm-ar", "rc", str(archive), str(obj)], check=True, capture_output=True, text=True)

    bundle = tmp_path / "bundle.zip"
    created = create_test_bundle(
        bundle,
        artifacts=[("static_library", archive)],
        authorization_statement="Synthetic library created and owned by this regression test.",
        expected_architecture="x86",
    )
    assert created["static_verification_passed"]
    report = inspect_test_bundle(bundle)
    assert report["passed"]
    archives = report["analyses"]["coff_archives"]
    assert len(archives) == 1
    assert any(member["kind"] == "coff_object" for member in archives[0]["archive"]["members"])
    assert report["supplied_code_executed"] is False

@pytest.mark.skipif(
    shutil.which("clang") is None or shutil.which("lld-link") is None,
    reason="LLVM Windows linker tools unavailable",
)
def test_real_import_library_records(tmp_path: Path) -> None:
    """Verify real import library records behavior."""
    source = tmp_path / "export.c"
    source.write_text("__declspec(dllexport) int exported_value(int x){return x+1;}\n", encoding="utf-8")
    obj = tmp_path / "export.obj"
    dll = tmp_path / "export.dll"
    library = tmp_path / "export.lib"
    subprocess.run(
        ["clang", "--target=i686-pc-windows-msvc", "-c", str(source), "-o", str(obj)],
        check=True,
        capture_output=True,
        text=True,
    )
    completed = subprocess.run(
        [
            "lld-link", "/nologo", "/dll", "/noentry", "/nodefaultlib", "/machine:x86",
            f"/out:{dll}", f"/implib:{library}", str(obj),
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0, completed.stderr
    report = parse_coff_archive(library).to_dict()
    imports = [member["import_object"] for member in report["members"] if member["kind"] == "import_object"]
    assert any(item["symbol"] == "_exported_value" and item["dll"] == "export.dll" for item in imports)
    assert any(entry["name"] == "__imp__exported_value" for entry in report["linker_symbols"])
