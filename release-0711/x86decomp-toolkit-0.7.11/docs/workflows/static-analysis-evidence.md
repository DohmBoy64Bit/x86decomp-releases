# Static-Analysis Evidence

**Technical objective:** End-to-end static analysis of an x86-64 PE binary — PE inspection, PDB correlation, MSVC metadata recovery, linker layout reconstruction, COFF COMDAT resolution, compilation validation, and evidence-gated claim creation.

**Game:** Wild Frontier (fictional open-world game, x86-64 PE32+, 18 MB executable, MSVC 2019, PDB available, `.map` file available).

---

## Overview

Wild Frontier shipped with a full PDB and a preserved `.map` file — an ideal candidate for thorough static analysis. The team needs to establish ground truth about the binary's compiler, linker, RTTI, exception handling, and section-to-object mapping before any decompilation begins. Every finding is recorded as provenance-bearing evidence that feeds into verified claims.

You will learn:

1. How to extract PE/PDB metadata and cross-reference them.
2. How to scan MSVC metadata (RTTI, vtables, unwind, TLS).
3. How to reconstruct linker layout from PE, `.map`, and COFF objects.
4. How to resolve COMDAT groups across multiple COFF objects.
5. How to validate findings by compiling and diffing.
6. How to build an evidence chain culminating in verified claims.

---

## Prerequisites

| Requirement | Detail |
|---|---|
| **Binary** | `games/wild-frontier/wild_frontier.exe` — PE32+ x86-64, 18 MB |
| **PDB** | `games/wild-frontier/wild_frontier.pdb` — MSF 7.0 format |
| **Linker map** | `games/wild-frontier/wild_frontier.map` — MSVC `/MAP` output |
| **COFF objects** | `games/wild-frontier/objects/` — 47 objects from the build tree |
| **Project** | `games/wild-frontier/project/` |

---

## Starting directory structure

```
games/wild-frontier/
├── wild_frontier.exe
├── wild_frontier.pdb
├── wild_frontier.map
├── objects/
│   ├── engine.obj
│   ├── renderer.obj
│   ├── world.obj
│   └── ...
├── exports/
│   └── (Ghidra export output)
└── project/
    ├── project.json
    ├── original/
    ├── analysis/
    ├── evidence/
    └── reports/
        └── analysis/
```

---

## Step 1: Initialize project and inspect the PE

```console
$ x86decomp init games/wild-frontier/wild_frontier.exe games/wild-frontier/project/
$ x86decomp inspect-pe games/wild-frontier/wild_frontier.exe
```

**What happens:** `inspect-pe` extracts the full PE32+ structure: machine type (`0x8664`), section table (`.text`, `.rdata`, `.data`, `.pdata`, `.xdata`, `.rsrc`), image base (`0x140000000`), imports, exports, TLS directory, exception directory, and debug directory.

Record the PE inspection as evidence:
```console
$ x86decomp evidence-add games/wild-frontier/project/ \
    --kind observed \
    --source inspect-pe \
    --locator "wild_frontier.exe:pe-header" \
    --assertion "PE32+ x86-64, 6 sections, image base 0x140000000, entry at RVA 0x1000, subsystem Windows GUI" \
    --independent-group group-pe-analysis
```

---

## Step 2: Inspect the PDB and match to PE

```console
$ x86decomp pdb-inspect games/wild-frontier/wild_frontier.pdb \
    --pe games/wild-frontier/wild_frontier.exe
```

**What happens:** `pdb-inspect` decodes MSF 7.0 streams: DBI (source files, sections), public symbols (277 exported names), type info (TPI stream — 12,400 types, 840 UDTs), and the PE match check. The `--pe` flag compares the PDB's embedded GUID+age against the PE debug directory.

Key findings from output:
- `pe_match.matched: true` — PDB built for this exact binary
- `dbi.sources` — 340 source files across 14 directories
- `public_symbols` — 277 named functions and globals
- `type_info.types_found: 12400` — rich type information available

Record the PDB match:
```console
$ x86decomp evidence-add games/wild-frontier/project/ \
    --kind observed \
    --source pdb-inspect \
    --locator "wild_frontier.pdb:match" \
    --assertion "PDB GUID matches PE debug directory; 277 public symbols, 340 source files, 12400 types" \
    --independent-group group-pdb-analysis
```

