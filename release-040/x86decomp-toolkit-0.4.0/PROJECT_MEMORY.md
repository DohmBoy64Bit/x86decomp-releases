# Project memory — x86decomp-toolkit 0.4.0

This document records durable repository-level decisions. Per-target projects keep their own append-only hash-chained memory under `memory/events.jsonl`.

## Mission

Build an evidence-governed platform that turns authorized native Windows x86/x86-64 binaries into durable, incrementally buildable decompilation projects. The platform automates extraction, orchestration, compilation, comparison, validation, and project operations without claiming recovery of information compilation erased.

## Permanent truth decisions

1. Matching and functional decompilation are independent per-function modes.
2. Ghidra is an analysis engine and adapter, not the canonical database.
3. AI output is a proposal and cannot count as evidence or accept itself.
4. Three-independent-source review is a governance gate, not certainty.
5. Every validator names its scope and non-claims.
6. Target-specific facts live in verified target packs or project records, not generic core code.
7. Unknown compiler, linker, language, layout, name, or type facts remain unknown until evidence or an explicit operator decision resolves them.
8. Static import never grants native execution consent.
9. No placeholder, shim, fake success, or silent capability downgrade is allowed.
10. Previous release surfaces are preserved or migrated with regression tests.

## Architecture evolution

### 0.1–0.2 foundation

Established PE ingestion, Ghidra function artifacts, compiler profiles, byte comparison, evidence, memory, two-mode workflows, dynamic/symbolic validators, patch/relink, MCP governance, work queue, service, and benchmark contracts.

### 0.3 depth

Added broader COFF/bigobj/archive/COMDAT handling, linker MAP evidence, MSVC C++ metadata, PDB inventory, compiler corpus, symbolic memory alias models, target-specific whole-image matching, authorized static test bundles, and the integrated comprehensive test suite.

### 0.4 production-pilot control plane

Added:

- verified target packs separating observations and decisions;
- grounded matching/functional/hybrid project templates;
- content-addressed immutable artifact storage;
- transactional project schema v3 and migration history;
- deterministic backup, bounded restore, repair, leases, and GC;
- durable pipelines with idempotency, dependencies, retries, cancellation, runner heartbeats, stale recovery, and sealed outputs;
- bounded local/container workers and compiler-worker orchestration;
- evidence-limited linker reconstruction plans;
- bounded C++ relationship and adjustor-thunk recovery;
- ABI-driven harness generation;
- whole-image convergence history;
- reproducibility manifests and target release gates;
- source/security/dependency/SBOM/release-manifest tooling;
- deterministic generated C/C++ source corpora;
- expanded read-only project-control service;
- test isolation from unrelated host pytest plugins.

## Implemented inventory (0.4.0)

The exact module/function/command/schema/adapter inventory is machine-pinned in:

```text
test-suite/src/x86decomp_testkit/data/feature_catalog.json
```

The integrated test suite fails on drift. Counts in prose are updated only from the final sealed release inventory.

## Project schema decision

Project schema version 3 owns:

- `state/project-state.sqlite3`;
- `artifacts/` content store;
- `target-pack/`;
- `orchestration/` pipelines, logs, work, and results;
- migration and snapshot records;
- artifact references and leases.

Schema v1/v2 projects remain readable and migrate monotonically to v3. Migration tests are release blockers.

## Target-pack decision

A target pack is the only automatic template input. It includes exact artifact identities, parsed observations, acceptance policy, image profile, template plan, and explicit decisions. Project generation does not infer historical compiler versions or original source organization from code appearance.

## Template decision

Templates may create working structure, pipeline manifests, policies, helper scripts, source lanes, and blockers. They may not emit fake decompiled function bodies, fake toolchains, or fake link order.

## Orchestration decision

Pipeline stages are concrete commands or evidence gates. Every success must have validated materialized outputs or an explicit no-output contract. Stage reuse is content-based. Altered or missing output invalidates success. Active workers heartbeat; recovery of abandoned `running` jobs is explicit and logged.

## Worker decision

`local_bounded` is operational containment, not a security sandbox. Container mode is the production isolation boundary offered by the toolkit and uses read-only root, no network, dropped capabilities, explicit mounts, and resource limits. Unknown target execution still belongs in a VM/external sandbox.

## Release decision

A toolkit release requires:

- zero previous-feature regressions;
- root and integrated test-suite success with zero skips;
- every defined Python function/method body executed at least once;
- exact feature catalog;
- valid schemas and Ghidra Java syntax;
- clean wheel/sdist installation;
- sealed source ZIP verification;
- synchronized toolkit/test-suite Mermaid and ASCII maps;
- no caches, venvs, generated results, downloaded adapters, or machine paths;
- honest disclosure of adapters unavailable for live validation.

A target release is separate. `release-gate` evaluates target-specific acceptance and includes an explicit non-proof statement.

## Architecture-map decision

Maintain these four synchronized files in every future release:

- `docs/ARCHITECTURE_MAP.md`;
- `docs/ARCHITECTURE_MAP_ASCII.txt`;
- `test-suite/docs/ARCHITECTURE_MAP.md`;
- `test-suite/docs/ARCHITECTURE_MAP_ASCII.txt`.

Update them whenever architecture, workflow states, commands, adapters, subsystem ownership, trust boundaries, or release structure changes.

## Security decision

- All archives are untrusted.
- All external commands use argument arrays and hard timeouts.
- Native target execution is opt-in and isolated.
- Proprietary toolchains remain user-owned.
- SBOM generation inventories the current environment; it is not a vulnerability scan.
- Dependency findings come from a real external scanner and preserve its exact result.
- Missing scanners or live adapters are unavailable/blocked, never clean passes.

## Known bounded limitations

- Exact whole-image matching remains target/compiler/linker-specific.
- PDB parsing is a bounded inventory, not complete CodeView semantics.
- RTTI/EH/vtable recovery remains evidence-limited and compiler-generation-sensitive.
- Unicorn harnesses model declared memory/registers/stubs, not a Windows process.
- Symbolic engines cover declared instruction/memory subsets and finite bounds.
- The read-only service observes state; it does not own canonical mutation.
- Production confidence still requires real authorized pilot targets and the exact external adapters/toolchains used by those targets.
