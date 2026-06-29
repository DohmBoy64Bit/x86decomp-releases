# Feature-parity matrix — 0.4.0

This matrix maps the production-pilot architecture to concrete code, contracts, commands, and tests. “Implemented” means executable code exists and local tests exercise its bounded contract. It does not mean every external installation or commercial target has been validated.

## Core modes and workflow

| Requirement | Implementation | Contract/test evidence |
|---|---|---|
| Independent matching/functional modes | `workflow.py` | workflow schemas and monotonic-state tests |
| Matching states through full relink | `MatchingStatus` | `test_modes_and_db.py`, architecture-map tests |
| Functional states through integration | `FunctionalStatus` | dynamic/symbolic/integration tests |
| Explicit blocked state | workflow + orchestrator | blocked/retry/recovery tests |
| No cross-mode promotion | workflow update rules | independent-mode tests |

## Target packs and templates

| Requirement | Implementation | Contract/test evidence |
|---|---|---|
| Target-specific evidence boundary | `target_pack.py` | `target-pack.schema.json`, integrity/tamper tests |
| Observations separate from decisions | `target.toml` + `observations.json` | target-pack tests |
| PE/PDB/MAP/OBJ/LIB/rebuilt-image inputs | target-pack inference | production tests and parser tests |
| Matching/functional/hybrid template selection | `project_template.py` | `project-template.schema.json` and template tests |
| Unknown facts preserved | blockers/truth policy | no-fabricated-source tests |
| Generated project helper and validation policy | template materializer | executable helper/layout tests |

## Project state and orchestration

| Requirement | Implementation | Contract/test evidence |
|---|---|---|
| Content-addressed immutable artifacts | `content_store.py` | round-trip, tamper and GC tests |
| Transactional state database | `project_state.py` | schema-v3 checks and transaction tests |
| Migrations from legacy project schemas | migration registry | v1/v2→v3 migration tests |
| Deterministic backup and bounded restore | `create_project_backup`, `restore_project_backup` | deterministic and malicious-archive tests |
| Repair and artifact GC | project-state repair/GC | dry-run/apply tests |
| Durable pipelines | `orchestrator.py` | resume/failure/retry/cancel tests |
| Idempotent stage reuse | input/output hashes | output reuse/tamper-rerun tests |
| Runner heartbeat and stale recovery | orchestrator runner metadata | active-cancel and stale-heartbeat tests |
| Evidence-gate stages | orchestrator + `EvidenceStore` | evidence gate tests |
| Materialized and sealed outputs | result tree + content store | output integrity tests |

## Static analysis and binary formats

| Requirement | Implementation | Contract/test evidence |
|---|---|---|
| PE32/i386 and PE32+/AMD64 | `pe.py`, `pe32.py` | PE fixtures and patch/hybrid tests |
| Imports, exports, delay imports, resources, TLS, relocations, debug/load config | PE parsers | parser and test-bundle tests |
| PDB/MSF bounded inventory | `pdb.py` | real LLD PDB tests |
| Classic COFF and bigobj | `coff.py` | synthetic and real Clang tests |
| COFF archives/import libraries | `coff_archive.py` | real archive/import-library tests |
| COMDAT/weak external/auxiliary records | COFF model and resolution | COMDAT tests |
| Linker MAP contributions/order | `linker_layout.py` | map/layout tests |
| MSVC RTTI/vtables/EH/unwind/TLS/initializers | `msvc_metadata.py` | metadata regression tests |
| Ghidra C/token/P-code/reference export | Java scripts | syntax/contract tests; live run requires Ghidra |
| Independent instruction decoder/CFG | `disassembly.py` | Capstone decode/cross-check tests |

## Matching and linker convergence

| Requirement | Implementation | Contract/test evidence |
|---|---|---|
| PE function ↔ COFF symbol compare | `exe_diff.py` | extraction/compare tests |
| Relocation-aware normalization | COFF/disassembly compare | relocation tests |
| Exact byte comparison | `diffing.py` | equality/mismatch tests |
| objdiff adapter | `objdiff_adapter.py` | fake-adapter contract; live run requires objdiff |
| Hybrid exact-byte assembly fallback | `hybrid.py` | real assembler build test |
| Hash-gated PE patching | `patching.py` | patch/hash/checksum tests |
| Manifest-driven relink | `relink.py` | real `lld-link` test where available |
| Evidence-limited linker reconstruction | `linker_reconstruction.py` | plan/uncertainty tests |
| Whole-image profile and convergence | `image_match.py`, `convergence.py` | normalization/history tests |
| Release-level convergence gate | `release_gate.py` | explicit gate tests |

## Compiler and corpus

