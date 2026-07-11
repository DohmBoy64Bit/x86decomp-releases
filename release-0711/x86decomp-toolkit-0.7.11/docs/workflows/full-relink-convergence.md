# Full Relink Convergence

**Graveyard Shift** — A fictional survival horror game compiled for x86 Windows PE. The game
shipped with a linker MAP file and several pre-built static libraries. The decompilation team
has matched most functions and needs to reconstruct the original link order, relink the entire
executable, and measure byte-level convergence toward the original.

---

## Scenario

> Graveyard Shift shipped in 2002 with `ghost.exe` and a companion `ghost.map` produced by the
> MSVC linker. The team has access to the MAP file, several original COFF objects recovered from
> a partial source leak, and the complete set of import libraries. After months of matching work,
> 73% of `.text` functions compile to byte-identical COFF objects. They now need to reconstruct
> the linker layout, build a relink manifest, relink the full image, and track convergence over
> time as more functions are matched.

## What you will accomplish

1. Parse the PE binary and linker MAP file
2. Reconstruct the linker layout — correlate sections, MAP contributions, and COFF objects
3. Build a grounded linker reconstruction plan
4. Write a relink manifest from the plan
5. Compile all matched source files into COFF objects
6. Extract and synthesize COFF objects for unmatched functions
7. Relink the full executable from the manifest
8. Derive an image layout profile and compare whole images
9. Analyze convergence and append to the history ledger

## Prerequisites

- x86decomp 0.7.11 installed
- `lld-link` available on PATH
- The target binary `games/graveyard/ghost.exe` (x86 PE)
- The linker MAP file `games/graveyard/ghost.map`
- COFF objects in `build/objects/` (matched + extracted)
- Import libraries in `build/libs/`

## Starting file structure

```
games/graveyard/
  ghost.exe                  # The target PE (x86, ~6 MB)
  ghost.map                  # MSVC linker MAP file
  ghost.pdb                  # Optional PDB (if available)

projects/graveyard-decomp/   # Decompilation project
  original/
    ghost.exe                 # Copied from games/graveyard/
    ghost.map                 # Copied from games/graveyard/
  src/
    matched/                  # Byte-matched C sources for each function
      crt0.c
      main.c
      renderer.c
      physics.c
      ...
  build/
    objects/                  # Compiled COFF objects
      crt0.obj
      main.obj
      renderer.obj
      physics.obj
      ...
    libs/                     # Import libraries
      kernel32.lib
      user32.lib
      d3d8.lib
    compiler/
    candidates/
    patches/
    relink/
  config/
    compiler-profiles/
      msvc-2002-x86-release.json
```

---

## Step 1: Parse the PE binary

```console
$ x86decomp inspect-pe projects/graveyard-decomp/original/ghost.exe
```

**Explanation:** `inspect-pe` parses the PE headers, extracts sections (`.text`, `.rdata`, `.data`,
`.rsrc`, `.reloc`), import/export tables, resources, relocations, and architecture. Key fields for
linker reconstruction: `image_base`, `size_of_image`, `entry_rva`, `sections` (names, RVAs, sizes,
characteristics), `subsystem`.

**Key output fields noted:**

```json
{
  "architecture": "x86",
  "machine": 332,
  "image_base": 4194304,
  "entry_rva": 4096,
  "size_of_image": 6291456,
  "number_of_sections": 5,
  "sections": [
    {"name": ".text", "virtual_address": 4096, "virtual_size": 3145728},
    {"name": ".rdata", "virtual_address": 3149824, "virtual_size": 524288},
    {"name": ".data", "virtual_address": 3674112, "virtual_size": 131072},
    {"name": ".rsrc", "virtual_address": 3805184, "virtual_size": 65536},
    {"name": ".reloc", "virtual_address": 3870720, "virtual_size": 131072}
  ],
  "subsystem": 2
}
```

Subsystem `2` = Windows GUI.

---

## Step 2: Parse the linker MAP file

```console
$ x86decomp map-inspect projects/graveyard-decomp/original/ghost.map
```

