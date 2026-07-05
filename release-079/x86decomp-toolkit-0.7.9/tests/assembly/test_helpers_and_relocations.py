"""Provide tests.assembly.test_helpers_and_relocations functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from x86decomp.contracts import ContractError
from x86decomp.assembly import cli as assembly_cli
from x86decomp.assembly.materialize import AssemblerError, InstructionCandidate, _render_source, materialize_function
from x86decomp.assembly.relocations import RelocationResolver, SymbolAddress


def test_assembly_cli_json_integer_and_error_helpers(tmp_path: Path) -> None:
    """Verify assembly cli json integer and error helpers.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    value = tmp_path / "value.json"
    value.write_text('{"x": 1}', encoding="utf-8")
    assert assembly_cli._int("0x20") == 32
    assert assembly_cli._json_file(value) == {"x": 1}
    assert assembly_cli._json_array('["clang", "-c"]') == ["clang", "-c"]
    assert assembly_cli._json_array(None) is None
    with pytest.raises(ContractError):
        assembly_cli._json_array('{}')
    with pytest.raises(ContractError):
        assembly_cli._json_file(tmp_path / "missing.json")


def test_symbol_address_error_and_render_helpers() -> None:
    """Verify symbol address error and render helpers.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    symbol = SymbolAddress("target", 0x2000, section_rva=0x1000, section_index=1, kind="function")
    assert symbol.safe_name == "target"
    assert symbol.to_dict()["rva"] == 0x2000
    error = AssemblerError("bad", line_numbers=[9, 2, 9, -1])
    assert error.line_numbers == (2, 9)
    unit = InstructionCandidate(0, 0x1000, 1, b"\xc3", "ret", "", "ret")
    source = _render_source(symbol="entry", architecture="x86", units=[unit], fallback_offsets=set(), externals=set())
    assert "entry:" in source and "ret" in source


def test_relocation_inspection_paths(tmp_path: Path) -> None:
    """Verify relocation inspection paths.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    source, obj, resolved = tmp_path / "entry.S", tmp_path / "entry.obj", tmp_path / "entry.bin"
    materialize_function(
        b"\xc3",
        symbol="entry",
        rva=0x1000,
        architecture="x86",
        symbol_map={"entry": 0x1000},
        source_path=source,
        object_path=obj,
        resolved_path=resolved,
    )
    resolver = RelocationResolver()
    whole = resolver.inspect(obj)
    extracted = resolver.inspect(obj, symbol="entry")
    assert whole["architecture"] == "x86" and whole["sections"]
    assert extracted["extracted"]["symbol"]["name"].lstrip("_") == "entry"
