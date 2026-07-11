# Benchmark corpus

`$id: urn:x86decomp:schema:benchmark-corpus:1` — schema version 1.

Validated against `schemas/benchmark-corpus.schema.json`.

A benchmark corpus defines a set of ground-truth test cases used to evaluate decompilation accuracy across different verification strategies.

---

## Required fields

| Field | Type | Constraint |
|-------|------|------------|
| `schema_version` | `1` (const) | — |
| `name` | string | minLength 1 |
| `cases` | array of objects | — |

---

## `cases` array

Each case:

| Field | Type | Required | Constraint |
|-------|------|----------|------------|
| `id` | string | yes | — |
| `kind` | enum | yes | One of 6 values |
| `human_interventions` | integer (optional) | no | minimum 0 |

Additional properties are allowed on each case object (`additionalProperties: true`).

### `kind` values (6 total)

| Value | Meaning |
|-------|---------|
| `byte_pair` | Pairwise byte-level comparisons between original and reconstructed |
| `pe_coff` | PE/COFF structure-level verification |
| `dynamic` | Runtime behavioral comparison |
| `symbolic` | Symbolic execution / SMT solver equality checks |
| `integration` | End-to-end integration scenario tests |
| `discovery_metrics` | Toolkit function-discovery and classification metrics |

### `human_interventions`

Tracks the number of human corrections required to pass the case. A value of `0` means fully automated success. Higher values indicate cases that required analyst guidance.

---

## Example

```json
{
  "schema_version": 1,
  "name": "x86decomp matching accuracy v0.7",
  "cases": [
    {
      "id": "case-001-msvc6-O2-fibonacci",
      "kind": "byte_pair",
      "human_interventions": 0,
      "compiler": "msvc6",
      "optimization": "O2",
      "functions": 1
    },
    {
      "id": "case-002-gcc-Os-sort",
      "kind": "byte_pair",
      "human_interventions": 1,
      "compiler": "gcc-mingw32",
      "optimization": "Os",
      "functions": 3,
      "note": "Required manual __cdecl override on one function"
    },
    {
      "id": "case-003-integration-relink",
      "kind": "integration",
      "human_interventions": 0,
      "functions": 12,
      "pipeline": "full-relink"
    },
    {
      "id": "case-004-discovery-metrics",
      "kind": "discovery_metrics",
      "human_interventions": 0,
      "total_functions": 137,
      "recovered": 129,
      "precision": 0.98,
      "recall": 0.94
    }
  ]
}
```

!!! note
    The `additionalProperties: true` on case objects allows benchmark maintainers to attach case-specific metadata (compiler, optimization level, function count, precision/recall metrics, etc.) without schema changes.
