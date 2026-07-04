import importlib.util

import pytest

from x86decomp.abi import ABIContract, CallingConvention, FloatMode, validate_abi


@pytest.mark.skipif(importlib.util.find_spec("capstone") is None, reason="capstone not installed")
def test_stdcall_ret_cleanup() -> None:
    contract = ABIContract("x86", CallingConvention.STDCALL, 8, 8, False, None, (), ("eax",), False, FloatMode.NONE)
    report = validate_abi(bytes.fromhex("31c0c20800"), contract)
    assert report["compatible_with_observed_code"]
