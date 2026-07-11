# Hybrid Project

**Neon Underground** — A fictional cyberpunk action game compiled for x86 Windows PE. The game
has a mix of easily matched utility functions and deeply SIMD-optimized rendering code. The team
uses a hybrid approach: target packs for automated project setup, templates for laying out source
directories, byte-form assembly stubs for unmatched functions, and hybrid generation to produce
a buildable project that mixes matched C and assembly.

---

## Scenario

> Neon Underground shipped in 2004 as `neon.exe` with an MSVC linker MAP file but no PDB. The
> team has identified the target compiler as MSVC 2003. About 40% of functions — mostly utility
> helpers, string operations, and initialization — have been matched to byte-identical C source.
> The remaining 60% — rendering, audio mixing, and SIMD vector math — resist exact matching.
> The team uses hybrid generation to emit a buildable project that links matched C sources
> alongside byte-form assembly stubs for unmatched functions, then patches individual matched
> functions into the original image incrementally.

## What you will accomplish

1. Initialize a project with a target pack from the binary and MAP file
2. Derive a project template and materialize the working layout
3. Compile matched C sources into COFF objects
4. Generate a hybrid project with byte-form assembly stubs
5. Verify the hybrid project structure
6. Patch individual matched functions into the original PE image
7. Byte-diff the patched image against the original
8. Verify the project integrity after patching

## Prerequisites

- x86decomp 0.7.11 installed
- `lld-link` available on PATH (for hybrid link step)
- The target binary `games/neon/neon.exe` (x86 PE)
- The linker MAP file `games/neon/neon.map`
- Matched C sources in `src/matched/`
- A compiler profile for MSVC 2003

## Starting file structure

```
games/neon/
  neon.exe                    # The target PE (x86, ~3.2 MB)
  neon.map                    # MSVC linker MAP file

projects/neon-decomp/         # Empty directory for the project
  src/
    matched/                  # Byte-matched C sources
      init.c
      string_utils.c
      memory_pool.c
      ...
```

---

## Step 1: Infer a target pack from the binary

```console
$ x86decomp target-pack-infer games/neon/neon.exe target-pack/ \
    --name "Neon Underground" \
    --map games/neon/neon.map \
    --decisions decisions.json
```

Where `decisions.json` contains:

```json
{
  "preferred_mode": "both",
  "compiler_family": "msvc",
  "compiler_version": "13.10.3077",
  "linker_family": "msvc",
  "source_language": "c++",
  "allow_host_execution": false,
  "target_description": "Cyberpunk action game executable, shipped 2004"
}
```

**Explanation:** `target-pack-infer` parses the primary PE and all supplied artifacts (MAP, PDB if
available, COFF objects, libraries). It produces a self-contained target-pack directory with
`target.toml` (identity and decisions), `observations.json` (bounded parser output),
`image-profile.json` (hash-bound layout profile), `acceptance.json` (matching/functional minima),
and `template-plan.json` (adapter needs). The `--decisions` file records user-supplied decisions
about compiler family, version, and source language. Inferences never invent missing information
— unknowns are recorded explicitly.

**Expected output structure:**

```
target-pack/
  target.toml                  # Schema v1 target identity and artifact inventory
  observations.json            # Parsed PE, MAP, PDB, COFF, library metadata
  image-profile.json           # Evidence- and hash-bound image layout
  acceptance.json              # Acceptance minima for matching and functional
  template-plan.json           # Required adapters and unresolved facts
  artifacts/                   # Copied artifact files
    neon.exe
    neon.map
```

**Verify the target pack:**

```console
$ x86decomp target-pack-verify target-pack/
```

```json
{
  "valid": true,
  "target_id": "x86-e3b0c44298fc1c14",
  "failures": [],
  "artifact_count": 2
}
```

---

## Step 2: Derive the project template contract

```console
$ x86decomp template-derive target-pack/
```