**Explanation:** `map-inspect` parses an MSVC-compatible linker MAP file (produced with `/MAP`)
and emits structured metadata: timestamp, preferred load address, section contributions from
each object, public symbol names and RVAs, entry point, and object link order.

**Key output fields:**

```json
{
  "timestamp": "2002-10-15T18:30:00Z",
  "preferred_load_address": 4194304,
  "entry_point": 4096,
  "object_order": [
    "crt0.obj", "main.obj", "renderer.obj", "physics.obj",
    "audio.obj", "input.obj", "d3d8.lib", "kernel32.lib", "user32.lib"
  ],
  "contributions": [
    {
      "object": "crt0.obj",
      "section": ".text",
      "rva": 4096,
      "end_rva": 4608,
      "length": 512
    },
    ...
  ],
  "public_symbols": [
    {"name": "_WinMain@16", "rva": 4352},
    {"name": "?RenderFrame@@YAXXZ", "rva": 8192},
    ...
  ]
}
```

---

## Step 3: Reconstruct the linker layout

```console
$ x86decomp layout-reconstruct projects/graveyard-decomp/original/ghost.exe \
    projects/graveyard-decomp/original/ghost.map \
    projects/graveyard-decomp/build/objects/crt0.obj \
    projects/graveyard-decomp/build/objects/main.obj \
    projects/graveyard-decomp/build/objects/renderer.obj \
    projects/graveyard-decomp/build/objects/physics.obj \
    --report projects/graveyard-decomp/reports/layout-reconstruct.json
```

**Explanation:** `layout-reconstruct` correlates PE section headers with MAP contributions and
supplied COFF object files. It matches objects by basename (e.g., `main.obj` maps to the MAP entry
for `main.obj`), computes RVA extents, records placement evidence, and flags unresolved objects
(objects in the MAP that have no matching COFF file).

**Expected output:**

```json
{
  "pe": "original/ghost.exe",
  "map": "original/ghost.map",
  "objects_supplied": 4,
  "objects_in_map": 9,
  "matched_objects": 4,
  "unresolved_objects": ["audio.obj", "input.obj", "d3d8.lib", "kernel32.lib", "user32.lib"],
  "placements": [
    {
      "object": "crt0.obj",
      "section": ".text",
      "rva": 4096,
      "end_rva": 4608,
      "evidence": "linker_map_contribution",
      "exact_extent": true
    }
  ]
}
```

!!! tip "Object naming"
    Name your rebuilt objects identically to the originals (e.g., `main.obj` not
    `main_matched.obj`). The basename is used for MAP-to-COFF correlation.

---

## Step 4: Build the linker reconstruction plan

```console
$ x86decomp linker-plan projects/graveyard-decomp/original/ghost.exe \
    projects/graveyard-decomp/original/ghost.map \
    projects/graveyard-decomp/build/objects/crt0.obj \
    projects/graveyard-decomp/build/objects/main.obj \
    projects/graveyard-decomp/build/objects/renderer.obj \
    projects/graveyard-decomp/build/objects/physics.obj \
    --library projects/graveyard-decomp/build/libs/kernel32.lib \
    --library projects/graveyard-decomp/build/libs/user32.lib \
    --library projects/graveyard-decomp/build/libs/d3d8.lib \
    --linker lld-link \
    --output-image projects/graveyard-decomp/build/relink/reconstructed.exe \
    --report projects/graveyard-decomp/reports/linker-plan.json \
    --write-relink-manifest projects/graveyard-decomp/build/relink/relink-manifest.json
```

**Explanation:** `linker-plan` builds a grounded reconstruction plan that records the reference
image, object order (from MAP), placement extents, COMDAT resolution, and a complete relink
manifest. `--library` adds static library archives for COMDAT resolution. `--linker` specifies
the linker executable (default `lld-link`). `--output-image` sets the nominal output path for the
relinked PE. `--write-relink-manifest` writes a standalone relink manifest ready for
`x86decomp relink`.

**Key plan fields:**

