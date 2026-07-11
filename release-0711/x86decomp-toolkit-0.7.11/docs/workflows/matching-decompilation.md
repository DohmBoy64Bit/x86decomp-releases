# Matching Decompilation

**Crystal Empire** — A fictional fantasy RPG compiled for x86-64 Windows PE with GCC 4.8. The
game shipped with DWARF debug information embedded in the binary and a complete set of original
COFF objects. The team pursues full matching decompilation: byte-identical C source for every
function, verified through COFF extraction, COMDAT resolution, function diffing, patching,
and final full relink with image-match verification.

---

## Scenario

> Crystal Empire shipped in 2014 as `crystal.exe`, an x86-64 PE built with GCC 4.8 (MinGW-w64).
> Remarkably, the original build directory was preserved, including all `.o` COFF objects and
> a linker map. The team has access to the binary, all original objects, and the GCC 4.8
> toolchain. Their goal: produce byte-identical C source for every function in the `.text`
> section, achieving a `full_relink_validated` state where the relinked executable is
> bit-identical to the original.

## What you will accomplish

1. Initialize the project and export Ghidra function artifacts
2. Inspect original COFF objects for symbol and relocation metadata
3. Resolve COMDAT groups across all objects
4. Write matching C source for each function
5. Compile sources against the GCC 4.8 profile
6. Extract compiled symbols from COFF objects
7. Synthesize new COFF objects from matched byte sequences
8. Diff each compiled function against the original PE
9. Patch matched functions into the PE image
10. Execute the full relink and verify with image-match

## Prerequisites

- x86decomp 0.7.11 installed
- GCC 4.8 (MinGW-w64) toolchain registered
- The target binary `games/crystal/crystal.exe` (x86-64 PE)
- Original COFF objects in `games/crystal/objects/`
- A GCC 4.8 compiler profile

## Starting file structure

```
games/crystal/
  crystal.exe                 # The target PE (x86-64, ~8 MB)
  objects/                    # Original COFF objects from the build directory
    crt0.o
    main.o
    combat.o
    inventory.o
    questlog.o
    spellbook.o
    worldmap.o
    ... (200+ objects)

projects/crystal-decomp/      # Empty directory for the project
```

---

## Step 1: Initialize the project

```console
$ x86decomp init games/crystal/crystal.exe projects/crystal-decomp/
```

**Explanation:** `init` creates the full project layout for an x86-64 PE project.
`default_modes` is set to `["matching", "functional"]`.

**Verification:**

```console
$ x86decomp verify-project projects/crystal-decomp/
```

**Expected:** `"architecture": "x86_64"`, `"valid": true`.

---

## Step 2: Export Ghidra function artifacts

```console
$ x86decomp ghidra-export games/crystal/crystal.exe \
    ghidra-workspace/ crystal-functions/ \
    functions-export/ \
    --ghidra-home /opt/ghidra \
    --selector all \
    --overwrite \
    --report projects/crystal-decomp/reports/ghidra-export.json
```

**Explanation:** Exports decompiler output, disassembly, and control-flow graphs for every
function in the x86-64 binary. The Ghidra export provides function boundaries, symbol names
(from DWARF if parsed), and type hints that guide the matching process.

**Import artifacts:**

```console
$ x86decomp artifact-import projects/crystal-decomp/ functions-export/
```

---

## Step 3: Inspect original COFF objects

```console
$ x86decomp coff-inspect games/crystal/objects/combat.o
$ x86decomp coff-inspect games/crystal/objects/inventory.o
$ x86decomp coff-inspect games/crystal/objects/spellbook.o
```

**Explanation:** `coff-inspect` parses each COFF object and returns its full structure: machine
type (`0x8664` for x86-64), section count, symbol table (names, values, section numbers, types,
storage classes), section headers (names, sizes, raw data offsets, characteristics, COMDAT info),
and relocation entries. This is read-only static analysis — a critical first step to understand
the object layout before writing matching sources.

**Expected output per object (abbreviated):**

