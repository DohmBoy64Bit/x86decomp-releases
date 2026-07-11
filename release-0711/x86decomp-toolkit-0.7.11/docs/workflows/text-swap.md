# Text Swap

**Technical objective:** Canonical text-swap workflow for embedded string replacement in a PE binary — string table identification, replacement build, injection, and verification with PE integrity checking.

**Game:** Rising Phoenix (fictional 2D fighting game, x86 PE32, embedded strings in `.rdata`, `.text` references via immediate operands).

---

## Overview

Rising Phoenix embeds all UI strings (character names, move lists, menu labels, combo announcements) directly in the `.rdata` section. The team wants to produce a localization patch that swaps English strings to Japanese without recompiling the full binary. Because `.text` section references to `.rdata` are via absolute addresses and relative displacements, a naive hex-editor copy risks corrupting the instruction stream. The text-swap workflow plans, builds, injects, and verifies the swap with full relocation awareness.

You will learn:

1. How to export PE sections and inventory the image structure.
2. How to identify string tables with `metadata-scan` and `inspect-pe`.
3. How to plan a text swap with the `text-swap plan` canonical command.
4. How to build replacement data and inject it into the PE.
5. How to verify the patched image and confirm PE integrity.

---

## Prerequisites

| Requirement | Detail |
|---|---|
| **Binary** | `games/rising-phoenix/rising_phoenix.exe` — PE32 x86, 3.1 MB |
| **Ghidra** | Ghidra 11.2+ for `ghidra-export` of the `.rdata` section |
| **Project** | `games/rising-phoenix/project/` |

---

## Starting directory structure

```
games/rising-phoenix/
├── rising_phoenix.exe
├── exports/
│   └── (Ghidra export output)
├── replacements/
│   ├── strings_en.json            # extracted English strings
│   └── strings_ja.json            # replacement Japanese strings
├── swap/
│   ├── plan.json                  # text-swap plan
│   ├── built_replacement.bin      # built replacement data
│   └── injected.exe               # patched image
└── project/
    ├── project.json
    ├── original/
    │   └── rising_phoenix.exe
    └── reports/
        └── text-swap/
```

---

## Step 1: Initialize project and export Ghidra artifacts

```console
$ x86decomp init games/rising-phoenix/rising_phoenix.exe games/rising-phoenix/project/
$ x86decomp ghidra-export games/rising-phoenix/rising_phoenix.exe \
    games/rising-phoenix/ghidra-project/ rising_phoenix \
    games/rising-phoenix/exports/ \
    --ghidra-home "C:\ghidra_11.2_PUBLIC" --overwrite

$ x86decomp artifact-import games/rising-phoenix/project/ games/rising-phoenix/exports/
```

---

## Step 2: Inspect PE and identify sections

```console
$ x86decomp inspect-pe games/rising-phoenix/rising_phoenix.exe
```

Focus on the section layout. Key output excerpt:
```json
{
  "sections": [
    {"name": ".text", "virtual_address": 4096, "virtual_size": 196608, "characteristics": "CODE|EXECUTE|READ"},
    {"name": ".rdata", "virtual_address": 200704, "virtual_size": 65536, "characteristics": "INITIALIZED_DATA|READ"},
    {"name": ".data", "virtual_address": 266240, "virtual_size": 16384, "characteristics": "INITIALIZED_DATA|READ|WRITE"},
    {"name": ".rsrc", "virtual_address": 282624, "virtual_size": 8192, "characteristics": "INITIALIZED_DATA|READ"}
  ]
}
```

Also run the canonical `pe inventory` to get a rich image summary:
```console
$ x86decomp pe inventory games/rising-phoenix/rising_phoenix.exe --project games/rising-phoenix/project/
```

---

## Step 3: Export PE sections and scan metadata

Export the `.rdata` section for string analysis:
```console
$ x86decomp pe export-sections games/rising-phoenix/rising_phoenix.exe \
    games/rising-phoenix/project/build/sections/ \
    --section .rdata --section .text \
    --project games/rising-phoenix/project/
```

**What happens:** The canonical `pe export-sections` command extracts raw section data from the PE image. The `--section` flag selects specific sections by name. Output goes to `build/sections/` as individual binary files.

Scan metadata to find string references:
```console
$ x86decomp metadata-scan games/rising-phoenix/rising_phoenix.exe \
    --report games/rising-phoenix/project/reports/text-swap/metadata.json \
    --project games/rising-phoenix/project/
```

**What happens:** `metadata-scan` identifies data references, string tables, and cross-references between `.text` and `.rdata`. The report includes:
- String boundaries in `.rdata`
- Immediate operand values in `.text` that reference `.rdata` addresses
- Relocation entries for string pointers

