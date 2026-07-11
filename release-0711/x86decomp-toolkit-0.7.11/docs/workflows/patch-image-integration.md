# Patch-Image Integration

**Technical objective:** Ghidra export through matching C compilation, COFF extraction/synthesis, PE function patching, and byte-level validation — a closed-loop matching-decompilation integration for a single function.

**Game:** Iron Battalion (fictional mech combat game, x86 PE32, MSVC 2008 /GS- /O2).

---

## Overview

Iron Battalion is a 32-bit mech combat title compiled with MSVC 2008. The team has identified the `sub_4AB100` function — a 224-byte physics helper that computes joint torque from leg actuator positions — as the first matching-decompilation target. This workflow takes a Ghidra export of that function from project initialization through a fully validated patched PE image.

You will learn:

1. How to initialize a project and export Ghidra artifacts for a single function.
2. How to write matching C, compile it under a mirroring compiler profile, and extract the COFF symbol.
3. How to synthesize a relocation-carrying COFF and patch it back into the original PE.
4. How to verify PE integrity and confirm byte identity.

---

## Prerequisites

| Requirement | Detail |
|---|---|
| **Binary** | `games/iron-battalion/iron_battalion.exe` — PE32 x86, valid digital signature not required |
| **Ghidra** | Ghidra 11.2+ installed with headless support; path known |
| **Compiler** | MSVC 2008 toolchain registered via `toolchain-register` |
| **Compiler profile** | A JSON profile mirroring the original `/GS- /O2 /MT` flags |
| **Disassembly** | Function `sub_4AB100` at RVA `0xAB100`, size 224 bytes (0xE0) |
| **Project root** | `games/iron-battalion/project/` (initialized) |

---

## Starting directory structure

```
games/iron-battalion/
├── iron_battalion.exe              # original PE (backed up)
├── project/                        # x86decomp project root
│   ├── project.json
│   ├── original/
│   │   └── iron_battalion.exe
│   ├── src/
│   │   ├── matched/
│   │   └── staging/
│   ├── build/
│   │   ├── cache/
│   │   ├── candidates/
│   │   ├── compiler/
│   │   └── patches/
│   ├── config/
│   │   └── compiler-profiles/
│   │       └── msvc2008-o2.json
│   └── functions/
├── ghidra-project/                 # Ghidra project directory
└── exports/                        # Ghidra export output
    └── sub_4AB100/
        ├── function.json
        ├── decompiled.c
        ├── disassembly.jsonl
        └── cfg.json
```

---

## Step 1: Initialize the project and snapshot tools

```console
$ x86decomp init games/iron-battalion/iron_battalion.exe games/iron-battalion/project/
$ x86decomp snapshot-tools --output games/iron-battalion/project/config/tools.json \
    --ghidra-home "C:\ghidra_11.2_PUBLIC"
```

**What happens:** `init` copies the binary into `project/original/`, records its SHA-256, architecture (`x86`), and creates the full project tree with SQLite databases. `snapshot-tools` captures tool versions and paths for later reproducibility.

```json
{
  "schema_version": 3,
  "project_id": "x86d-...",
  "architecture": "x86",
  "valid": true
}
```

---

## Step 2: Export Ghidra artifacts and inspect

```console
$ x86decomp ghidra-export games/iron-battalion/iron_battalion.exe \
    games/iron-battalion/ghidra-project/ iron_battalion \
    games/iron-battalion/exports/ \
    --ghidra-home "C:\ghidra_11.2_PUBLIC" \
    --selector sub_4AB100 --overwrite
```

**What happens:** Runs Ghidra headless with `--selector sub_4AB100` to export only that function. The output directory contains `function.json` (RVA, size, hash), `decompiled.c` (Ghidra decompiler output), `disassembly.jsonl` (instruction records), and `cfg.json` (control-flow graph).

Inspect the PE to confirm section layout and RVA:
```console
$ x86decomp inspect-pe games/iron-battalion/project/original/iron_battalion.exe
```

Verify the exported artifact:
```console
$ x86decomp artifact-verify games/iron-battalion/exports/sub_4AB100/
```

Then import into the project:
```console
$ x86decomp artifact-import games/iron-battalion/project/ games/iron-battalion/exports/
```

---

## Step 3: Initialize workflow state

```console
$ x86decomp workflow-init games/iron-battalion/project/ sub_4AB100 \
    --mode matching --mode functional
```

**What happens:** Creates per-function tracking for both matching and functional modes. The function starts with `source-stage: not_started`, `matching-status: unmatched`, `functional-status: unvalidated`.

Confirm:
```console
$ x86decomp workflow-show games/iron-battalion/project/ sub_4AB100
```

---

## Step 4: Write matching C and compile

Write `games/iron-battalion/project/src/staging/torque_actuator.c` based on the Ghidra decompiler output, mirroring the original register usage and instruction patterns.