```json
{
  "machine": 34404,
  "architecture": "x86_64",
  "section_count": 5,
  "symbol_count": 47,
  "symbols": [
    {
      "name": "_Z14calculateArmorii",
      "value": 0,
      "section_number": 1,
      "type": 32,
      "storage_class": 2
    },
    {
      "name": "_Z8rollDicei",
      "value": 256,
      "section_number": 1,
      "type": 32,
      "storage_class": 2
    },
    ...
  ],
  "sections": [
    {
      "name": ".text",
      "size": 2048,
      "characteristics": 32,
      "comdat": null,
      "relocation_count": 12
    },
    {
      "name": ".xdata",
      "size": 128,
      "characteristics": 1073741888,
      "relocation_count": 0
    }
  ]
}
```

Key observations:
- `architecture: "x86_64"` confirms x86-64 COFF objects
- Symbol names are mangled (GCC Itanium ABI): `_Z14calculateArmorii` = `calculateArmor(int, int)`
- Sections include `.text` (code), `.xdata` (exception handling), `.rdata` (read-only data)

---

## Step 4: Resolve COMDAT groups across all objects

```console
$ x86decomp coff-comdat-resolve games/crystal/objects/crt0.o \
    games/crystal/objects/main.o \
    games/crystal/objects/combat.o \
    games/crystal/objects/inventory.o \
    games/crystal/objects/questlog.o \
    games/crystal/objects/spellbook.o \
    games/crystal/objects/worldmap.o \
    --report projects/crystal-decomp/reports/comdat-resolution.json
```

**Explanation:** `coff-comdat-resolve` parses all supplied COFF objects, identifies COMDAT
sections (sections with the `IMAGE_SCN_LNK_COMDAT` flag), and resolves duplicate COMDAT groups
by selecting one definition per group. This is critical for C++ templates and inline functions
that may appear in multiple objects — the resolution report tells you which object "wins" each
COMDAT symbol.

**Expected output:**

```json
{
  "objects_analyzed": 7,
  "comdat_groups_found": 23,
  "resolved": {
    "_ZNSt6vectorIiSaIiEE9push_backERKi": "inventory.o",
    "_ZSt4moveIRiEONSt16remove_referenceIT_E4typeEONS0_IS3_EE": "spellbook.o",
    "_ZNSsC1EPKcRKSaIcE": "questlog.o"
  },
  "unresolved": []
}
```

---

## Step 5: Write matching C source for each function

Using the Ghidra decompiler output and COFF symbol metadata, write byte-accurate C source for
the `combat` module.

Create `projects/crystal-decomp/src/matched/combat.c`:

```c
#include <stdint.h>

int32_t calculateArmor(int32_t base_armor, int32_t quality_mod) {
    int32_t result = base_armor + quality_mod;
    if (result < 0) {
        result = 0;
    }
    if (result > 100) {
        result = 100;
    }
    return result;
}

int32_t rollDice(int32_t sides) {
    if (sides <= 0) {
        return 0;
    }
    int32_t a = 1103515245;
    int32_t c = 12345;
    static int32_t seed = 1;
    seed = a * seed + c;
    int32_t roll = ((uint32_t)seed >> 16) % sides;
    return roll + 1;
}

void applyDamage(int32_t* hp, int32_t damage, int32_t armor) {
    int32_t mitigated = damage - (armor / 2);
    if (mitigated < 1) {
        mitigated = 1;
    }
    *hp -= mitigated;
    if (*hp < 0) {
        *hp = 0;
    }
}
```

!!! tip "Matching accuracy"
    For byte-accurate matching with GCC 4.8, you must replicate the original's exact type
    choices (`int32_t` vs `int`), initialization order, variable scoping, and control
    structure. Even semantically equivalent code (e.g., `if (!cond)` vs `if (cond == 0)`)
    can produce different codegen with older GCC versions.

---

## Step 6: Compile against the GCC 4.8 profile

Create `projects/crystal-decomp/config/compiler-profiles/gcc-4.8-x64-release.json`:

