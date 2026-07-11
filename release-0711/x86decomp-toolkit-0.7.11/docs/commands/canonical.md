# Canonical Command Structure

## Overview

The canonical command surface merges four capability owners — **governance**, **reconstruction**, **native**, and **assembly** — into one unified CLI. Each group contains one or more leaf *actions*, and each action resolves to a single owner that implements it.

### Statistics

- **59** canonical command groups
- **239** canonical routes (leaf commands)
- **4** capability owners

### How it works

Canonical commands use the `group action` syntax:

```
x86decomp GROUP ACTION [--project DIR] [--actor NAME] [action-specific args...]
```

The `--project` and `--actor` options are shared across every canonical group:

| Option | Default | Description |
|---|---|---|
| `--project DIR` | `.` (current directory) | Project root directory |
| `--actor NAME` | `analyst` | Actor identifier for provenance |

Each action-specific parser is inherited from the owning subsystem. The route is resolved by precedence:

1. An explicit declaration in the merged-groups table (for groups like `project`, `changeset`, `hybrid` that span multiple owners)
2. A latest-shared-owner override
3. The sole available owner (unique group-owner mapping)

### Cataloging commands

Use `x86decomp commands` to list all canonical routes:

```
x86decomp commands [--group GROUP] [--owner OWNER]
```

| Option | Description |
|---|---|
| `--group GROUP` | Filter to routes in one canonical group |
| `--owner OWNER` | Filter to routes implemented by one capability owner |

```console
$ x86decomp commands
$ x86decomp commands --group abi
$ x86decomp commands --owner reconstruction
```

The catalog output includes release metadata, group and route counts, merged-group declarations, and each route's `group`, `action`, and `owner`.

## Capability owners

| Owner | Description |
|---|---|
| `governance` | Evidence, claims, hypotheses, campaigns, reviews, consensus, proofs, workers, plugins |
| `reconstruction` | ABI, build, headers, libraries, decompiler patterns, LLM integration, source maps, modules, types, vtables |
| `native` | Boundary auditing, hybrid composition and verification, loop analysis, matching, PE patching, runtime, staging, Windows tooling |
| `assembly` | Assembly annotation, batch processing, listing, materialization, roundtrip verification, relocation inspection, project init/check, hybrid generation |

## Canonical groups

