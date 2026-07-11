# Schema catalog

All schemas are JSON Schema draft 2020-12. Each `$id` includes a version number. The catalog below lists every schema shipped with the toolkit.

---

## Core schemas

| Path | `$id` | Version | Validates |
|------|-------|---------|-----------|
| `schemas/project.schema.json` | `project:3` | 1/2/3 | `project.json` — project configuration |
| `schemas/project-template.schema.json` | — | — | Project template definitions |
| `schemas/target-pack.schema.json` | `target-pack:1` | 1 | `target-pack/target.toml` JSON representation |
| `schemas/target-decisions.schema.json` | — | — | Target decision fields within target packs |

---

## Compiler and build schemas

| Path | `$id` | Version | Validates |
|------|-------|---------|-----------|
| `schemas/compiler-profile.schema.json` | `compiler-profile:2` | 2 | Compiler profile JSON files |
| `schemas/compiler-lab.schema.json` | `compiler-lab:1` | 1 | Compiler experiment lab definitions |
| `schemas/compiler-ground-truth.schema.json` | — | — | Ground-truth compiler test cases |
| `schemas/compiler-ground-truth-comparison.schema.json` | — | — | Comparisons between ground-truth runs |
| `schemas/msvc-metadata.schema.json` | — | — | MSVC compiler/linker version metadata |

---

## Linker and relink schemas

| Path | `$id` | Version | Validates |
|------|-------|---------|-----------|
| `schemas/relink-manifest.schema.json` | `relink-manifest:1` | 1 | Relink manifest files |
| `schemas/linker-reconstruction-plan.schema.json` | `linker-reconstruction-plan:1` | 1 | Linker reconstruction plans |
| `schemas/linker-layout.schema.json` | — | — | Linker section layouts |
| `schemas/comdat-resolution.schema.json` | — | — | COMDAT resolution records |
| `schemas/coff-archive.schema.json` | — | — | COFF static library archives |
| `schemas/objdiff-manifest.schema.json` | — | — | objdiff comparison manifests |

---

## Native/PE schemas

| Path | `$id` | Version | Validates |
|------|-------|---------|-----------|
| `schemas/native/windows-tool.schema.json` | — | — | Windows tool descriptors |
| `schemas/native/staging-symbol.schema.json` | — | — | Symbol staging records |
| `schemas/native/section-export.schema.json` | — | — | PE section exports |
| `schemas/native/runtime-validation.schema.json` | — | — | Runtime validation reports |
| `schemas/native/patch-plan.schema.json` | — | — | Binary patch plans |
| `schemas/native/match-run.schema.json` | — | — | Match run records |
| `schemas/native/loop-run.schema.json` | — | — | Loop analysis run records |
| `schemas/native/hybrid-composition.schema.json` | — | — | Hybrid matching/functional compositions |
| `schemas/native/function-slot.schema.json` | — | — | Function slot assignment records |
| `schemas/native/function-match.schema.json` | — | — | Function match comparison records |
| `schemas/native/candidate-manifest.schema.json` | — | — | Candidate function manifests |
| `schemas/native/boundary-finding.schema.json` | — | — | Function boundary detection records |
| `schemas/pdb.schema.json` | — | — | PDB debug symbol metadata |
| `schemas/image-profile.schema.json` | — | — | PE image profile (sections, imports, exports) |
| `schemas/image-match-report.schema.json` | — | — | Image-level byte comparison reports |
| `schemas/hybrid-project.schema.json` | — | — | Hybrid decompilation project config |

---

## Assembly schemas

| Path | `$id` | Version | Validates |
|------|-------|---------|-----------|
| `schemas/assembly/symbol-map.schema.json` | — | — | Symbol-to-address mappings |
| `schemas/assembly/roundtrip-report.schema.json` | — | — | Assembly roundtrip verification reports |
| `schemas/assembly/relocation-resolution.schema.json` | — | — | Relocation resolution records |
| `schemas/assembly/asm-run.schema.json` | — | — | Assembly compilation run records |
| `schemas/assembly/asm-function.schema.json` | — | — | Assembly function descriptors |

---

## Reconstruction schemas

| Path | `$id` | Version | Validates |
|------|-------|---------|-----------|
| `schemas/reconstruction/translation-unit.schema.json` | — | — | Translation unit metadata |
| `schemas/reconstruction/source-provenance.schema.json` | — | — | Source file provenance records |
| `schemas/reconstruction/semantic-changeset.schema.json` | — | — | Semantic changeset records |
| `schemas/reconstruction/security-finding.schema.json` | — | — | Security finding records |
| `schemas/reconstruction/module.schema.json` | — | — | Module assignment definitions |
| `schemas/reconstruction/library-match.schema.json` | — | — | Library matching records |
| `schemas/reconstruction/header.schema.json` | — | — | Reconstructed header files |
| `schemas/reconstruction/generated-test.schema.json` | — | — | Generated test records |
| `schemas/reconstruction/compatibility-shim.schema.json` | — | — | Compatibility shim definitions |
| `schemas/reconstruction/capsule.schema.json` | — | — | Function capsule packaging |
| `schemas/reconstruction/build.schema.json` | — | — | Build system descriptors |
| `schemas/reconstruction/abi-contract.schema.json` | — | — | ABI contract definitions |

---

## Evidence and verification schemas

