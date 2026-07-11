# Project: init / verify-project

## `x86decomp init`

Initializes a native PE decompilation project from a Windows PE binary.

### Synopsis

```bash
x86decomp init BINARY PROJECT [--reference-binary]
```

### Purpose

Parses the target PE (PE32 or PE32+), auto-detects the architecture, creates the full project directory layout, writes `project.json`, the program manifest (`analysis/program.json`), the host environment record (`analysis/host.json`), initializes the analysis database, work queue, project-state database, content store, and project memory ledger. Records the first project-memory event with the binary identity.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `BINARY` | Yes | path | Native Windows PE32 or PE32+ file to analyze. |
| `PROJECT` | Yes | path | Project root directory. Must be empty or non-existent. |

### Options

| Option | Default | Description |
|---|---|---|
| `--reference-binary` | off (binary is copied) | When set, references the external binary path instead of copying it into `PROJECT/original/`. |

!!! warning "Empty directory required"
    `init` rejects non-empty project directories. Use a fresh directory or an empty existing one.

### What it creates

| Path | Description |
|---|---|
| `project.json` | Schema v3 project identity, binary hash, paths to all subsystems. |
| `analysis/program.json` | Full PE metadata dump (`parse_pe(...).to_dict()`). |
| `analysis/host.json` | Python version, platform, and implementation at creation time. |
| `analysis/database/analysis.sqlite3` | Empty SQLite analysis database. |
| `work/tasks.sqlite3` | Empty SQLite work queue. |
| `state/project-state.sqlite3` | Project-state database with schema-metadata row. |
| `artifacts/` | Content store root directory. |
| `memory/events.jsonl` | Project memory ledger (first event written). |

Plus the full 37-directory project layout (`PROJECT_DIRS` in `src/x86decomp/project.py`), including `src/asm/`, `src/matched/`, `src/functional/`, `build/`, `evidence/`, `functions/`, `reports/`, `tests/`, `config/`, `orchestration/`, `target-pack/`, `templates/`, and `analysis/ghidra/`.

### Exit behavior

- Success: emits the project dictionary as JSON on stdout, exit `0`.
- Failure: exits `2` with a JSON error on stderr (empty directory, invalid PE, etc.).

### Project ID convention

The project ID is constructed as:
```
x86d-{sha256[:16]}-{uuid8}    # for x86 PE32
x64d-{sha256[:16]}-{uuid8}    # for x86-64 PE32+
```

### Example

```bash
x86decomp init target.exe ./myproject
```

```json
{
  "schema_version": 3,
  "project_id": "x86d-e3b0c44298fc1c14-1a2b3c4d",
  "created_at": "2025-07-11T12:00:00Z",
  "supported_scope": "native Windows PE32 x86",
  "architecture": "x86",
  "default_modes": ["matching", "functional"],
  "binary": {
    "name": "target.exe",
    "source_kind": "copied",
    "path": "original/target.exe",
    "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "size": 102400
  },
  "program_manifest": "analysis/program.json",
  "analysis_database": "analysis/database/analysis.sqlite3",
  "work_queue": "work/tasks.sqlite3",
  "memory_ledger": "memory/events.jsonl",
  "function_root": "functions",
  "evidence_root": "evidence",
  "project_state_database": "state/project-state.sqlite3",
  "content_store": "artifacts",
  "target_pack": "target-pack/target.toml",
  "orchestration_root": "orchestration",
  "toolkit_release": "0.7.11",
  "status": "initialized"
}
```

### Related commands

- [`verify-project`](#x86decomp-verify-project) — validate the project after initialization
- [`target-pack-infer`](target-pack.md) — create a project from a target pack
- [`project-check`](operations.md#x86decomp-project-check) — check project state integrity

---

## `x86decomp verify-project`

Validates a project's structure, binary hash, program manifest, and state database integrity.

### Synopsis

```bash
x86decomp verify-project PROJECT
```

### Purpose

Reads `project.json`, verifies the schema version, checks the declared binary path and SHA-256, reparses the binary against the recorded program manifest, validates the analysis database, work queue, project-state database, content store, and memory ledger.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PROJECT` | Yes | path | Project root directory containing `project.json`. |

### Checks performed

1. `project.json` exists and contains a valid object.
2. Schema version is 1, 2, or 3.
3. Binary file exists at the resolved path.
4. Binary SHA-256 matches the recorded hash.
5. Program manifest (`analysis/program.json`) exists.
6. Program manifest fields (`file_sha256`, `machine`, `image_base`, `entry_rva`, `number_of_sections`, `size_of_image`, `architecture`) match the reparsed binary.
7. For schema v2+: `analysis_database` and `work_queue` files exist.
8. For schema v2+: `default_modes` is `["matching", "functional"]`.
9. For schema v3: `project_state_database` file exists.
10. For schema v3: `content_store` directory exists.
11. Project memory ledger integrity check.

### Exit behavior

- Success: emits verification result as JSON on stdout, exit `0`.
- Failure: exits `2` with a JSON error on stderr.

### Example

```bash
x86decomp verify-project ./myproject
```

```json
{
  "project_id": "x86d-e3b0c44298fc1c14-1a2b3c4d",
  "architecture": "x86",
  "valid": true,
  "failures": [],
  "binary_path": "/path/to/myproject/original/target.exe",
  "memory_event_count": 1
}
```

### Related commands

- [`init`](#x86decomp-init) — create the project
- [`project-check`](operations.md#x86decomp-project-check) — schema v3 integrity check via `ProjectCheck`
- [`project-repair`](operations.md#x86decomp-project-repair) — repair reconstructible indexes

---

## `x86decomp inspect-pe`

Parses PE32 or PE32+ metadata from a binary file.

### Synopsis

```bash
x86decomp inspect-pe BINARY
```

### Purpose

Parses the PE headers, sections, imports, exports, relocations, resources, and architecture. Returns the full `PEImage.to_dict()` representation. This is a read-only, non-mutating operation.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `BINARY` | Yes | path | PE32 or PE32+ file to parse. |

### Options

None.

### Example

```bash
x86decomp inspect-pe target.exe
```

### Related commands

- [`pdb-inspect`](#x86decomp-pdb-inspect) — inspect a companion PDB
- [`coff-inspect`](../analysis/coff.md) — inspect individual COFF objects

---

## `x86decomp pdb-inspect`

Inspects an MSF 7.0 PDB file and optionally matches it to a companion PE.

### Synopsis

```bash
x86decomp pdb-inspect PDB [--pe PE_PATH]
```

### Purpose

Parses an MSF 7.0 (Multi-Stream Format) PDB file. When `--pe` is provided, matches DBI stream source information, section contributions, and public/global symbol records against the PE.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PDB` | Yes | path | MSF 7.0 PDB file to inspect. |

### Options

| Option | Default | Description |
|---|---|---|
| `--pe` | (none) | Optional companion PE path for cross-referencing symbol and section information. |

### Example

```bash
x86decomp pdb-inspect target.pdb --pe target.exe
```

### Related commands

- [`inspect-pe`](#x86decomp-inspect-pe) — parse the PE itself
- [`metadata-scan`](../analysis/metadata.md) — recover MSVC RTTI/vtable metadata from PE and PDB
- [`target-pack-infer`](target-pack.md) — include PDB in a target pack
