# x86decomp-toolkit 0.4.0

An evidence-governed, resumable toolkit for incremental native Windows x86 and x86-64 decompilation. Version 0.4.0 turns the broad 0.3 architecture into a production-pilot platform: target packs, grounded project templates, durable jobs, transactional project state, bounded workers, reproducibility manifests, release gates, and operational recovery are now first-class.

## Truth boundary

The toolkit does not claim to recover erased source facts or prove arbitrary programs equivalent. It distinguishes:

- **observations** captured from artifacts or execution;
- **derived facts** calculated deterministically from observations;
- **proposals** from analysts, decompilers, or AI;
- **verified claims** that pass the project’s narrow evidence gate;
- **bounded validations** whose instruction, path, memory, input, and environment scope is recorded.

The three-independent-source rule is a governance control, not a guarantee of truth. AI output is never evidence by itself.

## Two independent function modes

### Matching decompilation

```text
not_started → decompiled → compiles → abi_compatible
            → instruction_similar → byte_matched
            → image_integrated → full_relink_validated
```

### Functional decompilation

```text
not_started → decompiled → compiles → abi_compatible
            → differentially_validated
            → symbolically_bounded
            → integration_validated
```

Either mode can enter `blocked`. Advancing one mode never advances the other.

## What 0.4.0 adds

- **Verified target packs** that separate observed artifacts from explicit operator decisions.
- **Automatic/semi-automatic project templates** for matching, functional, or hybrid work. Unknown compiler, linker, language, and layout facts become blockers rather than fabricated configuration.
- **Durable pipelines** with idempotency keys, dependencies, retries, cancellation, runner heartbeats, stale-run recovery, and content-sealed outputs.
- **Transactional project state** with schema migrations, deterministic backups, safe restore, repair, snapshots, leases, and artifact garbage collection.
- **Content-addressed immutable storage** with SHA-256 objects and transactional references.
- **Bounded workers** for local execution and hardened Docker/Podman execution with a read-only root, disabled network, dropped capabilities, and resource limits.
- **Compiler-worker orchestration** for user-owned toolchains with exact provenance and cache support.
- **Linker reconstruction plans** grounded in PE, MAP, COFF, archive, relocation, and COMDAT evidence.
- **C++ recovery models** for validated RTTI/vtable relationships and conservative adjustor-thunk candidates.
- **Harness generation** from explicit ABI contracts and pointer-region declarations.
- **Whole-image convergence** with target-specific normalization and historical progress records.
- **Reproducibility manifests** explaining what a second machine can and cannot reproduce.
- **Release gates** combining integrity, target-pack, workflow, evidence, pipeline, security, reproducibility, and convergence requirements.
- **Security tooling** for source-tree audits, release-manifest verification, CycloneDX SBOM generation, and a real `pip-audit` adapter.
- **Deterministic generated corpora** that expand reviewed C/C++ template families without pretending source generation is compiler validation.
- **Read-only project service** exposing control-plane state without granting mutation authority.

All 0.3.1 commands, schemas, matching/functional states, parsers, validators, adapters, Ghidra scripts, and package boundaries remain supported or have explicit migration paths.

## Repository layout

```text
x86decomp-toolkit/
  src/x86decomp/             Python runtime and CLI
  ghidra_scripts/            Ghidra Java exporters/queries
  schemas/                   machine-readable contracts
  skills/x86decomp/          evidence-engineering operating skill
  docs/                      architecture and operations documentation
  examples/                  bounded examples and compatibility fixtures
  corpus/                    reviewed source corpus inputs
  tests/                     toolkit regression tests
  test-suite/                independently packaged comprehensive verifier
```

Architecture views:

- [Mermaid toolkit map](docs/ARCHITECTURE_MAP.md)
- [ASCII toolkit map](docs/ARCHITECTURE_MAP_ASCII.txt)
- [Mermaid test-suite map](test-suite/docs/ARCHITECTURE_MAP.md)
- [ASCII test-suite map](test-suite/docs/ARCHITECTURE_MAP_ASCII.txt)

## Supported baseline

The implemented baseline covers native PE32/i386 and PE32+/AMD64, conventional unpacked user-mode C/C++, COFF/bigobj objects, bounded static/import archives, and function-oriented incremental work. Packed, virtualized, encrypted, self-modifying, kernel-mode, managed CLR, or anti-analysis targets are not silently accepted as ordinary inputs.

## Install

Core runtime:

```bash
python -m pip install .
```

Common validators and read-only service:

```bash
python -m pip install '.[disassembly,dynamic,symbolic,service]'
```

Full optional Python integrations:

```bash
python -m pip install '.[full]'
```

External installations such as Ghidra, DynamoRIO, historical MSVC, `lld-link`, Docker/Podman, and objdiff remain operator-managed. Proprietary toolchains are registered by path and hash; they are never redistributed.

## Recommended target-first workflow

### 1. Build a target pack

```bash
x86decomp target-pack-infer target.exe target-pack/ \
  --pdb target.pdb \
  --map target.map \
  --object obj/main.obj \
  --library lib/runtime.lib \
  --decisions target-decisions.json
```

