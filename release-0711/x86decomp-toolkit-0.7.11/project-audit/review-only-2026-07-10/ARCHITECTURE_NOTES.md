# Architecture notes

## Status

This is the final architecture model derived from complete repository review, parser introspection, tests, documentation, and source call relationships. Statements about runtime behavior are limited to executed paths or directly inspected contracts.

## Entry points

- `x86decomp` → `x86decomp.cli:main` is the primary unified CLI.
- `x86decomp-test` → the separately packaged `x86decomp_testkit` CLI drives adapter-aware verification.
- Three Ghidra Java scripts export/query analysis artifacts inside Ghidra.
- A read-only FastAPI/Uvicorn project service is available through the `serve` command and defaults to loopback.

## Major planes

1. **Ingestion and evidence:** project initialization, immutable artifacts, content store, evidence/claim records, project-state database, manifests.
2. **Static binary parsing:** bounded reader, PE32/PE32+, COFF/archive, PDB/MSVC metadata, resources/imports/relocations/debug/TLS.
3. **Analysis and reconstruction:** disassembly, ABI, symbolic/dynamic analysis, linker layout, candidate generation, compiler/worker, reconstruction package.
4. **Governance/control:** workflows, reviews, hypotheses, proofs, campaigns, candidates, changesets, durable workers and orchestration.
5. **Native/assembly:** native PE reconstruction, matching, slots, staging, annotation, relocation materialization, closed-loop validation.
6. **Local-model proposal:** profiles, bounded HTTP transports, prompts, matching, compiler/relocation/raw-byte validation. Model output is treated as untrusted proposal text.
7. **Verification harness:** inventory, schemas, adapter detection/capabilities, process logging, reports, package self-tests, toolkit public-contract tests.

## Data and control flow

Input binaries are hashed and represented as evidence before interpretation. Parsers transform bounded byte ranges into structured records. The project/control planes persist claims, artifacts, workflow state, and provenance. Candidate generators—including local-model integrations—produce proposals that advance only through explicit compiler, relocation, differential, symbolic, integration, or exact-byte checks. Reports and schemas provide machine/human consumption.

## Configuration and persistence

Configuration is JSON/TOML/CLI driven. SQLite stores project/control state. Content-addressed artifacts preserve hashes. JSON schemas define 97 contracts. Deterministic root/suite/all-file manifests bind release files. External-tool and model-server integrations are optional and represented as available, blocked, or unresolved rather than silently successful.

## Error handling and logging

The package centralizes contract and command errors, generally emits structured JSON for command failures, and records process/evidence output. Broad exception handlers exist but were not treated as defects without a demonstrated masking path. The exact test runner rejects failures, errors, skips, missing JUnit output, and inventory mismatches.

## Trust boundaries

- Binary/archive inputs are untrusted and bounded by readers, member/path checks, and size/count limits.
- Native execution and non-loopback services require explicit authorization.
- Remote/local-model output remains untrusted until deterministic validation.
- Subprocess invocations use argument arrays; the static scan found no `shell=True` call.
- Path normalization and containment checks protect workflow/project boundaries.
- Optional integrations and network behavior remain an operational boundary not fully exercised here.

## Dependency direction and risks

The core package contains several broad CLI/dispatch modules and many store-oriented subsystems. Cross-package coupling is mostly routed through models/contracts and project paths. Primary architecture risks are documentation scale, duplicated packaged tests, high-branch dispatch functions, and release-gate self-mutation rather than a verified cyclic-dependency failure.