---

## Step 3: Scan MSVC metadata

```console
$ x86decomp metadata-scan games/wild-frontier/wild_frontier.exe \
    --object games/wild-frontier/objects/engine.obj \
    --object games/wild-frontier/objects/renderer.obj \
    --map games/wild-frontier/wild_frontier.map \
    --report games/wild-frontier/project/reports/analysis/metadata.json
```

**What happens:** `metadata-scan` recovers bounded MSVC metadata from the PE and linked object files:
- **RTTI:** `RTTICompleteObjectLocator` structures, type descriptors, class hierarchy descriptors
- **Vtables:** Virtual function table arrays with their RVA and associated class names (from RTTI)
- **Unwind:** `.pdata`/`.xdata` entries — `RUNTIME_FUNCTION` records, `UNWIND_INFO` structures
- **TLS:** Thread-local storage directory and callback arrays
- **Initializers:** `.CRT` section — `__xc_a`/`__xc_z` ranges for static constructors
- **SEH:** Exception handler tables

Record metadata findings:
```console
$ x86decomp evidence-add games/wild-frontier/project/ \
    --kind derived \
    --source metadata-scan \
    --locator "wild_frontier.exe:msvc-metadata" \
    --assertion "48 RTTI CompleteObjectLocators found; 22 vtable arrays identified; 340 UNWIND_INFO entries" \
    --independent-group group-metadata \
    --file games/wild-frontier/project/reports/analysis/metadata.json
```

---

## Step 4: Inspect the linker map

```console
$ x86decomp map-inspect games/wild-frontier/wild_frontier.map
```

**What happens:** `map-inspect` parses the MSVC-compatible linker map, extracting:
- **Section contributions:** Which `.obj` contributed to each section and how many bytes
- **Symbol table:** Every public symbol with its RVA and section
- **Load address:** The image base and entry point
- **Discarded sections:** Sections eliminated by `/OPT:REF` or `/OPT:ICF`

Record map findings:
```console
$ x86decomp evidence-add games/wild-frontier/project/ \
    --kind observed \
    --source map-inspect \
    --locator "wild_frontier.map:sections" \
    --assertion "Linker map parsed: 14 object files contribute to .text, 47 total objects, entry at 0x1000" \
    --independent-group group-linker-analysis
```

---

## Step 5: Reconstruct linker layout

```console
$ x86decomp layout-reconstruct games/wild-frontier/wild_frontier.exe \
    games/wild-frontier/wild_frontier.map \
    games/wild-frontier/objects/engine.obj \
    games/wild-frontier/objects/renderer.obj \
    games/wild-frontier/objects/world.obj \
    --report games/wild-frontier/project/reports/analysis/layout.json
```

**What happens:** `layout-reconstruct` correlates three data sources:
1. PE section table (virtual addresses, sizes, and raw offsets)
2. Linker map contributions (object name → section → byte range)
3. COFF object metadata (section names, symbol offsets, COMDAT groups)

The report maps every COFF symbol to its PE RVA, validates that section boundaries are consistent across all three sources, and identifies any contributions from missing objects.

Inspect a COFF object for cross-reference:
```console
$ x86decomp coff-inspect games/wild-frontier/objects/engine.obj
```

Record the layout reconstruction:
```console
$ x86decomp evidence-add games/wild-frontier/project/ \
    --kind derived \
    --source layout-reconstruct \
    --locator "wild_frontier.exe:layout" \
    --assertion "Full section-to-object mapping reconstructed for 47 objects; all section boundaries consistent" \
    --independent-group group-layout \
    --file games/wild-frontier/project/reports/analysis/layout.json
```

---

## Step 6: Inspect libraries and resolve COMDATs

Inspect a static library:
```console
$ x86decomp lib-inspect games/wild-frontier/objects/world.lib
```

**What happens:** `lib-inspect` parses COFF archive (`.lib`) headers, member offsets, and symbol indices. Useful for identifying which library members (and thus which source files with `/Gy`) contributed COMDAT groups.

Resolve COMDAT groups across COFF objects:
```console
$ x86decomp coff-comdat-resolve \
    games/wild-frontier/objects/engine.obj \
    games/wild-frontier/objects/renderer.obj \
    games/wild-frontier/objects/world.obj \
    --report games/wild-frontier/project/reports/analysis/comdats.json
```

