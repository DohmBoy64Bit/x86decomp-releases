# Linker reconstruction plan

`$id: urn:x86decomp:schema:linker-reconstruction-plan:1` — schema version 1.

Validated against `schemas/linker-reconstruction-plan.schema.json`.

A linker reconstruction plan captures everything discovered about the original link: the reference image, object files, section layout, COMDAT resolution, unresolved symbols, and a derived relink manifest.

---

## Required fields

| Field | Type | Constraint |
|-------|------|------------|
| `schema_version` | `1` (const) | — |
| `kind` | `"linker_reconstruction_plan"` (const) | Identifies the document type |
| `reference_image` | object | PE metadata for the reference binary |
| `map` | object | Linker map data (segments, symbols, addresses) |
| `objects` | array of objects | Discovered object files in link order |
| `sections` | array of objects | Section layout in the output image |
| `placements` | array of objects | Section-to-address placements |
| `comdat_resolution` | object | COMDAT selection decisions |
| `relink_manifest` | object | The derived relink manifest (see [relink-manifest.md](relink-manifest.md)) |
| `unresolved` | array of strings | Symbols that could not be resolved |
| `ready_for_relink` | boolean | Whether the plan is complete enough to attempt relinking |

---

## Optional fields

| Field | Type | Meaning |
|-------|------|---------|
| `created_at` | string | Timestamp of plan creation |
| `libraries` | array of objects | Import/dependency libraries used |
| `archives` | array of objects | Static libraries (.lib) linked |
| `linker` | string | Linker executable identified or inferred |
| `limitations` | array of strings | Known limitations of this reconstruction |
| `complete_original_link_command_claimed` | `false` (const) | Always `false` — the original link command is never fully known |

!!! warning
    `complete_original_link_command_claimed` is constrained to `false`. The toolkit never claims to know the exact original linker command — only the reconstructed equivalent.

---

## Example skeleton

```json
{
  "schema_version": 1,
  "kind": "linker_reconstruction_plan",
  "created_at": "2026-07-01T12:00:00Z",
  "reference_image": {},
  "map": {},
  "objects": [],
  "libraries": [],
  "archives": [],
  "sections": [],
  "placements": [],
  "comdat_resolution": {},
  "linker": "link.exe version 12.00.8804",
  "relink_manifest": {},
  "unresolved": ["_unknown_import_42"],
  "ready_for_relink": false,
  "complete_original_link_command_claimed": false,
  "limitations": [
    "One COFF object has no matching source candidate",
    "Three import thunks could not be attributed to a known library"
  ]
}
```

!!! tip
    Check `ready_for_relink` before attempting a relink. When it is `false`, the `unresolved` and `limitations` arrays explain what is missing.