```json
{
  "reference_image": {
    "path": ".../original/ghost.exe",
    "sha256": "...",
    "architecture": "x86"
  },
  "object_order": ["crt0.obj", "main.obj", "renderer.obj", "physics.obj", "audio.obj", "input.obj"],
  "comdat_resolution": {
    "selections": {
      "??_7exception@std@@6B@": "msvcrt.lib"
    }
  },
  "unresolved": ["audio.obj", "input.obj"],
  "ready_for_relink": false,
  "relink_manifest": {
    "schema_version": 1,
    "linker": "lld-link",
    "objects": [...],
    "output": "build/relink/reconstructed.exe",
    "arguments": [
      "/NOLOGO",
      "/MACHINE:X86",
      "/SUBSYSTEM:WINDOWS",
      "/BASE:0x400000",
      "/FILEALIGN:512",
      "/ALIGN:4096",
      "/OUT:build/relink/reconstructed.exe"
    ]
  },
  "complete_original_link_command_claimed": false
}
```

!!! warning "Readiness gate"
    `ready_for_relink: false` means the plan cannot be used with `x86decomp relink` until all
    unresolved items (missing objects, unknown subsystem, overlapping contributions) are addressed.

---

## Step 5: Compile matched source files into COFF objects

```console
$ x86decomp compile projects/graveyard-decomp/config/compiler-profiles/msvc-2002-x86-release.json \
    projects/graveyard-decomp/src/matched/renderer.c \
    projects/graveyard-decomp/build/objects/renderer.obj \
    --report projects/graveyard-decomp/reports/compile-renderer.json \
    --cache projects/graveyard-decomp/build/cache

$ x86decomp compile projects/graveyard-decomp/config/compiler-profiles/msvc-2002-x86-release.json \
    projects/graveyard-decomp/src/matched/physics.c \
    projects/graveyard-decomp/build/objects/physics.obj \
    --report projects/graveyard-decomp/reports/compile-physics.json \
    --cache projects/graveyard-decomp/build/cache
```

**Explanation:** `compile` invokes the external compiler as specified by the profile. The
`--cache` flag enables content-addressed caching — if the same source, profile, and arguments
are compiled again, the cached output is reused without invoking the compiler.

---

## Step 6: Extract and synthesize COFF objects for unmatched functions

For functions that don't yet have matching C source, extract the original bytes from the PE
and synthesize placeholder COFF objects:

```console
$ x86decomp coff-extract projects/graveyard-decomp/original/ghost.exe-sections/audio.bin \
    _AudioInit@0 projects/graveyard-decomp/build/objects/audio-extracted.bin \
    --size 0x200

$ x86decomp coff-synthesize projects/graveyard-decomp/build/objects/audio-extracted.bin \
    _AudioInit@0 projects/graveyard-decomp/build/objects/audio.obj \
    --architecture x86
```

**Explanation:** `coff-extract` pulls the symbol's raw bytes. `coff-synthesize` wraps those bytes
into a valid COFF object. This creates a placeholder that occupies the correct RVA extent in the
relink without requiring matching source. The object will be byte-identical in the relinked
output.

---

## Step 7: Regenerate the linker plan and relink

After adding the synthesized objects, regenerate the plan:

```console
$ x86decomp linker-plan projects/graveyard-decomp/original/ghost.exe \
    projects/graveyard-decomp/original/ghost.map \
    projects/graveyard-decomp/build/objects/*.obj \
    --library projects/graveyard-decomp/build/libs/*.lib \
    --linker lld-link \
    --output-image projects/graveyard-decomp/build/relink/reconstructed.exe \
    --report projects/graveyard-decomp/reports/linker-plan-v2.json \
    --write-relink-manifest projects/graveyard-decomp/build/relink/relink-manifest.json
```

**Expected:** `"ready_for_relink": true` (all objects now present).

Run the relink:

```console
$ x86decomp relink projects/graveyard-decomp/build/relink/relink-manifest.json \
    --report projects/graveyard-decomp/reports/relink-report.json
```

**Explanation:** `relink` invokes the linker (`lld-link`) with the arguments from the manifest,
then performs post-link verification: byte comparison against `reference_image`, whole-image
match if `layout_profile` is present, and layout reconstruction if `map_file` is present.

