"""Verify the current toolkit behavior covered by `tests/assembly/test_annotation_materialize.py`."""
from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

from x86decomp.hybrid import _assembly_bytes
from x86decomp.contracts import ContractError
from x86decomp.errors import ExternalToolError
from x86decomp.assembly.annotation import (
    annotate_source,
    parse_byte_directives,
    render_byte_assembly,
    validate_symbol,
)
from x86decomp.assembly.materialize import materialize_function, verify_existing_source


def _capstone_available() -> bool:
    """Return whether the optional Capstone decoder is importable."""
    return importlib.util.find_spec("capstone") is not None


def _assert_capstone_required(callable_, *args, **kwargs) -> None:
    """Assert that a decoder-backed operation reports the missing optional dependency."""
    with pytest.raises(ExternalToolError, match="Capstone is required"):
        callable_(*args, **kwargs)


def test_byte_form_is_exact_native_compatibility_output() -> None:
    """Verify byte form is exact native compatibility output behavior."""
    code = bytes(range(32))
    assert render_byte_assembly("sub_00001000", code, "x86") == _assembly_bytes(
        "sub_00001000", code, "x86"
    )
    assert parse_byte_directives(render_byte_assembly("sub_00001000", code, "x86")) == code
    with pytest.raises(ContractError, match="unsafe assembly symbol"):
        validate_symbol("bad symbol")


def test_annotation_is_idempotent_and_keeps_bytes(tmp_path: Path) -> None:
    """Verify annotation is idempotent and keeps bytes behavior."""
    code = bytes.fromhex("5589e5e8000000005dc3")
    source = tmp_path / "input.S"
    source.write_text(render_byte_assembly("sub_00001000", code, "x86"), encoding="utf-8")
    first = tmp_path / "first.S"
    second = tmp_path / "second.S"
    if not _capstone_available():
        _assert_capstone_required(
            annotate_source, source, first, symbol="sub_00001000", architecture="x86", base_address=0x401000
        )
        return
    result = annotate_source(
        source, first, symbol="sub_00001000", architecture="x86", base_address=0x401000
    )
    annotate_source(
        first, second, symbol="sub_00001000", architecture="x86", base_address=0x401000
    )
    assert result["byte_identical_by_construction"]
    assert first.read_text(encoding="utf-8") == second.read_text(encoding="utf-8")
    assert parse_byte_directives(first.read_text(encoding="utf-8")) == code
    assert "# x86decomp:" in first.read_text(encoding="utf-8")


def _materialize(tmp_path: Path, code: bytes, *, architecture: str, symbols: dict[str, object]):
    """Materialize the requested operation."""
    return materialize_function(
        code,
        symbol="sub_00001000",
        rva=0x1000,
        architecture=architecture,
        symbol_map={"sub_00001000": {"rva": 0x1000}, **symbols},
        source_path=tmp_path / "candidate.S",
        object_path=tmp_path / "candidate.obj",
        resolved_path=tmp_path / "candidate.bin",
    )


def test_x86_external_and_local_calls_roundtrip_exactly(tmp_path: Path) -> None:
    """Verify x86 external and local calls roundtrip exactly behavior."""
    external = _materialize(
        tmp_path / "external",
        bytes.fromhex("e8fb0f0000c3"),
        architecture="x86",
        symbols={"sub_00002000": {"rva": 0x2000}},
    )
    if not _capstone_available():
        assert external["classification"] == "byte-form-fallback"
        assert external["exact_match"]
        assert not external["semantic_equivalence_claimed"]
        return
    assert external["classification"] == "fully-mnemonic"
    assert external["resolved_relocation_count"] == 1
    assert (tmp_path / "external/candidate.bin").read_bytes() == bytes.fromhex("e8fb0f0000c3")
    assert "call sub_00002000" in (tmp_path / "external/candidate.S").read_text()

    local = _materialize(
        tmp_path / "local",
        bytes.fromhex("e800000000c3"),
        architecture="x86",
        symbols={},
    )
    assert local["classification"] == "fully-mnemonic"
    assert local["relocation_count"] == 0
    assert (tmp_path / "local/candidate.bin").read_bytes() == bytes.fromhex("e800000000c3")
    assert ".L_1005:" in (tmp_path / "local/candidate.S").read_text()


