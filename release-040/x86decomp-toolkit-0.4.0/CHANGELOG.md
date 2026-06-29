# Changelog

## 0.4.0 — 2026-06-28

### Production-pilot control plane

- Added verified target packs that separate parsed observations from explicit operator decisions and preserve unknown compiler/linker/language facts.
- Added grounded matching, functional, and hybrid project-template derivation/materialization without fake source or toolchain profiles.
- Added project schema v3, transactional state database, migration history, snapshots, leases, artifact references, deterministic backup, bounded restore, repair, and dry-run-first garbage collection.
- Added SHA-256 content-addressed immutable storage with atomic writes and reference tracking.
- Added durable pipeline orchestration with dependencies, idempotency keys, retries, cancellation, runner heartbeats, stale-run recovery, evidence-gate stages, materialized outputs, and output-tamper invalidation.

### Worker, compiler, linker, and convergence depth

- Added bounded local workers and hardened Docker/Podman command generation with read-only root, disabled network, dropped capabilities, no-new-privileges, resource limits, and explicit mounts.
- Added compiler-worker orchestration that copies declared inputs into ephemeral workspaces and preserves exact provenance.
- Added evidence-limited linker reconstruction plans and relink-manifest generation from PE, MAP, object, archive, relocation, COMDAT, and alignment evidence.
- Added target-specific convergence reports and append-only convergence history.
- Added bounded C++ relationship recovery and instruction-pattern adjustor-thunk candidates without claiming original class identity.
- Added ABI-driven differential harness generation with explicit pointer regions and observation scope.
- Extended the built-in symbolic engine with carry/borrow, flag-control, SETcc, and CMOVcc semantics.

### Reproducibility, release, and security

- Added reproducibility manifest creation/verification and clean-machine mismatch explanations.
- Added target release gates aggregating project integrity, target-pack validity, workflow minima, claims, durable pipelines, reproducibility, security, and convergence.
- Added deterministic source-tree security auditing, release-manifest verification, CycloneDX SBOM generation, and a real pip-audit adapter.
- Added read-only service visibility for target packs, durable pipelines, convergence, reproducibility, security, worker capabilities, functions, workflows, and work queue.
- Added deterministic generated C/C++ source corpora with exact seeds/hashes and explicit non-claims until compilers are actually run.

### Regression and documentation contracts

- Preserved the complete 0.3.1 command, schema, parser, validator, adapter, workflow, Ghidra, package, and architecture-map surface.
- Added migration and compatibility tests for legacy project schemas and command/schema contracts.
- Updated the integrated test suite catalog for every 0.4.0 module, defined function/method, command, schema, Ghidra script, state, and adapter.
- Isolated pytest subprocesses from unrelated host plugin autoload after identifying a host ddtrace shutdown hang.
- Updated the evidence-engineering skill to 4.0.0 and synchronized toolkit/test-suite Mermaid and ASCII maps.
- Added target-pack/template, operations/recovery, release-gate, worker, security, and corpus documentation.

### Truth boundary

- The release does not claim original-source recovery, arbitrary-program equivalence, generic whole-image reconstruction, complete C++ recovery, or safe ordinary-host execution of unknown targets.
- Live integration claims remain conditional on the exact adapter/toolchain being detected and tested; unavailable integrations are reported as BLOCKED.

## 0.3.1 — 2026-06-28

### Repository and package normalization

- Integrated the comprehensive verification harness under the stable `test-suite/`
  source directory while preserving its independent Python package metadata.
- Updated toolkit, test-suite, skill, feature-catalog, documentation, and package
  release contracts to 0.3.1.
- Removed generated test runs, virtual environments, coverage output, downloaded
  adapter binaries, editable-install metadata, Python caches, and machine-specific
  configuration from the source release.
- Added `docs/ARCHITECTURE_MAP.md` as the maintained Mermaid architecture/state-map
  source of truth for future releases.
- Added synchronized ASCII toolkit architecture/state maps and dedicated Mermaid/ASCII
  test-suite architecture maps as required future-release artifacts.

### Test suite integration (Windows)

- Added MinGW/MSVC detection gating and test-suite adapter configuration for Windows.
- Added `_prefer_windows_executable()` heuristic in Ghidra adapter detection
  (`src/x86decomp_testkit/adapters/detection.py`) so that `.bat`/`.exe` variants are
  preferred over bare filenames on Windows.
- Fixed `_ghidra_test()` in `src/x86decomp_testkit/live_adapters.py` to create
  `work`/`project` directories before the analyzer runs.
