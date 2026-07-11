# Linker Reconstruction

Linker reconstruction builds an evidence-driven plan for relinking a PE image from COFF
objects. It parses MSVC MAP files, correlates PE sections with COFF object contributions,
resolves COMDATs, and produces a relink manifest.

## Inputs

The reconstruction requires three categories of input:

1. **The target PE** — `game.exe`, the image to reconstruct.
2. **The MAP file** — `game.map`, produced by the MSVC linker (`/MAP` flag).
3. **COFF objects** — Individual `.obj` files that were linked into the PE.

Optional:
- **Static libraries** (`.lib` archives) — for COMDAT resolution and symbol provenance.

## Building a Reconstruction Plan

```bash
x86decomp linker-plan \
  --pe original/game.exe \
  --map original/game.map \
  --objects build/objects/*.obj \
  --libraries build/libs/*.lib \
  --linker lld-link \
  --output build/reconstructed.exe \
  --report linker-plan.json
```

### Required Arguments

| Argument | Purpose |
|---|---|
| `--pe` | The reference PE image to reconstruct |
| `--map` | MSVC linker MAP file for the PE |
| `--objects` | One or more COFF object files |
| `--linker` | Linker to use (default: `lld-link`) |
| `--output` | Output path for the reconstructed PE |

### Optional Arguments

| Argument | Purpose |
|---|---|
| `--libraries` | Static library archives for COMDAT resolution |
| `--report` | Path for the JSON reconstruction plan |

## What the Plan Contains

### Reference Image

```json
"reference_image": {
  "path": "/project/original/game.exe",
  "sha256": "abc123...",
  "architecture": "x86"
}
```

### Object Order

The plan preserves the object link order derived from the MAP file:

```json
"objects": [
  {"path": "/project/build/objects/crt0.obj", "sha256": "..."},
  {"path": "/project/build/objects/main.obj", "sha256": "..."},
  {"path": "/project/build/objects/utils.obj", "sha256": "..."}
]
```

Objects present in the MAP but not supplied are listed under `unresolved`.

### Placements

Each section contribution from the MAP is recorded with its exact RVA extent:

```json
"placements": [
  {
    "object": "crt0.obj",
    "section": ".text",
    "rva": 4096,
    "end_rva": 4608,
    "length": 512,
    "evidence": "linker_map_contribution",
    "exact_extent": true
  }
]
```

Overlapping contributions are flagged as unresolved.

### COMDAT Resolution

```json
"comdat_resolution": {
  "selections": {
    "??_7exception@std@@6B@": "msvcrt.lib",
    "??0exception@std@@QEAA@AEBV01@@Z": "crt0.obj"
  }
}
```

### Relink Manifest

The plan embeds a complete relink manifest ready for `x86decomp relink`:

```json
"relink_manifest": {
  "schema_version": 1,
  "linker": "lld-link",
  "objects": ["/project/build/objects/crt0.obj", "..."],
  "output": "build/reconstructed.exe",
  "arguments": [
    "/NOLOGO",
    "/MACHINE:X86",
    "/SUBSYSTEM:WINDOWS",
    "/BASE:0x400000",
    "/FILEALIGN:512",
    "/ALIGN:4096",
    "/OUT:build/reconstructed.exe",
    "@response_file"
  ],
  "reference_image": "/project/original/game.exe",
  "timeout_seconds": 600,
  "inherit_environment": true
}
```

### Readiness Check

The plan reports whether it is ready for relinking:

```json
"ready_for_relink": false,
"unresolved": [
  "object order entry not supplied: d3d8.lib",
  "linker subsystem argument not generated for numeric subsystem 2"
]
```

A plan with `ready_for_relink: false` cannot be used for `x86decomp relink` until all
unresolved items are addressed.

## MAP File Parsing

The `parse_msvc_map` function in `linker_layout.py` extracts:

- **Timestamp**: When the MAP was generated.
- **Preferred load address**: The image base.
- **Section contributions**: Which object contributed to which section at which RVA.
- **Public symbols**: Symbol names and their RVAs.
- **Entry point**: The program entry point RVA.

!!! note "MAP file limitations"
    MAP files may omit private-symbol and padding decisions. The reconstructed order is
    evidenced but cannot guarantee compatibility with original linker behavior for edge
    cases like identical COMDAT selection in archive members.

## COMDAT Resolution

COMDATs (COMDAT sections) are the MSVC mechanism for inline functions and templates.
Multiple objects may define the same COMDAT symbol; the linker picks one. The
reconstruction plan records which object or archive provided each COMDAT.

`resolve_comdats(parsed_objects)` examines every supplied object and archive to
determine which symbols are provided by which source, then records the selection.

## Using the Plan for Relinking

Once a plan is `ready_for_relink`:

```bash
# Extract the relink manifest from the plan
x86decomp linker-plan \
  --pe original/game.exe \
  --map original/game.map \
  --objects build/objects/*.obj \
  --report linker-plan.json

# Run the relink
x86decomp relink --manifest linker-plan.json
```

!!! warning "Complete original link command not claimed"
    The plan records this explicitly: `"complete_original_link_command_claimed": false`.
    Map files preserve object order and section placement but not every linker flag,
    response file content, or environment variable that influenced the original link.

## Reconciling MAPs Without Original Objects

When you have a MAP file but not all original objects:

1. Parse the MAP to extract section layout and symbol addresses.
2. Build COFF objects for every function you've matched.
3. Supply only those matched objects to `linker-plan`.
4. Unmatched objects will appear in `unresolved`.
5. Incrementally supply more objects as matching progresses.

## Layout Reconstruction

The `reconstruct_linker_layout` function performs the core correlation:

```
PE sections  ←→  MAP contributions  ←→  COFF objects
     │                  │                    │
     └──────────────────┴────────────────────┘
                       │
               Reconstruction Plan
```

It reads section headers from the PE (`.text`, `.rdata`, `.data`, etc.), matches MAP
entries to those sections by RVA ranges, and correlates contribution entries with
supplied COFF objects by basename matching.

!!! tip "Object naming"
    Name your rebuilt objects identically to the originals (e.g., `main.obj` not
    `main_matched.obj`). The basename is used for MAP-to-COFF correlation.
