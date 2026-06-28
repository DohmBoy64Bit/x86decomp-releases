# Feature-parity matrix — 0.2.0

This matrix maps the discussed architecture to concrete source, CLI, contracts and
verification. “Implemented” means a real code path exists and fails explicitly when
its declared prerequisites are absent. It does not mean arbitrary-binary correctness
or universal decompilation has been solved.

## Two independent modes

| Requirement | Implementation | Command/contract | Verification |
|---|---|---|---|
| Matching mode per function | `workflow.py` matching state machine | `workflow-init`, `workflow-update`; `function-workflow.schema.json` | `test_modes_and_db.py` |
| Functional mode per function | `workflow.py` functional state machine | same, independently stored | `test_modes_and_db.py` |
| Independent progression | separate status/report/blocker fields | monotonic transition checks; explicit regression flag | positive and invalid-transition tests |
| Hybrid source stages | original bytes → generated assembly → decompiler/human/accepted source | workflow and hybrid project manifests | workflow and hybrid tests |

## Ingestion and immutable evidence

| Requirement | Implementation | Verification |
|---|---|---|
| PE32/i386 | `pe32.py`, `pe.py` | valid/malformed fixtures |
| PE32+/AMD64 | `pe.py` | PE64 tests |
| Sections/image layout | bounded PE parser | parser tests |
| Imports/delay imports/exports | bounded directory parsers | parser contracts/tests |
| Resources | recursive bounded resource directory records | parser contracts |
| Base relocations | PE relocation records | parser/patch tests |
| Debug/CodeView/PDB references | debug directory and CodeView parser | parser contracts |
| TLS callbacks | bounded TLS parser | parser contracts |
| Load configuration | bounded load-config records | parser contracts |
| x64 runtime functions | exception-directory entries | PE64 tests |
| Immutable original | project hash manifest and verification | project tamper tests |
| Copied evidence | content-addressed evidence store | evidence copy/tamper tests |

## Ghidra analysis

| Requirement | Implementation | Artifact |
|---|---|---|
| Project manifest | `ExportProjectManifest.java` | program, sections, functions, symbols, types, metrics |
| Per-function packets | `ExportFunctionArtifacts.java` | `function.json`, exact ranges, instructions, references |
| Decompiled C | Ghidra decompiler export | `decompiler.c` |
| Token/AST-like structure | recursive `ClangNode` export | `decompiler-tree.jsonl` |
| Raw P-code | instruction P-code export | `raw-pcode.jsonl` |
| High P-code | decompiler high-function export | `high-pcode.jsonl`, `high-pcode.txt` |
| Discontiguous bodies | every Ghidra `AddressRange` retained separately | range files and manifests |
| Queries | `QueryAnalysis.java` | refs, disassembly and function lookup |
| Headless orchestration | `ghidra.py` | `ghidra-export` and `verify-ghidra.sh` |

Live Ghidra runtime verification remains installation-dependent and is explicitly
recorded in `VERIFICATION.md`.

## Independent decoding and cross-check

| Requirement | Implementation | Verification |
|---|---|---|
| x86/x64 decode | `disassembly.py` with Capstone | decoder tests |
| Structured operands | normalized instruction records | decoder tests |
| Direct branches/CFG | branch target and edge extraction | CFG tests |
| Ghidra disagreement report | `cross_check_ghidra_instructions` | CLI and tests |

## Global analysis database

| Requirement | Implementation | Verification |
|---|---|---|
| Entities/symbols/functions | `analysis_db.py` SQLite schema | DB tests |
| References/call relations | reference ingestion | DB tests |
| ABI observations | stored provenance records | DB tests |
| Type constraints | subject/relation/value/provenance/evidence | conflict tests |
| Conflict detection/acceptance | explicit APIs and commands | conflict tests |

## Matching decompilation