**What happens:** `coff-comdat-resolve` analyzes COMDAT group definitions across multiple objects, matches `IMAGE_COMDAT_SELECT_ANY` duplicates, identifies which object "won" the link (first in link order), and which were discarded. This is essential for understanding which version of a `/Gy`-compiled function actually appears in the final PE.

Record COMDAT resolution:
```console
$ x86decomp evidence-add games/wild-frontier/project/ \
    --kind derived \
    --source coff-comdat-resolve \
    --locator "objects:comdat-resolution" \
    --assertion "31 COMDAT groups resolved across 47 objects; 14 duplicates identified with clear link-order winner" \
    --independent-group group-linker-analysis \
    --file games/wild-frontier/project/reports/analysis/comdats.json
```

---

## Step 7: Compile and validate against ground truth

With the compiler identified as MSVC 2019, validate by compiling a known pattern:

```console
$ x86decomp compile games/wild-frontier/project/config/compiler-profiles/msvc2019-x64.json \
    games/wild-frontier/project/src/staging/prologue_pattern.c \
    games/wild-frontier/project/build/candidates/prologue_test.obj \
    --report games/wild-frontier/project/reports/analysis/compile-validation.json
```

Compare byte ranges:
```console
$ x86decomp diff-bytes games/wild-frontier/project/original/wild_frontier.exe \
    games/wild-frontier/project/build/candidates/prologue_test.obj \
    --report games/wild-frontier/project/reports/analysis/prologue-diff.json
```

For a specific function match:
```console
$ x86decomp diff-function games/wild-frontier/wild_frontier.exe \
    0x1500 96 \
    games/wild-frontier/project/build/candidates/prologue_test.obj \
    _function_pattern \
    --report games/wild-frontier/project/reports/analysis/func-diff.json
```

Record the validation results:
```console
$ x86decomp evidence-add games/wild-frontier/project/ \
    --kind corroborated \
    --source diff-function \
    --locator "func:prologue_pattern" \
    --assertion "Prologue pattern at RVA 0x1500 confirmed 96 bytes byte-identical under MSVC 2019 /O2 /GS-" \
    --independent-group group-compiler-validation \
    --file games/wild-frontier/project/reports/analysis/func-diff.json
```

---

## Step 8: Create and verify claims

Synthesize the static analysis evidence into claims:

```console
$ x86decomp claim-create games/wild-frontier/project/ \
    --subject "wild_frontier.exe" \
    --predicate "compiler-identity" \
    --object "MSVC 2019 (19.29.30151) /O2 /GS- /Gy /MT" \
    --evidence ev-compiler-1 ev-compiler-2

$ x86decomp claim-create games/wild-frontier/project/ \
    --subject "wild_frontier.exe" \
    --predicate "pdb-matched" \
    --object true \
    --evidence ev-pdb-1

$ x86decomp claim-create games/wild-frontier/project/ \
    --subject "wild_frontier.exe" \
    --predicate "section-layout-reconstructed" \
    --object "47 objects mapped to 6 PE sections" \
    --evidence ev-layout-1
```

Attach additional evidence to existing claims:
```console
$ x86decomp claim-attach games/wild-frontier/project/ claim-compiler ev-metadata-1
```

Verify each claim:
```console
$ x86decomp claim-verify games/wild-frontier/project/ claim-compiler
$ x86decomp claim-verify games/wild-frontier/project/ claim-pdb
$ x86decomp claim-verify games/wild-frontier/project/ claim-layout
```

**What happens:** `claim-verify` evaluates whether each claim has sufficient independent evidence from distinct sources. A claim with one piece of evidence is `corroborated` (one source). A claim with two or more independent pieces (e.g., `diff-function` + `metadata-scan` + `compile`) can reach `accepted` status.

Add contradictory evidence (for rigor):
```console
$ x86decomp claim-contradict games/wild-frontier/project/ claim-compiler ev-alternate-compiler
```

**What happens:** `claim-contradict` attaches evidence that contradicts an existing claim. This does not auto-reject the claim — it forces re-evaluation. Run `claim-verify` again to see if the claim now requires additional corroborating evidence.

---

## Expected state after each stage

