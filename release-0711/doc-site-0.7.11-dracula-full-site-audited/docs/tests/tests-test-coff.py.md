---
title: tests/test_coff.py
description: Test source page for tests/test_coff.py.
---

# `tests/test_coff.py`

- SHA-256: `0db7135636f4571252ebc19b33c78b736d1c0e552707a4b9f7d0cfdb85b7796a`
- Size: `1000` bytes
- Test functions: `2`

```python
"""Verify the current toolkit behavior covered by `tests/test_coff.py`."""
from pathlib import Path

from x86decomp.coff import CoffRelocation, build_synthetic_coff, extract_symbol, parse_coff_bytes


def test_synthetic_coff_round_trip() -> None:
    """Verify synthetic coff round trip behavior."""
    code = b"\x31\xc0\xc3"
    data = build_synthetic_coff(code=code, symbol_name="very_long_function_name")
    obj = parse_coff_bytes(data)
    extracted = extract_symbol(obj, "very_long_function_name")
    assert extracted.data == code
    assert obj.architecture == "x86"


def test_synthetic_coff_relocation() -> None:
    """Verify synthetic coff relocation behavior."""
    code = b"\xe8\x00\x00\x00\x00\xc3"
    data = build_synthetic_coff(code=code, symbol_name="f", relocations=[CoffRelocation(1, 0, 0x14)])
    obj = parse_coff_bytes(data)
    extracted = extract_symbol(obj, "f")
    assert extracted.relocations[0].offset == 1
    assert extracted.relocations[0].width(obj.machine) == 4
```