**Expected output:**

```json
{
  "linker_exit_code": 0,
  "output": "build/relink/reconstructed.exe",
  "output_sha256": "...",
  "elapsed_ms": 2450.0,
  "byte_comparison": {
    "match": false,
    "similarity": 0.73
  },
  "image_match": {}
}
```

`similarity: 0.73` corresponds to the 73% of functions that are byte-matched.

---

## Step 8: Derive an image layout profile

```console
$ x86decomp image-profile projects/graveyard-decomp/original/ghost.exe \
    projects/graveyard-decomp/build/relink/ghost-profile.json
```

**Explanation:** `image-profile` derives a target-specific whole-image layout profile from the
reference PE. The profile captures section headers, alignment, entry point, and structural
properties used by `image-match` and `convergence-analyze` for accurate section-level comparison.

---

## Step 9: Compare whole images under the profile

```console
$ x86decomp image-match projects/graveyard-decomp/original/ghost.exe \
    projects/graveyard-decomp/build/relink/reconstructed.exe \
    --profile projects/graveyard-decomp/build/relink/ghost-profile.json \
    --report projects/graveyard-decomp/reports/image-match.json
```

**Explanation:** `image-match` compares the candidate PE against the reference under the explicit
layout profile. The report breaks down byte-level mismatches by section, providing a quantitative
measure of how close the relinked image is to the original.

---

## Step 10: Byte-level diff of the two images

```console
$ x86decomp diff-bytes projects/graveyard-decomp/original/ghost.exe \
    projects/graveyard-decomp/build/relink/reconstructed.exe \
    --report projects/graveyard-decomp/reports/diff-bytes-initial.json \
    --max-mismatches 256
```

**Explanation:** `diff-bytes` performs an exact byte-for-byte comparison of two files. Reports
mismatched byte positions and values up to `--max-mismatches` (default 64). Also computes prefix
and suffix matching spans and a `SequenceMatcher` similarity ratio.

---

## Step 11: Analyze convergence and append to history

```console
$ x86decomp convergence-analyze projects/graveyard-decomp/original/ghost.exe \
    projects/graveyard-decomp/build/relink/reconstructed.exe \
    --profile projects/graveyard-decomp/build/relink/ghost-profile.json \
    --report projects/graveyard-decomp/reports/convergence-v1.json \
    --history projects/graveyard-decomp/reports/convergence-history.jsonl
```

**Explanation:** `convergence-analyze` compares the reference and candidate images under a layout
profile. It classifies differences by section kind (executable, read_only_data, writable_data,
resources, relocations) and ranks next actions by impact. `--history` appends the result to a
JSONL convergence history file for tracking progress over time.

**Expected output:**

```json
{
  "reference_sha256": "...",
  "candidate_sha256": "...",
  "total_bytes": 6291456,
  "matching_bytes": 4592768,
  "mismatching_bytes": 1698688,
  "convergence_ratio": 0.73,
  "section_results": [
    {
      "section": ".text",
      "kind": "executable",
      "matching_bytes": 2293760,
      "mismatching_bytes": 851968,
      "convergence_ratio": 0.729
    },
    {
      "section": ".rdata",
      "kind": "read_only_data",
      "matching_bytes": 524288,
      "mismatching_bytes": 0,
      "convergence_ratio": 1.0
    }
  ],
  "remaining_actions": [
    {
      "impact": "high",
      "action": "Match audio.obj: 6 functions, 2048 bytes",
      "section": ".text"
    },
    {
      "impact": "high",
      "action": "Match input.obj: 4 functions, 1536 bytes",
      "section": ".text"
    }
  ],
  "previous_comparison": null,
  "history_entry": "appended"
}
```

---

## Step 12: Iterate and measure progress

After matching more functions (e.g., `audio.obj` functions), recompile, regenerate the linker
plan, relink, and run convergence again with the `--previous` flag:

```console
$ x86decomp convergence-analyze projects/graveyard-decomp/original/ghost.exe \
    projects/graveyard-decomp/build/relink/reconstructed-v2.exe \
    --profile projects/graveyard-decomp/build/relink/ghost-profile.json \
    --previous projects/graveyard-decomp/reports/convergence-v1.json \
    --report projects/graveyard-decomp/reports/convergence-v2.json \
    --history projects/graveyard-decomp/reports/convergence-history.jsonl
```

The `previous_comparison` field now shows deltas from v1 → v2: how many bytes were fixed, which
sections improved, and the new convergence ratio.

---

## Common failure cases and recovery

| Failure | Likely cause | Recovery |
|---|---|---|
| `linker-plan` reports `ready_for_relink: false` | Missing objects or libraries | Supply all objects in the MAP's `object_order` or accept unresolved entries |
| `relink` produces a non-functional PE | Object order mismatch or wrong linker flags | Verify object order matches `map-inspect` output exactly |
| `image-match` reports high `.reloc` mismatches | Base address or alignment differs | Check `/BASE` and `/ALIGN` in relink manifest arguments |
| `convergence-analyze` shows zero progress | Candidate image not updated after recompile | Verify the relinked PE path is correct |
| `layout-reconstruct` cannot match objects | Object filenames differ from MAP entries | Rename objects to match MAP basenames exactly |
| `lld-link` fails with unresolved externals | Missing import libraries | Add all required `.lib` files with `--library` |

---

## Related reference pages

- [Linker Reconstruction concept](../concepts/linker-reconstruction.md) — MAP parsing, COMDAT resolution, relink manifests
- [inspect-pe command](../commands/analysis/pe-pdb.md) — PE parsing
- [Linker Analysis commands](../commands/reconstruction/linker.md) — `map-inspect`, `layout-reconstruct`, `linker-plan`
- [relink command](../commands/reconstruction/relink.md) — Relink manifest schema and post-link verification
- [image-match / image-profile commands](../commands/reconstruction/image-match.md) — Whole-image comparison
- [convergence-analyze command](../commands/convergence/convergence.md) — Convergence measurement and history
- [diff-bytes command](../commands/validation/diff-bytes.md) — Byte-for-byte comparison
- [diff-function command](../commands/validation/diff-function.md) — PE function to COFF symbol comparison
- [COFF Commands](../commands/analysis/coff.md) — `coff-extract`, `coff-synthesize`
- [compile command](../commands/compilation/compile.md) — Compile source under a profile

---

## Optional extensions

1. **PDB matching** — If the game shipped with a PDB, use `pdb-inspect --pe ghost.exe` to
   cross-reference symbols and source files. Feed symbol names into `diff-function` for targeted
   matching.

2. **MSVC metadata scan** — Run `metadata-scan` to recover RTTI, vtable, unwind, and TLS metadata
   from the PE. This helps with COMDAT resolution for C++ objects.

3. **Patch-image for incremental patches** — Instead of full relinking, use `patch-image` to patch
   individual matched functions into the original PE at their original RVAs:

   ```console
   $ x86decomp patch-image projects/graveyard-decomp/original/ghost.exe \
       projects/graveyard-decomp/build/candidates/render-frame.bin \
       projects/graveyard-decomp/build/patches/ghost-patched.exe \
       --rva 0x8200 \
       --expected-original-sha256 abc123... \
       --expected-function-sha256 def456... \
       --report projects/graveyard-decomp/reports/patch-render.json
   ```

4. **Release-gate convergence threshold** — Use `release-gate` with the convergence report to
   enforce a minimum convergence ratio before accepting a release:

   ```console
   $ x86decomp release-gate projects/graveyard-decomp/ \
       --convergence-report reports/convergence-v2.json \
       --require-workflows \
       --report reports/release-gate.json
   ```

5. **Reproducibility manifest** — Create a reproducibility manifest to lock the full relink
   environment:

   ```console
   $ x86decomp reproduce-create projects/graveyard-decomp/ \
       projects/graveyard-decomp/reports/reproduce-manifest.json \
       --required-tool lld-link
   ```

   Then verify at any point:

   ```console
   $ x86decomp reproduce-verify projects/graveyard-decomp/ \
       projects/graveyard-decomp/reports/reproduce-manifest.json
   ```