| Stage | Artifacts created |
|---|---|
| **inspect-pe** | PE header report, evidence record `ev-pe-*` |
| **pdb-inspect** | PDB decode report with PE match status, evidence record |
| **metadata-scan** | `reports/analysis/metadata.json` — RTTI, vtables, unwind, TLS |
| **map-inspect** | Linker map parse report, evidence record |
| **layout-reconstruct** | `reports/analysis/layout.json` — full section-to-object map |
| **coff-comdat-resolve** | `reports/analysis/comdats.json` — COMDAT group resolution |
| **compile + diff-bytes/diff-function** | Compilation report, byte-diff report |
| **claim-create + claim-verify** | Claims with `accepted` or `corroborated` status |

---

## Verification checklist

- [ ] `inspect-pe` confirms PE32+ x86-64 with 6 sections
- [ ] `pdb-inspect --pe` returns `pe_match.matched: true`
- [ ] `metadata-scan` produces a non-empty RTTI, vtable, and unwind report
- [ ] `map-inspect` parses all section contributions
- [ ] `layout-reconstruct` output has zero section-boundary violations
- [ ] `coff-comdat-resolve` resolves all COMDAT groups without errors
- [ ] `compile` succeeds under the identified compiler profile
- [ ] `diff-function` or `diff-bytes` shows the exact match count
- [ ] All evidence records have `--independent-group` values that diversify verification
- [ ] At least one claim reaches `accepted` status via `claim-verify`

---

## Common failure cases and recovery

| Failure | Cause | Recovery |
|---|---|---|
| `pdb-inspect` reports `pe_match.matched: false` | Wrong PDB for this PE | Locate correct PDB with matching GUID+age |
| `metadata-scan` returns empty RTTI | Binary compiled with `/GR-` (no RTTI) | Accept as a finding — record as evidence of RTTI disabled |
| `layout-reconstruct` reports section-boundary violations | Missing object files or map/PE mismatch | Include all objects from the build tree; verify map matches PE build |
| `coff-comdat-resolve` has unresolvable groups | Objects from different builds or missing members | Provide the full object set from the original link command line |
| `compile` fails with compiler profile mismatch | Toolchain not registered or wrong flags | Use `compiler-lab` to matrix-test flags until the pattern matches |
| `claim-verify` returns `rejected` | Contradictory evidence attached | Review contradictions, provide additional independent evidence |

---

## Related reference pages

- [inspect-pe / pdb-inspect](../commands/analysis/pe-pdb.md)
- [COFF Commands](../commands/analysis/coff.md)
- [metadata-scan](../commands/analysis/metadata.md)
- [Linker Analysis](../commands/reconstruction/linker.md)
- [Evidence and Claims](../commands/workflow/evidence-claims.md)
- [compile](../commands/compilation/compile.md)
- [diff-bytes](../commands/validation/diff-bytes.md)
- [diff-function](../commands/validation/diff-function.md)

---

## Optional extensions

1. **C++ recovery from metadata:** Use `cpp-recover` to transform the metadata-scan output into class hierarchies:
   ```console
   $ x86decomp cpp-recover games/wild-frontier/wild_frontier.exe \
       --metadata-report games/wild-frontier/project/reports/analysis/metadata.json \
       --report games/wild-frontier/project/reports/analysis/cpp-model.json
   ```

2. **Image profiling:** Create a layout profile for whole-image comparison:
   ```console
   $ x86decomp image-profile games/wild-frontier/wild_frontier.exe \
       games/wild-frontier/project/reports/analysis/layout-profile.json
   ```

3. **Dynamic cross-validation:** Generate an execution harness and validate specific functions:
   ```console
   $ x86decomp harness-generate config/harnesses/abi-contract.json \
       games/wild-frontier/project/tests/harnesses/test_harness.c
   $ x86decomp dynamic-validate original.exe candidate.exe \
       games/wild-frontier/project/tests/harnesses/test_harness.c \
       --report dynamic-validation.json
   ```

4. **COFF export from PE sections:** Use the canonical `pe export-coff` route to extract COFF objects directly from PE sections for comparison with build-tree objects.

5. **Cross-reference Ghidra analysis:** Import the Ghidra export artifacts and cross-check disassembly:
   ```console
   $ x86decomp crosscheck-ghidra exports/disassembly.jsonl \
       games/wild-frontier/project/original/wild_frontier.exe \
       --base 0x140001000 --architecture x86_64 \
       --report crosscheck.json
   ```