```json
{
  "schema_version": 1,
  "id": "gcc-4.8-x64-release",
  "executable": "C:\\MinGW\\bin\\gcc.exe",
  "arguments": [
    "-c", "-O2", "-fomit-frame-pointer", "-fno-strict-aliasing",
    "-m64", "-mno-sse", "-Wall",
    "{source}", "-o", "{output}"
  ],
  "timeout_seconds": 60,
  "output_kind": "coff_object"
}
```

Compile:

```console
$ x86decomp compile projects/crystal-decomp/config/compiler-profiles/gcc-4.8-x64-release.json \
    projects/crystal-decomp/src/matched/combat.c \
    projects/crystal-decomp/build/objects/combat.o \
    --report projects/crystal-decomp/reports/compile-combat.json \
    --extra-arg -std=c99 \
    --cache projects/crystal-decomp/build/cache
```

**Explanation:** `compile` invokes GCC 4.8 with the profile arguments plus `--extra-arg -std=c99`.
The output is a COFF object at `build/objects/combat.o`.

---

## Step 7: Extract compiled symbols from the COFF object

```console
$ x86decomp coff-extract projects/crystal-decomp/build/objects/combat.o \
    _Z14calculateArmorii \
    projects/crystal-decomp/build/candidates/calculateArmor.bin \
    --size 0x80

$ x86decomp coff-extract projects/crystal-decomp/build/objects/combat.o \
    _Z8rollDicei \
    projects/crystal-decomp/build/candidates/rollDice.bin \
    --size 0x60

$ x86decomp coff-extract projects/crystal-decomp/build/objects/combat.o \
    _Z11applyDamagePiii \
    projects/crystal-decomp/build/candidates/applyDamage.bin \
    --size 0x90
```

**Explanation:** Each function's raw bytes are extracted from the compiled COFF object. The
`--size` flag validates against the expected function size from the Ghidra export.

---

## Step 8: Synthesize COFF objects for diffing

```console
$ x86decomp coff-synthesize projects/crystal-decomp/build/candidates/calculateArmor.bin \
    _Z14calculateArmorii \
    projects/crystal-decomp/build/candidates/calculateArmor-synth.o \
    --architecture x86_64

$ x86decomp coff-synthesize projects/crystal-decomp/build/candidates/rollDice.bin \
    _Z8rollDicei \
    projects/crystal-decomp/build/candidates/rollDice-synth.o \
    --architecture x86_64

$ x86decomp coff-synthesize projects/crystal-decomp/build/candidates/applyDamage.bin \
    _Z11applyDamagePiii \
    projects/crystal-decomp/build/candidates/applyDamage-synth.o \
    --architecture x86_64
```

**Explanation:** `coff-synthesize` wraps extracted machine-code bytes into valid COFF objects with
the correct symbol names. `--architecture x86_64` sets the machine type to `0x8664`. Optionally,
use `--relocations` with a JSON relocation file to apply relocation entries if the function
contains position-dependent references.

---

## Step 9: Diff each compiled function against the original PE

Determine the RVA of each function using the Ghidra export (from `function.json` in the artifact):

```console
$ x86decomp diff-function projects/crystal-decomp/original/crystal.exe \
    0x140001000 128 \
    projects/crystal-decomp/build/candidates/calculateArmor-synth.o \
    _Z14calculateArmorii \
    --report projects/crystal-decomp/reports/matching/diff-calculateArmor.json

$ x86decomp diff-function projects/crystal-decomp/original/crystal.exe \
    0x140001080 96 \
    projects/crystal-decomp/build/candidates/rollDice-synth.o \
    _Z8rollDicei \
    --report projects/crystal-decomp/reports/matching/diff-rollDice.json

$ x86decomp diff-function projects/crystal-decomp/original/crystal.exe \
    0x1400010E0 144 \
    projects/crystal-decomp/build/candidates/applyDamage-synth.o \
    _Z11applyDamagePiii \
    --report projects/crystal-decomp/reports/matching/diff-applyDamage.json
```

