---
title: 'Example: ABI and type-recovery project'
description: Recover calling-convention and C++ relationship candidates, store provenance-bearing
  constraints, reject conflicts, and generate bounded harnesses before implementation
  work proceeds.
original_path: project-examples/abi-type-recovery.html
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

Section: Project examples

# Example: ABI and type-recovery project

Recover calling-convention and C++ relationship candidates, store provenance-bearing constraints, reject conflicts, and generate bounded harnesses before implementation work proceeds.

> **Example notation.** Paths and function identifiers are representative local names. Commands and options are exact v0.7.11 parser forms; target-specific hashes, addresses, profiles, reports, and passing outcomes must come from the actual project.

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

## v0.7.11 source basis

> **Verification model.** Command syntax is checked against the live parser. The source files below are hashed from the current release; implementation and test rows are retained as independent truth boundaries.

| Evidence file | SHA-256 |
| --- | --- |
| `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/abi.py` | `e69b8d4ba247b2e3dbd3553cd207ee8fbe24fe244878c4dabb4afffbebb33903` |
| `src/x86decomp/cpp_recovery.py` | `c1f07b15f8649be4235cb56bb2e8f953ed31211b98311633d6beccde38dce8fa` |
| `src/x86decomp/harness_generator.py` | `75ab6f14bcef35574409e280dad90a705f71bc5763d507258f705ad8f4c431f2` |
| `src/x86decomp/analysis_db.py` | `409e503d6c264dba48a00e1d1afc475ce735cf25f1ec4aab7ac41b07ed5b9bad` |
| `tests/test_abi_disassembly.py` | `7707cba729a70b66986595aea747f5c1e782023e2b58134d2786680b52840a64` |


## Related examples

[Matching project

Open the source-verified workflow.](matching-project.md)[Functional project

Open the source-verified workflow.](functional-project.md)[Hybrid composition

Open the source-verified workflow.](hybrid-project.md)