- Added `angr`, `unicorn`, `z3-solver`, `objdiff` CLI, DynamoRIO, and `make` alias
  to the development environment.
- Result: `ghidra:headless` was **ERROR**, now **PASS**.

### Hybrid assembly build portability

- Stripped `.type`, `.size`, `.def`, `.endef`, `.scl` assembly directives from
  `_assembly_bytes()` in `src/x86decomp/hybrid.py` — `.globl` alone is sufficient on
  both ELF and COFF targets.
- Changed `CC ?= gcc` to `CC := gcc` in the generated Makefile
  (`src/x86decomp/hybrid.py`, `generate_hybrid_project()`) to override GNU Make's
  built-in `CC = cc` default.
- Replaced platform-specific `mkdir` commands (`mkdir -p build` on POSIX,
  `mkdir build 2>NUL` on Windows) with GNU Make's `-@mkdir build` error-ignoring prefix
  in `src/x86decomp/hybrid.py`.
- Removed the `import platform` import and all `os.name`/`platform.system()` branching
  from `src/x86decomp/hybrid.py`.
- Result: hybrid assembly build was **FAIL**, now **PASS**.

### Pinned manifest

- Regenerated `MANIFEST.sha256` for the normalized source tree. The root manifest
  seals the integrated repository and the nested test-suite manifest independently
  seals the harness source.
- Result: `structure:manifest-hashes` was **FAIL**, now **PASS**.

### Test results

- Clean normalized-source validation in this environment: **109 passed, 0 failed, 0 skipped**.

- Final run: **121 pass, 5 fail, 0 error, 0 blocked**.
- Three original blockers resolved (Ghidra headless, hybrid assembly, manifest hashes).
- Remaining 5 failures are pre-existing: 1 symlink privilege, 4 coverage/pytest gaps
  that were previously hidden behind the hybrid build failure.

## 0.3.0 — 2026-06-28

### COFF, COMDAT, and layout

- Added classic COFF and ANON_OBJECT_HEADER_BIGOBJ parsing under one compatible API.
- Added broader i386/AMD64 relocation names, widths, PC-relative classification,
  in-place addends, relocation-overflow handling, alignment decoding, and long names.
- Added section-definition, function-definition, weak-external, file, and raw auxiliary
  records; fixed real Clang weak-external storage-class handling.
- Added COMDAT resolution for NODUPLICATES, ANY, SAME_SIZE, EXACT_MATCH, ASSOCIATIVE,
  LARGEST, and NEWEST, including conflicts and associative parents.
- Added multi-section synthetic object generation and COMDAT object generation.
- Added MSVC/LLD map parsing, public-symbol object ownership, map/object correlation,
  contribution-vs-public evidence separation, object order, and COMDAT-aware layout
  reconstruction.

### Microsoft C++ and runtime metadata

- Added bounded Microsoft RTTI TypeDescriptor, CompleteObjectLocator, class hierarchy,
  PMD base, and vftable address-point recovery for x86 and x64.
- Added x64 runtime-function and UNWIND_INFO decoding, chained unwind records, handler
  and map-symbol correlation, x86 SafeSEH parsing, and conservative EH FuncInfo scans.
- Added linked TLS template/index/callback reporting and object-level `.tls$*` and
  `.CRT$XL*` subsection inventories.
- Added `.CRT$X*` static-initializer subsection ordering, hashes, relocations, and
  initializer-symbol references.

### Compiler corpus and symbolic depth

- Expanded the bundled freestanding ground-truth corpus to 24 C/C++ cases covering
  bitfields, floating point, loops, varargs, indirect/tail calls, vectorization,
  unions, virtual inheritance, templates, member pointers, and multi-catch EH.
- Added x86/x64, O0/O1/O2/Os, and frame-pointer matrix generation with exact compiler
  executable/version hashes.
- Added cross-report compiler/version corpus comparison without inferring semantic
  equivalence or compiler identity from byte appearance.
- Added symbolic region bases, byte-addressable symbolic memory, selected memory
  observations, and equal/distinct/disjoint/may-alias constraints to the angr backend.

### Whole-image matching and authorized test bundles

- Added reference-hash-bound image profiles, section-layout checks, base-relocation
  rebasing, and explicit timestamp/checksum/certificate/debug normalization ranges.
- Added target-specific raw, profile-normalized, and differing whole-image classes.
- Added deterministic authorized ZIP bundle creation and static inspection.
- Added archive traversal, backslash, drive path, duplicate, symlink, size, expansion,
  authorization, and artifact-hash guardrails.
