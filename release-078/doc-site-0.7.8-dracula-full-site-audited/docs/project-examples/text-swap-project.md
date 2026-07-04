---
title: End-to-end text-swap project
description: Container-preserving text-section replacement workflow for earlier playable testing without claiming full relink.
---

# End-to-end text-swap project

A text-swap project is an intermediate reconstruction workflow. It builds or composes a replacement `.text` byte stream, injects that byte stream into the original PE container, and verifies that the planned bytes are present at the planned section offset.

It is useful when a full relink is not ready yet, but the project needs an executable that preserves the original PE container, resources, imports, data sections, and headers while replacing code bytes in a controlled way.

It is **not** a full relink claim. It is also not a source-recovery claim. The text-swap commands only prove the bounded section-replacement facts reported by their JSON outputs.

```text
original PE container
        +
replacement .text bytes
        ↓
text-swap plan
        ↓
text-swap inject
        ↓
text-swap verify
        ↓
derived executable for bounded testing
```

## 1. Establish the target and function evidence

Start from the normal evidence workflow:

```powershell
x86decomp target-pack-infer target.exe target-pack --decisions target-decisions.json
x86decomp target-pack-verify target-pack
x86decomp project-from-target target-pack project
x86decomp project-check project
```

Then import function evidence or generate function records through the project workflow. If you need a discovered range list for triage, the generic discovery command can create one:

```powershell
x86decomp function discover target.exe --profile prologue --architecture x86 --output reports\functions\discover.json
x86decomp function reconcile reports\functions\discover.json --output reports\functions\reconciled.json
x86decomp function sort reports\functions\reconciled.json --key rva --output reports\functions\sorted.json
x86decomp function classify reports\functions\sorted.json --output reports\functions\classified.json
```

The `prologue` profile is a heuristic profile name. It is not an MSVC-only or game-specific promise. The report remains triage evidence until it is reconciled with project function packets, exact bytes, and later validation reports.

## 2. Produce or compose replacement `.text` bytes

The text-swap workflow requires a replacement byte stream. The current `image-text compose` command can compose bytes from project function records or from a supplied function list:

```powershell
x86decomp image-text --project project compose build\replacement-text.bin --function-list reports\functions\sorted.json
```

If project function records contain artifact ranges, the composed report records those bytes as `artifact_range`. Missing ranges are filled with the configured fallback byte. That fallback is useful for detecting gaps, but it should not be misread as decompiled source.

The command writes a companion report next to the output byte stream:

```text
build\replacement-text.bin.compose.json
```

That report states the output hash, output size, and which declared records contributed bytes.

## 3. Create a text-swap plan

Create a bounded replacement plan against the original executable:

```powershell
x86decomp text-swap plan target.exe build\replacement-text.bin reports\text-swap\plan.json --section-name .text
```

The plan records:

```text
original image path and hash
replacement byte-stream path and hash
selected section name
section raw offset and raw size
section virtual address and virtual size
planned output path
```

The planner rejects a replacement that exceeds the selected section's original raw allocation. It does not claim that the replacement is semantically correct, source-derived, or fully matched.

## 4. Inject the replacement bytes into a derived executable

Inject using the plan:

```powershell
x86decomp text-swap inject reports\text-swap\plan.json --output build\target-text-swap.exe
```

The inject step re-hashes the original image and replacement byte stream before writing. If either hash differs from the plan, injection is blocked.

The derived image preserves the original file size and replaces only the planned section raw range. Bytes after the replacement length inside the original raw section allocation are preserved by the current implementation.

## 5. Verify the derived executable

Verify the planned bytes in the derived image:

```powershell
x86decomp text-swap verify reports\text-swap\plan.json build\target-text-swap.exe --output reports\text-swap\verify.json
```

A valid verification report means the replacement bytes from the plan are present at the planned raw section offset in the derived image. It does not prove a full relink, all-function byte matching, or successful game execution.

## 6. Run isolated functional tests

Use integration scenarios to test only declared observations:

```powershell
x86decomp integration-run integration\launch-smoke.json --report reports\integration\launch-smoke.json
```

Unknown native programs should run behind an explicit isolation boundary such as a disposable VM or an external wrapper. A launch smoke test does not prove that the whole game works.

## 7. Reconcile progress and source stages

After the derived image is produced, reconcile project accounting:

```powershell
x86decomp progress --project project reconcile --output reports\progress\reconcile.json
x86decomp source-stage --project project classify --output reports\progress\source-stage.json
x86decomp project --project project health --output reports\progress\health.json
```

This separates byte-form fallbacks, generated wrappers, pattern-generated source, LLM-generated source, and human-reviewed source. For a moddable project, byte-preserving wrappers and raw assembly fallbacks should not be counted as human-readable decompilation.

## 8. Move toward full relink later

Text-swap is an intermediate milestone. A full source project should still converge toward explicit source files, accepted compiler profiles, linker plans, relink manifests, image comparison, and release gates:

```powershell
x86decomp linker-plan target.exe target.map build\entry.obj --report reports\linker-plan.json --write-relink-manifest config\relink.json
x86decomp relink config\relink.json --report reports\relink.json
x86decomp image-profile target.exe config\image-profile.json
x86decomp image-match target.exe build\reconstructed.exe --profile config\image-profile.json --report reports\image-match.json
```

Use text-swap to get earlier bounded executable feedback. Do not use it to claim that full image reconstruction is complete.

## Bounded claims

A successful text-swap workflow can claim:

```text
The planned replacement bytes were injected into the selected section raw range of the original PE container, and the derived image contains those bytes at the planned offset.
```

It cannot claim:

```text
original source recovered
full relink validated
all functions matched
whole game behavior proven
mod-ready human-readable source achieved
```

Those claims require separate matching, functional, source-stage, relink, integration, and release-gate evidence.

## v0.7.8 source basis

> **Verification model.** Command syntax is checked against the live parser. The source files below are hashed from the current release; implementation and test rows are retained as independent truth boundaries.

| Evidence file |
| --- |
| `src/x86decomp/cli.py` |
| `src/x86decomp/reconstruction/cli.py` |
| `src/x86decomp/reconstruction/acceleration.py` |
| `tests/reconstruction/test_real_project_acceleration.py` |

## Related examples

- [Full relink convergence](full-relink-convergence.md)
- [Patch-image integration](patch-image-integration.md)
- [Project operations and recovery](project-operations-recovery.md)