```console
$ x86decomp compile games/iron-battalion/project/config/compiler-profiles/msvc2008-o2.json \
    games/iron-battalion/project/src/staging/torque_actuator.c \
    games/iron-battalion/project/build/candidates/torque_actuator.obj \
    --report games/iron-battalion/project/reports/matching/torque_actuator-compile.json \
    --cache games/iron-battalion/project/build/cache/
```

**What happens:** `compile` invokes the MSVC 2008 toolchain registered for the profile, applies `/GS- /O2 /MT`, and emits a COFF object. The `--cache` flag enables content-addressed compilation caching. The `--report` emits compiler exit code, stdout, and output hash.

!!! tip "Compiler profile"
    The compiler profile JSON must declare `family: msvc`, `version: 15.00`, and the exact flags observed in the binary: `/GS- /O2 /MT /Gy`. See [Compiler Profile](../config/compiler-profile.md).

---

## Step 5: Inspect and extract the COFF symbol

```console
$ x86decomp coff-inspect games/iron-battalion/project/build/candidates/torque_actuator.obj
```

**What happens:** Parses COFF header, section table, symbol table, and relocation entries. Look for the `_torque_actuator` symbol and note its section number, value, and size.

Extract the symbol:
```console
$ x86decomp coff-extract games/iron-battalion/project/build/candidates/torque_actuator.obj \
    _torque_actuator \
    games/iron-battalion/project/build/candidates/torque_actuator.bin \
    --size 224
```

**What happens:** `coff-extract` locates `_torque_actuator` in the COFF symbol table, reads its raw section data, applies any section-relative relocations within the extracted body, and writes the resolved bytes to the output file. `--size` validates the payload length.

---

## Step 6: Compare extracted bytes against the original PE function

```console
$ x86decomp diff-function games/iron-battalion/project/original/iron_battalion.exe \
    0xAB100 224 \
    games/iron-battalion/project/build/candidates/torque_actuator.obj \
    _torque_actuator \
    --report games/iron-battalion/project/reports/matching/torque_actuator-diff.json
```

**What happens:** `diff-function` extracts the 224-byte function body from the PE at RVA `0xAB100`, extracts `_torque_actuator` from the COFF, resolves relocations, and compares every byte. The report shows match status, mismatch count, and per-offset details.

!!! success "Exact match"
    If all 224 bytes match, the function is byte-identical. Proceed to patching. If there are mismatches, review the C source, compiler flags, and relocation resolution before iterating.

---

## Step 7: Synthesize a COFF and patch the PE image

If the diff passes but relocations need to be packaged for patching, synthesize a COFF:
```console
$ x86decomp coff-synthesize games/iron-battalion/project/build/candidates/torque_actuator.bin \
    _torque_actuator \
    games/iron-battalion/project/build/patches/torque_actuator.obj \
    --architecture x86 \
    --relocations games/iron-battalion/project/build/candidates/torque_relocs.json
```

**What happens:** `coff-synthesize` creates a COFF object with the raw code bytes and specified relocations. The `--architecture x86` flag sets the machine type to `0x014C`.

Patch the PE image:
```console
$ x86decomp patch-image games/iron-battalion/project/original/iron_battalion.exe \
    games/iron-battalion/project/build/candidates/torque_actuator.bin \
    games/iron-battalion/project/build/patches/iron_battalion_patched.exe \
    --rva 0xAB100 \
    --expected-original-sha256 abc123... \
    --expected-function-sha256 def456... \
    --report games/iron-battalion/project/reports/matching/patch-report.json
```

**What happens:** `patch-image` validates the original binary's SHA-256, confirms the replacement payload's hash, overwrites the 224-byte window at RVA `0xAB100` with the new bytes, and writes the patched PE. Both `--expected-*` hashes are safety preconditions — the command fails if they don't match, preventing accidental patching of the wrong binary or wrong payload.

---

## Step 8: Verify PE integrity

```console
$ x86decomp inspect-pe games/iron-battalion/project/build/patches/iron_battalion_patched.exe
```

**What happens:** Confirms the PE header, section table, imports, and relocations remain valid. The patched binary should report identical metadata except for the modified `.text` section bytes at the patched RVA.

Byte-level comparison against the original:
```console
$ x86decomp diff-bytes games/iron-battalion/project/original/iron_battalion.exe \
    games/iron-battalion/project/build/patches/iron_battalion_patched.exe \
    --report games/iron-battalion/project/reports/matching/full-diff.json \
    --max-mismatches 1024
```

**What happens:** `diff-bytes` compares the two PE files byte-for-byte. With `--max-mismatches 1024`, reports up to 1024 differing byte offsets. Expect exactly 224 mismatches — the size of the patched function — all contiguous at the function RVA. Any additional mismatches indicate unintended corruption.

---

## Step 9: Record evidence and claims

```console
$ x86decomp evidence-add games/iron-battalion/project/ \
    --kind observed \
    --source diff-function \
    --locator "sub_4AB100:patch-v1" \
    --assertion "Function sub_4AB100 at RVA 0xAB100 produces 224 byte-identical bytes after patch" \
    --independent-group group-compiler-evidence \
    --file games/iron-battalion/project/reports/matching/torque_actuator-diff.json

$ x86decomp claim-create games/iron-battalion/project/ \
    --subject sub_4AB100 \
    --predicate "byte-identical-reconstruction" \
    --object true \
    --evidence evidence-id-from-above

$ x86decomp claim-verify games/iron-battalion/project/ claim-id
```

