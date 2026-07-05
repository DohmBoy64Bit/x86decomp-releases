"""Provide tests.test_coff functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from pathlib import Path

from x86decomp.coff import CoffRelocation, build_synthetic_coff, extract_symbol, parse_coff_bytes


def test_synthetic_coff_round_trip() -> None:
    """Verify synthetic coff round trip.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    code = b"\x31\xc0\xc3"
    data = build_synthetic_coff(code=code, symbol_name="very_long_function_name")
    obj = parse_coff_bytes(data)
    extracted = extract_symbol(obj, "very_long_function_name")
    assert extracted.data == code
    assert obj.architecture == "x86"


def test_synthetic_coff_relocation() -> None:
    """Verify synthetic coff relocation.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    code = b"\xe8\x00\x00\x00\x00\xc3"
    data = build_synthetic_coff(code=code, symbol_name="f", relocations=[CoffRelocation(1, 0, 0x14)])
    obj = parse_coff_bytes(data)
    extracted = extract_symbol(obj, "f")
    assert extracted.relocations[0].offset == 1
    assert extracted.relocations[0].width(obj.machine) == 4
