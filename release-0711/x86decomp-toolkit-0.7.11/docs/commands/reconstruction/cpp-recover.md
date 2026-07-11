# C++ Recovery

Recover C++ class relationships, vtable layouts, and MSVC metadata from a PE image.

## `x86decomp cpp-recover`

```console
x86decomp cpp-recover PE \
    --metadata-report PATH \
    --object OBJ... \
    --map MAP \
    --report REPORT
```

### Purpose

Recover bounded C++ metadata and class relationships including RTTI hierarchies,
vtable layouts, inheritance chains, and MSVC-specific metadata (unwind tables, TLS
callbacks, initializer lists). Operates on a PE image with optional supporting
evidence from COFF objects and linker maps.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PE` | yes | path | PE image to analyze |
| `--metadata-report` | no | path | Pre-computed MSVC metadata scan report (`metadata-scan` output) |
| `--object` | no | path (repeatable) | COFF object files for cross-referencing |
| `--map` | no | path | MSVC linker MAP file for symbol and layout evidence |
| `--report` | no | path | Write recovery report as JSON |

### Recovery Pipeline

The tool combines multiple evidence sources:

1. **MSVC metadata** — Runtime Type Information (RTTI), Complete Object Locators,
   vtable references extracted via `metadata-scan`
2. **COFF cross-references** — Symbol tables and relocation entries from supplied
   objects
3. **MAP evidence** — Public symbol names and address ranges

### Output

The report includes:

- Recovered class hierarchy (base/derived relationships)
- Vtable entries with resolved symbol names where available
- Constructor/destructor associations
- Inheritance type annotations (single, multiple, virtual)
- Unresolved or ambiguous entries tagged with evidence provenance

!!! note "Bounded recovery"
    Recovery is bounded to what the PE metadata exposes. RTTI may be stripped or
    partial in release builds. Unresolved relationships are reported as such with
    the available evidence.

### Example

```console
$ x86decomp cpp-recover original/game.exe \
    --metadata-report metadata-scan.json \
    --object build/objects/game_main.obj \
    --object build/objects/game_entity.obj \
    --map original/game.map \
    --report cpp-recovery.json
```

### Related Commands

- [`metadata-scan`](../analysis/metadata.md) — scan for MSVC RTTI, vtables, unwind, TLS metadata
- [`coff-inspect`](../analysis/coff.md) — inspect COFF object symbols and relocations
- [`map-inspect`](linker.md#x86decomp-map-inspect) — parse MSVC linker map