**Explanation:** `template-derive` uses only verified pack contents and explicit decisions to
calculate: enabled modes; whether hybrid assembly fallback is needed; whether object comparison,
linker reconstruction, or whole-image comparison have enough supplied artifacts; whether
compiler/linker identities are confirmed; evidence-backed source-language candidates; and
unresolved blockers. Does not emit candidate function bodies or fake compiler profiles.

---

## Step 3: Initialize the project from the target pack

```console
$ x86decomp project-from-target target-pack/ projects/neon-decomp/

$ x86decomp template-materialize projects/neon-decomp/
```

**Explanation:** `project-from-target` verifies the target pack, initializes a standard project
with `init`, copies the entire target pack into `projects/neon-decomp/target-pack/`, updates
`project.json`, copies Ghidra scripts if available, writes `config/target-decisions.json`, creates
a default pipeline, and writes a `TARGET.md` summary. `template-materialize` then creates the
source, header, build, test, report, and configuration directories for the hybrid template kind.

**Expected output from `project-from-target`:**

```json
{
  "project": {
    "project_id": "x86d-...",
    "architecture": "x86",
    "default_modes": ["matching", "functional"],
    "status": "initialized"
  },
  "target_pack_verification": {"valid": true},
  "pipeline": "orchestration/pipelines/default.json",
  "template": "materialized"
}
```

---

## Step 4: Compile matched C sources

```console
$ x86decomp compile projects/neon-decomp/config/compiler-profiles/msvc-2003-x86-release.json \
    projects/neon-decomp/src/matched/init.c \
    projects/neon-decomp/build/objects/init.obj \
    --report projects/neon-decomp/reports/compile-init.json \
    --cache projects/neon-decomp/build/cache

$ x86decomp compile projects/neon-decomp/config/compiler-profiles/msvc-2003-x86-release.json \
    projects/neon-decomp/src/matched/string_utils.c \
    projects/neon-decomp/build/objects/string_utils.obj \
    --report projects/neon-decomp/reports/compile-string-utils.json \
    --cache projects/neon-decomp/build/cache

$ x86decomp compile projects/neon-decomp/config/compiler-profiles/msvc-2003-x86-release.json \
    projects/neon-decomp/src/matched/memory_pool.c \
    projects/neon-decomp/build/objects/memory_pool.obj \
    --report projects/neon-decomp/reports/compile-memory-pool.json \
    --cache projects/neon-decomp/build/cache
```

**Explanation:** Each matched source file is compiled against the identified compiler profile.
The `--cache` flag enables content-addressed caching to skip redundant builds across iterations.

---

## Step 5: Generate the hybrid project

```console
$ x86decomp hybrid-generate projects/neon-decomp/ projects/neon-decomp/build/hybrid/ \
    --architecture x86 \
    --asm-format bytes \
    --image-base 0x400000 \
    --symbol-map projects/neon-decomp/config/symbols.json \
    --overwrite
```

**Explanation:** `hybrid-generate` (a compatibility alias for the canonical `x86decomp hybrid generate`)
produces a hybrid assembly project from the source project. It reads the project layout, emits
byte-form assembly stubs (`--asm-format bytes`) for unmatched functions alongside compiled C
sources for matched functions. `--architecture x86` targets 32-bit. `--image-base 0x400000`
sets the image base address. `--symbol-map` provides a JSON symbol map for resolving external
references in assembly stubs. `--overwrite` replaces any existing output.

**Assembly format options:**

| Format | Description |
|---|---|
| `bytes` | Raw machine-code bytes (conservative default) |
| `annotated` | Disassembly with address and evidence annotations |
| `mnemonic` | Human-readable mnemonic assembly |

!!! tip "Canonical equivalent"
    `x86decomp hybrid-generate` delegates to the canonical route. The equivalent
    canonical command is `x86decomp hybrid generate`.

**Expected output structure:**