**Explanation:** `diff-function` extracts the function body from the PE at the given RVA and size,
extracts the matching symbol from the COFF object, normalizes relocations (zeroing relocation
target bytes), and performs both byte-level and instruction-stream comparison. Returns a
classification: `byte_matched`, `relocation_normalized_match`, `instruction_similar`, or `mismatch`.

**Expected output for a perfect match:**

```json
{
  "classification": "byte_matched",
  "byte_comparison": {
    "match": true,
    "length": {"target": 128, "candidate": 128, "common": 128},
    "prefix": 128,
    "suffix": 0,
    "similarity": 1.0,
    "mismatches": []
  },
  "instruction_comparison": {
    "instruction_count": 32,
    "matching_instructions": 32
  },
  "normalized_similarity": 1.0
}
```

!!! warning "Relocation normalization"
    `relocation_normalized_match` means the same codegen but relocation fixups differ — this
    still counts as a matching success for most purposes. Use `instruction_similar` as the
    diagnostic level: correct compiler and flags, but the source needs further refinement.

---

## Step 10: Initialize per-function workflow states

```console
$ x86decomp workflow-init projects/crystal-decomp/ pe-rva:0140001000 --mode matching
$ x86decomp workflow-init projects/crystal-decomp/ pe-rva:0140001080 --mode matching
$ x86decomp workflow-init projects/crystal-decomp/ pe-rva:01400010E0 --mode matching
```

**Explanation:** Each function gets its own workflow with only the matching pipeline active.

Advance workflow states after byte-match verification:

```console
$ x86decomp workflow-update projects/crystal-decomp/ pe-rva:0140001000 \
    --matching-status byte_matched \
    --source-stage human_candidate \
    --candidate src/matched/combat.c \
    --compiler-profile gcc-4.8-x64-release \
    --report-kind byte_match \
    --report-path reports/matching/diff-calculateArmor.json

$ x86decomp workflow-update projects/crystal-decomp/ pe-rva:0140001080 \
    --matching-status byte_matched \
    --source-stage human_candidate \
    --candidate src/matched/combat.c \
    --compiler-profile gcc-4.8-x64-release \
    --report-kind byte_match \
    --report-path reports/matching/diff-rollDice.json

$ x86decomp workflow-update projects/crystal-decomp/ pe-rva:01400010E0 \
    --matching-status byte_matched \
    --source-stage human_candidate \
    --candidate src/matched/combat.c \
    --compiler-profile gcc-4.8-x64-release \
    --report-kind byte_match \
    --report-path reports/matching/diff-applyDamage.json
```

---

## Step 11: Patch matched functions into the PE image

```console
$ x86decomp patch-image projects/crystal-decomp/original/crystal.exe \
    projects/crystal-decomp/build/candidates/calculateArmor.bin \
    projects/crystal-decomp/build/patches/crystal-combat-patched.exe \
    --rva 0x140001000 \
    --expected-original-sha256 e3b0c44298fc1c149afbf4c8... \
    --expected-function-sha256 a1b2c3d4e5f67890... \
    --report projects/crystal-decomp/reports/patch-calculateArmor.json
```

**Explanation:** `patch-image` writes the replacement function bytes into the PE at the original
RVA. The output is a new file — the original is never modified. Chain patches for subsequent
functions, using the previous patched output as the next `ORIGINAL`.

For the next functions:

```console
$ x86decomp patch-image projects/crystal-decomp/build/patches/crystal-combat-patched.exe \
    projects/crystal-decomp/build/candidates/rollDice.bin \
    projects/crystal-decomp/build/patches/crystal-combat-patched-v2.exe \
    --rva 0x140001080 \
    --expected-function-sha256 ... \
    --report projects/crystal-decomp/reports/patch-rollDice.json

$ x86decomp patch-image projects/crystal-decomp/build/patches/crystal-combat-patched-v2.exe \
    projects/crystal-decomp/build/candidates/applyDamage.bin \
    projects/crystal-decomp/build/patches/crystal-combat-patched-v3.exe \
    --rva 0x1400010E0 \
    --expected-function-sha256 ... \
    --report projects/crystal-decomp/reports/patch-applyDamage.json
```

