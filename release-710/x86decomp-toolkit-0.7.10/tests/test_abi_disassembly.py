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