```
build/hybrid/
  src/
    matched/
      init.c                   # Matched C source (compiled)
      string_utils.c           # Matched C source (compiled)
      memory_pool.c            # Matched C source (compiled)
    asm/
      render_frame.asm         # Byte-form assembly stub
      audio_mix.asm            # Byte-form assembly stub
      vector_normalize.asm     # Byte-form assembly stub
      ... (all unmatched functions)
  build/
    CMakeLists.txt or Makefile
  config/
    compiler-profile.json
    linker-script.json
```

---

## Step 6: Verify the hybrid project

```console
$ x86decomp verify-project projects/neon-decomp/
```

**Explanation:** `verify-project` checks the project structure, binary SHA-256, program manifest,
analysis database, work queue, project-state database, content store, and memory ledger. The
hybrid generation does not modify the core project structure — only creates build outputs — so
the project should remain valid.

**Expected output:**

```json
{
  "project_id": "x86d-...",
  "architecture": "x86",
  "valid": true,
  "failures": [],
  "memory_event_count": 3
}
```

---

## Step 7: Patch individual matched functions into the original PE

For each matched function, extract the compiled bytes and patch them into the original image:

```console
$ x86decomp coff-extract projects/neon-decomp/build/objects/init.obj \
    _GameInit@0 projects/neon-decomp/build/candidates/init.bin \
    --size 0x180

$ x86decomp patch-image projects/neon-decomp/original/neon.exe \
    projects/neon-decomp/build/candidates/init.bin \
    projects/neon-decomp/build/patches/neon-init-patched.exe \
    --rva 0x1000 \
    --expected-original-sha256 e3b0c44298fc1c149afbf4c8... \
    --expected-function-sha256 a1b2c3d4e5f67890... \
    --report projects/neon-decomp/reports/patch-init.json
```

**Explanation:** `coff-extract` pulls the compiled function bytes from the COFF object.
`patch-image` reads the original PE, extracts the original function bytes at `--rva`, writes the
candidate bytes in-place, zeroes the PE checksum, and writes a new output file — the original is
never modified. `--expected-original-sha256` guards against using the wrong original PE.
`--expected-function-sha256` guards against patching a function that was already modified.

**Expected output:**

```json
{
  "kind": "patch_image",
  "original_sha256": "e3b0c44298fc1c149afbf4c8...",
  "candidate_sha256": "...",
  "output_sha256": "...",
  "function_rva": 4096,
  "file_offset": 1024,
  "patch_size": 384,
  "original_function_sha256": "a1b2c3d4e5f67890..."
}
```

!!! warning "Size constraint"
    The candidate byte sequence must not exceed the original function size. If the candidate is
    shorter, remaining original bytes are left untouched. Consider rebuilding the object and
    relinking for resized functions.

Patch the remaining matched functions:

```console
$ x86decomp patch-image projects/neon-decomp/build/patches/neon-init-patched.exe \
    projects/neon-decomp/build/candidates/string_utils.bin \
    projects/neon-decomp/build/patches/neon-v2-patched.exe \
    --rva 0x2000 \
    --expected-original-sha256 ... \
    --expected-function-sha256 ... \
    --report projects/neon-decomp/reports/patch-string-utils.json
```

!!! tip "Incremental patching"
    Chain patches by using the previous patched output as the next `ORIGINAL`. The SHA-256
    of each intermediate file changes, so update `--expected-original-sha256` accordingly
    for each step.

---

## Step 8: Byte-diff the patched image against the original

```console
$ x86decomp diff-bytes projects/neon-decomp/original/neon.exe \
    projects/neon-decomp/build/patches/neon-v2-patched.exe \
    --report projects/neon-decomp/reports/diff-patched-v2.json \
    --max-mismatches 256
```

**Explanation:** `diff-bytes` compares the original and patched images byte-for-byte. With two
functions patched, the only differences should be in the two function bodies (byte-identical
matches should produce zero differences in those regions — mismatch reports on RVA-aligned
positions indicate patching errors).

**Expected output for byte-matched patches:**

```json
{
  "match": true,
  "length": {"target": 3358720, "candidate": 3358720, "common": 3358720},
  "prefix": 3358720,
  "suffix": 0,
  "similarity": 1.0,
  "mismatches": [],
  "target_sha256": "...",
  "candidate_sha256": "..."
}
```

