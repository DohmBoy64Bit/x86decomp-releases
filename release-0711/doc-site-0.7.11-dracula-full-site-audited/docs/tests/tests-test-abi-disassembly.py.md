---
title: tests/test_abi_disassembly.py
description: Test source page for tests/test_abi_disassembly.py.
---

# `tests/test_abi_disassembly.py`

- SHA-256: `91ebeb183e6f9728fff8d8d828615c79506b7b1d2752a0caaf016379aec1c590`
- Size: `784` bytes
- Test functions: `1`

```python
"""Verify the current toolkit behavior covered by `tests/test_abi_disassembly.py`."""
import importlib.util

import pytest

from x86decomp.abi import ABIContract, CallingConvention, FloatMode, validate_abi
from x86decomp.errors import ExternalToolError


def test_stdcall_ret_cleanup() -> None:
    """Verify stdcall ret cleanup behavior."""
    contract = ABIContract("x86", CallingConvention.STDCALL, 8, 8, False, None, (), ("eax",), False, FloatMode.NONE)
    if importlib.util.find_spec("capstone") is None:
        with pytest.raises(ExternalToolError, match="Capstone is required"):
            validate_abi(bytes.fromhex("31c0c20800"), contract)
        return
    report = validate_abi(bytes.fromhex("31c0c20800"), contract)
    assert report["compatible_with_observed_code"]
```
