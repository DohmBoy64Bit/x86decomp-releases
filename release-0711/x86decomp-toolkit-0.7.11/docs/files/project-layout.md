# Project directory layout

Every x86decomp project is created with a standard directory structure of 43 directories organized by function. All paths are relative to the project root.

---

## Directory inventory

### Analysis (`analysis/`)

| Directory | Purpose |
|-----------|---------|
| `analysis/database/` | SQLite analysis database (`analysis.sqlite3`) — PE structure, function metadata, cross-references |
| `analysis/exports/` | Exported analysis data (JSON dumps, symbol tables) |
| `analysis/ghidra/` | Ghidra project files, scripts, and exported data |
| `analysis/mcp-transactions/` | Recorded MCP (Model Context Protocol) transactions with Ghidra or other tools |

### Build (`build/`)

| Directory | Purpose |
|-----------|---------|
| `build/compiler/` | Compiler output objects (`.obj`, `.o`) from experiments and matched builds |
| `build/candidates/` | Candidate source files awaiting compilation and validation |
| `build/cache/` | Build cache for incremental compilation |
| `build/patches/` | Binary patch files for incremental relinking |
| `build/relink/` | Relink workspace — manifests, object staging, relinked outputs |

### Configuration (`config/`)

| Directory | Purpose |
|-----------|---------|
| `config/compiler-profiles/` | Compiler profile JSON files (see [compiler-profile.md](../config/compiler-profile.md)) |
| `config/toolchains/` | Toolchain definitions and wrapper scripts |
| `config/harnesses/` | Execution harness definitions for functional testing |

### Evidence (`evidence/`)

| Directory | Purpose |
|-----------|---------|
| `evidence/items/` | Evidence records (see [evidence-claim.md](../config/evidence-claim.md)) |
| `evidence/claims/` | Claim records |
| `evidence/files/` | File-backed evidence artifacts |

### Functions (`functions/`)

| Directory | Purpose |
|-----------|---------|
| `functions/` | One subdirectory per function (named `pe-rva_XXXXXXXX`), each containing `function.json`, source code, and verification artifacts |

### Memory (`memory/`)

| Directory | Purpose |
|-----------|---------|
| `memory/` | Project memory event ledger (`events.jsonl`) — append-only audit log |

### Orchestration (`orchestration/`)

| Directory | Purpose |
|-----------|---------|
| `orchestration/pipelines/` | Pipeline manifests (see [pipeline.md](../config/pipeline.md)) |
| `orchestration/logs/` | Pipeline execution logs |
| `orchestration/work/` | Pipeline work artifacts |

### Original (`original/`)

| Directory | Purpose |
|-----------|---------|
| `original/resources/` | Original binary resources (extracted icons, bitmaps, strings) |

### Reports (`reports/`)

| Directory | Purpose |
|-----------|---------|
| `reports/matching/` | Match verification reports (byte comparison, ABI checks) |
| `reports/functional/` | Functional validation reports (harness results, symbolic proofs) |
| `reports/benchmarks/` | Benchmark corpus execution reports |
| `reports/convergence/` | Convergence tracking reports across project iterations |
| `reports/reproducibility/` | Build reproducibility audit reports |
| `reports/security/` | Security audit reports |

### Source (`src/`)

| Directory | Purpose |
|-----------|---------|
| `src/asm/` | Assembly source files (byte-form default) |
| `src/staging/` | Staging area for source files under active development |
| `src/matched/` | Source files that have achieved byte-identical matching |
| `src/functional/` | Source files validated for functional equivalence |

### State (`state/`)

| Directory | Purpose |
|-----------|---------|
| `state/` | Project state SQLite database (`project-state.sqlite3`) and workflow files |

### Target pack (`target-pack/`)

| Directory | Purpose |
|-----------|---------|
| `target-pack/` | Target pack data — `target.toml`, `observations.json`, `image-profile.json`, `acceptance.json`, `template-plan.json`, `artifacts/` |

### Templates (`templates/`)

| Directory | Purpose |
|-----------|---------|
| `templates/` | Reusable project templates |

### Tests (`tests/`)

| Directory | Purpose |
|-----------|---------|
| `tests/harnesses/` | Execution harness source files for functional testing |

### Work (`work/`)

| Directory | Purpose |
|-----------|---------|
| `work/` | Work queue SQLite database (`tasks.sqlite3`) |

### Artifacts (`artifacts/`)

| Directory | Purpose |
|-----------|---------|
| `artifacts/` | Content-addressed artifact store for immutable build outputs |

---

## Root-level files

| File | Purpose |
|------|---------|
| `project.json` | Project configuration (see [project.md](../config/project.md)) |
| `analysis/program.json` | PE program manifest — parsed binary metadata |
| `analysis/host.json` | Host environment snapshot (Python version, platform, timestamp) |
| `memory/events.jsonl` | Append-only memory event ledger |
| `analysis/database/analysis.sqlite3` | SQLite analysis database |
| `work/tasks.sqlite3` | SQLite work queue database |
| `state/project-state.sqlite3` | SQLite project state database |

---

## Directory listing (flat)

```text
analysis/database/
analysis/exports/
analysis/ghidra/
analysis/mcp-transactions/
artifacts/
build/cache/
build/candidates/
build/compiler/
build/patches/
build/relink/
config/compiler-profiles/
config/harnesses/
config/toolchains/
evidence/claims/
evidence/files/
evidence/items/
functions/
memory/
orchestration/logs/
orchestration/pipelines/
orchestration/work/
original/resources/
reports/benchmarks/
reports/convergence/
reports/functional/
reports/matching/
reports/reproducibility/
reports/security/
src/asm/
src/functional/
src/matched/
src/staging/
state/
target-pack/
templates/
tests/harnesses/
work/
```

!!! note
    All directories are created at project initialization by `x86decomp project init` and validated by `x86decomp project verify`.