| Requirement | Implementation | Command/test |
|---|---|---|
| Compiler profiles | `compiler.py` | `compile`; real GCC `-m32` test |
| Isolated work directories | temporary or declared work directory | compiler tests |
| Compiler hashing/reporting | executable/source/output hashes and version | compiler tests |
| Flag search/cache | `compiler_lab.py` matrix and cache | `compiler-lab`; example run |
| Historical toolchains | `toolchains.py` external registry | register/verify commands |
| i386/AMD64 COFF parser | `coff.py` | COFF tests |
| Symbol extraction | COFF symbol extent and bytes | COFF tests |
| Synthetic COFF | real object writer with supplied relocations | COFF/relink tests |
| PE function ↔ COFF symbol | `exe_diff.py` | `diff-function`; tests |
| Relocation normalization | modeled candidate relocation spans | diff report/tests |
| Instruction/CFG comparison | Capstone normalized comparison | diff/decoder tests |
| ABI validation | `abi.py` | `abi-check`; ABI tests |
| Continuously buildable hybrid | `hybrid.py` exact-byte `.S` fallback | real `make`/assembler test |
| Patch-image backend | `patching.py` hash-gated copy patch/checksum | patch tests |
| Full relink | `relink.py` explicit linker manifest | real `lld-link` PE test |
| objdiff adapter | `objdiff_adapter.py` exact manifest execution | subprocess/JSON test |
| decomp.me packet | `decompme.py`, no network upload | packet test |

## Functional decompilation

| Requirement | Implementation | Command/test |
|---|---|---|
| Function harnesses | `dynamic.py` declarative memory/register/stack model | `dynamic-validate` |
| Original/candidate execution | independent Unicorn runs | equal/different tests |
| Register/memory observations | explicitly selected observations | dynamic reports/tests |
| Deterministic external calls | harness stubs | dynamic contract |
| Bounded symbolic validation | `symbolic.py` Capstone/Z3 engine | equal/different/counterexample tests |
| Optional secondary symbolic backend | `angr_backend.py` | real example execution |
| Runtime coverage | `dynamorio.py` drcov execution/parser | parser tests; live tool external |
| Integration scenario runner | `integration.py` target/candidate processes | consent/equality/mismatch tests |
| Exit/stdout/stderr/file comparison | declared observation contract | integration report/schema |
| VM/container wrapper support | `external_wrapper` command prefix | integration manifest contract |
| Functional status gate | separate workflow state and required reports | workflow/work-queue tests |

## Ghidra MCP and AI governance

| Requirement | Implementation | Verification |
|---|---|---|
| MCP stdio | JSON-RPC client | real mock-server protocol test |
| MCP Streamable HTTP | HTTP/SSE-capable client | implementation/contract |
| Read-only default | gateway read path rejects mutation-like use | MCP policy |
| Transactional mutation | proposed request hash then exact commit | MCP mutation test |
| Evidence/rationale | required proposal fields | MCP schema/test |
| Agent work queue | `work_queue.py` SQLite tasks/proposals | work-queue tests |
| Validator-gated acceptance | all named validators must pass | work-queue tests |
| AI is not evidence | skill, AGENTS and queue contract | governance checks |

## Validation states and metrics

| Requirement | Implementation |
|---|---|
| `decompiled` / `compiles` | both mode workflows |
| `abi_compatible` | ABI reports |
| `instruction_similar` | normalized executable/object report |
| `byte_matched` | raw scoped equality only |
| `differentially_validated` | passing concrete harness corpus |
| `symbolically_bounded` | passing bounded model report |
| `integration_validated` | named scenario reports |
| `image_integrated` | patch/integration report |
| `full_relink_validated` | linker and project-defined image gate |
| Boundary/CFG/call metrics | benchmark discovery case |
| Matching/dynamic/symbolic/integration rates | benchmark corpus runner |
| Human interventions | explicit per-case count |

## Evidence, memory and contracts

| Requirement | Implementation |
|---|---|
| Three-source claim gate | `evidence.py`: count, independence, diversity, hash, contradiction |
| No guarantee wording | skill/docs/report scope statements |
| Append-only memory | `memory.py` hash chain |
| Stable identities | `pe-rva:XXXXXXXX` and half-open ranges |
| Machine contracts | JSON Schemas in `schemas/` |
| Detailed agent skill | `skills/x86decomp/SKILL.md` version 2.0.0 |
| Contributor guardrails | `AGENTS.md`, `SECURITY.md` |
| Read-only dashboard | `service.py` FastAPI endpoints/UI |

## Deliberate non-claims

The package has implementation parity with the architecture, not omniscience. It does
not claim generic recovery of erased source facts, every original object relocation,
every compiler/linker decision, arbitrary indirect control flow, safe host execution,
or all-input equivalence. Target-specific reconstruction and environment provisioning
remain real reverse-engineering work and are represented as evidence, manifests,
constraints and bounded reports rather than hidden placeholders.