Inspect COFF objects if available:
```console
$ x86decomp coff-inspect games/rising-phoenix/project/build/sections/.rdata.bin
```

---

## Step 4: Plan the text swap

```console
$ x86decomp text-swap plan games/rising-phoenix/rising_phoenix.exe \
    games/rising-phoenix/replacements/strings_ja.json \
    games/rising-phoenix/swap/plan.json \
    --section-name .rdata \
    --project games/rising-phoenix/project/
```

**What happens:** `text-swap plan` analyzes the original PE and the replacement data, then produces a plan JSON that records:

- **Original string offsets, lengths, and hashes** in `.rdata`
- **Replacement string data** with target offsets
- **Overflow handling:** Strings longer than the originals are tracked; shorter ones are padded
- **Reference updates:** Any `.text` section offsets that must be modified because a string's absolute address changed
- **Section layout impact:** Whether the swap changes `.rdata` size (and thus shifts subsequent sections)

Example plan excerpt:
```json
{
  "section_name": ".rdata",
  "original_size": 65536,
  "replacement_size": 65536,
  "strings": [
    {
      "original_offset": 512,
      "original_length": 24,
      "original_sha256": "abc123...",
      "original_text": "Character Select\0",
      "replacement_offset": 512,
      "replacement_length": 24,
      "replacement_text": "キャラ選択\0\0\0\0\0\0\0\0",
      "overflow": false
    }
  ],
  "reference_updates": [
    {"section": ".text", "rva": 65540, "original_value": 201216, "new_value": 201216, "kind": "absolute"}
  ],
  "layout_changes": []
}
```

!!! note "In-place swap when sizes match"
    If every replacement fits within its original string's byte bounds, the swap is in-place — no section resizing, no `.text` reference updates. Only the `.rdata` section bytes change.

---

## Step 5: Build replacement data

```console
$ x86decomp text-swap build games/rising-phoenix/replacements/strings_ja.json \
    games/rising-phoenix/swap/built_replacement.bin \
    --original games/rising-phoenix/rising_phoenix.exe \
    --section-name .rdata \
    --project games/rising-phoenix/project/
```

**What happens:** `text-swap build` reads the original `.rdata` section bytes, applies the replacement strings at their target offsets, pads or truncates as needed, and writes a complete replacement section binary. If the replacement data is larger than the original section, the build reports an overflow error — section resizing requires a full relink.

Inspect the built replacement:
```console
$ x86decomp coff-inspect games/rising-phoenix/swap/built_replacement.bin
```

---

## Step 6: Inject the replacement

```console
$ x86decomp text-swap inject games/rising-phoenix/swap/plan.json \
    --output games/rising-phoenix/swap/injected.exe \
    --project games/rising-phoenix/project/
```

**What happens:** `text-swap inject` reads the plan, the original PE, and the built replacement data, then:

1. Copies the original PE to the output path.
2. Overwrites the `.rdata` section with the replacement bytes.
3. Applies any `.text` reference updates (for absolute addresses that shifted).
4. Recalculates the PE checksum.
5. Updates section hashes in the plan.

If `--output` is not specified, the command reports the injection plan without modifying any files (dry-run mode).

---

## Step 7: Verify the injected image

```console
$ x86decomp text-swap verify games/rising-phoenix/swap/plan.json \
    games/rising-phoenix/swap/injected.exe \
    --output games/rising-phoenix/project/reports/text-swap/verify.json \
    --project games/rising-phoenix/project/
```

**What happens:** `text-swap verify` validates the injected image against the plan:

- Every replacement string appears at its declared offset
- No unexpected bytes were modified outside the planned regions
- PE headers remain valid (run `inspect-pe` internally)
- Section sizes and alignments are preserved
- Import/export tables are intact
- No reference-update targets point outside valid section bounds

Inspecting the injected PE externally:
```console
$ x86decomp inspect-pe games/rising-phoenix/swap/injected.exe
```

Byte diff against the original:
```console
$ x86decomp diff-bytes games/rising-phoenix/rising_phoenix.exe \
    games/rising-phoenix/swap/injected.exe \
    --report games/rising-phoenix/project/reports/text-swap/diff.json \
    --max-mismatches 200000
```

**What happens:** The diff report should show mismatches only in the `.rdata` section at the declared string offsets, plus any `.text` reference updates. Any mismatches outside these regions indicate corruption.

---

## Step 8: Record evidence