| Group | Owner | Actions |
|---|---|---|
| `abi` | reconstruction | `compare`, `export`, `recover`, `shim`, `show`, `verify` |
| `asm` | assembly | `annotate`, `batch`, `list`, `materialize`, `report`, `verify-roundtrip` |
| `asset` | reconstruction | `inventory` |
| `boundary` | native | `audit`, `audit-project`, `export-ghidra-fixes`, `list`, `show` |
| `build` | reconstruction | `add-target`, `add-variant`, `compare-modes`, `create`, `generate`, `matrix`, `show`, `validate` |
| `campaign` | governance | `branch`, `create`, `list`, `pause`, `plan`, `resume`, `snapshot`, `start`, `status`, `stop` |
| `candidate` | governance/reconstruction | `add-file`, `compare`, `create`, `evaluate`, `list`, `promote`, `search`, `show`, `transition` |
| `capsule` | reconstruction | `create`, `inspect`, `reproduce`, `verify` |
| `changeset` | governance/reconstruction | `add-operation`, `apply`, `conflicts`, `create`, `export`, `inspect`, `merge`, `rebase`, `show`, `verify` |
| `class` | reconstruction | `scaffold` |
| `compiler-rules` | reconstruction | `compare-flags`, `learn-rule`, `rule-report` |
| `consensus` | governance | `conflicts`, `explain`, `record`, `resolve`, `scan` |
| `counterexample` | governance | `add`, `list`, `promote`, `show` |
| `decompiler` | reconstruction | `cleanup` |
| `diff` | reconstruction | `explain` |
| `family` | governance | `add`, `correlate`, `create`, `report` |
| `function` | reconstruction | `classify`, `discover`, `reconcile`, `sort` |
| `game-pattern` | reconstruction | `state-machine` |
| `ghidra-mcp` | reconstruction | `batch-decompile`, `decompile`, `functions`, `probe`, `sync-names` |
| `graph` | governance | `edge`, `impact`, `node` |
| `headers` | reconstruction | `create`, `cycles`, `declare`, `explain`, `include`, `synthesize`, `synthesize-project`, `validate` |
| `hybrid` | native/assembly | `compose`, `generate`, `verify` |
| `hypothesis` | governance | `create`, `dependency`, `evidence`, `gate`, `list`, `show`, `transition` |
| `image-text` | reconstruction | `compose` |
| `library` | reconstruction | `accept`, `candidates`, `externalize`, `identify`, `reconstruct`, `reject` |
| `llm` | reconstruction | `batch-create`, `batch-match`, `cpp-generate`, `generate`, `job-create`, `job-from-range`, `match`, `probe`, `profile-create`, `profile-validate`, `prompt`, `providers`, `verify` |
| `loop` | native | `list`, `run`, `show` |
| `match` | native | `batch`, `compare`, `mismatches`, `report` |
| `mod` | reconstruction | `branch-init` |
| `module` | reconstruction | `add-member`, `add-unit-member`, `assign`, `create`, `create-unit`, `list`, `show`, `show-unit`, `suggest` |
| `pattern` | reconstruction | `catalog`, `generate`, `match`, `promote`, `scan` |
| `pe` | native | `export-coff`, `export-sections`, `inventory`, `patch-apply`, `patch-plan`, `text-swap` |
| `playability` | reconstruction | `smoke-plan` |
| `plugin` | governance | `doctor`, `install`, `invoke`, `list`, `validate` |
| `progress` | reconstruction | `reconcile` |
| `project` | assembly/reconstruction | `check`, `doctor-paths`, `explain-boundaries`, `export`, `health`, `init`, `synthesize-layout` |
| `proof` | governance | `evaluate`, `export`, `inspect`, `obligation`, `result`, `verify` |
| `provenance` | reconstruction | `binary`, `export`, `record`, `source` |
| `regression` | reconstruction | `compare` |
| `release-policy` | reconstruction | `moddable-source` |
| `reloc` | assembly | `inspect`, `resolve`, `supported` |
| `review` | governance | `assign`, `create`, `decide`, `list`, `lock`, `show` |
| `runtime` | native | `launch`, `map-crash`, `validate-image` |
| `runtime-analysis` | reconstruction | `identify`, `match-library`, `quarantine` |
| `script-port` | reconstruction | `audit` |
| `security` | reconstruction | `finding`, `policy`, `report`, `scan` |
| `source` | reconstruction | `impact`, `lock`, `reconcile`, `unlock` |
| `source-map` | reconstruction | `annotate`, `verify` |
| `source-stage` | reconstruction | `classify` |
| `staging` | native | `compile-check`, `generate-context`, `resolve`, `scan`, `unresolved` |
| `subsystem` | reconstruction | `detect` |
| `tests` | reconstruction | `add`, `explain`, `list`, `promote-counterexample`, `synthesize` |
| `text-swap` | reconstruction | `build`, `inject`, `plan`, `verify` |
| `toolchain` | reconstruction | `hash-tree`, `redact-package`, `verify-local` |
| `triage` | reconstruction | `next` |
| `type` | reconstruction | `propagate` |
| `vtable` | reconstruction | `recover` |
| `windows` | native | `discover-ghidra`, `doctor`, `response-file` |
| `worker` | governance | `doctor`, `list`, `register`, `select`, `status` |

### Examples

```console
# Canonical project initialization
$ x86decomp project init target.exe ./my-project

# Canonical ABI comparison
$ x86decomp abi compare --project ./my-project --target target.asm --candidate candidate.asm

# Canonical assembly annotation
$ x86decomp asm annotate --project ./my-project --function pe-rva:00001234

# Catalog all routes
$ x86decomp commands

# Catalog routes for one owner
$ x86decomp commands --owner native

# Catalog routes for one group
$ x86decomp commands --group llm
```

!!! info "Legacy flat commands"
    Many commands are also available in flat `x86decomp command-name` form
    (e.g., `x86decomp init`, `x86decomp compile`). The canonical `group action`
    form is the unified surface; the flat form is maintained for compatibility.

!!! note "Groups spanning multiple owners"
    Three groups are merged across owners: `project` (assembly + reconstruction),
    `changeset` (governance + reconstruction), and `hybrid` (native + assembly).
    Each action in these groups routes to its declared owner via the merged-groups table.