| Path | `$id` | Version | Validates |
|------|-------|---------|-----------|
| `schemas/evidence.schema.json` | `evidence:1` | 1 | Evidence records |
| `schemas/claim.schema.json` | `claim:1` | 1 | Claim records |
| `schemas/verification.schema.json` | — | — | Verification records |
| `schemas/work-task.schema.json` | `work-task:1` | 1 | Work task records |
| `schemas/worker-report.schema.json` | — | — | Worker status reports |
| `schemas/pipeline.schema.json` | `pipeline:1` | 1 | Pipeline definitions |
| `schemas/release-gate.schema.json` | — | — | Release gate checklists |
| `schemas/reproduction.schema.json` | — | — | Reproduction manifests |
| `schemas/dependency-audit.schema.json` | — | — | Dependency audit records |
| `schemas/security-audit.schema.json` | — | — | Security audit reports |

---

## Dynamic and trace schemas

| Path | `$id` | Version | Validates |
|------|-------|---------|-----------|
| `schemas/dynamic-report.schema.json` | — | — | Dynamic analysis reports |
| `schemas/drcov-trace.schema.json` | — | — | DynamoRIO coverage traces |
| `schemas/execution-harness.schema.json` | — | — | Execution harness definitions |
| `schemas/execution-harness-generated.schema.json` | — | — | Auto-generated execution harnesses |
| `schemas/symbolic-report.schema.json` | — | — | Symbolic execution reports |
| `schemas/symbolic-memory-report.schema.json` | — | — | Symbolic memory analysis reports |
| `schemas/symbolic-memory-harness.schema.json` | — | — | Symbolic memory harness definitions |
| `schemas/function-workflow.schema.json` | — | — | Function workflow lifecycles |

---

## Local LLM schemas

| Path | `$id` | Version | Validates |
|------|-------|---------|-----------|
| `schemas/local-llm/profile.schema.json` | `local-llm/profile` | 1 | LLM provider profiles |
| `schemas/local-llm/job.schema.json` | — | — | LLM job definitions |
| `schemas/local-llm/candidate.schema.json` | — | — | LLM-generated candidate records |
| `schemas/local-llm/report.schema.json` | — | — | LLM job execution reports |

---

## Governance schemas

| Path | `$id` | Version | Validates |
|------|-------|---------|-----------|
| `schemas/governance/worker.schema.json` | — | — | Worker node records |
| `schemas/governance/review.schema.json` | — | — | Review records |
| `schemas/governance/proof-bundle.schema.json` | — | — | Cryptographic proof bundles |
| `schemas/governance/plugin.schema.json` | — | — | Plugin descriptors |
| `schemas/governance/knowledge-graph.schema.json` | — | — | Knowledge graph records |
| `schemas/governance/hypothesis.schema.json` | — | — | Hypothesis records |
| `schemas/governance/family.schema.json` | — | — | Function family grouping records |
| `schemas/governance/counterexample.schema.json` | — | — | Counterexample records |
| `schemas/governance/consensus.schema.json` | — | — | Consensus records |
| `schemas/governance/changeset.schema.json` | — | — | Changeset packaging |
| `schemas/governance/candidate.schema.json` | — | — | Governance candidate records |
| `schemas/governance/campaign.schema.json` | — | — | Campaign/workflow records |

---

## Other schemas

| Path | `$id` | Version | Validates |
|------|-------|---------|-----------|
| `schemas/function.schema.json` | — | — | Function packet manifests (`function.json`) |
| `schemas/memory-event.schema.json` | — | — | Memory event ledger entries |
| `schemas/benchmark-corpus.schema.json` | `benchmark-corpus:1` | 1 | Benchmark corpus definitions |
| `schemas/test-bundle.schema.json` | `test-bundle:1` | 1 | Test bundle definitions |
| `schemas/test-bundle-report.schema.json` | — | — | Test bundle execution reports |
| `schemas/convergence-report.schema.json` | — | — | Project convergence reports |
| `schemas/exe-diff-report.schema.json` | — | — | Executable diff reports |
| `schemas/integration-report.schema.json` | — | — | Integration test reports |
| `schemas/integration-scenarios.schema.json` | — | — | Integration scenario definitions |
| `schemas/cpp-recovery.schema.json` | — | — | C++ class/vtable recovery records |
| `schemas/decompme-packet.schema.json` | — | — | decomp.me integration packets |
| `schemas/mcp-mutation.schema.json` | — | — | MCP mutation records |
| `schemas/synthetic-corpus.schema.json` | — | — | Synthetic test corpus definitions |
| `schemas/type-constraint.schema.json` | — | — | Type constraint definitions |
| `schemas/abi-contract.schema.json` | — | — | ABI contract definitions |

---

## Test suite schemas

| Path | `$id` | Version | Validates |
|------|-------|---------|-----------|
| `test-suite/schemas/test-config.schema.json` | — | — | Test suite configuration |
| `test-suite/schemas/run-report.schema.json` | — | — | Test suite run reports |
| `test-suite/schemas/feature-catalog.schema.json` | — | — | Feature test catalogs |

!!! note
    "Total schema files" refers to unique `.schema.json` files in `schemas/` (84) plus `test-suite/schemas/` (3) = 87 total. Core toolkit schemas with explicit `$id` and version number: `project` (v3), `compiler-profile` (v2), `compiler-lab` (v1), `pipeline` (v1), `relink-manifest` (v1), `linker-reconstruction-plan` (v1), `target-pack` (v1), `evidence` (v1), `claim` (v1), `test-bundle` (v1), `work-task` (v1), `benchmark-corpus` (v1), and `local-llm/profile` (v1) — 13 versioned schemas.