```console
$ x86decomp evidence-add games/rising-phoenix/project/ \
    --kind observed \
    --source text-swap \
    --locator "rising_phoenix.exe:text-swap-ja-v1" \
    --assertion "87 strings swapped in .rdata; 0 .text reference updates required (all strings fit in-place); injected image passes PE integrity" \
    --independent-group group-text-swap \
    --file games/rising-phoenix/project/reports/text-swap/verify.json

$ x86decomp memory-add games/rising-phoenix/project/ \
    --actor localization-team \
    --category text-swap \
    --summary "Japanese localization v1: 87 strings swapped in-place, zero overflows" \
    --details-json '{"strings_swapped": 87, "overflows": 0, "section": ".rdata"}'
```

---

## Expected state after each stage

| Stage | Key output |
|---|---|
| **init + ghidra-export** | Project tree, exported function artifacts |
| **inspect-pe + pe inventory** | PE section layout, import/export tables |
| **pe export-sections** | Raw `.rdata` and `.text` binary files in `build/sections/` |
| **metadata-scan** | String boundaries, cross-references report |
| **text-swap plan** | `swap/plan.json` — offsets, lengths, reference updates |
| **text-swap build** | `swap/built_replacement.bin` — replacement `.rdata` section |
| **text-swap inject** | `swap/injected.exe` — patched PE image |
| **text-swap verify** | Verification report — all strings confirmed, PE valid |
| **diff-bytes** | Diff report showing mismatches only in planned regions |

---

## Verification checklist

- [ ] `inspect-pe` on the injected image shows identical headers (except checksum)
- [ ] All 87 strings in the plan appear at their declared offsets in the injected image
- [ ] `diff-bytes` mismatches are confined to `.rdata` string regions and any `.text` reference updates
- [ ] Section sizes unchanged (all replacements fit in-place)
- [ ] Import table, export table, and resource directory intact
- [ ] PE checksum recalculated after injection
- [ ] `text-swap verify` returns `valid: true`

---

## Common failure cases and recovery

| Failure | Cause | Recovery |
|---|---|---|
| `text-swap plan` reports overflows | Japanese strings longer than English originals | Shorten translations, or use shorter Japanese phrases; alternatively, accept overflow and plan for relink |
| `text-swap build` fails with size error | Replacement section exceeds original `.rdata` bounds | Reduce string lengths, or use `linker-plan` + `relink` for full section resize |
| `text-swap inject` corrupts `.text` | Reference update targeted wrong RVA | Re-check the plan's `reference_updates` list; verify with `disassemble` on the region |
| `inspect-pe` on injected image fails | Section header or data directory corrupted | Restore from original, verify the plan does not touch PE header fields |
| `diff-bytes` shows unexpected mismatches | Injection wrote outside planned byte ranges | Check plan for incorrect offsets; re-export sections and compare |
| Strings appear garbled in patched binary | Encoding mismatch (Shift-JIS vs UTF-8) | Verify the replacement JSON uses the exact encoding expected by the game engine |

---

## Related reference pages

- [inspect-pe / pdb-inspect](../commands/analysis/pe-pdb.md)
- [metadata-scan](../commands/analysis/metadata.md)
- [COFF Commands](../commands/analysis/coff.md)
- [diff-bytes](../commands/validation/diff-bytes.md)
- [Canonical Commands](../commands/canonical.md)
- [Linker Analysis](../commands/reconstruction/linker.md)

---

## Optional extensions

1. **Multi-language batch swap:** Create separate plans for Japanese, Korean, and Chinese, then run `text-swap inject` for each against a fresh copy of the original. Verify all with `text-swap verify`.

2. **Text overflow with relink:** If strings overflow the original `.rdata` section, use `linker-plan` to build a reconstruction plan that resizes `.rdata`, then `relink` to produce a full relinked PE with the expanded section.

3. **Coff export from sections:** Use the canonical `pe export-coff` route to extract `.rdata` as a COFF object, enabling symbol-level inspection of string data:
   ```console
   $ x86decomp pe export-coff games/rising-phoenix/rising_phoenix.exe \
       games/rising-phoenix/project/build/coff-export/ \
       --section .rdata \
       --project games/rising-phoenix/project/
   ```

4. **String reference cross-checking:** Load the original and injected images in Ghidra, use `crosscheck-ghidra` to verify that all `.text` instructions referencing `.rdata` still point to the correct strings.

5. **Dynamic validation:** Run the injected binary (with authorization) under `drcov-run` and verify that the string-using code paths execute without crashes:
   ```console
   $ x86decomp drcov-run games/rising-phoenix/swap/injected.exe \
       games/rising-phoenix/project/reports/text-swap/coverage/ \
       --timeout 30 --report coverage-report.json
   ```
