"""Explicit x86 ABI contracts and bounded static compatibility checks."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Any

from .disassembly import decode_instructions
from .errors import ContractError
from .util import load_json, utc_now, write_json


class CallingConvention(StrEnum):
    """Enumerate supported calling convention values."""
    CDECL = "cdecl"
    STDCALL = "stdcall"
    THISCALL = "thiscall"
    FASTCALL = "fastcall"
    VECTORCALL = "vectorcall"
    UNKNOWN = "unknown"


class FloatMode(StrEnum):
    """Enumerate supported float mode values."""
    X87 = "x87"
    SSE = "sse"
    MIXED = "mixed"
    NONE = "none"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class ABIContract:
    """Store validated a b i contract fields used by toolkit reports and adapters."""
    architecture: str
    convention: CallingConvention
    stack_argument_bytes: int | None
    callee_stack_cleanup: int | None
    variadic: bool
    this_register: str | None
    register_arguments: tuple[str, ...]
    return_registers: tuple[str, ...]
    structure_return: bool
    floating_point: FloatMode

    @classmethod
    def from_dict(cls, value: Any) -> "ABIContract":
        """Build abicontract from validated mapping data."""
        if not isinstance(value, dict):
            raise ContractError("ABI contract must be an object")
        architecture = value.get("architecture")
        if architecture not in ("x86", "x86_64"):
            raise ContractError("ABI architecture must be x86 or x86_64")
        try:
            convention = CallingConvention(value.get("convention", "unknown"))
            floating_point = FloatMode(value.get("floating_point", "unknown"))
        except ValueError as exc:
            raise ContractError(f"invalid ABI enum: {exc}") from exc
        def optional_nonnegative(key: str) -> int | None:
            """Validate an optional integer and reject negative values."""
            raw = value.get(key)
            if raw is None:
                return None
            if not isinstance(raw, int) or isinstance(raw, bool) or raw < 0:
                raise ContractError(f"{key} must be null or a non-negative integer")
            return raw
        register_arguments = value.get("register_arguments", [])
        return_registers = value.get("return_registers", ["eax"] if architecture == "x86" else ["rax"])
        if not isinstance(register_arguments, list) or not all(isinstance(item, str) for item in register_arguments):
            raise ContractError("register_arguments must be an array of strings")
        if not isinstance(return_registers, list) or not all(isinstance(item, str) for item in return_registers):
            raise ContractError("return_registers must be an array of strings")
        this_register = value.get("this_register")
        if this_register is not None and not isinstance(this_register, str):
            raise ContractError("this_register must be null or a string")
        return cls(
            architecture=architecture,
            convention=convention,
            stack_argument_bytes=optional_nonnegative("stack_argument_bytes"),
            callee_stack_cleanup=optional_nonnegative("callee_stack_cleanup"),
            variadic=bool(value.get("variadic", False)),
            this_register=this_register,
            register_arguments=tuple(item.lower() for item in register_arguments),
            return_registers=tuple(item.lower() for item in return_registers),
            structure_return=bool(value.get("structure_return", False)),
            floating_point=floating_point,
        )


def load_abi_contract(path: Path) -> ABIContract:
    """Load ABI contract."""
    return ABIContract.from_dict(load_json(path))


def analyze_abi(code: bytes, *, architecture: str = "x86", base_address: int = 0) -> dict[str, Any]:
    """Analyze ABI."""
    instructions = decode_instructions(code, base_address=base_address, architecture=architecture)
    mnemonics = [record.mnemonic for record in instructions]
    ret_immediates: list[int] = []
    uses_ecx = False
    uses_edx = False
    uses_x87 = False
    uses_sse = False
    frame_pointer = False
    stack_adjustments: list[str] = []
    for record in instructions:
        text = f"{record.mnemonic} {record.op_str}".lower()
        if record.mnemonic == "ret" and record.op_str:
            try:
                ret_immediates.append(int(record.op_str, 0))
            except ValueError:
                pass
        uses_ecx |= "ecx" in text or "rcx" in text
        uses_edx |= "edx" in text or "rdx" in text
        uses_x87 |= record.mnemonic.startswith("f") and record.mnemonic not in ("fs",)
        uses_sse |= "xmm" in text or "ymm" in text or "zmm" in text
        frame_pointer |= text in ("push ebp", "mov ebp, esp", "push rbp", "mov rbp, rsp")
        if record.mnemonic in ("add", "sub") and ("esp" in text or "rsp" in text):
            stack_adjustments.append(text)
    inferred_cleanup = None
    if ret_immediates and len(set(ret_immediates)) == 1:
        inferred_cleanup = ret_immediates[0]
    float_mode = (
        "mixed" if uses_x87 and uses_sse else "x87" if uses_x87 else "sse" if uses_sse else "none"
    )
    convention_candidates: list[str] = []
    if architecture == "x86":
        if inferred_cleanup and uses_ecx and uses_edx:
            convention_candidates.append("fastcall")
        if inferred_cleanup and uses_ecx:
            convention_candidates.append("thiscall")
        if inferred_cleanup:
            convention_candidates.append("stdcall")
        else:
            convention_candidates.append("cdecl_or_variadic")
    else:
        convention_candidates.append("windows_x64_or_sysv_x64_requires_context")
    return {
        "architecture": architecture,
        "instruction_count": len(instructions),
        "return_instruction_count": mnemonics.count("ret"),
        "ret_immediates": ret_immediates,
        "inferred_callee_stack_cleanup": inferred_cleanup,
        "uses_ecx_or_rcx": uses_ecx,
        "uses_edx_or_rdx": uses_edx,
        "frame_pointer_pattern_observed": frame_pointer,
        "stack_adjustments": stack_adjustments,
        "floating_point_observed": float_mode,
        "convention_candidates": convention_candidates,
        "limitations": [
            "Register occurrence is not proof of parameter passing.",
            "Optimized leaf functions may omit standard prologues and epilogues.",
            "Caller-side evidence is required to establish a convention reliably.",
        ],
    }


def validate_abi(
    code: bytes,
    contract: ABIContract,
    *,
    base_address: int = 0,
    report_path: Path | None = None,
) -> dict[str, Any]:
    """Validate ABI."""
    analysis = analyze_abi(code, architecture=contract.architecture, base_address=base_address)
    checks: list[dict[str, Any]] = []
    observed_cleanup = analysis["inferred_callee_stack_cleanup"]
    expected_cleanup = contract.callee_stack_cleanup
    if expected_cleanup is not None:
        checks.append(
            {
                "name": "callee_stack_cleanup",
                "passed": observed_cleanup == expected_cleanup,
                "expected": expected_cleanup,
                "observed": observed_cleanup,
                "strength": "direct_epilogue_observation",
            }
        )
    if contract.variadic:
        checks.append(
            {
                "name": "variadic_caller_cleanup",
                "passed": observed_cleanup in (None, 0),
                "expected": "no ret immediate",
                "observed": observed_cleanup,
                "strength": "necessary_not_sufficient",
            }
        )
    if contract.this_register is not None:
        used = analysis["uses_ecx_or_rcx"] if contract.this_register.lower() in ("ecx", "rcx") else None
        checks.append(
            {
                "name": "this_register_observed",
                "passed": used is True,
                "expected": contract.this_register,
                "observed": used,
                "strength": "weak_static_signal",
            }
        )
    if contract.floating_point != FloatMode.UNKNOWN:
        observed = analysis["floating_point_observed"]
        checks.append(
            {
                "name": "floating_point_mode",
                "passed": observed == contract.floating_point.value or (contract.floating_point == FloatMode.NONE and observed == "none"),
                "expected": contract.floating_point.value,
                "observed": observed,
                "strength": "instruction_family_observation",
            }
        )
    if contract.convention == CallingConvention.CDECL:
        checks.append(
            {
                "name": "cdecl_no_callee_argument_pop",
                "passed": observed_cleanup in (None, 0),
                "expected": 0,
                "observed": observed_cleanup,
                "strength": "necessary_not_sufficient",
            }
        )
    elif contract.convention in (CallingConvention.STDCALL, CallingConvention.THISCALL, CallingConvention.FASTCALL):
        if contract.stack_argument_bytes is not None:
            checks.append(
                {
                    "name": "callee_pop_matches_stack_arguments",
                    "passed": observed_cleanup == contract.stack_argument_bytes,
                    "expected": contract.stack_argument_bytes,
                    "observed": observed_cleanup,
                    "strength": "direct_epilogue_observation",
                }
            )
    failed = [check for check in checks if not check["passed"]]
    report = {
        "schema_version": 1,
        "created_at": utc_now(),
        "kind": "bounded_static_abi_validation",
        "contract": {
            "architecture": contract.architecture,
            "convention": contract.convention.value,
            "stack_argument_bytes": contract.stack_argument_bytes,
            "callee_stack_cleanup": contract.callee_stack_cleanup,
            "variadic": contract.variadic,
            "this_register": contract.this_register,
            "register_arguments": list(contract.register_arguments),
            "return_registers": list(contract.return_registers),
            "structure_return": contract.structure_return,
            "floating_point": contract.floating_point.value,
        },
        "analysis": analysis,
        "checks": checks,
        "compatible_with_observed_code": not failed,
        "semantic_or_full_abi_equivalence_claimed": False,
    }
    if report_path is not None:
        write_json(report_path, report)
    return report