- Added static PE, COFF, COMDAT, map, metadata, layout, and optional whole-image analysis
  for uploaded bundles without executing supplied code.

### Contracts, skill, and regression

- Added bounded COFF static/import archive parsing with long names, dual linker
  indexes, embedded object/COMDAT inspection, and import-object records.
- Added bounded MSF 7.0/PDB parsing for stream layout, GUID/age identity, TPI/IPI
  headers, DBI modules, section contributions, source mappings, and PE RSDS matching.
- Preserved the 0.2.0 CLI and schema fields while adding the v0.3 command surface.
- Added schemas for COMDAT, image-match, symbolic-memory, compiler comparison, and test
  bundle inputs/reports.
- Upgraded the evidence-engineer skill to 3.0.0 with both mode state machines and
  detailed linker, metadata, corpus, alias, image, upload, and release guardrails.
- Added real Clang COFF/TLS/weak-external and LLVM CodeView image regression tests.
- Expanded the test suite from 33 tests in the 0.2.0 release to the v0.3 verified count
  recorded in `VERIFICATION.md`.

## 0.2.0 — 2026-06-27

### Two-mode workflow

- Added independent per-function `matching` and `functional` modes.
- Added monotonic matching states through `full_relink_validated`.
- Added monotonic functional states through `integration_validated`.
- Added explicit blockers, candidates, compiler profiles, report links, audited
  regressions, and memory events.

### Binary formats and static analysis

- Added PE32+/AMD64 parsing alongside PE32/i386.
- Added bounded parsing for resources, delay imports, load configuration, x64 runtime
  functions, exports, imports, relocations, debug/CodeView and TLS.
- Added i386/AMD64 COFF parsing, symbols, relocations, symbol extraction and synthetic
  object generation.
- Expanded Ghidra exports with decompiler token trees, raw/high P-code JSONL, exact
  discontiguous ranges, references, types, symbols and metrics.
- Added Capstone x86/x64 instruction normalization, CFG extraction and Ghidra
  cross-checking.
- Added SQLite entity/reference/ABI/type-constraint storage with conflict detection.

### Matching mode

- Added linked PE function to COFF symbol comparison.
- Added raw byte, relocation-normalized, instruction and CFG classifications.
- Added compiler result caching and bounded flag-matrix experiments.
- Added hash-pinned user-owned historical toolchain registry.
- Added static ABI contracts for x86 conventions and x64 observations.
- Added continuously buildable exact-byte assembly fallback projects.
- Added hash-gated PE copy patching and PE checksum regeneration.
- Added real manifest-driven linker invocation and optional image comparison.
- Added manifest-driven external objdiff execution with full tool/input/output
  provenance.
- Added local decomp.me-style packet generation with no automatic upload.

### Functional mode

- Added bounded Unicorn target/candidate differential execution.
- Added deterministic external-call summaries and explicit register/memory observations.
- Added bounded Capstone/Z3 symbolic comparison and an optional angr backend.
- Added DynamoRIO drcov execution and text-log parsing.
- Added explicit-consent integration scenario execution with target/candidate exit,
  stream and file comparison, separate work trees, and external-wrapper support.

### Governance, orchestration and service

- Added stdio and Streamable HTTP MCP clients.
- Added read-only MCP defaults and hash-approved, evidence-backed mutation transactions.
- Added validator-gated human/AI work queue.
- Added decomposed benchmark corpus runner and metrics.
- Added local read-only FastAPI JSON service/dashboard.
- Added machine-readable schemas for every implemented subsystem.
- Upgraded the evidence-engineer skill to version 2.0.0 with strict truth, security,
  mode, validation and completion contracts.

### Verification

- Expanded the suite to 33 passing tests.
- Added real GCC `-m32`, `lld-link`, Unicorn, Z3, angr, subprocess integration, MCP
  protocol, hybrid Makefile and external-tool adapter checks.
- Added full contract/example validation and Java syntax parsing.

## 0.1.0 — 2026-06-27

- Added project-owned immutable evidence copies and integrity path confinement.
- Added function-artifact import/verification CLI commands and path traversal tests.
- Added compiler executable hashing, unknown-token rejection, and stale-output removal.
- Added an explicit package verification record.
- Added a standard-library-only Python orchestration core.
- Added strict PE32/x86 parsing, project initialization, immutable hashes, and verification.
- Added evidence claims with a three-independent-source verification gate.
- Added tamper-evident project-memory events.
- Added compiler profile execution and byte-level verification reports.
- Added Ghidra project/function exporters and analysis query script.
- Added schemas, contracts, guardrails, CI, tests, and an agent skill.
