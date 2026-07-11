# Relink manifest

`$id: urn:x86decomp:schema:relink-manifest:1` — schema version 1.

Validated against `schemas/relink-manifest.schema.json`.

A relink manifest defines the linker invocation needed to reconstruct a binary from a set of object files. It is the output of linker reconstruction planning and the input to the relink command.

---

## Required fields

| Field | Type | Constraint |
|-------|------|------------|
| `schema_version` | `1` (const) | — |
| `linker` | string | minLength 1 — path or name of the linker |
| `objects` | array of strings | minItems 1 — object file paths in link order |
| `output` | string | minLength 1 — output file path |
| `arguments` | array of strings | minItems 1 — must contain `{output}` |
| `environment` | object (string→string) | Environment variables for the linker |
| `timeout_seconds` | integer | minimum 1 |

### `arguments`

Must contain the placeholder `{output}` at least once. Unlike compiler profiles, there is no `{source}` requirement — object files are listed in the `objects` array and appended or interpolated by the invoking tool.

```json
"arguments": ["/OUT:{output}", "/NOLOGO"]
```

---

## Optional fields

| Field | Type | Default | Meaning |
|-------|------|---------|---------|
| `inherit_environment` | boolean | — | Whether to inherit the parent process environment |
| `reference_image` | string | — | Path to the original binary for byte-level comparison |

---

## Example

```json
{
  "schema_version": 1,
  "linker": "link.exe",
  "objects": [
    "build/compiler/startup.obj",
    "build/compiler/main.obj",
    "build/compiler/utils.obj"
  ],
  "output": "build/relink/output.exe",
  "arguments": [
    "/OUT:{output}",
    "/NOLOGO",
    "/SUBSYSTEM:CONSOLE",
    "/MACHINE:X86"
  ],
  "environment": {
    "PATH": "C:\\MSVC\\bin;C:\\MSVC\\bin\\HostX86\\x86",
    "LIB": "C:\\MSVC\\lib",
    "INCLUDE": "C:\\MSVC\\include"
  },
  "inherit_environment": false,
  "timeout_seconds": 120,
  "reference_image": "original/target.exe"
}
```

!!! tip
    The `reference_image` field enables the relink command to perform byte-level comparison of the output against the original binary, generating a match report automatically.