| Requirement | Implementation | Contract/test evidence |
|---|---|---|
| Reproducible compiler profiles | `compiler.py` | real i386 object test |
| Compiler flag matrices and cache | `compiler_lab.py` | deterministic fake/real compiler tests |
| User-owned toolchain registry | `toolchains.py` | registration/hash tests |
| Bounded local/container workers | `worker.py` | resource/command/cancel/container-contract tests |
| Compiler worker | `compiler_worker.py` | real subprocess test |
| Reviewed 24-case built-in corpus | packaged corpus | 384-build matrix verification in v0.3 record |
| Deterministic generated C/C++ corpus | `synthetic_corpus.py` | reproducibility/tamper tests |
| Cross-version corpus comparison | `ground_truth.py` | report-comparison tests |

## Functional validation

| Requirement | Implementation | Contract/test evidence |
|---|---|---|
| ABI contract/check | `abi.py` | calling-convention tests |
| Grounded harness generation | `harness_generator.py` | deterministic pointer-region tests |
| Unicorn differential execution | `dynamic.py` | equal/unequal tests |
| DynamoRIO drcov collection/parse | `dynamorio.py` | parser/fake-process contract; live run requires DynamoRIO |
| Built-in bounded symbolic engine | `symbolic.py` | arithmetic/flags/SETcc/CMOVcc tests |
| Symbolic memory/alias model | `angr_backend.py` | equal/distinct/disjoint/may-alias tests |
| Integration scenarios | `integration.py` | consent/equal/different process tests |
| Counterexample and truncation reporting | symbolic backends | report tests |

## C++ recovery

| Requirement | Implementation | Contract/test evidence |
|---|---|---|
| RTTI/vtable relationship model | `cpp_recovery.py` | empty and metadata-backed tests |
| Adjustor-thunk candidates | instruction-pattern classifier | positive pattern test |
| Provenance and uncertainty | recovery report | no-original-identity claims |
| Complete source class recovery | deliberately not claimed | documented non-goal |

## Evidence, AI, and governance

| Requirement | Implementation | Contract/test evidence |
|---|---|---|
| Three independent evidence groups | `evidence.py` | verified/same-group/contradiction tests |
| Hash-chained memory | `memory.py` | chain/tamper tests |
| Global constraint DB | `analysis_db.py` | conflict/acceptance tests |
| Validator-gated work queue | `work_queue.py` | required-validator tests |
| Ghidra MCP read/write governance | `mcp.py` | proposal/approval-hash tests |
| AI output is proposal, not evidence | skill/AGENTS/work queue | policy and contract validation |

## Operations, security, and service

| Requirement | Implementation | Contract/test evidence |
|---|---|---|
| Reproducibility manifest | `reproducibility.py` | create/verify tests |
| Source-tree security audit | `security_audit.py` | secret/symlink/manifest tests |
| CycloneDX SBOM | `generate_sbom` | schema/content tests |
| Dependency audit | real `pip-audit` adapter | fake-adapter parser test; live run requires pip-audit |
| Release manifest verification | `verify_release_manifest` | hash tests |
| Target release gate | `release_gate.py` | truth-scoped pass/fail tests |
| Read-only service/API | `service.py` | snapshot/app tests; Uvicorn live run optional |
| Deterministic backup/restore | project state | operational tests |

## Integrated comprehensive test suite

| Requirement | Implementation | Verification |
|---|---|---|
| Exact surface catalog | `test-suite/.../feature_catalog.json` | drift test |
| Every defined Python function body executed | coverage audit | all-function contract |
| Every command parse-tested | CLI surface stage | one process per subcommand |
| Zero silent skips | JUnit skip gate | skips fail |
| Missing adapters explicit | `BLOCKED` state | strict exit code 2 |
| Detection before prompt | adapter resolver | prompt-behavior tests |
| Custom path only if missing | resolver contract | self-tests |
| Consent-gated install | installer contracts | safety tests |
| Detailed logs/reports | run log, JSONL, JSON/MD/HTML/JUnit/coverage | report tests |
| Wheel/sdist clean install | packaging stage | package tests |
| Four synchronized architecture maps | map contract tests | Mermaid/ASCII tests |

## External validation boundary

Executable adapters and strict test procedures exist for Ghidra, DynamoRIO, objdiff, Docker/Podman, and historical MSVC. A local release record may claim a live integration only when that exact installation was detected and its live probe passed. Unavailable adapters remain `BLOCKED`; they are not converted into passes.

## Deliberate non-claims

The release does not claim original-source recovery, reliable erased names, universal C++ reconstruction, safe native execution of unknown programs, complete compiler/linker identification, generic whole-image matching for every target, or all-input semantic proof.
