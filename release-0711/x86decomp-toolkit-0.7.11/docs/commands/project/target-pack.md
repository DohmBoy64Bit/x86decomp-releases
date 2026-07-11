# Project: Target Pack

## Overview

Target packs bridge the gap between a raw binary and a project. They record observed parser facts separately from user-supplied decisions, then drive template derivation and project generation.

---

## `x86decomp target-pack-infer`

Infers a fact-preserving target pack from a primary PE image and optional supporting artifacts.

### Synopsis

```bash
x86decomp target-pack-infer PRIMARY_IMAGE OUTPUT_DIR
    [--name NAME]
    [--pdb PDB]
    [--map MAP]
    [--object OBJ...]
    [--library LIB...]
    [--rebuilt-image REBUILT]
    [--decisions DECISIONS]
    [--reference-artifacts]
```

### Purpose

Parses the primary PE and all supplied artifacts. Produces a self-contained target-pack directory with `target.toml` (identity, decisions, artifact inventory), `observations.json` (bounded parser output), `image-profile.json` (reference-hash-bound image layout), `acceptance.json` (matching/functional minima), and `template-plan.json` (adapter needs and unresolved facts). Inferences never invent compiler versions, linker flags, names, or source layout.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PRIMARY_IMAGE` | Yes | path | Native PE32 or PE32+ to analyze. Must be a regular file. |
| `OUTPUT_DIR` | Yes | path | Output directory for the target pack. Must be empty or non-existent. |

### Options

| Option | Default | Description |
|---|---|---|
| `--name` | (stem of `PRIMARY_IMAGE`) | Human-readable target name written into `target.toml`. |
| `--pdb` | (none) | Companion MSF 7.0 PDB. Source file extensions in the DBI stream are recorded as language evidence only (never promoted to decisions). |
| `--map` | (none) | MSVC-compatible linker map (`.map` file). Parsed into `observations.json`. |
| `--object` | `[]` | COFF object file. Repeatable. Each is parsed for architecture, section count, symbol count, and COMDAT sections. |
| `--library` | `[]` | COFF archive/static or import library. Repeatable. Each is parsed for member count, symbol count, and object breakdown. |
| `--rebuilt-image` | (none) | A previously rebuilt PE image. Compared to confirm same architecture, hash, and path recorded. |
| `--decisions` | (none) | JSON file with explicit user decisions. Supported keys: `preferred_mode`, `compiler_family`, `compiler_version`, `linker_family`, `source_language`, `allow_host_execution`, `target_description`. Unknown keys raise an error. |
| `--reference-artifacts` | off (copies artifacts) | When set, records external artifact paths without copying files into the pack. Less portable; use only when policy forbids copies. |

### Decision fields

| Key | Type | Default | Valid values |
|---|---|---|---|
| `preferred_mode` | string | `"both"` | `matching`, `functional`, `both` |
| `compiler_family` | string | `"unknown"` | Any string |
| `compiler_version` | string | `"unknown"` | Any string |
| `linker_family` | string | `"unknown"` | Any string |
| `source_language` | string | `"unknown"` | Any string |
| `allow_host_execution` | boolean | `false` | `true` / `false` |
| `target_description` | string | `"No target-specific description supplied."` | Any string |

### Files written to `OUTPUT_DIR`

| File | Description |
|---|---|
| `target.toml` | Schema v1 target identity, decisions, scope, and artifact inventory. |
| `observations.json` | Bounded parser output: PE metadata, PDB, linker map, COFF objects, libraries, rebuilt image, source language evidence. |
| `image-profile.json` | Evidence- and hash-bound image layout profile. |
| `acceptance.json` | Matching and functional acceptance minima. |
| `template-plan.json` | Required/optional external adapters and facts needing user confirmation. |
| `artifacts/` | Copied artifact files (unless `--reference-artifacts`). |

### Exit behavior

- Success: emits `{target_pack, observations, output_directory}` as JSON on stdout, exit `0`.
- Failure: exits `2` with a JSON error on stderr.

### Example

```bash
x86decomp target-pack-infer target.exe ./target-pack \
    --name "MyTarget" \
    --pdb target.pdb \
    --map target.map \
    --object obj1.obj --object obj2.obj \
    --library libc.lib \
    --decisions decisions.json
