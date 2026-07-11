# Artifact Commands

Import and verify exported function artifacts with hash-sealed integrity.

---

## `x86decomp artifact-import`

Import a validated exported function artifact into a project.

### Purpose

Imports a function artifact directory (containing a `function.json` manifest, disassembly, decompiled source, and optional Ghidra listing) into a project. The import validates the artifact manifest, copies files into the project's artifact storage, and returns a verification result.

### Syntax

```
x86decomp artifact-import PROJECT EXPORTED_DIR
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PROJECT` | yes | path | Project root directory |
| `EXPORTED_DIR` | yes | path | Exported function artifact directory containing `function.json` |

### Files read

- `EXPORTED_DIR/function.json` — validated function manifest with `pe-rva:XXXXXXXX` identifier and body ranges
- `EXPORTED_DIR/*` — disassembly, C source, and optional Ghidra listing files

### Files written

- Project artifact storage directory

### Example

```console
$ x86decomp artifact-import ./my-project exported/function_pe-rva-00001234/
```

---

## `x86decomp artifact-verify`

Verify an exported function artifact and its hashes.

### Purpose

Validates a function artifact directory: checks that the `function.json` manifest is well-formed, that every declared file is present and matches its recorded SHA-256 hash, and that no undeclared files exist. Returns a structured verification result.

### Syntax

```
x86decomp artifact-verify ARTIFACT_DIR
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `ARTIFACT_DIR` | yes | path | Function artifact directory to verify |

### Files read

- `ARTIFACT_DIR/function.json` — function manifest
- `ARTIFACT_DIR/*` — all declared artifact files

### Verification checks

| Check | Description |
|---|---|
| Manifest validity | `function.json` has valid schema, `pe-rva:XXXXXXXX` ID, and non-empty body ranges |
| File presence | Every file declared in the manifest exists |
| Hash integrity | Every file matches its declared SHA-256 hash |
| No extras | No undeclared files exist in the artifact directory |

### Example

```console
$ x86decomp artifact-verify exported/function_pe-rva-00001234/
```

### Related commands

- [decompme-pack](decompme.md) — Create a decomp.me-compatible packet
- [test-bundle-create](test-bundle.md#x86decomp-test-bundle-create) — Create a hash-sealed test bundle
