# toolchain-register / toolchain-verify

## `x86decomp toolchain-register`

Register a versioned compiler toolchain in a user-owned registry.

### Purpose

Records compiler executable paths and their SHA-256 hashes in a JSON registry
file. The registry is user-owned — proprietary compiler binaries are never
copied, only referenced by path. Profiles can then reference toolchain IDs
instead of absolute executable paths.

### Syntax

```
x86decomp toolchain-register REGISTRY TOOLCHAIN_ID FAMILY VERSION --executable role=path...
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `REGISTRY` | yes | path | Path to a JSON toolchain registry file (created if missing) |
| `TOOLCHAIN_ID` | yes | string | Unique identifier for this toolchain entry |
| `FAMILY` | yes | string | Compiler family name (e.g. `msvc`, `clang`, `gcc`) |
| `VERSION` | yes | string | Compiler version string (e.g. `19.29.30137`) |

### Options

| Option | Required | Repeatable | Description |
|---|---|---|---|
| `--executable role=path` | yes (at least one) | yes | Map a role name (e.g. `compiler`, `linker`) to an executable path |

Each executable is resolved, verified as an existing regular file, and recorded with its SHA-256 hash and file size.

### Accepted values

- `REGISTRY`: any valid filesystem path; the file is created with schema version 1 if it does not exist
- `TOOLCHAIN_ID`, `FAMILY`, `VERSION`: non-empty strings
- `--executable role=path`: `role` and `path` separated by `=`, e.g. `compiler=C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.38.33130\bin\Hostx64\x86\cl.exe`

### Files read

- `REGISTRY` — existing registry JSON (if present)

### Files written

- `REGISTRY` — updated registry JSON with the new toolchain entry

### Registry format

```json
{
    "schema_version": 1,
    "toolchains": {
        "msvc-2022-x86": {
            "id": "msvc-2022-x86",
            "family": "msvc",
            "version": "19.38.33130",
            "registered_at": "2026-07-11T12:00:00Z",
            "ownership": "user_supplied_external_reference",
            "executables": {
                "compiler": {
                    "path": "C:\\msvc\\cl.exe",
                    "sha256": "abc123...",
                    "size": 123456
                }
            },
            "metadata": {}
        }
    }
}
```

### Exit behavior

- Exit 0 on success with JSON result on stdout
- Exit 2 on argument error with argparse diagnostics on stderr
- Exit 2 on runtime error with JSON `{"error": ..., "message": ...}` on stderr

### Example

```console
$ x86decomp toolchain-register toolchains.json msvc-2022-x86 msvc 19.38.33130 \
    --executable "compiler=C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.38.33130\bin\Hostx64\x86\cl.exe" \
    --executable "linker=C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.38.33130\bin\Hostx64\x86\link.exe"
```

---

## `x86decomp toolchain-verify`

Verify that all registered toolchain executables are present and their hashes match.

### Purpose

Checks each executable file referenced in a toolchain registry entry. Reports
whether each file exists at its recorded path and whether its current SHA-256
matches the registered hash.

### Syntax

```
x86decomp toolchain-verify REGISTRY TOOLCHAIN_ID
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `REGISTRY` | yes | path | Path to the toolchain registry JSON file |
| `TOOLCHAIN_ID` | yes | string | Toolchain identifier to verify |

### Output

Returns a JSON object:

```json
{
    "toolchain_id": "msvc-2022-x86",
    "valid": true,
    "failures": []
}
```

If executables are missing or have changed hashes, `valid` is `false` and
`failures` lists each failure reason:

```json
{
    "toolchain_id": "msvc-2022-x86",
    "valid": false,
    "failures": [
        "compiler: missing C:\\msvc\\cl.exe",
        "linker: hash changed"
    ]
}
```

### Files read

- `REGISTRY` — toolchain registry JSON

### Exit behavior

- Exit 0 on success with JSON result on stdout
- Exit 2 on argument error with argparse diagnostics on stderr
- Exit 2 on runtime error with JSON `{"error": ..., "message": ...}` on stderr

### Example

```console
$ x86decomp toolchain-verify toolchains.json msvc-2022-x86
{"toolchain_id": "msvc-2022-x86", "valid": true, "failures": []}
```

!!! warning "User-supplied external references"
    Toolchain executables are never copied or bundled. The registry stores paths
    and hashes only. You are responsible for maintaining the referenced files at
    those paths and re-registering after updates.

### Related commands

- [compile / compile-worker](compile.md) — Compile source using a compiler profile
- [compiler-lab](compiler-lab.md) — Matrix experiments across multiple toolchains