```

Example `decisions.json`:
```json
{
  "preferred_mode": "both",
  "compiler_family": "msvc",
  "compiler_version": "19.29",
  "source_language": "c++",
  "allow_host_execution": false,
  "target_description": "Windows game executable, circa 2003"
}
```

### Related commands

- [`target-pack-verify`](#x86decomp-target-pack-verify) — verify artifact integrity
- [`template-derive`](#x86decomp-template-derive) — derive a template contract
- [`project-from-target`](#x86decomp-project-from-target) — generate a project

---

## `x86decomp target-pack-verify`

Verifies a target pack's artifact integrity: file existence, hash matching, and size matching.

### Synopsis

```bash
x86decomp target-pack-verify TARGET_PACK
```

### Purpose

Loads `target.toml`, validates schema version, and for each artifact record verifies that the referenced file exists, is a regular file (not a symlink), its SHA-256 matches the recorded hash, and its file size matches. Also confirms the primary image hash matches `primary_sha256`.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `TARGET_PACK` | Yes | path | Path to a `target.toml` file, or a directory containing `target.toml`. |

### Exit behavior

- Success: emits `{valid, target_id, failures, artifact_count}` as JSON on stdout, exit `0`.
- Failure: exits `2` with a JSON error on stderr (unsupported schema, invalid TOML).

### Example

```bash
x86decomp target-pack-verify ./target-pack
```

```json
{
  "valid": true,
  "target_id": "x86-e3b0c44298fc1c149afbf4c8",
  "failures": [],
  "artifact_count": 3
}
```

### Related commands

- [`target-pack-infer`](#x86decomp-target-pack-infer) — create the pack
- [`project-from-target`](#x86decomp-project-from-target) — use the verified pack

---

## `x86decomp project-from-target`

Initializes a decompilation project from a verified target pack.

### Synopsis

```bash
x86decomp project-from-target TARGET_PACK PROJECT [--reference-binary]
```

### Purpose

Verifies the target pack, resolves the primary image artifact, initializes a standard project with `init`, copies the entire target pack into `PROJECT/target-pack/`, updates `project.json` with the target pack path and template kind, copies Ghidra scripts if available, writes `config/target-decisions.json`, creates a default pipeline, and materializes the project template layout. Also writes a `TARGET.md` summary.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `TARGET_PACK` | Yes | path | Directory containing `target.toml`. |
| `PROJECT` | Yes | path | Project output directory. Must be empty or non-existent. |

### Options

| Option | Default | Description |
|---|---|---|
| `--reference-binary` | off (binary is copied) | Passed through to the underlying `init` call. |

### What it creates

Beyond the standard project layout, also produces:

| Path | Description |
|---|---|
| `target-pack/` | Full copy of the target pack directory. |
| `config/target-decisions.json` | Schema v1 record of all decisions from the target pack. |
| `orchestration/pipelines/default.json` | Default durable pipeline manifest. |
| `ghidra_scripts/` | Copied from the toolkit repository if available. |
| `TARGET.md` | Markdown summary with target ID, architecture, unknowns, and pipeline command. |

The full template layout is also materialized (see [`template-materialize`](#x86decomp-template-materialize)).

### Exit behavior

- Success: emits `{project, target_pack_verification, project_root, pipeline, template}` as JSON on stdout, exit `0`.
- Failure: exits `2` with a JSON error on stderr.

### Example

```bash
x86decomp project-from-target ./target-pack ./myproject
```

### Related commands

- [`target-pack-infer`](#x86decomp-target-pack-infer) — create the pack
- [`template-materialize`](#x86decomp-template-materialize) — materialize layout separately

---

## `x86decomp template-derive`

Derives a grounded project-template contract from a target pack.

### Synopsis

```bash
x86decomp template-derive TARGET_PACK
```

### Purpose

Uses only verified pack contents and explicit decisions to calculate: enabled modes; exact assembly fallback need; whether object comparison, linker reconstruction, or whole-image comparison has enough supplied artifacts; whether compiler/linker identities are confirmed; whether dynamic host execution is authorized; evidence-backed source-language candidates; and unresolved blockers. Does not emit candidate function bodies or fake compiler profiles.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `TARGET_PACK` | Yes | path | Directory containing `target.toml`. |

### Example

```bash
x86decomp template-derive ./target-pack
```

### Related commands

- [`template-materialize`](#x86decomp-template-materialize) — materialize the template into a project
- [`target-pack-infer`](#x86decomp-target-pack-infer) — create the pack that drives derivation

---

## `x86decomp template-materialize`

Materializes the grounded working layout for an existing target project.

### Synopsis

```bash
x86decomp template-materialize PROJECT
```

### Purpose

Creates the source, header, build, test, report, and configuration directories needed for the project's template kind (matching, functional, or hybrid). Writes placeholder guidance files (`config/project-template.json`, `config/validation-policy.json`, `config/next-steps.json`, `scripts/project.py`) that describe the template contract without inventing source code.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PROJECT` | Yes | path | Project root directory with `project.json`. |

### Example

```bash
x86decomp template-materialize ./myproject
```

### Related commands

- [`template-derive`](#x86decomp-template-derive) — derive the contract first
- [`project-from-target`](#x86decomp-project-from-target) — does both verification and materialization
