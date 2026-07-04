import importlib.util
from pathlib import Path

import pytest

from x86decomp.dynamic import ExecutionSpec, differential_validate
from x86decomp.symbolic import bounded_symbolic_compare

ADD = bytes.fromhex("8b44240403442408c3")
SUB = bytes.fromhex("8b4424042b442408c3")


@pytest.mark.skipif(importlib.util.find_spec("unicorn") is None, reason="unicorn not installed")
def test_dynamic_equivalence_and_difference() -> None:
    spec = ExecutionSpec(
        architecture="x86", code_base=0x1000000, stack_base=0x70000000, stack_size=0x20000,
        sentinel_address=0x0FFF0000, max_instructions=100, timeout_ms=1000,
        registers={}, stack_arguments=(3).to_bytes(4, "little") + (4).to_bytes(4, "little"),
        memory=(), observe_registers=("eax", "esp"), observe_memory=(), stubs={},
    )
    assert differential_validate(ADD, ADD, spec)["equivalent_for_harness"]
    assert not differential_validate(ADD, SUB, spec)["equivalent_for_harness"]


@pytest.mark.skipif(importlib.util.find_spec("z3") is None or importlib.util.find_spec("capstone") is None, reason="symbolic deps not installed")
def test_symbolic_bounded_equivalence() -> None:
    same = bounded_symbolic_compare(ADD, ADD, stack_argument_words=2)
    assert same["equivalent_within_model"]
    different = bounded_symbolic_compare(ADD, SUB, stack_argument_words=2)
    assert not different["equivalent_within_model"]
    assert different["counterexample"] is not None