`match: true` and `similarity: 1.0` — all patched functions produced byte-identical output,
and no other regions of the image were disturbed.

---

## Step 9: Verify project integrity after patching iteration

```console
$ x86decomp verify-project projects/neon-decomp/

$ x86decomp snapshot-tools --output projects/neon-decomp/tools-snapshot.json
```

Record the tool environment for reproducibility tracking.

---

## Common failure cases and recovery

| Failure | Likely cause | Recovery |
|---|---|---|
| `target-pack-infer` fails to parse MAP | MAP file is not MSVC-compatible or is corrupted | Verify MAP was produced with `/MAP` (not `/MAPINFO`) |
| `project-from-target` rejects target pack | `target-pack-verify` found hash mismatches or missing files | Run `target-pack-verify` and fix reported failures |
| `hybrid-generate` produces empty asm stubs | Project has no functions in `functions/` directory | Run `ghidra-export` and `artifact-import` first |
| `patch-image` rejects with `ContractError` | `--expected-original-sha256` doesn't match the actual original | Recompute the hash with `inspect-pe` and update the flag |
| `patch-image` candidate is too large | Recompiled function is bigger than the original | Trim inline expansions or padding; consider relinking instead |
| `diff-bytes` shows mismatches outside patched RVAs | Intermediate patching changed section alignment or checksum | Verify only function bytes changed via `--report` inspection |

---

## Related reference pages

- [Target Pack commands](../commands/project/target-pack.md) — `target-pack-infer`, `target-pack-verify`, `project-from-target`, `template-derive`, `template-materialize`
- [init / verify-project commands](../commands/project/init-verify.md) — Project initialization and verification
- [hybrid-generate command](../commands/reconstruction/relink.md) — Hybrid assembly project generation
- [patch-image command](../commands/reconstruction/patch.md) — PE function patching
- [diff-bytes command](../commands/validation/diff-bytes.md) — Byte-for-byte comparison
- [compile command](../commands/compilation/compile.md) — Compile source under a profile
- [COFF Commands](../commands/analysis/coff.md) — `coff-extract`, `coff-synthesize`
- [Decompilation Modes concept](../concepts/decompilation-modes.md) — Matching, functional, and hybrid modes
- [Target Pack concept](../config/target-pack.md) — Target pack schema and decisions

---

## Optional extensions

1. **Canonical assembly batch** — Use the canonical `x86decomp asm batch` command to bulk-process
   all unmatched functions into assembly stubs with a single invocation, specifying the assembler
   command and output format.

2. **Incremental to full relink** — As more functions are matched, transition from patch-image
   to full relink. When enough matched objects are available, run `linker-plan` to build a
   reconstruction plan and `relink` to produce a complete rebuilt image:

   ```console
   $ x86decomp linker-plan projects/neon-decomp/original/neon.exe \
       projects/neon-decomp/original/neon.map \
       projects/neon-decomp/build/objects/*.obj \
       --library projects/neon-decomp/build/libs/*.lib \
       --linker lld-link \
       --report linker-plan.json \
       --write-relink-manifest relink-manifest.json

   $ x86decomp relink relink-manifest.json --report relink-report.json
   ```

3. **Template-guided source layout** — After `template-materialize`, inspect
   `config/next-steps.json` for guidance on which source directories to populate first, which
   headers are needed, and what validation gate must pass for each stage.

4. **Ghidra export with MCP** — Use the MCP gateway to query Ghidra for unresolved function
   metadata without re-exporting:

   ```console
   $ x86decomp mcp-tools --url http://localhost:8080
   $ x86decomp mcp-read projects/neon-decomp/ getFunction \
       '{"address": "0x401000"}'
   ```

5. **Symbol map automation** — Generate the symbol map for `--symbol-map` from the linker MAP
   and PDB (if available) by extracting public symbol names and RVAs. Feed this into
   `hybrid-generate` for accurate external symbol resolution in assembly stubs.