---

## Step 12: Relink the full image

Once all objects have matching sources, build a linker plan and relink the complete image:

```console
$ x86decomp linker-plan projects/crystal-decomp/original/crystal.exe \
    games/crystal/crystal.map \
    projects/crystal-decomp/build/objects/crt0.o \
    projects/crystal-decomp/build/objects/main.o \
    projects/crystal-decomp/build/objects/combat.o \
    projects/crystal-decomp/build/objects/inventory.o \
    projects/crystal-decomp/build/objects/questlog.o \
    projects/crystal-decomp/build/objects/spellbook.o \
    projects/crystal-decomp/build/objects/worldmap.o \
    --library projects/crystal-decomp/build/libs/libgcc.a \
    --library projects/crystal-decomp/build/libs/libmingw32.a \
    --linker lld-link \
    --output-image projects/crystal-decomp/build/relink/crystal-rebuilt.exe \
    --report projects/crystal-decomp/reports/linker-plan.json \
    --write-relink-manifest projects/crystal-decomp/build/relink/relink-manifest.json
```

Verify readiness:

```json
{
  "ready_for_relink": true,
  "unresolved": []
}
```

Execute the relink:

```console
$ x86decomp relink projects/crystal-decomp/build/relink/relink-manifest.json \
    --report projects/crystal-decomp/reports/relink-report.json
```

---

## Step 13: Compare the relinked image against the original

```console
$ x86decomp image-profile projects/crystal-decomp/original/crystal.exe \
    projects/crystal-decomp/build/relink/crystal-profile.json

$ x86decomp image-match projects/crystal-decomp/original/crystal.exe \
    projects/crystal-decomp/build/relink/crystal-rebuilt.exe \
    --profile projects/crystal-decomp/build/relink/crystal-profile.json \
    --report projects/crystal-decomp/reports/image-match.json
```

**Explanation:** `image-profile` derives a layout profile from the original. `image-match`
compares the relinked candidate against the original under that profile, producing section-level
mismatch counts.

**Byte-level verification:**

```console
$ x86decomp diff-bytes projects/crystal-decomp/original/crystal.exe \
    projects/crystal-decomp/build/relink/crystal-rebuilt.exe \
    --report projects/crystal-decomp/reports/diff-relink.json \
    --max-mismatches 256
```

**Expected: `"match": true`** — the relinked image is bit-identical to the original.

---

## Step 14: Final workflow advancement

```console
$ x86decomp workflow-update projects/crystal-decomp/ pe-rva:0140001000 \
    --matching-status full_relink_validated \
    --report-kind image_match \
    --report-path reports/image-match.json

$ x86decomp workflow-update projects/crystal-decomp/ pe-rva:0140001080 \
    --matching-status full_relink_validated \
    --report-kind image_match \
    --report-path reports/image-match.json

$ x86decomp workflow-update projects/crystal-decomp/ pe-rva:01400010E0 \
    --matching-status full_relink_validated \
    --report-kind image_match \
    --report-path reports/image-match.json
```

**Explanation:** `full_relink_validated` is the terminal matching status — the function is part
of a relinked image that is byte-identical to the original.

**Verify workflow state:**

```console
$ x86decomp workflow-show projects/crystal-decomp/ pe-rva:0140001000
```

```json
{
  "function_id": "pe-rva:0140001000",
  "selected_modes": ["matching"],
  "source_stage": "human_candidate",
  "matching_status": "full_relink_validated",
  "active_candidate": "src/matched/combat.c",
  "compiler_profile": "gcc-4.8-x64-release",
  "reports": {
    "byte_match": "reports/matching/diff-calculateArmor.json",
    "image_match": "reports/image-match.json"
  },
  "blockers": []
}
```

---

## Common failure cases and recovery

