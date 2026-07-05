"""Optional angr comparative symbolic execution backend for bounded code blobs.

The built-in symbolic engine remains the default deterministic backend. This
module integrates angr when installed and performs finite path comparison over
explicit input/output registers and stack arguments. Results are scoped to the
selected architecture, code blobs, path/step limits, and observable registers.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .errors import ContractError, ExternalToolError
from .util import sha256_bytes, utc_now, write_json


def _load_angr() -> tuple[Any, Any]:
    """Load angr.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    try:
        import angr  # type: ignore[import-not-found]
        import claripy  # type: ignore[import-not-found]
    except ImportError as exc:
        raise ExternalToolError("angr backend requires the optional 'angr' dependency") from exc
    return angr, claripy


def _arch_name(architecture: str) -> str:
    """Implement arch name.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if architecture == "x86":
        return "x86"
    if architecture == "x86_64":
        return "amd64"
    raise ContractError("architecture must be x86 or x86_64")


def _summaries(
    code: bytes,
    *,
    architecture: str,
    input_registers: tuple[str, ...],
    stack_argument_words: int,
    output_registers: tuple[str, ...],
    max_steps: int,
    max_paths: int,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Implement summaries.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    angr, claripy = _load_angr()
    if not code:
        raise ContractError("symbolic code blob may not be empty")
    if max_steps <= 0 or max_paths <= 0:
        raise ContractError("max_steps and max_paths must be positive")
    arch = _arch_name(architecture)
    bits = 32 if architecture == "x86" else 64
    byte_width = bits // 8
    base = 0x100000
    sentinel = 0x200000
    stack = 0x7FFF0000 if architecture == "x86" else 0x7FFF00000000
    project = angr.load_shellcode(code, arch=arch, load_address=base)
    state = project.factory.blank_state(addr=base)
    stack_reg = "esp" if architecture == "x86" else "rsp"
    state.registers.store(stack_reg, claripy.BVV(stack, bits))
    state.memory.store(stack, claripy.BVV(sentinel, bits), endness=project.arch.memory_endness)
    inputs: dict[str, Any] = {}
    for register in input_registers:
        if not hasattr(state.regs, register):
            raise ContractError(f"angr architecture has no register {register}")
        symbol = claripy.BVS(f"reg_{register}", bits, explicit_name=True)
        state.registers.store(register, symbol)
        inputs[f"register:{register}"] = symbol
    for index in range(stack_argument_words):
        symbol = claripy.BVS(f"stack_arg_{index}", bits, explicit_name=True)
        state.memory.store(stack + byte_width * (index + 1), symbol, endness=project.arch.memory_endness)
        inputs[f"stack:{index}"] = symbol
    manager = project.factory.simulation_manager(state)
    finals: list[Any] = []
    steps = 0
    truncated = False
    while manager.active and steps < max_steps:
        arrived = [candidate for candidate in manager.active if candidate.addr == sentinel]
        if arrived:
            finals.extend(arrived)
            manager.active = [candidate for candidate in manager.active if candidate.addr != sentinel]
        if not manager.active:
            break
        if len(manager.active) > max_paths:
            manager.active = manager.active[:max_paths]
            truncated = True
        manager.step()
        steps += 1
    finals.extend(candidate for candidate in manager.active if candidate.addr == sentinel)
    if manager.active and steps >= max_steps:
        truncated = True
    summaries: list[dict[str, Any]] = []
    for final in finals[:max_paths]:
        outputs = {}
        for register in output_registers:
            if not hasattr(final.regs, register):
                raise ContractError(f"angr architecture has no output register {register}")
            outputs[register] = getattr(final.regs, register)
        summaries.append({"constraints": tuple(final.solver.constraints), "outputs": outputs, "inputs": inputs})
    metadata = {
        "steps": steps,
        "final_path_count": len(summaries),
        "active_path_count": len(manager.active),
        "deadended_path_count": len(manager.deadended),
        "errored_path_count": len(manager.errored),
        "truncated": truncated,
    }
    return summaries, metadata


def _counterexample(left: list[dict[str, Any]], right: list[dict[str, Any]], output_registers: tuple[str, ...]) -> dict[str, int] | None:
    """Implement counterexample.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    _, claripy = _load_angr()
    for left_path in left:
        alternatives = []
        for right_path in right:
            equal_outputs = [left_path["outputs"][reg] == right_path["outputs"][reg] for reg in output_registers]
            alternatives.append(claripy.And(*right_path["constraints"], *equal_outputs))
        mismatch = claripy.And(*left_path["constraints"], claripy.Not(claripy.Or(*alternatives)) if alternatives else claripy.true())
        solver = claripy.Solver()
        solver.add(mismatch)
        if solver.satisfiable():
            model: dict[str, int] = {}
            for name, symbol in left_path["inputs"].items():
                model[name] = int(solver.eval(symbol, 1)[0])
            return model
    return None