**What happens:** Each `evidence-add` records a provenance-bearing observation. `claim-create` links evidence to a claim. `claim-verify` evaluates whether the claim passes its evidence gate (e.g., two independent validator sources, or one exact-byte-match source).

Update the workflow state:
```console
$ x86decomp workflow-update games/iron-battalion/project/ sub_4AB100 \
    --source-stage matched \
    --matching-status exact_match \
    --candidate torque_actuator \
    --compiler-profile config/compiler-profiles/msvc2008-o2.json \
    --report-kind diff-function \
    --report-path reports/matching/torque_actuator-diff.json
```

---

## Expected state after each stage

| Stage | Key output |
|---|---|
| **init** | `project.json`, `original/iron_battalion.exe`, SQLite databases |
| **ghidra-export** | `exports/sub_4AB100/` with `function.json`, `decompiled.c`, `disassembly.jsonl`, `cfg.json` |
| **compile** | `build/candidates/torque_actuator.obj` (COFF) |
| **coff-extract** | `build/candidates/torque_actuator.bin` (224 resolved bytes) |
| **diff-function** | `reports/matching/torque_actuator-diff.json` with `match: true` |
| **patch-image** | `build/patches/iron_battalion_patched.exe` (PE with patched function) |
| **diff-bytes** | `reports/matching/full-diff.json` — exactly 224 mismatches |
| **evidence/claims** | Evidence records, verified claim |

---

## Verification checklist

- [ ] `verify-project` returns `valid: true`
- [ ] `artifact-verify` passes for the exported function directory
- [ ] `coff-inspect` shows the expected symbol name and size
- [ ] `diff-function` reports `match: true` with zero mismatches
- [ ] `patch-image` succeeds without SHA-256 precondition failure
- [ ] `inspect-pe` on the patched binary reports correct headers
- [ ] `diff-bytes` shows exactly 224 mismatches at the function RVA range
- [ ] `claim-verify` returns `status: accepted`

---

## Common failure cases and recovery

| Failure | Cause | Recovery |
|---|---|---|
| `patch-image` SHA-256 mismatch | Wrong original binary or wrong payload file | Re-calculate hashes with `inspect-pe` and `coff-inspect`, verify paths |
| `diff-function` shows trailing byte mismatches | Compiler padding differences or missing `/Gy` flag | Use `--pad-bytes-json` in the `match compare` native route, or adjust compiler profile |
| `diff-function` shows relocation mismatches | Incorrect symbol map or missing COFF relocation entries | Re-inspect with `coff-inspect`, verify relocation types in the symbol table |
| `compile` fails with unknown toolchain | Toolchain not registered | Run `toolchain-register` with the correct MSVC 2008 `cl.exe` path |
| `diff-bytes` mismatches exceed 224 | Adjacent function or padding was overwritten | Confirm RVA and size from `function.json`; re-patch with exact bounds |
| `ghidra-export` times out | Default 3600s insufficient for large binary | Pass `--timeout 7200` or larger |

---

## Related reference pages

- [Compiler Profile](../config/compiler-profile.md)
- [Toolchains](../commands/compilation/toolchains.md)
- [compile](../commands/compilation/compile.md)
- [COFF Commands](../commands/analysis/coff.md)
- [diff-function](../commands/validation/diff-function.md)
- [diff-bytes](../commands/validation/diff-bytes.md)
- [patch-image](../commands/reconstruction/patch.md)
- [Evidence and Claims](../commands/workflow/evidence-claims.md)
- [Workflow Commands](../commands/workflow/workflow.md)

---

## Optional extensions

1. **Batch patch multiple functions:** Export all functions with `--selector all`, loop through each, and apply patch-image per function. Use `work-create` and `work-queue` to distribute tasks across analysts.

2. **Relink the full image:** After patching multiple functions, use `linker-plan` with the original `.map` file and `relink` to produce a fully relinked PE. This validates the entire image, not just patched functions.

3. **Image convergence tracking:** After each patch, run `convergence-analyze` against the original to plot byte-identity convergence over time:
   ```console
   $ x86decomp convergence-analyze original.exe patched.exe \
       --history games/iron-battalion/project/reports/convergence/history.json \
       --report games/iron-battalion/project/reports/convergence/latest.json
   ```

4. **Symbolic validation:** For functions where exact matching is blocked by register allocation, use `symbolic-validate` to prove functional equivalence:
   ```console
   $ x86decomp symbolic-validate original_func.bin candidate_func.bin \
       --architecture x86 --max-steps 2000 --max-paths 128 \
       --report symbolic-report.json
   ```

5. **Dynamically validate post-patch:** Run the patched binary under `drcov-run` to collect coverage, then compare against the original's coverage log with `drcov-parse`.
