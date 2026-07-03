---
title: 'Example: end-to-end functional project'
description: Reconstruct a function for declared behavioral equivalence using compilation,
  ABI validation, bounded concrete execution, bounded symbolic checks, and explicit
  integration scenarios.
original_path: project-examples/functional-project.html
---

<a id="model"></a>
<a id="functional-project-flow-title"></a>
<a id="functional-project-flow-desc"></a>
<a id="arrow-functional-project"></a>
<a id="functional-project-flow-caption"></a>
<a id="project"></a>
<a id="candidate"></a>
<a id="dynamic"></a>
<a id="symbolic"></a>
<a id="integration"></a>
<a id="state"></a>
<a id="limits"></a>
<a id="source-basis"></a>

Section: Project examples

# Example: end-to-end functional project

Reconstruct a function for declared behavioral equivalence using compilation, ABI validation, bounded concrete execution, bounded symbolic checks, and explicit integration scenarios.

> **Example notation.** Paths and function identifiers are representative local names. Commands and options are exact v0.7.5 parser forms; target-specific hashes, addresses, profiles, reports, and passing outcomes must come from the actual project.

> **Classification.** This is an official `functional` project mode. It does not require identical instructions or bytes.

**On this page**

1. [Functional model](#model)
2. [Create the project](#project)
3. [Prepare the candidate](#candidate)
4. [Differential execution](#dynamic)
5. [Bounded symbolic validation](#symbolic)
6. [Integration scenarios](#integration)
7. [Record status](#state)
8. [Truth boundary](#limits)
9. [Source basis](#source-basis)

## Functional model

Each validation layer adds bounded behavioral evidence without claiming all-input equivalence.Target evidence → Source candidate → Compile + ABI → Concrete harness → Symbolic model → Integration → Functional status

Target evidenceSource candidateCompile + ABIConcrete harnessSymbolic modelIntegrationFunctional status

Each validation layer adds bounded behavioral evidence without claiming all-input equivalence.

```ascii-fallback
Target evidence → Source candidate → Compile + ABI → Concrete harness → Symbolic model → Integration → Functional status
```

The functional state machine is `not_started → decompiled → compiles → abi_compatible → differentially_validated → symbolically_bounded → integration_validated`, with `blocked` for an explicit obstruction.

1

## Create a functional-only project and materialize the target range

```
x86decomp target-pack-infer target.exe target-pack --decisions decisions-functional.json
x86decomp target-pack-verify target-pack
x86decomp project-from-target target-pack project
x86decomp workflow-init project pe-rva:00401230 --mode functional
```

```
{
  "preferred_mode": "functional",
  "compiler_family": "unknown",
  "compiler_version": "unknown",
  "linker_family": "unknown",
  "source_language": "unknown",
  "allow_host_execution": false,
  "target_description": "Authorized target for bounded functional reconstruction."
}
```

Export and import the function packet, then materialize a flat target byte file only when the example function has one contiguous body range:

```
x86decomp ghidra-export target.exe ghidra-projects TargetProject exports/ghidra --selector all --report reports/ghidra-export.json
x86decomp artifact-import project exports/ghidra/functions/pe-rva_00401230
x86decomp artifact-verify project/functions/pe-rva_00401230
$functionDir = "project/functions/pe-rva_00401230"
$manifest = Get-Content "$functionDir/function.json" | ConvertFrom-Json
if ($manifest.body_ranges.Count -ne 1) { throw "This flat-code example requires one contiguous body range." }
$range = $manifest.body_ranges[0]
$targetBase = 0x400000 + [int64]$range.start_rva
New-Item -ItemType Directory -Force target | Out-Null
Copy-Item (Join-Path $functionDir $range.file) target/sub_00401230.bin
x86decomp harness-generate contracts/sub_00401230-abi.json harnesses/sub_00401230.json --no-observe-pointers --max-instructions 100000 --timeout-ms 1000
```

A functional project can use a modern compiler, but the ABI and all observations still have to be declared and tested. The generated harness contains deterministic test values, not recovered production inputs; add explicit pointer regions and deterministic stubs when the function requires them.

2

## Compile and ABI-check a candidate

```
x86decomp compile profiles/functional-x86.json src/sub_00401230.c build/sub_00401230.obj --report reports/compile/sub_00401230.json
x86decomp coff-extract build/sub_00401230.obj sub_00401230 build/sub_00401230.bin
x86decomp abi-check build/sub_00401230.bin contracts/sub_00401230-abi.json --base 0 --report reports/abi/sub_00401230.json
```

Compilation and ABI compatibility are prerequisites for meaningful behavior comparisons. They do not establish equivalent outputs, memory effects, calls, or failure behavior.

3

## Run bounded concrete differential execution

```
x86decomp dynamic-validate target/sub_00401230.bin build/sub_00401230.bin harnesses/sub_00401230.json --target-base $targetBase --candidate-base 0 --report reports/dynamic/sub_00401230.json
```

The Unicorn-backed validator compares the observations declared by the harness under its initial register, stack, memory, stub, timeout, and instruction bounds. The key report claim is equivalence for that harness—not semantic equivalence for every input or a complete Windows process model.

4

## Run bounded symbolic checks

```
x86decomp symbolic-validate target/sub_00401230.bin build/sub_00401230.bin --architecture x86 --stack-argument-words 2 --output-register eax --max-steps 64 --max-paths 16 --report reports/symbolic/sub_00401230.json
x86decomp symbolic-memory-validate target/sub_00401230.bin build/sub_00401230.bin harnesses/sub_00401230-memory.json --report reports/symbolic-memory/sub_00401230.json
```

The first command compares configured symbolic inputs and output registers. The memory-aware command adds symbolic regions and explicit alias constraints. An UNSAT/equivalent result is bounded by supported instructions, path limits, memory model, inputs, outputs, and alias assumptions.

5

## Run explicit integration scenarios

```
x86decomp integration-run integration/sub_00401230.json --report reports/integration/sub_00401230.json
```

Use an `external_wrapper` execution mode for an isolation boundary supplied by your environment. Host execution requires both an acknowledged `host_explicit` manifest and the `--allow-host-execution` flag:

```
x86decomp integration-run integration/sub_00401230-host.json --allow-host-execution --report reports/integration/sub_00401230-host.json
```

> **Isolation boundary.** The toolkit validates the manifest and wrapper contract but does not certify that an external wrapper is a secure sandbox. Never run unknown native code directly on an ordinary development host.

6

## Record the independently justified state

```
x86decomp workflow-update project pe-rva:00401230 --source-stage human_candidate --functional-status integration_validated --candidate src/sub_00401230.c --report-kind integration --report-path reports/integration/sub_00401230.json
x86decomp workflow-show project pe-rva:00401230
```

> **State recording is separate.** Validators emit reports, but they do not automatically promote a function workflow. Inspect a passing report first, then use `workflow-update` to attach that report and record the justified status.

Attach additional dynamic and symbolic reports under distinct report kinds as the project policy requires. Functional progress never promotes the matching lane.

## What a passing functional project means

| Layer | Supported statement | Not supported |
| --- | --- | --- |
| Dynamic | Equivalent for the supplied concrete harness and observations. | All-input equivalence. |
| Symbolic | Equivalent within the declared supported bounded model. | A proof outside its instructions, paths, memory, and outputs. |
| Integration | All declared scenarios produced equivalent requested observations. | Safety, completeness, or behavior outside those scenarios. |

## v0.7.5 source basis

> **Verification model.** Command syntax is checked against the live parser. The source files below are hashed from the current release; implementation and test rows are retained as independent truth boundaries.

| Evidence file | SHA-256 |
| --- | --- |
| `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/dynamic.py` | `a09cbba16f498158cf30191397884f0a70051c767b778cd520ac229b6e85e451` |
| `src/x86decomp/symbolic.py` | `93d98f6e85a01a107881131821d5eb04875d310795c4f173448918c5a96fdcd3` |
| `src/x86decomp/integration.py` | `cb8157c8210544e2ed4730e8bdb01f0a77dc9d05f683d43154cba1bf93c1e845` |
| `src/x86decomp/workflow.py` | `cae8a093f08f66f9412393e59867c4d32ca7caf88533a175d22eebe1f325c0a5` |
| `tests/test_dynamic_symbolic.py` | `0b21be2ee69be29d2dde6951f147195bd8042462690dea72fac0b6509deb3402` |


## Related examples

[Matching project

Open the source-verified workflow.](matching-project.md)[Hybrid composition

Open the source-verified workflow.](hybrid-project.md)[Static analysis

Open the source-verified workflow.](static-analysis-evidence.md)