def angr_bounded_compare(
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
    """Implement angr bounded compare.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if stack_argument_words < 0:
        raise ContractError("stack_argument_words may not be negative")
    outputs = output_registers or (("eax",) if architecture == "x86" else ("rax",))
    target_paths, target_meta = _summaries(target, architecture=architecture, input_registers=input_registers, stack_argument_words=stack_argument_words, output_registers=outputs, max_steps=max_steps, max_paths=max_paths)
    candidate_paths, candidate_meta = _summaries(candidate, architecture=architecture, input_registers=input_registers, stack_argument_words=stack_argument_words, output_registers=outputs, max_steps=max_steps, max_paths=max_paths)
    forward = _counterexample(target_paths, candidate_paths, outputs)
    reverse = _counterexample(candidate_paths, target_paths, outputs)
    complete = bool(target_paths and candidate_paths and not target_meta["truncated"] and not candidate_meta["truncated"])
    equivalent = complete and forward is None and reverse is None
    report = {
        "schema_version": 1,
        "kind": "angr_bounded_comparison",
        "created_at": utc_now(),
        "architecture": architecture,
        "target_sha256": sha256_bytes(target),
        "candidate_sha256": sha256_bytes(candidate),
        "input_registers": list(input_registers),
        "stack_argument_words": stack_argument_words,
        "output_registers": list(outputs),
        "max_steps": max_steps,
        "max_paths": max_paths,
        "target_execution": target_meta,
        "candidate_execution": candidate_meta,
        "counterexample_target_to_candidate": forward,
        "counterexample_candidate_to_target": reverse,
        "equivalent_within_completed_model": equivalent,
        "scope_statement": "The result covers only angr paths completed within the selected blob model, observables, hooks, and finite path/step bounds; it is not universal program equivalence.",
    }
    if report_path is not None:
        write_json(report_path, report)
    return report


def angr_bounded_compare_files(target: Path, candidate: Path, **kwargs: Any) -> dict[str, Any]:
    """Implement angr bounded compare files.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    left = target.resolve()
    right = candidate.resolve()
    if not left.is_file() or not right.is_file():
        raise ContractError("angr comparison inputs must be files")
    return angr_bounded_compare(left.read_bytes(), right.read_bytes(), **kwargs)


def _load_memory_harness(path: Path) -> dict[str, Any]:
    """Load memory harness.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    from .util import load_json

    harness = load_json(path)
    if not isinstance(harness, dict):
        raise ContractError("symbolic memory harness must be an object")
    if harness.get("architecture") not in ("x86", "x86_64"):
        raise ContractError("symbolic memory harness architecture must be x86 or x86_64")
    regions = harness.get("regions")
    if not isinstance(regions, list) or not regions:
        raise ContractError("symbolic memory harness requires a non-empty regions array")
    names: set[str] = set()
    for region in regions:
        if not isinstance(region, dict):
            raise ContractError("symbolic memory regions must be objects")
        name = region.get("name")
        if not isinstance(name, str) or not name or name in names:
            raise ContractError("symbolic memory region names must be unique non-empty strings")
        names.add(name)
        if not isinstance(region.get("pointer_register"), str):
            raise ContractError(f"region {name} requires pointer_register")
        size = region.get("size")
        if not isinstance(size, int) or size <= 0 or size > 1_048_576:
            raise ContractError(f"region {name} size must be between 1 and 1048576")
    return harness


def _memory_summaries(
    code: bytes,
    *,
    harness: dict[str, Any],
    side: str,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Implement memory summaries.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    angr, claripy = _load_angr()
    architecture = str(harness["architecture"])
    arch = _arch_name(architecture)
    bits = 32 if architecture == "x86" else 64
    byte_width = bits // 8
    base = 0x100000 if side == "target" else 0x300000
    sentinel = 0x500000 if side == "target" else 0x600000
    stack = 0x70000000 if architecture == "x86" else 0x700000000000
    slot_base = 0x10000000 if architecture == "x86" else 0x1000000000
    slot_stride = int(harness.get("slot_stride", 0x10000))
    slots = int(harness.get("alias_slots", max(2, len(harness["regions"]))))
    if slots <= 0 or slots > 32 or slot_stride <= 0:
        raise ContractError("alias_slots must be 1..32 and slot_stride must be positive")
    project = angr.load_shellcode(code, arch=arch, load_address=base)
    state = project.factory.blank_state(addr=base)
    stack_reg = "esp" if architecture == "x86" else "rsp"
    setattr(state.regs, stack_reg, claripy.BVV(stack, bits))
    state.memory.store(stack, claripy.BVV(sentinel, bits), endness=project.arch.memory_endness)

    inputs: dict[str, Any] = {}
    for register in harness.get("input_registers", []):
        if not isinstance(register, str) or not hasattr(state.regs, register):
            raise ContractError(f"unsupported symbolic input register {register}")
        symbol = claripy.BVS(f"input_register_{register}", bits, explicit_name=True)
        state.registers.store(register, symbol)
        inputs[f"register:{register}"] = symbol

    region_bases: dict[str, Any] = {}
    region_sizes: dict[str, int] = {}
    for region in harness["regions"]:
        name = str(region["name"])
        pointer_register = str(region["pointer_register"])
        if not hasattr(state.regs, pointer_register):
            raise ContractError(f"architecture has no register {pointer_register}")
        size = int(region["size"])
        base_symbol = claripy.BVS(f"region_base_{name}", bits, explicit_name=True)
        allowed = [base_symbol == claripy.BVV(slot_base + index * slot_stride, bits) for index in range(slots)]
        state.solver.add(claripy.Or(*allowed))
        alignment = int(region.get("alignment", 1))
        if alignment <= 0 or alignment & (alignment - 1):
            raise ContractError(f"region {name} alignment must be a positive power of two")
        state.solver.add((base_symbol & (alignment - 1)) == 0)
        state.registers.store(pointer_register, base_symbol)
        region_bases[name] = base_symbol
        region_sizes[name] = size
        inputs[f"region_base:{name}"] = base_symbol
        initial = region.get("initial", "symbolic")
        if isinstance(initial, str) and initial not in ("symbolic", "zero"):
            try:
                initial_bytes = bytes.fromhex(initial)
            except ValueError as exc:
                raise ContractError(f"region {name} initial must be symbolic, zero, or hex") from exc
            if len(initial_bytes) != size:
                raise ContractError(f"region {name} hex initialization length does not match size")
        else:
            initial_bytes = None
        for offset in range(size):
            if initial == "zero":
                value = claripy.BVV(0, 8)
            elif initial_bytes is not None:
                value = claripy.BVV(initial_bytes[offset], 8)
            else:
                value = claripy.BVS(f"memory_{name}_{offset}", 8, explicit_name=True)
                inputs[f"memory:{name}:{offset}"] = value
            state.memory.store(base_symbol + offset, value, size=1)

    for relation in harness.get("alias_constraints", []):
        if not isinstance(relation, dict):
            raise ContractError("alias constraints must be objects")
        left_name = str(relation.get("left"))
        right_name = str(relation.get("right"))
        if left_name not in region_bases or right_name not in region_bases:
            raise ContractError("alias constraint references unknown region")
        left = region_bases[left_name]
        right = region_bases[right_name]
        kind = relation.get("relation")
        if kind == "equal":
            state.solver.add(left == right)
        elif kind == "distinct":
            state.solver.add(left != right)
        elif kind == "disjoint":
            state.solver.add(
                claripy.Or(
                    left + region_sizes[left_name] <= right,
                    right + region_sizes[right_name] <= left,
                )
            )
        elif kind == "may_alias":
            pass
        else:
            raise ContractError(f"unsupported alias relation {kind}")

    for index in range(int(harness.get("stack_argument_words", 0))):
        symbol = claripy.BVS(f"stack_arg_{index}", bits, explicit_name=True)
        state.memory.store(stack + byte_width * (index + 1), symbol, endness=project.arch.memory_endness)
        inputs[f"stack:{index}"] = symbol

    max_steps = int(harness.get("max_steps", 1000))
    max_paths = int(harness.get("max_paths", 64))
    if max_steps <= 0 or max_paths <= 0:
        raise ContractError("symbolic bounds must be positive")
    manager = project.factory.simulation_manager(state)
    finals: list[Any] = []
    steps = 0
    truncated = False
    while manager.active and steps < max_steps:
        arrived = [candidate for candidate in manager.active if candidate.addr == sentinel]
        if arrived:
            finals.extend(arrived)
            manager.active = [candidate for candidate in manager.active if candidate.addr != sentinel]
        if not manager.active:
            break
        if len(manager.active) > max_paths:
            manager.active = manager.active[:max_paths]
            truncated = True
        manager.step()
        steps += 1
    finals.extend(candidate for candidate in manager.active if candidate.addr == sentinel)
    if manager.active and steps >= max_steps:
        truncated = True

    output_registers = tuple(harness.get("output_registers", ["eax" if architecture == "x86" else "rax"]))
    observations = harness.get("observe_memory", [])
    summaries: list[dict[str, Any]] = []
    for final in finals[:max_paths]:
        outputs: dict[str, Any] = {}
        for register in output_registers:
            if not isinstance(register, str) or not hasattr(final.regs, register):
                raise ContractError(f"architecture has no output register {register}")
            outputs[f"register:{register}"] = getattr(final.regs, register)
        for observation in observations:
            if not isinstance(observation, dict):
                raise ContractError("observe_memory entries must be objects")
            region_name = str(observation.get("region"))
            if region_name not in region_bases:
                raise ContractError(f"memory observation references unknown region {region_name}")
            offset = int(observation.get("offset", 0))
            size = int(observation.get("size", region_sizes[region_name]))
            if offset < 0 or size <= 0 or offset + size > region_sizes[region_name]:
                raise ContractError(f"memory observation outside region {region_name}")
            outputs[f"memory:{region_name}:{offset}:{size}"] = final.memory.load(
                region_bases[region_name] + offset,
                size,
                endness=project.arch.memory_endness,
            )
        summaries.append(
            {"constraints": tuple(final.solver.constraints), "outputs": outputs, "inputs": inputs}
        )
    metadata = {
        "steps": steps,
        "final_path_count": len(summaries),
        "active_path_count": len(manager.active),
        "deadended_path_count": len(manager.deadended),
        "errored_path_count": len(manager.errored),
        "truncated": truncated,
        "region_count": len(region_bases),
        "alias_slots": slots,
    }
    return summaries, metadata


def _memory_counterexample(
    left: list[dict[str, Any]], right: list[dict[str, Any]]
) -> dict[str, int] | None:
    """Implement memory counterexample.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    _angr, claripy = _load_angr()
    for left_path in left:
        alternatives = []
        for right_path in right:
            names = sorted(set(left_path["outputs"]) | set(right_path["outputs"]))
            equal_outputs = []
            for name in names:
                if name not in left_path["outputs"] or name not in right_path["outputs"]:
                    equal_outputs.append(claripy.false())
                else:
                    equal_outputs.append(left_path["outputs"][name] == right_path["outputs"][name])
            alternatives.append(claripy.And(*right_path["constraints"], *equal_outputs))
        mismatch = claripy.And(
            *left_path["constraints"],
            claripy.Not(claripy.Or(*alternatives)) if alternatives else claripy.true(),
        )
        solver = claripy.Solver()
        solver.add(mismatch)
        if solver.satisfiable():
            model: dict[str, int] = {}
            for name, symbol in left_path["inputs"].items():
                model[name] = int(solver.eval(symbol, 1)[0])
            return model
    return None


def angr_memory_alias_compare(
    target: bytes,
    candidate: bytes,
    harness: dict[str, Any],
    *,
    report_path: Path | None = None,
) -> dict[str, Any]:
    """Implement angr memory alias compare.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    target_paths, target_meta = _memory_summaries(target, harness=harness, side="target")
    candidate_paths, candidate_meta = _memory_summaries(candidate, harness=harness, side="candidate")
    forward = _memory_counterexample(target_paths, candidate_paths)
    reverse = _memory_counterexample(candidate_paths, target_paths)
    complete = bool(
        target_paths
        and candidate_paths
        and not target_meta["truncated"]
        and not candidate_meta["truncated"]
    )
    report = {
        "schema_version": 1,
        "kind": "angr_memory_alias_comparison",
        "created_at": utc_now(),
        "architecture": harness["architecture"],
        "target_sha256": sha256_bytes(target),
        "candidate_sha256": sha256_bytes(candidate),
        "harness": harness,
        "target_execution": target_meta,
        "candidate_execution": candidate_meta,
        "counterexample_target_to_candidate": forward,
        "counterexample_candidate_to_target": reverse,
        "equivalent_within_completed_model": complete and forward is None and reverse is None,
        "scope_statement": "The result models symbolic region bases, configured alias relations, byte-addressable symbolic memory, selected observations, and finite angr paths only.",
        "universal_equivalence_claimed": False,
    }
    if report_path is not None:
        write_json(report_path, report)
    return report


def angr_memory_alias_compare_files(
    target_path: Path,
    candidate_path: Path,
    harness_path: Path,
    *,
    report_path: Path | None = None,
) -> dict[str, Any]:
    """Implement angr memory alias compare files.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    target = target_path.resolve()
    candidate = candidate_path.resolve()
    if not target.is_file() or not candidate.is_file():
        raise ContractError("symbolic memory comparison inputs must be files")
    harness = _load_memory_harness(harness_path.resolve())
    return angr_memory_alias_compare(
        target.read_bytes(), candidate.read_bytes(), harness, report_path=report_path
    )
