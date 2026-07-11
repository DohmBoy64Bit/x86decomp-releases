# Compiler lab

`$id: urn:x86decomp:schema:compiler-lab:1` — schema version 1.

Validated against `schemas/compiler-lab.schema.json`.

A compiler lab definition describes a matrix of compiler experiments — which source file to compile, which compiler profiles to use, and optionally a cross-product of compiler option axes and a target narrowing constraint.

---

## Required fields

| Field | Type | Constraint |
|-------|------|------------|
| `source` | string | Path to the source file to compile |
| `profiles` | array of strings | minItems 1 — compiler profile IDs to use |

Each string in `profiles` must reference a valid compiler profile ID (see [compiler-profile.md](compiler-profile.md)).

---

## Optional fields

| Field | Type | Constraint |
|-------|------|------------|
| `output_root` | string | Directory for compiled outputs |
| `cache_root` | string | Directory for build cache |
| `output_name` | string | Override output filename |
| `max_experiments` | integer | minimum 1 — limit total experiment count |
| `matrix` | object | Compiler option axes (see below) |
| `target` | object (oneOf) | Narrow to a specific function or file (see below) |

---

## `matrix` object

| Field | Type | Constraint |
|-------|------|------------|
| `axes` | object (map of string to string[]) | Each key maps to an array of option values |

Each axis key/value pair generates a combinatorial expansion. For example:

```json
"matrix": {
  "axes": {
    "opt": ["/Od", "/O1", "/O2", "/Ox"],
    "arch": ["/arch:IA32", "/arch:SSE"]
  }
}
```

This generates 8 experiments (4 optimizations × 2 architecture flags) per profile.

!!! warning
    `max_experiments` caps the total number of experiments that will be run. If the full matrix exceeds the limit, the lab is truncated.

---

## `target` object

One of three shapes, selected via `oneOf`:

### `pe_function` target

| Field | Type | Required | Constraint |
|-------|------|----------|------------|
| `kind` | `"pe_function"` (const) | yes | — |
| `pe` | string | yes | Path to the PE binary |
| `rva` | integer | yes | minimum 0 — function RVA |
| `size` | integer | yes | minimum 1 — function byte size |
| `symbol` | string | yes | Function symbol name |

### `file` target

| Field | Type | Required | Constraint |
|-------|------|----------|------------|
| `kind` | `"file"` (const) | yes | — |
| `path` | string | yes | Path to target file |

### Empty target

An empty object `{}` means no narrowing — compile the full source against all profiles/axes.

---

## Example

```json
{
  "source": "test/cases/fib.c",
  "profiles": ["msvc6-x86-O2", "gcc-mingw32-O2"],
  "output_root": "build/compiler",
  "cache_root": "build/cache",
  "output_name": "fib",
  "max_experiments": 100,
  "matrix": {
    "axes": {
      "opt": ["/Od", "/O2"],
      "inl": ["/Ob0", "/Ob2"]
    }
  },
  "target": {
    "kind": "pe_function",
    "pe": "original/target.exe",
    "rva": 4096,
    "size": 256,
    "symbol": "_fib"
  }
}
```