| Failure | Likely cause | Recovery |
|---|---|---|
| `diff-function` returns `mismatch` | Source is not byte-accurate | Refine the C source — check variable types, initialization order, control flow structure |
| `diff-function` returns `relocation_normalized_match` | Same codegen but relocation fixups differ | Acceptable for matching; investigate relocation differences for full fix |
| `coff-inspect` reports `architecture: "x86"` for x86-64 object | Object was compiled for wrong target | Add `-m64` flag to GCC profile arguments |
| `coff-comdat-resolve` reports unresolved COMDATs | Missing objects in the resolution set | Add all objects that participate in the link |
| `linker-plan` reports overlapping placements | Two objects claim the same MAP RVA extent | Verify MAP contributions — may be COMDAT folding artifacts |
| `relink` produces a different file size | Alignment or padding differs | Check `/FILEALIGN` and `/ALIGN` in relink manifest arguments |
| `patch-image` rejects candidate larger than original | GCC inlining or loop unrolling produced larger code | Match original optimization flags exactly; adjust source to match original codegen |

---

## Related reference pages

- [Decompilation Modes concept](../concepts/decompilation-modes.md) — Matching pipeline and statuses
- [Linker Reconstruction concept](../concepts/linker-reconstruction.md) — MAP files, COMDATs, relink manifests
- [Matching vs Functional concept](../concepts/matching-vs-functional.md) — Independent status tracking
- [Workflow Commands](../commands/workflow/workflow.md) — `workflow-init`, `workflow-show`, `workflow-update`
- [COFF Commands](../commands/analysis/coff.md) — `coff-inspect`, `coff-extract`, `coff-synthesize`, `coff-comdat-resolve`
- [diff-function command](../commands/validation/diff-function.md) — PE function to COFF symbol comparison
- [patch-image command](../commands/reconstruction/patch.md) — PE function patching
- [Linker Analysis commands](../commands/reconstruction/linker.md) — `linker-plan`
- [relink command](../commands/reconstruction/relink.md) — Full-image relinking
- [image-match command](../commands/reconstruction/image-match.md) — Whole-image comparison
- [diff-bytes command](../commands/validation/diff-bytes.md) — Byte-for-byte comparison
- [compile command](../commands/compilation/compile.md) — Compile source under a profile
- [ghidra-export command](../commands/ghidra/export.md) — Ghidra export workflow

---

## Optional extensions

1. **COFF comparison** — Compare your compiled COFF objects against the originals using
   `diff-bytes` and `coff-inspect` to verify structural identity beyond just function bytes:

   ```console
   $ x86decomp diff-bytes games/crystal/objects/combat.o \
       projects/crystal-decomp/build/objects/combat.o \
       --report reports/diff-combat-coff.json
   ```

2. **Convergence tracking** — As more objects are matched, track progress with
   `convergence-analyze`:

   ```console
   $ x86decomp convergence-analyze projects/crystal-decomp/original/crystal.exe \
       projects/crystal-decomp/build/relink/crystal-rebuilt.exe \
       --profile build/relink/crystal-profile.json \
       --previous reports/convergence-v1.json \
       --report reports/convergence-v2.json \
       --history reports/convergence-history.jsonl
   ```

3. **objdiff integration** — Create an objdiff manifest to visually compare original vs compiled
   COFF objects:

   ```console
   $ x86decomp objdiff-run objdiff-manifest.json --report reports/objdiff.json
   ```

4. **Release-gate acceptance** — When all functions reach `full_relink_validated`, pass the
   release gate:

   ```console
   $ x86decomp release-gate projects/crystal-decomp/ \
       --convergence-report reports/convergence-final.json \
       --require-workflows \
       --require-verified-claims \
       --report reports/release-gate.json
   ```

5. **Debug symbol recovery** — If the binary has embedded DWARF or a companion PDB, use
   `pdb-inspect` to cross-reference symbol names and source file paths, then feed recovered
   names into `workflow-init` as function IDs:

   ```console
   $ x86decomp pdb-inspect games/crystal/crystal.pdb --pe games/crystal/crystal.exe
   ```
