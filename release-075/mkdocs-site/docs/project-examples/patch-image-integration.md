---
title: 'Example: patch-image integration project'
description: Replace one caller-selected in-place byte range in a copied PE, preserve
  the pristine original, refresh the PE checksum, and validate the derived image under
  explicit hashes and scenarios.
original_path: project-examples/patch-image-integration.html
---

<a id="model"></a>
<a id="patch-image-integration-flow-title"></a>
<a id="patch-image-integration-flow-desc"></a>
<a id="arrow-patch-image-integration"></a>
<a id="patch-image-integration-flow-caption"></a>
<a id="baseline"></a>
<a id="candidate"></a>
<a id="patch"></a>
<a id="inspect"></a>
<a id="validate"></a>
<a id="record"></a>
<a id="limits"></a>
<a id="source-basis"></a>

Section: Project examples

# Example: patch-image integration project

Replace one caller-selected in-place byte range in a copied PE, preserve the pristine original, refresh the PE checksum, and validate the derived image under explicit hashes and scenarios.

> **Example notation.** Paths and function identifiers are representative local names. Commands and options are exact v0.7.5 parser forms; target-specific hashes, addresses, profiles, reports, and passing outcomes must come from the actual project.

> **Classification.** This is an incremental integration workflow, not a project mode and not a general binary rewriter.

**On this page**

1. [Patch model](#model)
2. [Seal the baseline](#baseline)
3. [Prepare bytes](#candidate)
4. [Create the image](#patch)
5. [Verify structure](#inspect)
6. [Run bounded validation](#validate)
7. [Record provenance](#record)
8. [Hard constraints](#limits)
9. [Source basis](#source-basis)

## Patch model

The operation creates a new image and gates mutation by explicit target and function identities.Pristine PE → Expected hashes → Evidence-sized bytes → Patch copied image → Refresh checksum → Static check → Isolated test

Pristine PEExpected hashesEvidence-sized bytesPatch copied imageRefresh checksumStatic checkIsolated test

The operation creates a new image and gates mutation by explicit target and function identities.

```ascii-fallback
Pristine PE → Expected hashes → Evidence-sized bytes → Patch copied image → Refresh checksum → Static check → Isolated test
```

1

## Seal the original and function identities

```
x86decomp inspect-pe target.exe
x86decomp diff-bytes target/sub_00401230.bin candidate/sub_00401230.bin --report reports/prepatch-byte-diff.json
```

Compute and retain the SHA-256 of the complete original and the original function bytes using your standard hashing tool. Pass those exact values to `patch-image` so a changed or wrong input is rejected.

2

## Produce exact replacement bytes

```
x86decomp compile profiles/target-coff.json src/sub_00401230.c build/sub_00401230.obj --report reports/compile/sub_00401230.json
x86decomp coff-extract build/sub_00401230.obj sub_00401230 build/sub_00401230.bin --size 0x20
```

For this workflow, `0x20` must be the independently established target function size. The patch backend itself does not know function boundaries: the candidate file length defines how many bytes are overwritten. It does not pad, relocate, allocate a trampoline, or prevent a wrongly sized candidate from overwriting adjacent bytes. Resolve size, code references, relocations, unwind requirements, and data assumptions before patching.

3

## Create a derived patched PE

```
x86decomp patch-image target.exe build/sub_00401230.bin build/target-patched.exe --rva 0x401230 --expected-original-sha256 ORIGINAL_SHA256 --expected-function-sha256 FUNCTION_SHA256 --report reports/patch/sub_00401230.json
```

Replace `ORIGINAL_SHA256` and `FUNCTION_SHA256` with measured 64-hex digests. The function digest covers the original bytes for exactly the candidate length; it is not an independent function-boundary check. The implementation copies the original, patches that range in place, refreshes the PE checksum, and writes a report. It does not mutate the pristine input.

4

## Re-parse and compare the derived image

```
x86decomp inspect-pe build/target-patched.exe
x86decomp image-profile target.exe config/patch-image-profile.json
x86decomp image-match target.exe build/target-patched.exe --profile config/patch-image-profile.json --report reports/patch/image-match.json
```

The expected whole-image result is normally “different” because the function was intentionally changed. The report measures raw and profile-normalized whole-image differences. Use it together with the patch report and a separate byte-diff review; `image-match` does not itself certify that every difference is confined to the intended patch range.

5

## Validate behavior in an explicit execution boundary

```
x86decomp integration-run integration/patched-image.json --report reports/integration/patched-image.json
```

> **Execution safety.** Use an external wrapper or another deliberately configured isolation boundary for unknown native code. Host execution requires both manifest acknowledgment and the CLI opt-in flag.

6

## Record the patch as derived evidence

```
x86decomp evidence-add project --kind human_review --source analyst --locator pe-rva:00401230 --assertion "Analyst reviewed the same-size patch report and derived image" --independent-group patch-review --file reports/patch/sub_00401230.json --id ev-patch-00401230
x86decomp memory-add project --actor analyst --category integration --summary "Created and tested derived patch image" --details-json '{"rva":"0x401230","output":"build/target-patched.exe"}' --evidence ev-patch-00401230
```

Keep the patch report, image hash, input hashes, validator reports, and authorization context together.

## Hard constraints

- In-place replacement of exactly the candidate byte length. Correct same-size function replacement is an operator-enforced workflow condition, not an independently discovered boundary check.
- No automatic code-cave allocation, trampoline synthesis, relocation repair, unwind regeneration, or import reconstruction.
- A valid PE checksum is not a code-signature replacement and does not establish trust.
- A passing integration scenario is bounded to its declared observations.

## v0.7.5 source basis

> **Verification model.** Command syntax is checked against the live parser. The source files below are hashed from the current release; implementation and test rows are retained as independent truth boundaries.

| Evidence file | SHA-256 |
| --- | --- |
| `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/patching.py` | `61b9d802fc2c9c89f06877876f72efb7fc16d3a1fb283dddfd561dfd4fe61741` |
| `src/x86decomp/pe32.py` | `746651d78b0b8401565dd22e99f73c8c902b13400fd80094d4675ab52c8c4be5` |
| `tests/test_pe64_patch_hybrid.py` | `6894dd0e5abce06a30df7ce445f6cf7faa87bcc16dac9f314f187e938697a62f` |


## Related examples

[Matching project

Open the source-verified workflow.](matching-project.md)[Functional project

Open the source-verified workflow.](functional-project.md)[Hybrid composition

Open the source-verified workflow.](hybrid-project.md)
