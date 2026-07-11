# Compiler profile

`$id: urn:x86decomp:schema:compiler-profile:2` — schema version 2.

Validated against `schemas/compiler-profile.schema.json`.

A compiler profile defines a specific compiler executable, its invocation syntax, and execution constraints. Profiles are referenced by name in compiler lab matrices and compilation commands.

---

## Required fields

| Field | Type | Constraint |
|-------|------|------------|
| `schema_version` | `2` (const) | Must be exactly 2 |
| `id` | string | minLength 1 — unique profile identifier |
| `description` | string | minLength 1 — human-readable description |
| `executable` | string | minLength 1 — path to compiler binary |
| `language` | enum | `c`, `c++`, or `assembly` |
| `output_kind` | enum | See below |
| `timeout_seconds` | integer | minimum 1 |
| `arguments` | array of strings | minItems 2, must contain `{source}` and `{output}` |
| `environment` | object | string-to-string map of env vars |

### `language`

| Value | Meaning |
|-------|---------|
| `c` | C source compilation |
| `c++` | C++ source compilation |
| `assembly` | Assembly source compilation |

### `output_kind`

| Value | Meaning |
|-------|---------|
| `relocatable_object` | Emit a `.obj` / `.o` object file |
| `executable` | Emit a linked executable |
| `assembly` | Emit assembly listing (e.g. `/FA` in MSVC) |
| `binary` | Emit a raw binary blob |

### `arguments`

Must include the placeholders `{source}` (input source file path) and `{output}` (output file path). These are replaced at invocation time.

```json
"arguments": ["/c", "/O2", "/Fo{output}", "{source}"]
```

!!! warning
    Both `{source}` and `{output}` are validated with `contains` — the schema rejects any argument list missing either placeholder.

---

## Optional fields

| Field | Type | Default | Meaning |
|-------|------|---------|---------|
| `family` | string or null | — | Compiler family (e.g. `msvc`, `gcc`, `clang`) |
| `version` | string or null | — | Compiler version string |
| `command_prefix` | array of strings | — | Prefix args before the compiler (e.g. `["wine"]`, `["timeout", "30"]`) |
| `version_arguments` | array of strings | — | Args to query compiler version (e.g. `["--version"]`) |
| `inherit_environment` | boolean | — | Whether to inherit the parent process environment |

---

## Full example

```json
{
  "schema_version": 2,
  "id": "msvc6-x86-O2",
  "description": "Microsoft C/C++ Optimizing Compiler Version 12.00.8804 for 80x86, /O2 optimizations",
  "family": "msvc",
  "version": "12.00.8804",
  "executable": "cl.exe",
  "language": "c",
  "output_kind": "relocatable_object",
  "timeout_seconds": 60,
  "arguments": ["/nologo", "/c", "/O2", "/GX-", "/GR-", "/Fo{output}", "{source}"],
  "environment": {
    "INCLUDE": "C:\\MSVC\\include",
    "LIB": "C:\\MSVC\\lib"
  },
  "inherit_environment": false
}
```

!!! tip
    Set `inherit_environment` to `true` when the compiler needs the host PATH. Set environment variables explicitly for reproducible, isolated builds.
