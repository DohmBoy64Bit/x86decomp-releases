---
title: 'Example: ABI and type-recovery project'
description: Recover calling-convention and C++ relationship candidates, store provenance-bearing
  constraints, reject conflicts, and generate bounded harnesses before implementation
  work proceeds.
---

<a id="model"></a>
<a id="abi-type-recovery-flow-title"></a>
<a id="abi-type-recovery-flow-desc"></a>
<a id="arrow-abi-type-recovery"></a>
<a id="abi-type-recovery-flow-caption"></a>
<a id="observe"></a>
<a id="abi"></a>
<a id="cpp"></a>
<a id="constraints"></a>
<a id="conflicts"></a>
<a id="harness"></a>
<a id="limits"></a>
<a id="source-basis"></a>

# Example: ABI and type-recovery project

Recover calling-convention and C++ relationship candidates, store provenance-bearing constraints, reject conflicts, and generate bounded harnesses before implementation work proceeds.

> **Example notation.** Paths and function identifiers are representative local names. Commands and options are exact v0.7.8 parser forms; target-specific hashes, addresses, profiles, reports, and passing outcomes must come from the actual project.

> **Classification.** This is a supporting recovery workflow. It establishes interface constraints for matching and functional candidates; it is not original-header recovery.

**On this page**

1. [Constraint model](#model)
2. [Collect observations](#observe)
3. [Write and check ABI](#abi)
4. [Recover C++ metadata](#cpp)
5. [Store constraints](#constraints)
6. [Resolve conflicts](#conflicts)
7. [Generate harness](#harness)
8. [Truth boundary](#limits)
9. [Source basis](#source-basis)

## Constraint model

No inferred type becomes accepted merely because one analysis tool proposed it.Call sites → Instruction evidence → ABI contract → C++ metadata → Type constraints → Conflict gate → Harness

Call sitesInstruction evidenceABI contractC++ metadataType constraintsConflict gateHarness

No inferred type becomes accepted merely because one analysis tool proposed it.

```ascii-fallback
Call sites → Instruction evidence → ABI contract → C++ metadata → Type constraints → Conflict gate → Harness
```

1

## Collect independent call and metadata observations

```
x86decomp metadata-scan target.exe --object original/foo.obj --map target.map --report reports/metadata.json
x86decomp disassemble target/sub_00401230.bin --base 0x401230 --architecture x86 --report reports/disassembly/sub_00401230.json
x86decomp crosscheck-ghidra project/functions/pe-rva_00401230/instructions.jsonl target/sub_00401230.bin --base 0x401230 --architecture x86 --report reports/crosscheck/sub_00401230.json
```

Look for stack cleanup, register use, return behavior, this-pointer patterns, structure-return conventions, vtable references, RTTI, unwind data, and static initializer evidence. Record disagreements rather than averaging them away.

2

## Write an explicit ABI contract and check bytes

The bundled stdcall example is a complete contract for two 32-bit integer stack arguments:

```
{
  "architecture": "x86",
  "convention": "stdcall",
  "stack_argument_bytes": 8,
  "callee_stack_cleanup": 8,
  "variadic": false,
  "this_register": null,
  "register_arguments": [],
  "return_registers": ["eax"],
  "structure_return": false,
  "floating_point": "none"
}
```

```
x86decomp abi-check target/sub_00401230.bin examples/abi/stdcall-two-ints.json --base 0x401230 --report reports/abi/target.json
x86decomp abi-check build/sub_00401230.bin examples/abi/stdcall-two-ints.json --base 0 --report reports/abi/candidate.json
```

Passing means the implemented checks are consistent with the declared contract. It is not a complete proof of every ABI property or all caller/callee interactions.

3

## Recover bounded C++ relationships

```
x86decomp cpp-recover target.exe --metadata-report reports/metadata.json --object original/foo.obj --map target.map --report reports/cpp-recovery.json
```

The recovery model can report bounded RTTI, vtables, base relationships, adjustor-thunk candidates, and static initializer order when evidence exists. It explicitly does not recover original class declarations, source names, access modifiers, or templates.

4

## Store provenance-bearing type constraints

```
x86decomp db-constraint-add project/analysis.sqlite pe-rva:00401230 calling_convention stdcall disassembly-crosscheck --evidence-id ev-callsite-1 --confidence 0.85
x86decomp db-constraint-add project/analysis.sqlite pe-rva:00401230 return_register eax abi-report --evidence-id ev-abi-1 --confidence 0.95
x86decomp db-constraint-conflicts project/analysis.sqlite pe-rva:00401230 calling_convention
```

Every constraint carries its provenance and optional confidence. Confidence is metadata, not automatic acceptance.

5

## Resolve contradictions before acceptance

```
x86decomp db-query project/analysis.sqlite "SELECT id, subject_entity, relation, object_value, provenance, status FROM type_constraints WHERE subject_entity = ?" --parameters-json '["pe-rva:00401230"]' 
x86decomp db-constraint-accept project/analysis.sqlite 42
```

The analysis database refuses acceptance while contradictory constraints remain. Resolve the evidence first, then accept the surviving constraint ID.

6

## Generate a deterministic bounded harness

```
x86decomp harness-generate contracts/sub_00401230-abi.json harnesses/sub_00401230.json --pointer-parameters contracts/sub_00401230-pointers.json --max-instructions 100000 --timeout-ms 1000
```

The generator creates deterministic test inputs from the ABI and declared pointer regions. These are test inputs, not recovered original runtime inputs. External calls still require explicit stubs, and pointer observations are included only when declared.

## Truth boundary

- ABI checks are bounded to implemented observations and the supplied contract.
- Recovered C++ structures are candidates derived from metadata, not original declarations.
- Constraint confidence does not replace corroborating evidence.
- Generated harnesses do not model an entire application or operating system.

## v0.7.8 source basis

> **Verification model.** Command syntax is checked against the live parser. The source files below are hashed from the current release; implementation and test rows are retained as independent truth boundaries.

| Evidence file |
| --- |
| `src/x86decomp/cli.py` |
| `src/x86decomp/abi.py` |
| `src/x86decomp/cpp_recovery.py` |
| `src/x86decomp/harness_generator.py` |
| `src/x86decomp/analysis_db.py` |
| `tests/test_abi_disassembly.py` |


## Related examples

- [Matching project](matching-project.md)
- [Functional project](functional-project.md)
- [Hybrid composition](hybrid-project.md)
