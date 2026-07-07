"""Bounded symbolic equivalence for small pure x86/x86-64 leaf functions.

The executor intentionally rejects instructions or addressing modes it cannot
model. A successful UNSAT result is therefore meaningful only for the modeled
instruction subset, configured inputs, explored paths, and selected outputs.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .errors import ContractError, ExternalToolError
from .util import sha256_bytes, utc_now, write_json


def _deps() -> tuple[Any, Any, Any]:
    """Import and return the optional Capstone and z3 dependencies.

    Returns:
        A ``(capstone, capstone.x86_const, z3)`` tuple with the imported modules.

    Raises:
        ExternalToolError: If Capstone or z3-solver is not installed.
    """
    try:
        import capstone  # type: ignore
        from capstone import x86_const  # type: ignore
        import z3  # type: ignore
    except ImportError as exc:
        raise ExternalToolError(
            "Capstone and z3-solver are required; install x86decomp-toolkit[symbolic]"
        ) from exc
    return capstone, x86_const, z3


class UnsupportedSymbolicInstruction(ContractError):
    """Raised when the bounded executor encounters an instruction or addressing mode
    it does not model."""
    pass


@dataclass
class SymState:
    """Store validated sym state fields used by toolkit reports and adapters."""
    pc: int
    regs: dict[str, Any]
    memory: dict[int, Any]
    constraints: list[Any] = field(default_factory=list)
    flags: dict[str, Any] = field(default_factory=dict)
    steps: int = 0

    def clone(self) -> "SymState":
        """Return a deep copy of this state with independent register, memory,
        constraint, and flag containers."""
        return SymState(
            pc=self.pc,
            regs=dict(self.regs),
            memory=dict(self.memory),
            constraints=list(self.constraints),
            flags=dict(self.flags),
            steps=self.steps,
        )


@dataclass(frozen=True)
class Outcome:
    """Store validated outcome fields used by toolkit reports and adapters."""
    constraints: tuple[Any, ...]
    outputs: dict[str, Any]
    stack_delta: Any


_REG_ALIASES_32 = {
    "eax": ("eax", 0, 32), "ax": ("eax", 0, 16), "al": ("eax", 0, 8), "ah": ("eax", 8, 8),
    "ebx": ("ebx", 0, 32), "bx": ("ebx", 0, 16), "bl": ("ebx", 0, 8), "bh": ("ebx", 8, 8),
    "ecx": ("ecx", 0, 32), "cx": ("ecx", 0, 16), "cl": ("ecx", 0, 8), "ch": ("ecx", 8, 8),
    "edx": ("edx", 0, 32), "dx": ("edx", 0, 16), "dl": ("edx", 0, 8), "dh": ("edx", 8, 8),
    "esi": ("esi", 0, 32), "si": ("esi", 0, 16),
    "edi": ("edi", 0, 32), "di": ("edi", 0, 16),
    "ebp": ("ebp", 0, 32), "bp": ("ebp", 0, 16),
    "esp": ("esp", 0, 32), "sp": ("esp", 0, 16),
}
_REG_ALIASES_64 = {
    "rax": ("rax", 0, 64), "eax": ("rax", 0, 32), "ax": ("rax", 0, 16), "al": ("rax", 0, 8), "ah": ("rax", 8, 8),
    "rbx": ("rbx", 0, 64), "ebx": ("rbx", 0, 32), "bx": ("rbx", 0, 16), "bl": ("rbx", 0, 8), "bh": ("rbx", 8, 8),
    "rcx": ("rcx", 0, 64), "ecx": ("rcx", 0, 32), "cx": ("rcx", 0, 16), "cl": ("rcx", 0, 8), "ch": ("rcx", 8, 8),
    "rdx": ("rdx", 0, 64), "edx": ("rdx", 0, 32), "dx": ("rdx", 0, 16), "dl": ("rdx", 0, 8), "dh": ("rdx", 8, 8),
    "rsi": ("rsi", 0, 64), "esi": ("rsi", 0, 32), "si": ("rsi", 0, 16), "sil": ("rsi", 0, 8),
    "rdi": ("rdi", 0, 64), "edi": ("rdi", 0, 32), "di": ("rdi", 0, 16), "dil": ("rdi", 0, 8),
    "rbp": ("rbp", 0, 64), "ebp": ("rbp", 0, 32), "bp": ("rbp", 0, 16), "bpl": ("rbp", 0, 8),
    "rsp": ("rsp", 0, 64), "esp": ("rsp", 0, 32), "sp": ("rsp", 0, 16), "spl": ("rsp", 0, 8),
}
for index in range(8, 16):
    _REG_ALIASES_64[f"r{index}"] = (f"r{index}", 0, 64)
    _REG_ALIASES_64[f"r{index}d"] = (f"r{index}", 0, 32)
    _REG_ALIASES_64[f"r{index}w"] = (f"r{index}", 0, 16)
    _REG_ALIASES_64[f"r{index}b"] = (f"r{index}", 0, 8)


def _aliases(architecture: str) -> dict[str, tuple[str, int, int]]:
    """Return the register alias table for the given architecture.

    Args:
        architecture: Either ``"x86"`` or ``"x86_64"``.

    Returns:
        A mapping from register name to its ``(canonical, low_bit, width)`` tuple.
    """
    return _REG_ALIASES_32 if architecture == "x86" else _REG_ALIASES_64


def _read_reg(state: SymState, name: str, architecture: str, z3: Any) -> Any:
    """Read a (possibly sub-width) register as a z3 bit-vector expression.

    Args:
        state: The symbolic state holding the canonical register values.
        name: Register name, including sub-register aliases such as ``al`` or ``ax``.
        architecture: Either ``"x86"`` or ``"x86_64"``.
        z3: The imported z3 module.

    Returns:
        The full register expression, or an ``Extract`` slice for a sub-register.

    Raises:
        UnsupportedSymbolicInstruction: If the register name is not in the alias table.
    """
    try:
        canonical, low, width = _aliases(architecture)[name]
    except KeyError as exc:
        raise UnsupportedSymbolicInstruction(f"unsupported register {name}") from exc
    full = state.regs[canonical]
    full_width = full.size()
    if low == 0 and width == full_width:
        return full
    return z3.Extract(low + width - 1, low, full)


def _write_reg(state: SymState, name: str, value: Any, architecture: str, z3: Any) -> None:
    """Write a value into a (possibly sub-width) register, preserving unaffected bits.

    The value is truncated or zero-extended to the target width. Writing a 32-bit
    sub-register on x86_64 zero-extends into the full 64-bit register.

    Args:
        state: The symbolic state to mutate.
        name: Register name, including sub-register aliases.
        value: The z3 bit-vector value to store.
        architecture: Either ``"x86"`` or ``"x86_64"``.
        z3: The imported z3 module.

    Raises:
        UnsupportedSymbolicInstruction: If the register name is not in the alias table.
    """
    try:
        canonical, low, width = _aliases(architecture)[name]
    except KeyError as exc:
        raise UnsupportedSymbolicInstruction(f"unsupported register {name}") from exc
    full = state.regs[canonical]
    full_width = full.size()
    value = z3.Extract(width - 1, 0, value) if value.size() > width else z3.ZeroExt(width - value.size(), value)
    if architecture == "x86_64" and low == 0 and width == 32:
        state.regs[canonical] = z3.ZeroExt(32, value)
        return
    high_width = full_width - (low + width)
    pieces = []
    if high_width > 0:
        pieces.append(z3.Extract(full_width - 1, low + width, full))
    pieces.append(value)
    if low > 0:
        pieces.append(z3.Extract(low - 1, 0, full))
    state.regs[canonical] = pieces[0] if len(pieces) == 1 else z3.Concat(*pieces)


def _concrete(expr: Any, z3: Any) -> int | None:
    """Return the concrete integer value of a bit-vector expression, or None.

    Args:
        expr: A z3 bit-vector expression.
        z3: The imported z3 module.

    Returns:
        The integer value if the simplified expression is a bit-vector literal,
        otherwise ``None``.
    """
    simplified = z3.simplify(expr)
    return simplified.as_long() if z3.is_bv_value(simplified) else None


def _memory_address(instruction: Any, operand: Any, state: SymState, architecture: str, engine: Any, z3: Any) -> int:
    """Compute the concrete effective address of a memory operand.

    Combines displacement, base register (with RIP-relative handling), and scaled
    index register, then requires the result to be concrete.

    Args:
        instruction: The decoded Capstone instruction (used for RIP-relative bases).
        operand: The memory operand being addressed.
        state: The current symbolic state.
        architecture: Either ``"x86"`` or ``"x86_64"``.
        engine: The Capstone engine, used to resolve register names.
        z3: The imported z3 module.

    Returns:
        The concrete effective address as an integer.

    Raises:
        UnsupportedSymbolicInstruction: If the computed address is not concrete.
    """
    memory = operand.mem
    width = 32 if architecture == "x86" else 64
    address = z3.BitVecVal(memory.disp & ((1 << width) - 1), width)
    if memory.base:
        base_name = engine.reg_name(memory.base)
        if base_name == "rip":
            address += z3.BitVecVal(instruction.address + instruction.size, width)
        else:
            address += _read_reg(state, base_name, architecture, z3)
    if memory.index:
        index_name = engine.reg_name(memory.index)
        address += _read_reg(state, index_name, architecture, z3) * memory.scale
    concrete = _concrete(address, z3)
    if concrete is None:
        raise UnsupportedSymbolicInstruction("symbolic memory addresses are outside the bounded model")
    return concrete


def _read_memory(state: SymState, address: int, width: int, z3: Any) -> Any:
    """Read ``width`` bits from little-endian byte-addressed symbolic memory.

    Bytes not yet present are lazily initialized to fresh symbolic bit-vectors.

    Args:
        state: The current symbolic state.
        address: The base byte address to read from.
        width: The read width in bits; must be a positive multiple of 8.
        z3: The imported z3 module.

    Returns:
        A bit-vector expression of the requested width.

    Raises:
        UnsupportedSymbolicInstruction: If ``width`` is not a positive multiple of 8.
    """
    if width % 8 != 0 or width <= 0:
        raise UnsupportedSymbolicInstruction(f"unsupported memory width {width}")
    bytes_ = []
    for offset in range(width // 8):
        if address + offset not in state.memory:
            state.memory[address + offset] = z3.BitVec(f"mem_{address + offset:x}", 8)
        bytes_.append(state.memory[address + offset])
    return bytes_[0] if len(bytes_) == 1 else z3.Concat(*reversed(bytes_))


def _write_memory(state: SymState, address: int, width: int, value: Any, z3: Any) -> None:
    """Write ``width`` bits of a value into little-endian byte-addressed memory.

    The value is zero-extended or truncated to ``width`` before being split into bytes.

    Args:
        state: The symbolic state to mutate.
        address: The base byte address to write to.
        width: The write width in bits; must be a positive multiple of 8.
        value: The z3 bit-vector value to store.
        z3: The imported z3 module.

    Raises:
        UnsupportedSymbolicInstruction: If ``width`` is not a positive multiple of 8.
    """
    if width % 8 != 0 or width <= 0:
        raise UnsupportedSymbolicInstruction(f"unsupported memory width {width}")
    if value.size() < width:
        value = z3.ZeroExt(width - value.size(), value)
    elif value.size() > width:
        value = z3.Extract(width - 1, 0, value)
    for offset in range(width // 8):
        state.memory[address + offset] = z3.Extract(offset * 8 + 7, offset * 8, value)


def _read_operand(instruction: Any, operand: Any, state: SymState, architecture: str, engine: Any, x86_const: Any, z3: Any) -> Any:
    """Read a register, immediate, or memory operand as a bit-vector expression.

    Args:
        instruction: The decoded Capstone instruction.
        operand: The operand to read.
        state: The current symbolic state.
        architecture: Either ``"x86"`` or ``"x86_64"``.
        engine: The Capstone engine, used to resolve register names.
        x86_const: The Capstone x86 constants module.
        z3: The imported z3 module.

    Returns:
        A bit-vector expression for the operand value.

    Raises:
        UnsupportedSymbolicInstruction: If the operand type is not register, immediate,
            or memory.
    """
    width = max(1, operand.size * 8)
    if operand.type == x86_const.X86_OP_REG:
        return _read_reg(state, engine.reg_name(operand.reg), architecture, z3)
    if operand.type == x86_const.X86_OP_IMM:
        return z3.BitVecVal(int(operand.imm) & ((1 << width) - 1), width)
    if operand.type == x86_const.X86_OP_MEM:
        address = _memory_address(instruction, operand, state, architecture, engine, z3)
        return _read_memory(state, address, width, z3)
    raise UnsupportedSymbolicInstruction(f"unsupported operand type {operand.type}")


def _write_operand(instruction: Any, operand: Any, value: Any, state: SymState, architecture: str, engine: Any, x86_const: Any, z3: Any) -> None:
    """Write a value into a register or memory destination operand.

    Args:
        instruction: The decoded Capstone instruction.
        operand: The destination operand.
        value: The z3 bit-vector value to store.
        state: The symbolic state to mutate.
        architecture: Either ``"x86"`` or ``"x86_64"``.
        engine: The Capstone engine, used to resolve register names.
        x86_const: The Capstone x86 constants module.
        z3: The imported z3 module.

    Raises:
        UnsupportedSymbolicInstruction: If the operand is neither a register nor memory.
    """
    width = max(1, operand.size * 8)
    if operand.type == x86_const.X86_OP_REG:
        _write_reg(state, engine.reg_name(operand.reg), value, architecture, z3)
        return
    if operand.type == x86_const.X86_OP_MEM:
        address = _memory_address(instruction, operand, state, architecture, engine, z3)
        _write_memory(state, address, width, value, z3)
        return
    raise UnsupportedSymbolicInstruction("destination operand is not writable")


def _coerce_pair(left: Any, right: Any, z3: Any) -> tuple[Any, Any]:
    """Zero-extend two bit-vectors to their common maximum width.

    Args:
        left: The first bit-vector expression.
        right: The second bit-vector expression.
        z3: The imported z3 module.

    Returns:
        The ``(left, right)`` pair, each widened to the larger of the two widths.
    """
    width = max(left.size(), right.size())
    if left.size() < width:
        left = z3.ZeroExt(width - left.size(), left)
    if right.size() < width:
        right = z3.ZeroExt(width - right.size(), right)
    return left, right


def _set_logic_flags(state: SymState, result: Any, z3: Any) -> None:
    """Set ZF, SF, CF, and OF for a logical (bitwise) result.

    CF and OF are cleared per x86 logical-instruction semantics; ZF and SF are
    derived from ``result``.

    Args:
        state: The symbolic state whose flags are updated.
        result: The operation result bit-vector.
        z3: The imported z3 module.
    """
    state.flags["zf"] = result == 0
    state.flags["sf"] = z3.Extract(result.size() - 1, result.size() - 1, result) == 1
    state.flags["cf"] = z3.BoolVal(False)
    state.flags["of"] = z3.BoolVal(False)


def _set_add_flags(state: SymState, left: Any, right: Any, result: Any, z3: Any) -> None:
    """Set ZF, SF, CF, and OF for an addition result.

    Args:
        state: The symbolic state whose flags are updated.
        left: The left addend bit-vector.
        right: The right addend bit-vector.
        result: The addition result bit-vector.
        z3: The imported z3 module.
    """
    left, right = _coerce_pair(left, right, z3)
    result = z3.Extract(left.size() - 1, 0, result)
    state.flags["zf"] = result == 0
    state.flags["sf"] = z3.Extract(left.size() - 1, left.size() - 1, result) == 1
    state.flags["cf"] = z3.ULT(result, left)
    sign_left = z3.Extract(left.size() - 1, left.size() - 1, left)
    sign_right = z3.Extract(right.size() - 1, right.size() - 1, right)
    sign_result = z3.Extract(result.size() - 1, result.size() - 1, result)
    state.flags["of"] = z3.And(sign_left == sign_right, sign_result != sign_left)


def _set_sub_flags(state: SymState, left: Any, right: Any, result: Any, z3: Any) -> None:
    """Set ZF, SF, CF, and OF for a subtraction result.

    Args:
        state: The symbolic state whose flags are updated.
        left: The minuend bit-vector.
        right: The subtrahend bit-vector.
        result: The subtraction result bit-vector.
        z3: The imported z3 module.
    """
    left, right = _coerce_pair(left, right, z3)
    result = z3.Extract(left.size() - 1, 0, result)
    state.flags["zf"] = result == 0
    state.flags["sf"] = z3.Extract(left.size() - 1, left.size() - 1, result) == 1
    state.flags["cf"] = z3.ULT(left, right)
    sign_left = z3.Extract(left.size() - 1, left.size() - 1, left)
    sign_right = z3.Extract(right.size() - 1, right.size() - 1, right)
    sign_result = z3.Extract(result.size() - 1, result.size() - 1, result)
    state.flags["of"] = z3.And(sign_left != sign_right, sign_result != sign_left)


def _condition(mnemonic: str, flags: dict[str, Any], z3: Any) -> Any:
    """Map a Jcc mnemonic to the boolean condition over the current flags.

    Args:
        mnemonic: A conditional-jump mnemonic such as ``je`` or ``jl``.
        flags: The current flag expressions; must define ZF, SF, CF, and OF.
        z3: The imported z3 module.

    Returns:
        A z3 boolean expression that is true when the branch is taken.

    Raises:
        UnsupportedSymbolicInstruction: If required flags are missing or the mnemonic
            is not a supported conditional branch.
    """
    required = {"zf", "sf", "cf", "of"}
    if not required.issubset(flags):
        raise UnsupportedSymbolicInstruction(f"{mnemonic} depends on flags not established by the model")
    zf, sf, cf, of = flags["zf"], flags["sf"], flags["cf"], flags["of"]
    mapping = {
        "je": zf, "jz": zf, "jne": z3.Not(zf), "jnz": z3.Not(zf),
        "jb": cf, "jc": cf, "jnae": cf, "jae": z3.Not(cf), "jnb": z3.Not(cf), "jnc": z3.Not(cf),
        "jbe": z3.Or(cf, zf), "jna": z3.Or(cf, zf), "ja": z3.And(z3.Not(cf), z3.Not(zf)), "jnbe": z3.And(z3.Not(cf), z3.Not(zf)),
        "jl": sf != of, "jnge": sf != of, "jge": sf == of, "jnl": sf == of,
        "jle": z3.Or(zf, sf != of), "jng": z3.Or(zf, sf != of),
        "jg": z3.And(z3.Not(zf), sf == of), "jnle": z3.And(z3.Not(zf), sf == of),
        "js": sf, "jns": z3.Not(sf), "jo": of, "jno": z3.Not(of),
    }
    if mnemonic not in mapping:
        raise UnsupportedSymbolicInstruction(f"unsupported conditional branch {mnemonic}")
    return mapping[mnemonic]


def _condition_for_family(mnemonic: str, flags: dict[str, Any], z3: Any) -> Any:
    """Resolve Jcc, SETcc, and CMOVcc names through the same flag model."""
    lower = mnemonic.lower()
    if lower.startswith("cmov"):
        suffix = lower[4:]
    elif lower.startswith("set"):
        suffix = lower[3:]
    elif lower.startswith("j"):
        suffix = lower[1:]
    else:
        raise UnsupportedSymbolicInstruction(f"not a conditional instruction: {mnemonic}")
    suffix_aliases = {
        "e": "e", "z": "z", "ne": "ne", "nz": "nz",
        "b": "b", "c": "c", "nae": "nae", "ae": "ae", "nb": "nb", "nc": "nc",
        "be": "be", "na": "na", "a": "a", "nbe": "nbe",
        "l": "l", "nge": "nge", "ge": "ge", "nl": "nl",
        "le": "le", "ng": "ng", "g": "g", "nle": "nle",
        "s": "s", "ns": "ns", "o": "o", "no": "no",
    }
    if suffix not in suffix_aliases:
        raise UnsupportedSymbolicInstruction(f"unsupported condition code {mnemonic}")
    return _condition("j" + suffix_aliases[suffix], flags, z3)


def _set_adc_flags(state: SymState, left: Any, right: Any, carry: Any, result: Any, z3: Any) -> None:
    """Set ZF, SF, CF, and OF for an add-with-carry result.

    Args:
        state: The symbolic state whose flags are updated.
        left: The left addend bit-vector.
        right: The right addend bit-vector.
        carry: The incoming carry as a boolean expression.
        result: The add-with-carry result bit-vector.
        z3: The imported z3 module.
    """
    left, right = _coerce_pair(left, right, z3)
    width = left.size()
    carry_bv = z3.If(carry, z3.BitVecVal(1, width), z3.BitVecVal(0, width))
    extended = z3.ZeroExt(1, left) + z3.ZeroExt(1, right) + z3.ZeroExt(1, carry_bv)
    truncated = z3.Extract(width - 1, 0, result)
    state.flags["zf"] = truncated == 0
    state.flags["sf"] = z3.Extract(width - 1, width - 1, truncated) == 1
    state.flags["cf"] = z3.Extract(width, width, extended) == 1
    sign_left = z3.Extract(width - 1, width - 1, left)
    effective_right = right + carry_bv
    sign_right = z3.Extract(width - 1, width - 1, effective_right)
    sign_result = z3.Extract(width - 1, width - 1, truncated)
    state.flags["of"] = z3.And(sign_left == sign_right, sign_result != sign_left)


def _set_sbb_flags(state: SymState, left: Any, right: Any, borrow: Any, result: Any, z3: Any) -> None:
    """Set ZF, SF, CF, and OF for a subtract-with-borrow result.

    Args:
        state: The symbolic state whose flags are updated.
        left: The minuend bit-vector.
        right: The subtrahend bit-vector.
        borrow: The incoming borrow as a boolean expression.
        result: The subtract-with-borrow result bit-vector.
        z3: The imported z3 module.
    """
    left, right = _coerce_pair(left, right, z3)
    width = left.size()
    borrow_bv = z3.If(borrow, z3.BitVecVal(1, width), z3.BitVecVal(0, width))
    effective_right = right + borrow_bv
    truncated = z3.Extract(width - 1, 0, result)
    state.flags["zf"] = truncated == 0
    state.flags["sf"] = z3.Extract(width - 1, width - 1, truncated) == 1
    state.flags["cf"] = z3.ULT(left, effective_right)
    sign_left = z3.Extract(width - 1, width - 1, left)
    sign_right = z3.Extract(width - 1, width - 1, effective_right)
    sign_result = z3.Extract(width - 1, width - 1, truncated)
    state.flags["of"] = z3.And(sign_left != sign_right, sign_result != sign_left)


def _is_sat(constraints: list[Any], z3: Any) -> bool:
    """Return whether a conjunction of constraints is satisfiable.

    Args:
        constraints: The z3 boolean constraints to check.
        z3: The imported z3 module.

    Returns:
        ``True`` if the solver reports the constraints as satisfiable.
    """
    solver = z3.Solver()
    solver.add(*constraints)
    return solver.check() == z3.sat


def symbolic_execute(
    code: bytes,
    *,
    architecture: str = "x86",
    base_address: int = 0x100000,
    input_registers: tuple[str, ...] = (),
    stack_argument_words: int = 0,
    output_registers: tuple[str, ...] | None = None,
    max_steps: int = 1000,
    max_paths: int = 64,
) -> tuple[list[Outcome], dict[str, Any]]:
    """Symbolically execute a leaf function and enumerate its bounded outcomes.

    Decodes ``code`` with Capstone, seeds symbolic inputs, and explores paths depth-first
    up to the configured step and path limits, collecting an outcome per encountered
    ``ret``.

    Args:
        code: The raw machine-code bytes of a single function.
        architecture: Either ``"x86"`` or ``"x86_64"``.
        base_address: The address at which ``code`` is loaded.
        input_registers: Register names to seed with fresh symbolic inputs.
        stack_argument_words: Number of pointer-sized stack argument words to make symbolic.
        output_registers: Registers to capture as outputs; defaults to the return register.
        max_steps: Maximum instructions executed per path.
        max_paths: Maximum number of explored paths.

    Returns:
        A ``(outcomes, metadata)`` tuple, where ``metadata`` records instruction and
        outcome counts, explored-state count, unsupported sites, and the architecture.

    Raises:
        ContractError: If the architecture or bounds are invalid, or a step or path
            limit is exceeded.
        UnsupportedSymbolicInstruction: If decoding is incomplete or an unsupported
            instruction, operand, or control-flow target is reached.
    """
    if architecture not in ("x86", "x86_64"):
        raise ContractError("symbolic architecture must be x86 or x86_64")
    if max_steps <= 0 or max_paths <= 0 or stack_argument_words < 0:
        raise ContractError("symbolic bounds must be positive and stack_argument_words non-negative")
    capstone, x86_const, z3 = _deps()
    mode = capstone.CS_MODE_32 if architecture == "x86" else capstone.CS_MODE_64
    engine = capstone.Cs(capstone.CS_ARCH_X86, mode)
    engine.detail = True
    instructions = list(engine.disasm(code, base_address))
    if sum(instruction.size for instruction in instructions) != len(code):
        raise UnsupportedSymbolicInstruction("code contains bytes Capstone did not decode")
    by_address = {instruction.address: instruction for instruction in instructions}
    width = 32 if architecture == "x86" else 64
    pointer_size = width // 8
    canonical_registers = sorted({canonical for canonical, _low, _width in _aliases(architecture).values()})
    regs = {name: z3.BitVecVal(0, width) for name in canonical_registers}
    for name in input_registers:
        canonical, _low, _reg_width = _aliases(architecture).get(name, (None, None, None))
        if canonical is None:
            raise ContractError(f"unsupported symbolic input register {name}")
        regs[canonical] = z3.BitVec(f"input_{canonical}", width)
    sp_name = "esp" if architecture == "x86" else "rsp"
    bp_name = "ebp" if architecture == "x86" else "rbp"
    return_name = "eax" if architecture == "x86" else "rax"
    stack_base = 0x70000000 if architecture == "x86" else 0x700000000000
    regs[sp_name] = z3.BitVecVal(stack_base, width)
    regs[bp_name] = z3.BitVecVal(0, width)
    memory: dict[int, Any] = {}
    for index in range(pointer_size):
        memory[stack_base + index] = z3.BitVecVal(0, 8)  # concrete return sentinel
    for word_index in range(stack_argument_words):
        symbol = z3.BitVec(f"stack_arg_{word_index}", width)
        for byte_index in range(pointer_size):
            memory[stack_base + pointer_size + word_index * pointer_size + byte_index] = z3.Extract(
                byte_index * 8 + 7, byte_index * 8, symbol
            )
    initial_sp = regs[sp_name]
    queue = [SymState(pc=base_address, regs=regs, memory=memory)]
    outcomes: list[Outcome] = []
    unsupported: list[str] = []
    explored_states = 0
    selected_outputs = output_registers or (return_name,)

    while queue:
        if explored_states >= max_paths:
            raise ContractError(f"symbolic path limit exceeded ({max_paths})")
        state = queue.pop()
        explored_states += 1
        while True:
            if state.steps >= max_steps:
                raise ContractError(f"symbolic step limit exceeded ({max_steps})")
            instruction = by_address.get(state.pc)
            if instruction is None:
                raise UnsupportedSymbolicInstruction(f"control flow reached unmapped address 0x{state.pc:x}")
            state.steps += 1
            mnemonic = instruction.mnemonic.lower()
            operands = instruction.operands
            next_pc = instruction.address + instruction.size
            try:
                if mnemonic in ("nop", "endbr32", "endbr64"):
                    state.pc = next_pc
                elif mnemonic == "mov":
                    value = _read_operand(instruction, operands[1], state, architecture, engine, x86_const, z3)
                    _write_operand(instruction, operands[0], value, state, architecture, engine, x86_const, z3)
                    state.pc = next_pc
                elif mnemonic in ("movzx", "movsx", "movsxd"):
                    source = _read_operand(instruction, operands[1], state, architecture, engine, x86_const, z3)
                    destination_width = operands[0].size * 8
                    extension = destination_width - source.size()
                    value = z3.SignExt(extension, source) if mnemonic in ("movsx", "movsxd") else z3.ZeroExt(extension, source)
                    _write_operand(instruction, operands[0], value, state, architecture, engine, x86_const, z3)
                    state.pc = next_pc
                elif mnemonic == "lea":
                    if operands[1].type != x86_const.X86_OP_MEM:
                        raise UnsupportedSymbolicInstruction("lea source is not memory")
                    address = _memory_address(instruction, operands[1], state, architecture, engine, z3)
                    value = z3.BitVecVal(address, operands[0].size * 8)
                    _write_operand(instruction, operands[0], value, state, architecture, engine, x86_const, z3)
                    state.pc = next_pc
                elif mnemonic in ("add", "adc", "sub", "sbb", "xor", "and", "or"):
                    left = _read_operand(instruction, operands[0], state, architecture, engine, x86_const, z3)
                    right = _read_operand(instruction, operands[1], state, architecture, engine, x86_const, z3)
                    left, right = _coerce_pair(left, right, z3)
                    if mnemonic == "add":
                        result = left + right
                        _set_add_flags(state, left, right, result, z3)
                    elif mnemonic == "adc":
                        if "cf" not in state.flags:
                            raise UnsupportedSymbolicInstruction("adc depends on carry flag not established by the model")
                        carry_bv = z3.If(state.flags["cf"], z3.BitVecVal(1, left.size()), z3.BitVecVal(0, left.size()))
                        result = left + right + carry_bv
                        _set_adc_flags(state, left, right, state.flags["cf"], result, z3)
                    elif mnemonic == "sub":
                        result = left - right
                        _set_sub_flags(state, left, right, result, z3)
                    elif mnemonic == "sbb":
                        if "cf" not in state.flags:
                            raise UnsupportedSymbolicInstruction("sbb depends on carry flag not established by the model")
                        borrow_bv = z3.If(state.flags["cf"], z3.BitVecVal(1, left.size()), z3.BitVecVal(0, left.size()))
                        result = left - right - borrow_bv
                        _set_sbb_flags(state, left, right, state.flags["cf"], result, z3)
                    elif mnemonic == "xor":
                        result = left ^ right
                        _set_logic_flags(state, result, z3)
                    elif mnemonic == "and":
                        result = left & right
                        _set_logic_flags(state, result, z3)
                    else:
                        result = left | right
                        _set_logic_flags(state, result, z3)
                    _write_operand(instruction, operands[0], result, state, architecture, engine, x86_const, z3)
                    state.pc = next_pc
                elif mnemonic in ("inc", "dec", "neg", "not"):
                    value = _read_operand(instruction, operands[0], state, architecture, engine, x86_const, z3)
                    if mnemonic == "inc":
                        result = value + 1
                        old_cf = state.flags.get("cf")
                        _set_add_flags(state, value, z3.BitVecVal(1, value.size()), result, z3)
                        if old_cf is not None:
                            state.flags["cf"] = old_cf
                    elif mnemonic == "dec":
                        result = value - 1
                        old_cf = state.flags.get("cf")
                        _set_sub_flags(state, value, z3.BitVecVal(1, value.size()), result, z3)
                        if old_cf is not None:
                            state.flags["cf"] = old_cf
                    elif mnemonic == "neg":
                        result = -value
                        _set_sub_flags(state, z3.BitVecVal(0, value.size()), value, result, z3)
                    else:
                        result = ~value
                    _write_operand(instruction, operands[0], result, state, architecture, engine, x86_const, z3)
                    state.pc = next_pc
                elif mnemonic in ("shl", "sal", "shr", "sar"):
                    value = _read_operand(instruction, operands[0], state, architecture, engine, x86_const, z3)
                    count = _read_operand(instruction, operands[1], state, architecture, engine, x86_const, z3)
                    count = z3.ZeroExt(max(0, value.size() - count.size()), count)
                    if mnemonic in ("shl", "sal"):
                        result = value << count
                    elif mnemonic == "shr":
                        result = z3.LShR(value, count)
                    else:
                        result = value >> count
                    _set_logic_flags(state, result, z3)
                    _write_operand(instruction, operands[0], result, state, architecture, engine, x86_const, z3)
                    state.pc = next_pc
                elif mnemonic == "imul" and len(operands) in (2, 3):
                    if len(operands) == 2:
                        left = _read_operand(instruction, operands[0], state, architecture, engine, x86_const, z3)
                        right = _read_operand(instruction, operands[1], state, architecture, engine, x86_const, z3)
                    else:
                        left = _read_operand(instruction, operands[1], state, architecture, engine, x86_const, z3)
                        right = _read_operand(instruction, operands[2], state, architecture, engine, x86_const, z3)
                    left, right = _coerce_pair(left, right, z3)
                    result = left * right
                    _write_operand(instruction, operands[0], result, state, architecture, engine, x86_const, z3)
                    state.pc = next_pc
                elif mnemonic in ("clc", "stc", "cmc"):
                    if mnemonic == "clc":
                        state.flags["cf"] = z3.BoolVal(False)
                    elif mnemonic == "stc":
                        state.flags["cf"] = z3.BoolVal(True)
                    else:
                        if "cf" not in state.flags:
                            raise UnsupportedSymbolicInstruction("cmc depends on carry flag not established by the model")
                        state.flags["cf"] = z3.Not(state.flags["cf"])
                    state.pc = next_pc
                elif mnemonic.startswith("set"):
                    if len(operands) != 1:
                        raise UnsupportedSymbolicInstruction("setcc requires one destination operand")
                    condition = _condition_for_family(mnemonic, state.flags, z3)
                    width = max(1, operands[0].size * 8)
                    value = z3.If(condition, z3.BitVecVal(1, width), z3.BitVecVal(0, width))
                    _write_operand(instruction, operands[0], value, state, architecture, engine, x86_const, z3)
                    state.pc = next_pc
                elif mnemonic.startswith("cmov"):
                    if len(operands) != 2:
                        raise UnsupportedSymbolicInstruction("cmovcc requires destination and source operands")
                    condition = _condition_for_family(mnemonic, state.flags, z3)
                    old_value = _read_operand(instruction, operands[0], state, architecture, engine, x86_const, z3)
                    new_value = _read_operand(instruction, operands[1], state, architecture, engine, x86_const, z3)
                    old_value, new_value = _coerce_pair(old_value, new_value, z3)
                    _write_operand(instruction, operands[0], z3.If(condition, new_value, old_value), state, architecture, engine, x86_const, z3)
                    state.pc = next_pc
                elif mnemonic in ("cmp", "test"):
                    left = _read_operand(instruction, operands[0], state, architecture, engine, x86_const, z3)
                    right = _read_operand(instruction, operands[1], state, architecture, engine, x86_const, z3)
                    left, right = _coerce_pair(left, right, z3)
                    if mnemonic == "cmp":
                        _set_sub_flags(state, left, right, left - right, z3)
                    else:
                        _set_logic_flags(state, left & right, z3)
                    state.pc = next_pc
                elif mnemonic == "push":
                    value = _read_operand(instruction, operands[0], state, architecture, engine, x86_const, z3)
                    sp = _read_reg(state, sp_name, architecture, z3) - pointer_size
                    _write_reg(state, sp_name, sp, architecture, z3)
                    address = _concrete(sp, z3)
                    if address is None:
                        raise UnsupportedSymbolicInstruction("symbolic stack pointer")
                    _write_memory(state, address, pointer_size * 8, value, z3)
                    state.pc = next_pc
                elif mnemonic == "pop":
                    sp = _read_reg(state, sp_name, architecture, z3)
                    address = _concrete(sp, z3)
                    if address is None:
                        raise UnsupportedSymbolicInstruction("symbolic stack pointer")
                    value = _read_memory(state, address, pointer_size * 8, z3)
                    _write_operand(instruction, operands[0], value, state, architecture, engine, x86_const, z3)
                    _write_reg(state, sp_name, sp + pointer_size, architecture, z3)
                    state.pc = next_pc
                elif mnemonic == "leave":
                    bp = _read_reg(state, bp_name, architecture, z3)
                    _write_reg(state, sp_name, bp, architecture, z3)
                    address = _concrete(bp, z3)
                    if address is None:
                        raise UnsupportedSymbolicInstruction("symbolic frame pointer")
                    value = _read_memory(state, address, pointer_size * 8, z3)
                    _write_reg(state, bp_name, value, architecture, z3)
                    _write_reg(state, sp_name, bp + pointer_size, architecture, z3)
                    state.pc = next_pc
                elif mnemonic == "jmp":
                    if not operands or operands[0].type != x86_const.X86_OP_IMM:
                        raise UnsupportedSymbolicInstruction("indirect jmp is outside the bounded model")
                    state.pc = int(operands[0].imm)
                elif mnemonic.startswith("j"):
                    if not operands or operands[0].type != x86_const.X86_OP_IMM:
                        raise UnsupportedSymbolicInstruction("indirect conditional branch")
                    condition = _condition_for_family(mnemonic, state.flags, z3)
                    taken = state.clone()
                    taken.constraints.append(condition)
                    taken.pc = int(operands[0].imm)
                    not_taken = state.clone()
                    not_taken.constraints.append(z3.Not(condition))
                    not_taken.pc = next_pc
                    if _is_sat(not_taken.constraints, z3):
                        queue.append(not_taken)
                    if _is_sat(taken.constraints, z3):
                        state = taken
                        continue
                    break
                elif mnemonic == "ret":
                    sp = _read_reg(state, sp_name, architecture, z3)
                    increment = pointer_size
                    if operands:
                        immediate = _read_operand(instruction, operands[0], state, architecture, engine, x86_const, z3)
                        concrete = _concrete(immediate, z3)
                        if concrete is None:
                            raise UnsupportedSymbolicInstruction("symbolic ret immediate")
                        increment += concrete
                    final_sp = sp + increment
                    outputs = {name: _read_reg(state, name, architecture, z3) for name in selected_outputs}
                    outcomes.append(
                        Outcome(
                            constraints=tuple(state.constraints),
                            outputs=outputs,
                            stack_delta=z3.simplify(final_sp - initial_sp),
                        )
                    )
                    break
                else:
                    raise UnsupportedSymbolicInstruction(f"unsupported instruction: {instruction.mnemonic} {instruction.op_str}")
            except UnsupportedSymbolicInstruction as exc:
                unsupported.append(f"0x{instruction.address:x}: {exc}")
                raise
    metadata = {
        "instruction_count": len(instructions),
        "explored_states": explored_states,
        "outcome_count": len(outcomes),
        "unsupported": unsupported,
        "architecture": architecture,
    }
    return outcomes, metadata


def _constraint_formula(outcome: Outcome, z3: Any) -> Any:
    """Return the conjunction of an outcome's path constraints.

    Args:
        outcome: The outcome whose constraints are combined.
        z3: The imported z3 module.

    Returns:
        A z3 boolean expression, or ``BoolVal(True)`` when there are no constraints.
    """
    return z3.And(*outcome.constraints) if outcome.constraints else z3.BoolVal(True)


def bounded_symbolic_compare(
    target: bytes,
    candidate: bytes,
    *,
    architecture: str = "x86",
    input_registers: tuple[str, ...] = (),
    stack_argument_words: int = 0,
    output_registers: tuple[str, ...] | None = None,
    max_steps: int = 1000,
    max_paths: int = 64,
    report_path: Path | None = None,
) -> dict[str, Any]:
    """Compare two functions for bounded symbolic equivalence and build a report.

    Both inputs are symbolically executed, then a solver searches for an input under
    which their reachable path domains diverge or a shared path produces differing
    outputs or stack deltas. UNSAT establishes equality only within the modeled scope.

    Args:
        target: Machine-code bytes of the reference function.
        candidate: Machine-code bytes of the function under test.
        architecture: Either ``"x86"`` or ``"x86_64"``.
        input_registers: Register names to seed with fresh symbolic inputs.
        stack_argument_words: Number of pointer-sized stack argument words to make symbolic.
        output_registers: Registers to compare; defaults to the return register.
        max_steps: Maximum instructions executed per path.
        max_paths: Maximum number of explored paths.
        report_path: Optional path to write the JSON report to.

    Returns:
        A report dict including the solver result, an ``equivalent_within_model`` flag,
        any counterexample, per-input metadata, and an explicit scope statement.
    """
    _capstone, _x86_const, z3 = _deps()
    target_outcomes, target_meta = symbolic_execute(
        target,
        architecture=architecture,
        base_address=0x100000,
        input_registers=input_registers,
        stack_argument_words=stack_argument_words,
        output_registers=output_registers,
        max_steps=max_steps,
        max_paths=max_paths,
    )
    candidate_outcomes, candidate_meta = symbolic_execute(
        candidate,
        architecture=architecture,
        base_address=0x200000,
        input_registers=input_registers,
        stack_argument_words=stack_argument_words,
        output_registers=output_registers,
        max_steps=max_steps,
        max_paths=max_paths,
    )
    solver = z3.Solver()
    target_domain = z3.Or(*[_constraint_formula(outcome, z3) for outcome in target_outcomes])
    candidate_domain = z3.Or(*[_constraint_formula(outcome, z3) for outcome in candidate_outcomes])
    mismatch_terms: list[Any] = [z3.Xor(target_domain, candidate_domain)]
    for target_outcome in target_outcomes:
        for candidate_outcome in candidate_outcomes:
            overlap = z3.And(_constraint_formula(target_outcome, z3), _constraint_formula(candidate_outcome, z3))
            differences = [target_outcome.stack_delta != candidate_outcome.stack_delta]
            for name in sorted(set(target_outcome.outputs) | set(candidate_outcome.outputs)):
                if name not in target_outcome.outputs or name not in candidate_outcome.outputs:
                    differences.append(z3.BoolVal(True))
                else:
                    differences.append(target_outcome.outputs[name] != candidate_outcome.outputs[name])
            mismatch_terms.append(z3.And(overlap, z3.Or(*differences)))
    solver.add(z3.Or(*mismatch_terms))
    check = solver.check()
    counterexample: dict[str, str] | None = None
    if check == z3.sat:
        model = solver.model()
        counterexample = {str(declaration): str(model[declaration]) for declaration in model.decls()}
    equivalent = check == z3.unsat
    report = {
        "schema_version": 1,
        "created_at": utc_now(),
        "kind": "bounded_symbolic_equivalence",
        "architecture": architecture,
        "target_sha256": sha256_bytes(target),
        "candidate_sha256": sha256_bytes(candidate),
        "input_registers": list(input_registers),
        "stack_argument_words": stack_argument_words,
        "output_registers": list(output_registers or (("eax",) if architecture == "x86" else ("rax",))),
        "max_steps": max_steps,
        "max_paths": max_paths,
        "solver_result": str(check),
        "equivalent_within_model": equivalent,
        "counterexample": counterexample,
        "target": target_meta,
        "candidate": candidate_meta,
        "semantic_equivalence_claimed": False,
        "scope_statement": "UNSAT proves equality only for supported instructions, concrete stack addressing, configured symbolic inputs, selected outputs, and stated path/step bounds.",
    }
    if report_path is not None:
        write_json(report_path, report)
    return report


def bounded_symbolic_compare_files(
    target_path: Path,
    candidate_path: Path,
    **kwargs: Any,
) -> dict[str, Any]:
    """Load two code files and run :func:`bounded_symbolic_compare` on their bytes.

    Args:
        target_path: Path to the reference function's machine-code bytes.
        candidate_path: Path to the candidate function's machine-code bytes.
        **kwargs: Additional keyword arguments forwarded to
            :func:`bounded_symbolic_compare`.

    Returns:
        The bounded symbolic equivalence report dict.

    Raises:
        ContractError: If either path does not refer to an existing file.
    """
    if not target_path.is_file() or not candidate_path.is_file():
        raise ContractError("target and candidate code files must exist")
    return bounded_symbolic_compare(target_path.read_bytes(), candidate_path.read_bytes(), **kwargs)
