---
title: 'Example: end-to-end hybrid composition'
description: Keep byte-form assembly fallbacks continuously buildable while matching
  and functional source lanes advance independently for each imported function.
original_path: project-examples/hybrid-project.html
---

<a id="model"></a>
<a id="hybrid-project-flow-title"></a>
<a id="hybrid-project-flow-desc"></a>
<a id="arrow-hybrid-project"></a>
<a id="hybrid-project-flow-caption"></a>
<a id="target"></a>
<a id="artifacts"></a>
<a id="generate"></a>
<a id="candidate"></a>
<a id="lanes"></a>
<a id="promote"></a>
<a id="state"></a>
<a id="limits"></a>
<a id="source-basis"></a>

Section: Project examples

# Example: end-to-end hybrid composition

Keep byte-form assembly fallbacks continuously buildable while matching and functional source lanes advance independently for each imported function.

> **Example notation.** Paths and function identifiers are representative local names. Commands and options are exact v0.7.8 parser forms; target-specific hashes, addresses, profiles, reports, and passing outcomes must come from the actual project.

> **Classification correction.** v0.7.8 has two selected modes: `matching` and `functional`. “Hybrid” is the composition used when `preferred_mode` is `both`; it is not a third mode enum.

**On this page**

1. [Hybrid composition](#model)
2. [Create a both-mode project](#target)
3. [Import functions](#artifacts)
4. [Generate fallbacks](#generate)
5. [Develop candidates](#candidate)
6. [Validate independent lanes](#lanes)
7. [Promote source deliberately](#promote)
8. [Interpret state](#state)
9. [Truth boundary](#limits)
10. [Source basis](#source-basis)

## Hybrid composition

The generator preserves an assembly build path while source candidates earn acceptance in one or both independent lanes.Target pack mode: both → Function packets → Byte-form assembly → Staging C → Matching lane → Functional lane → Selected source

Target packmode: bothFunction packetsByte-form assemblyStaging CMatching laneFunctional laneSelected source

The generator preserves an assembly build path while source candidates earn acceptance in one or both independent lanes.

```ascii-fallback
Target pack mode: both → Function packets → Byte-form assembly → Staging C → Matching lane → Functional lane → Selected source
```

The source stages are `original_bytes`, `generated_assembly`, `decompiler_candidate`, `human_candidate`, and `accepted_source`. Matching and functional status are separate fields in the same per-function workflow record.

1

## Create the grounded both-mode project

```
x86decomp target-pack-infer target.exe target-pack --pdb target.pdb --map target.map --decisions examples/release/target-decisions.json
x86decomp target-pack-verify target-pack
x86decomp project-from-target target-pack project
x86decomp project-check project
```

The bundled decisions example uses `preferred_mode: both` and deliberately leaves compiler, linker, and source-language facts unknown. Project derivation turns that preference into the two selected modes.

2

## Export and import function packets

```
x86decomp ghidra-export target.exe ghidra-projects TargetProject exports/ghidra --selector all --report reports/ghidra-export.json
x86decomp artifact-import project exports/ghidra/functions/pe-rva_00401230
x86decomp artifact-verify project/functions/pe-rva_00401230
```

The exported packet can contain `function.json`, body-range byte files, `decompiler.c`, context, instruction JSONL, references, and p-code. The manifest labels these artifacts as analysis-derived and unverified.

3

## Generate the continuously buildable tree

```
x86decomp hybrid-generate project hybrid-output --architecture x86 --asm-format bytes --image-base 0x400000
```

The exact v0.7.8 syntax has two positional paths: the existing project and the output directory. The default `bytes` format writes exact `.byte` directives from imported body ranges. The output includes:

```
hybrid-output/
├── src/asm/          # compiled fallback sources
├── src/staging/      # copied, untrusted decompiler C when present
├── src/matched/      # promotion destination after matching validation
├── src/functional/   # promotion destination after functional validation
├── config/original/  # immutable function-byte copies
├── reports/asm/      # assembly materialization reports
├── build/
├── Makefile
└── hybrid-project.json
```

The generated Makefile builds only `src/asm/*.S` into objects. Staging C is intentionally not compiled automatically. On systems with GNU make and a compatible GCC assembler path, run `make -C hybrid-output`.

4

## Develop a human candidate without removing fallback safety

```
x86decomp compile profiles/target-coff.json hybrid-output/src/staging/sub_00401230.c build/sub_00401230.obj --report reports/compile/sub_00401230.json
x86decomp workflow-update project pe-rva:00401230 --source-stage human_candidate --candidate hybrid-output/src/staging/sub_00401230.c --compiler-profile profiles/target-coff.json
```

Keep the assembly source active until the project’s acceptance policy is satisfied. The toolkit creates promotion directories, but source promotion and build selection are explicit project actions rather than an automatic consequence of a report.

5

## Validate the two lanes independently

```
x86decomp coff-extract build/sub_00401230.obj sub_00401230 build/sub_00401230.bin --size 0x20
x86decomp diff-function target.exe 0x401230 0x20 build/sub_00401230.obj sub_00401230 --report reports/diff/sub_00401230.json
x86decomp dynamic-validate hybrid-output/config/original/sub_00401230.bin build/sub_00401230.bin harnesses/sub_00401230.json --target-base 0x401230 --candidate-base 0 --report reports/dynamic/sub_00401230.json
x86decomp symbolic-validate hybrid-output/config/original/sub_00401230.bin build/sub_00401230.bin --architecture x86 --stack-argument-words 2 --output-register eax --max-steps 64 --max-paths 16 --report reports/symbolic/sub_00401230.json
```

This flat validator example assumes the imported function has one contiguous `0x20`-byte body range. The generator concatenates multiple body-range files for its fallback image; do not treat that concatenation as an address-preserving executable mapping for a split function.

> **State recording is separate.** Validators emit reports, but they do not automatically promote a function workflow. Inspect a passing report first, then use `workflow-update` to attach that report and record the justified status.

6

## Promote only the lane that passed

After review, copy the candidate into `src/matched` when the matching policy passes, into `src/functional` when the functional policy passes, or into both when both policies pass. The generated README states this explicitly. Then update the project’s own build manifest or relink manifest to select the desired object; the generator does not silently rewrite it.

```
x86decomp workflow-update project pe-rva:00401230 --matching-status byte_matched --report-kind function-diff --report-path reports/diff/sub_00401230.json
x86decomp workflow-update project pe-rva:00401230 --functional-status symbolically_bounded --report-kind symbolic --report-path reports/symbolic/sub_00401230.json
x86decomp workflow-show project pe-rva:00401230
```

7

## Interpret a valid split outcome

```
{
  "function_id": "pe-rva:00401230",
  "selected_modes": ["functional", "matching"],
  "source_stage": "human_candidate",
  "matching_status": "instruction_similar",
  "functional_status": "integration_validated"
}
```

This means the candidate passed the project’s declared integration scenarios but did not byte-match. It is not contradictory and must not be collapsed into one vague “complete” flag.

## Hybrid truth boundaries

- Byte-form assembly preserves imported function body bytes; it does not recreate relocations or whole-image layout by itself.
- Decompiler C remains untrusted until validated.
- Generated staging source is not automatically part of the Makefile.
- A status update records reviewed evidence; it does not independently re-run or inspect a validator.
- `both` is a target decision that enables the two real modes, not a third workflow mode.

## v0.7.8 source basis

> **Verification model.** Command syntax is checked against the live parser. The source files below are hashed from the current release; implementation and test rows are retained as independent truth boundaries.

| Evidence file | SHA-256 |
| --- | --- |
| `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/hybrid.py` | `721221b69c86bd2e7152ea2f322c9b48d89a01891feb6906038509a1f4592e2f` |
| `src/x86decomp/workflow.py` | `cae8a093f08f66f9412393e59867c4d32ca7caf88533a175d22eebe1f325c0a5` |
| `src/x86decomp/dynamic.py` | `a09cbba16f498158cf30191397884f0a70051c767b778cd520ac229b6e85e451` |
| `src/x86decomp/symbolic.py` | `93d98f6e85a01a107881131821d5eb04875d310795c4f173448918c5a96fdcd3` |
| `tests/test_pe64_patch_hybrid.py` | `6894dd0e5abce06a30df7ce445f6cf7faa87bcc16dac9f314f187e938697a62f` |


## Related examples

[Matching project

Open the source-verified workflow.](matching-project.md)[Functional project

Open the source-verified workflow.](functional-project.md)[Static analysis

Open the source-verified workflow.](static-analysis-evidence.md)
