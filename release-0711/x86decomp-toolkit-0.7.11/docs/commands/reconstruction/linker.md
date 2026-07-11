# Linker Analysis

Commands for parsing MSVC linker maps, correlating PE sections with COFF objects,
and building linker reconstruction plans.

## `x86decomp map-inspect`

Parse an MSVC-compatible linker MAP file and emit structured metadata.

```console
x86decomp map-inspect MAP
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `MAP` | yes | path | MSVC linker MAP file (produced with `/MAP`) |

### Output

A deterministic JSON object containing:

| Field | Description |
|---|---|
| `timestamp` | MAP generation timestamp |
| `preferred_load_address` | Image base address |
| `contributions` | Per-object section contributions with RVA extents |
| `public_symbols` | Symbol names and their RVAs |
| `entry_point` | Program entry-point RVA |
| `object_order` | Ordered list of objects as seen by the linker |

### Example

```console
$ x86decomp map-inspect build/game.map
```

### Related Commands

- [`layout-reconstruct`](#x86decomp-layout-reconstruct) — correlate MAP with PE and COFF objects
- [`linker-plan`](#x86decomp-linker-plan) — build a full reconstruction plan

---

## `x86decomp layout-reconstruct`

Correlate PE section headers, linker MAP contributions, and COFF object files.

```console
x86decomp layout-reconstruct PE MAP [OBJECTS...] --report REPORT
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PE` | yes | path | Reference PE image |
| `MAP` | yes | path | MSVC linker MAP file |
| `OBJECTS` | no | path (variadic) | Zero or more COFF object files to correlate |
| `--report` | no | path | Write JSON reconstruction report |

### Output

A JSON object with section-to-object mappings, contribution placements, unresolved
entries, and object order. Each matched contribution carries an RVA extent and
evidence tag.

!!! note "Object matching"
    COFF objects are correlated to MAP entries by basename. Name rebuilt objects
    identically to the originals (e.g., `main.obj`, not `main_matched.obj`).

### Example

```console
$ x86decomp layout-reconstruct original/game.exe original/game.map \
    build/objects/crt0.obj build/objects/main.obj \
    --report layout-report.json
```

### Related Commands

- [`map-inspect`](#x86decomp-map-inspect) — parse MAP alone
- [`linker-plan`](#x86decomp-linker-plan) — build a complete reconstruction plan

---

## `x86decomp linker-plan`

Build a grounded linker reconstruction plan from a PE image, MAP file, and COFF
objects. Produces a relink manifest and readiness assessment.

```console
x86decomp linker-plan PE MAP OBJECTS... \
    --library LIB... \
    --linker lld-link \
    --output-image build/reconstructed.exe \
    --report REPORT \
    --write-relink-manifest PATH
```

### Arguments

| Argument | Required | Type | Default | Description |
|---|---|---|---|---|
| `PE` | yes | path | — | Reference PE image to reconstruct |
| `MAP` | yes | path | — | MSVC linker MAP file |
| `OBJECTS` | yes | path (one or more) | — | COFF object files |
| `--library` | no | path (repeatable) | `[]` | Static library archives for COMDAT resolution |
| `--linker` | no | string | `lld-link` | Linker executable or command name |
| `--output-image` | no | path | `build/reconstructed.exe` | Nominal output path for the relinked PE |
| `--report` | no | path | — | Write the full JSON reconstruction plan |
| `--write-relink-manifest` | no | path | — | Write a standalone relink manifest from the plan |

### What the Plan Produces

The reconstruction plan records:

- **Reference image** — PE path, SHA-256, architecture
- **Object order** — evidenced link order from MAP, with unresolved entries
- **Placements** — per-object, per-section RVA extents with evidence tags
- **COMDAT resolution** — which object or archive provides each COMDAT symbol
- **Relink manifest** — complete `x86decomp relink` arguments including linker,
  objects, `/MACHINE`, `/BASE`, `/ALIGN`, `/SUBSYSTEM`, `/OUT`
- **Readiness** — `ready_for_relink` boolean and `unresolved` list

!!! tip "Readiness"
    A plan with `ready_for_relink: false` cannot be used with `x86decomp relink`
    until all unresolved items (missing objects, unknown subsystem, overlapping
    contributions) are addressed.

!!! warning "Complete link command not claimed"
    The plan records `"complete_original_link_command_claimed": false`. MAP files
    preserve object order and section placement but not every linker flag,
    response-file content, or environment variable.

### Example

```console
$ x86decomp linker-plan original/game.exe original/game.map \
    build/objects/*.obj \
    --library build/libs/msvcrt.lib \
    --linker lld-link \
    --output-image build/reconstructed.exe \
    --report linker-plan.json \
    --write-relink-manifest relink.json

$ x86decomp relink relink.json
```

### Related Commands

- [`map-inspect`](#x86decomp-map-inspect) — inspect MAP file contents
- [`layout-reconstruct`](#x86decomp-layout-reconstruct) — layout correlation step
- [`relink`](relink.md) — execute the relink from the generated manifest
- [`coff-inspect`](../analysis/coff.md) — inspect individual COFF objects
