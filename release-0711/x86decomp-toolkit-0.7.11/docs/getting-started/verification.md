# Verification

x86decomp provides layered verification: project structure integrity, ground-truth corpus
consistency, and project state checks. This page covers running and interpreting each.

---

## Project verification

### `verify-project`

```console
$ x86decomp verify-project my-project/
```

This command validates:

| Check | Details |
|---|---|
| `project.json` exists | The project root must contain a valid `project.json`. |
| Schema version | Accepts versions 1, 2, and 3 (current). |
| Binary presence | The referenced binary must exist at its recorded path. |
| Binary SHA-256 | The binary's current SHA-256 must match `project.json`. |
| Program manifest | `analysis/program.json` must exist and its key fields must match a fresh PE parse of the binary. |
| Database files | `analysis_database`, `work_queue`, and `project_state_database` files must exist. |
| Content store | The `content_store` directory must exist. |
| Default modes | Must include both `["matching", "functional"]`. |
| Project memory | All memory events in `memory/events.jsonl` must have valid evidence references and hashes. |

### Understanding the output

#### Valid project

```json
{
  "project_id": "x86d-a1b2c3d4e5f67890-deadbeef",
  "architecture": "x86",
  "valid": true,
  "failures": [],
  "binary_path": "/home/user/my-project/original/target.exe",
  "memory_event_count": 4
}
```

#### Invalid project

```json
{
  "project_id": "x86d-a1b2c3d4e5f67890-deadbeef",
  "architecture": "x86",
  "valid": false,
  "failures": [
    "binary SHA-256 does not match project.json",
    "program manifest mismatch: size_of_image",
    "memory: event 3 references missing evidence id ev-002"
  ],
  "binary_path": "/home/user/my-project/original/target.exe",
  "memory_event_count": 4
}
```

!!! warning "SHA-256 mismatch"
    A binary SHA-256 mismatch means the file at the recorded path has changed since project
    initialization. If the binary was legitimately replaced, reinitialize the project or
    manually update `project.json` and regenerate the program manifest.

!!! note "Program manifest mismatch"
    A program manifest mismatch (`program manifest mismatch: size_of_image`) means a fresh
    parse of the binary disagrees with the recorded `analysis/program.json`. This typically
    means the binary was replaced with a different build.

---

## Checking project state

The `project-check` command runs the project state database validation:

```console
$ x86decomp project-check my-project/
```

Output:

```json
{
  "project_id": "x86d-a1b2c3d4e5f67890-deadbeef",
  "schema_version": 3,
  "migrations_applied": 2,
  "migrations_pending": 0,
  "checksums": {
    "project.json": "valid-stable",
    "analysis/program.json": "valid-stable",
    "analysis/host.json": "valid-stable"
  },
  "warnings": [],
  "errors": []
}
```

| Field | Meaning |
|---|---|
| `migrations_applied` | Number of schema migrations already applied. |
| `migrations_pending` | Number of available migrations not yet applied. Run `project-migrate` to apply them. |
| `checksums` | Stability state of tracked project files (`valid-stable`, `valid-modified`, `missing`, `corrupted`). |
| `warnings` | Non-fatal issues like pending migrations or stale cache entries. |
| `errors` | Fatal issues requiring repair. |

---

## Ground-truth corpus verification

### Building a corpus

A ground-truth corpus is a set of known source files compiled under declared toolchains, producing
byte-identical builds that serve as validation targets for decompilation candidates.

Create the bundled built-in manifest:

```console
$ x86decomp corpus-create-manifest corpus-sources/ manifest.json
```

Build the corpus from the manifest:

```console
$ x86decomp corpus-build manifest.json corpus-output/
```

This compiles every source in the manifest under every declared compiler profile, recording
input hashes, output hashes, compiler banners, and timings.

```json
{
  "manifest": {
    "path": "manifest.json",
    "sha256": "..."
  },
  "records": [
    {
      "source_file": "array_init.c",
      "source_sha256": "...",
      "compiler_profile": {
        "family": "gcc",
        "version": "13.2.0",
        "flags": "-O2 -m32"
      },
      "output_sha256": "...",
      "object_sha256": "...",
      "compile_time_ms": 84
    }
  ],
  "total_records": 240,
  "successful": 240,
  "failed": 0
}
```