Only supplied and parsed evidence is recorded. Decisions can establish known facts such as a compiler family, but omitted facts remain `unknown`.

### 2. Generate a grounded project

```bash
x86decomp project-from-target target-pack/ project/
python project/scripts/project.py check
```

The generated project includes a target-specific working layout, validation policy, blockers, default durable pipeline, helper command, source lanes, report directories, copied Ghidra scripts, and target documentation. It does not generate fake decompiled functions.

### 3. Run or inspect the durable pipeline

```bash
x86decomp pipeline-run project/ project/orchestration/pipelines/default.json
x86decomp pipeline-status project/ <pipeline-id>
x86decomp pipeline-recover project/ --stale-seconds 600
```

Missing adapters or unmet evidence gates become durable `blocked` records. Successful outputs are materialized outside ephemeral workspaces, hashed, and revalidated before reuse.

### 4. Recover and maintain project state

```bash
x86decomp project-check project/
x86decomp project-backup project/ project-backup.tar.gz
x86decomp project-migrate project/ --dry-run
x86decomp project-repair project/
x86decomp project-gc project/
```

Apply destructive or state-changing operations only after reviewing dry-run output and producing a backup.

### 5. Gate a target release

```bash
x86decomp release-gate project/ \
  --reproduction-manifest project/reports/reproducibility/manifest.json \
  --security-report project/reports/security/audit.json \
  --convergence-report project/reports/convergence/latest.json \
  --require-workflows \
  --require-verified-claims \
  --require-succeeded-pipelines \
  --report project/reports/release-gate.json
```

A passing release gate means the declared project acceptance contract passed. It is not proof of original-source recovery or all-input equivalence.

## Automatic/semi-automatic templates

Template selection uses only:

- parsed architecture and image kind;
- roles of supplied evidence (`pdb`, `linker_map`, `coff_object`, `static_library`, `rebuilt_image`);
- explicit mode and toolchain decisions;
- PDB source-extension evidence, labeled as a candidate rather than fact;
- target-pack integrity.

The template contract reports readiness and blockers separately. For example, a matching project with MAP and OBJ evidence can be linker-reconstruction-ready while still blocked on an unknown historical compiler version.

```bash
x86decomp template-derive target-pack/
x86decomp template-materialize project/
```

## Generated compiler corpus

```bash
x86decomp corpus-generate generated-corpus/ --cases-per-family 64 --seed 0x1234
x86decomp corpus-generated-verify generated-corpus/corpus-generation.json
```

This produces deterministic C/C++ source cases and hashes. It does not claim a compiler was tested. Add explicit compiler records and flag matrices, then run the normal corpus builder to create compiler evidence.

## Worker isolation

`local_bounded` applies time, resource, process, and output limits but is not a security boundary. `container` mode invokes Docker or Podman with:

- network disabled;
- read-only root filesystem;
- dropped Linux capabilities;
- `no-new-privileges`;
- explicit work-directory bind mount;
- bounded memory and process count;
- ephemeral `/tmp`.

Unknown native programs still belong in a disposable VM or external sandbox with explicit execution consent.

## Comprehensive test suite

The independently packaged verifier under `test-suite/`:

- detects adapters before prompting;
- asks for custom paths only when an adapter is missing;
- records unavailable integrations as `BLOCKED` rather than skipped;
- inventories every module, defined function/method, command, schema, Ghidra script, workflow state, and adapter;
- executes every defined Python function body at least once;
- runs native/supplemental tests, migration tests, CLI parse tests, packaging tests, live adapter probes, architecture-map checks, and detailed logging;
- builds and clean-installs the toolkit wheel and source distribution.

See [test-suite/README.md](test-suite/README.md).

## Key documentation

- [Architecture](docs/architecture.md)
- [Architecture map](docs/ARCHITECTURE_MAP.md)
- [Target packs and templates](docs/target-packs-and-templates.md)
- [Operations and recovery](docs/operations-and-recovery.md)
- [Build and verification](docs/build-and-verification.md)
- [Supported scope](docs/supported-scope.md)
- [Feature parity](FEATURE_PARITY.md)
- [Security](SECURITY.md)
- [Agent/contributor rules](AGENTS.md)
- [Project memory](PROJECT_MEMORY.md)
- [Release verification](VERIFICATION.md)

## Explicit non-goals

Version 0.4.0 does not claim:

- recovery of comments, original identifiers, macros, exact source-file boundaries, or erased template structure;
- universal compiler/linker identification;
- generic byte-identical whole-image reconstruction for every target;
- complete C++ RTTI/EH semantics for every compiler generation;
- safe host execution of arbitrary uploaded programs;
- all-path equivalence for arbitrary functions;
- support for packed, virtualized, malicious, or self-modifying targets as ordinary inputs.

The production-pilot goal is narrower: make substantial authorized targets durable, reproducible, recoverable, and measurably verifiable while preserving uncertainty and provenance.
