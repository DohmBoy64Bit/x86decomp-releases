---
title: 'Example: end-to-end matching project'
description: Reconstruct one PE function through compilation, ABI checks, instruction
  comparison, byte matching, image integration, and evidence-limited relinking.
original_path: project-examples/matching-project.html
---

<a id="model"></a>
<a id="matching-project-flow-title"></a>
<a id="matching-project-flow-desc"></a>
<a id="arrow-matching-project"></a>
<a id="matching-project-flow-caption"></a>
<a id="target"></a>
<a id="analysis"></a>
<a id="candidate"></a>
<a id="abi"></a>
<a id="diff"></a>
<a id="image"></a>
<a id="state"></a>
<a id="limits"></a>
<a id="source-basis"></a>

Section: Project examples

# Example: end-to-end matching project

Reconstruct one PE function through compilation, ABI checks, instruction comparison, byte matching, image integration, and evidence-limited relinking.

> **Example notation.** Paths and function identifiers are representative local names. Commands and options are exact v0.7.8 parser forms; target-specific hashes, addresses, profiles, reports, and passing outcomes must come from the actual project.

> **Classification.** This is an official `matching` project mode. It tracks the matching state machine without implying functional validation.

**On this page**

1. [Matching model](#model)
2. [Ground the target](#target)
3. [Import analysis](#analysis)
4. [Compile a candidate](#candidate)
5. [Check the ABI](#abi)
6. [Compare the function](#diff)
7. [Integrate and compare images](#image)
8. [Record the result](#state)
9. [Truth boundary](#limits)
10. [Source basis](#source-basis)

## Matching model

Matching evidence narrows from an individual candidate object to a target-specific whole-image claim.Target pack → Function artifact → COFF candidate → ABI check → Function diff → Image match → Relink gate

Target packFunction artifactCOFF candidateABI checkFunction diffImage matchRelink gate

Matching evidence narrows from an individual candidate object to a target-specific whole-image claim.

```ascii-fallback
Target pack → Function artifact → COFF candidate → ABI check → Function diff → Image match → Relink gate
```

The matching workflow has its own monotonic states: `not_started → decompiled → compiles → abi_compatible → instruction_similar → byte_matched → image_integrated → full_relink_validated`. `blocked` records an explicit obstruction rather than completion.

1

## Ground the target

```
x86decomp target-pack-infer target.exe target-pack --pdb target.pdb --map target.map --decisions decisions-matching.json
x86decomp target-pack-verify target-pack
x86decomp project-from-target target-pack project
x86decomp project-check project
```

Set `preferred_mode` to `matching` in the decisions file only when that is an explicit operator decision. Unknown compiler, linker, and source-language facts stay unknown.

```
{
  "preferred_mode": "matching",
  "compiler_family": "unknown",
  "compiler_version": "unknown",
  "linker_family": "unknown",
  "source_language": "unknown",
  "allow_host_execution": false,
  "target_description": "Authorized native target; unresolved build facts remain unknown."
}
```

2

## Export, import, and verify analysis artifacts

```
x86decomp ghidra-export target.exe ghidra-projects TargetProject exports/ghidra --selector all --report reports/ghidra-export.json
x86decomp artifact-import project exports/ghidra/functions/pe-rva_00401230
x86decomp artifact-verify project/functions/pe-rva_00401230
x86decomp workflow-init project pe-rva:00401230 --mode matching
```

The Ghidra packet is analysis-derived evidence, not authenticated original source. Import verifies the artifact contract and hashes; it does not prove the decompiler signature or types are correct.

3

## Compile a target-specific candidate

```
x86decomp compile profiles/target-coff.json src/sub_00401230.c build/sub_00401230.obj --cache build/compiler-cache --report reports/compile/sub_00401230.json
```

The profile must name a real installed compiler and produce the object format required by later steps. The compile report records the executable identity, arguments, input/output hashes, return code, and captured output. A successful compile justifies `compiles`, not a match.

4

## Check the candidate ABI

```
x86decomp coff-extract build/sub_00401230.obj sub_00401230 build/sub_00401230.bin --size 0x20
x86decomp abi-check build/sub_00401230.bin contracts/sub_00401230-abi.json --base 0 --report reports/abi/sub_00401230.json
```

Here `0x20` must be the function size established from the target artifact; it is not a toolkit default. The ABI contract is explicit: architecture, calling convention, stack arguments and cleanup, register arguments, return registers, structure-return behavior, and floating-point model. A passing report is limited to the checks encoded by the validator and contract.

5

## Compare the linked target function to the COFF symbol

```
x86decomp diff-function target.exe 0x401230 0x20 build/sub_00401230.obj sub_00401230 --report reports/diff/sub_00401230.json
```

The report classification can be `byte_matched`, `relocation_normalized_match`, `instruction_similar`, or `mismatch`. Only the first classification supports the exact-byte status for the declared RVA and size; normalization and instruction similarity are narrower claims.

> **State recording is separate.** Validators emit reports, but they do not automatically promote a function workflow. Inspect a passing report first, then use `workflow-update` to attach that report and record the justified status.

6

## Integrate, relink, and compare whole images

```
x86decomp linker-plan target.exe target.map build/entry.obj build/sub_00401230.obj --library runtime.lib --report reports/linker-plan.json --write-relink-manifest config/relink.json
x86decomp relink config/relink.json --report reports/relink.json
x86decomp image-profile target.exe config/image-profile.json
x86decomp image-match target.exe build/reconstructed.exe --profile config/image-profile.json --report reports/image-match.json
x86decomp convergence-analyze target.exe build/reconstructed.exe --profile config/image-profile.json --report reports/convergence.json --history reports/convergence-history.json
```

The linker plan preserves only evidence supported by the PE, MAP, supplied objects, libraries, and operator inputs. It reports unresolved facts and readiness; it does not reconstruct erased flags by guesswork. `image-match` distinguishes raw identity from profile-normalized equality.

7

## Record justified matching progress

```
x86decomp workflow-update project pe-rva:00401230 --source-stage human_candidate --matching-status byte_matched --candidate src/sub_00401230.c --compiler-profile profiles/target-coff.json --report-kind function-diff --report-path reports/diff/sub_00401230.json
x86decomp workflow-show project pe-rva:00401230
```

Advance to `image_integrated` or `full_relink_validated` only after the corresponding reports pass under the declared policy. Matching progress never promotes the functional lane.

## What this project does not prove

- A byte match over one RVA range is not proof that the whole program behaves correctly.
- A profile-normalized image match is not raw byte identity.
- A ranked compiler candidate is not proof of the historical compiler unless independent evidence supports it.
- A successful relink is not automatically a matching relink; inspect the image and convergence reports.

## v0.7.8 source basis

> **Verification model.** Command syntax is checked against the live parser. The source files below are hashed from the current release; implementation and test rows are retained as independent truth boundaries.

| Evidence file | SHA-256 |
| --- | --- |
| `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/compiler.py` | `f21f38f6ed0804a959188e31f5c9fa498d7d0740536fbb82594a375b12353944` |
| `src/x86decomp/exe_diff.py` | `997ffacbd833a3bb4c0545d1fb1981469e1d575680f4b39b7e6f34a4796abdf0` |
| `src/x86decomp/image_match.py` | `a9c72f376532369da77440496a1ea07564da5071ef8e6108e29c58e33e96fcf4` |
| `src/x86decomp/workflow.py` | `cae8a093f08f66f9412393e59867c4d32ca7caf88533a175d22eebe1f325c0a5` |
| `tests/test_modes_and_db.py` | `7b3e58d0cbef709f782c724956d752cd24fab83ec169cf6eb49562b883b4b174` |


## Related examples

[Functional project

Open the source-verified workflow.](functional-project.md)[Hybrid composition

Open the source-verified workflow.](hybrid-project.md)[Static analysis

Open the source-verified workflow.](static-analysis-evidence.md)