### Verifying a corpus

```console
$ x86decomp corpus-verify corpus-output/report.json
```

This re-hashes every source and output file recorded in the build report and compares against
the recorded hashes:

```json
{
  "valid": true,
  "failures": [],
  "total_checked": 240,
  "passed": 240,
  "failed": 0
}
```

!!! tip "Reproducible corpora"
    The same manifest, sources, and compiler versions should produce identical output hashes
    across machines. The corpus build and verify cycle is the proving ground for compiler
    profiles before they are used in matching decompilation.

### Generating a synthetic corpus

For compiler laboratory experiments, generate deterministic C/C++ source corpora:

```console
$ x86decomp corpus-generate synthetic-corpus/ --cases-per-family 16 --seed 0x86DEC0DE
$ x86decomp corpus-generated-verify synthetic-corpus/report.json
```

---

## Project operations

### Migration

If `project-check` reports pending migrations:

```console
$ x86decomp project-migrate my-project/ --backup pre-migration-backup.zip
```

Dry-run first to preview changes:

```console
$ x86decomp project-migrate my-project/ --dry-run
```

### Backup and restore

Create a deterministic project backup:

```console
$ x86decomp project-backup my-project/ my-project-20260711.zip
```

Restore from a verified backup:

```console
$ x86decomp project-restore my-project-20260711.zip restored-project/
```

### Repair

Inspect potential issues without applying fixes:

```console
$ x86decomp project-repair my-project/
```

Apply repairs:

```console
$ x86decomp project-repair my-project/ --apply
```

### Garbage collection

Inspect unreferenced content:

```console
$ x86decomp project-gc my-project/
```

Remove unreferenced content:

```console
$ x86decomp project-gc my-project/ --apply
```

---

## Common setup errors

### Wrong Python version

```
$ x86decomp --version
ERROR: Python 3.11 or newer is required
```

Install Python 3.11+ and ensure it is the default `python` on `PATH`.

### Missing tools

```
$ x86decomp disassemble code.bin --architecture x86
ERROR: capstone is not installed
```

This means the `[disassembly]` or `[symbolic]` extras are not installed:

```console
$ python -m pip install 'x86decomp-toolkit[disassembly]'
```

### Path issues

```
$ x86decomp init target.exe my-project/
ERROR: project directory is not empty
```

The target project directory must either not exist or be empty. Use a new directory name,
or remove the existing content.

```
$ x86decomp verify-project my-project/
ERROR: missing project.json
```

`verify-project` must point to the project root directory, not a subdirectory. Ensure you
are in or referencing the directory that contains `project.json`.

```
$ x86decomp ghidra-export target.exe ...
ERROR: Ghidra analyzeHeadless not found
```

Either set `GHIDRA_HOME` or pass `--ghidra-home`. Verify the launcher exists:

```console
$ ls "$GHIDRA_HOME/support/analyzeHeadless"
```

### Binary hash mismatch after rebuild

If you recompile the target binary and want to restart analysis:

```console
$ x86decomp init target-v2.exe my-project-v2/
```

Projects are bound to a specific binary SHA-256. Reinitialize with the new binary rather than
manually editing `project.json`.

---

## Next steps

- [Understand decompilation modes](../concepts/decompilation-modes.md) — matching vs functional vs hybrid.
- [Evidence and claims](../concepts/evidence-and-claims.md) — how the toolkit tracks provenance.
- [Compiler laboratory](../concepts/compiler-laboratory.md) — using compiler matrices to identify the target toolchain.
- [Workflows](../workflows/index.md) — guided workflows for matching and functional decompilation.
- [Project operations and recovery](../workflows/project-operations-recovery.md) — backup, restore, repair, and migration workflows.
- [Troubleshooting](../troubleshooting/index.md) — additional diagnostic procedures.