def test_x64_rip_relative_data_reference_roundtrips(tmp_path: Path) -> None:
    """Verify x64 rip relative data reference roundtrips behavior."""
    result = _materialize(
        tmp_path,
        bytes.fromhex("488b05f90f0000c3"),
        architecture="x86_64",
        symbols={"DAT_00002000": {"rva": 0x2000, "kind": "data"}},
    )
    if not _capstone_available():
        assert result["classification"] == "byte-form-fallback"
        assert result["exact_match"]
        assert not result["semantic_equivalence_claimed"]
        return
    assert result["classification"] == "fully-mnemonic"
    assert result["resolved_relocation_count"] == 1
    assert "DAT_00002000" in (tmp_path / "candidate.S").read_text()
    assert (tmp_path / "candidate.bin").read_bytes() == bytes.fromhex("488b05f90f0000c3")


def test_noncanonical_instruction_falls_back_per_instruction(tmp_path: Path) -> None:
    """Verify noncanonical instruction falls back per instruction behavior."""
    result = _materialize(
        tmp_path,
        bytes.fromhex("6690c3"),
        architecture="x86",
        symbols={},
    )
    if not _capstone_available():
        assert result["classification"] == "byte-form-fallback"
        assert result["byte_escape_bytes"] == 3
        return
    assert result["classification"] == "mixed-mnemonic-byte"
    assert result["mnemonic_count"] == 1
    assert result["byte_escape_count"] == 1
    text = (tmp_path / "candidate.S").read_text()
    assert ".byte 0x66, 0x90" in text and "ret" in text
    assert (tmp_path / "candidate.bin").read_bytes() == bytes.fromhex("6690c3")


def test_unknown_target_uses_byte_fallback_without_false_claim(tmp_path: Path) -> None:
    """Verify unknown target uses byte fallback without false claim behavior."""
    result = _materialize(
        tmp_path,
        bytes.fromhex("e8fb0f0000c3"),
        architecture="x86",
        symbols={},
    )
    assert result["exact_match"]
    if not _capstone_available():
        assert result["classification"] == "byte-form-fallback"
        assert not result["semantic_equivalence_claimed"]
        return
    assert result["classification"] == "mixed-mnemonic-byte"
    assert not result["semantic_equivalence_claimed"]
    assert ".byte 0xe8" in (tmp_path / "candidate.S").read_text()


def test_verify_existing_source_reports_exact_and_mismatch(tmp_path: Path) -> None:
    """Verify exact and mismatched existing-source reports."""
    code = bytes.fromhex("e8fb0f0000c3")
    source = tmp_path / "source.S"
    source.write_text(
        ".intel_syntax noprefix\n.text\n.code32\n.globl sub_00001000\n"
        ".extern sub_00002000\nsub_00001000:\n  call sub_00002000\n  ret\n",
        encoding="utf-8",
    )
    exact = verify_existing_source(
        source,
        code,
        symbol="sub_00001000",
        rva=0x1000,
        architecture="x86",
        symbol_map={"sub_00002000": {"rva": 0x2000}},
        object_path=tmp_path / "exact.obj",
        resolved_path=tmp_path / "exact.bin",
    )
    assert exact["exact_match"] and exact["classification"] == "exact"
    mismatch = verify_existing_source(
        source,
        bytes.fromhex("e8fa0f0000c3"),
        symbol="sub_00001000",
        rva=0x1000,
        architecture="x86",
        symbol_map={"sub_00002000": {"rva": 0x2000}},
        object_path=tmp_path / "mismatch.obj",
        resolved_path=tmp_path / "mismatch.bin",
    )
    assert not mismatch["exact_match"] and mismatch["classification"] == "mismatch"


def test_undecodable_tail_uses_complete_byte_form_fallback(tmp_path: Path) -> None:
    """Verify undecodable tail uses complete byte form fallback behavior."""
    result = _materialize(
        tmp_path,
        bytes.fromhex("0f"),
        architecture="x86",
        symbols={},
    )
    assert result["classification"] == "byte-form-fallback"
    assert result["mnemonic_count"] == 0
    assert result["byte_escape_bytes"] == 1
    assert (tmp_path / "candidate.bin").read_bytes() == bytes.fromhex("0f")
    assert ".byte 0x0f" in (tmp_path / "candidate.S").read_text()
