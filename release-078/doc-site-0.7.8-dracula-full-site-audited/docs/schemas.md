---
title: JSON Schema Reference
description: Source-derived JSON Schema coverage for x86decomp 0.7.8.
---

# JSON Schema Reference

This page is regenerated from the current v0.7.8 source tree. The release surface has **97 toolkit schema files**; the bundled test-suite contributes **3 additional schema files**. All 100 files are documented below.

- [Open the per-schema reference index](schema-reference/index.md)

## Toolkit schemas

This section covers **97** `toolkit` schema files.

| Source path | Title | Type | Properties | Required | Details |
| --- | --- | --- | ---: | ---: | --- |
| `schemas/abi-contract.schema.json` | x86decomp ABI contract | `object` | 10 | 2 | [details](schema-reference/schemas-abi-contract.schema.json.md) |
| `schemas/assembly/asm-function.schema.json` | v0.7.8 function assembly result | `object` | 14 | 8 | [details](schema-reference/schemas-assembly-asm-function.schema.json.md) |
| `schemas/assembly/asm-run.schema.json` | v0.7.8 assembly run | `object` | 5 | 5 | [details](schema-reference/schemas-assembly-asm-run.schema.json.md) |
| `schemas/assembly/relocation-resolution.schema.json` | v0.7.8 COFF relocation resolution | `object` | 8 | 8 | [details](schema-reference/schemas-assembly-relocation-resolution.schema.json.md) |
| `schemas/assembly/roundtrip-report.schema.json` | v0.7.8 mnemonic round-trip report | `object` | 10 | 9 | [details](schema-reference/schemas-assembly-roundtrip-report.schema.json.md) |
| `schemas/assembly/symbol-map.schema.json` | v0.7.8 original-RVA symbol map | `object` | 0 | 0 | [details](schema-reference/schemas-assembly-symbol-map.schema.json.md) |
| `schemas/benchmark-corpus.schema.json` | Ground-truth benchmark corpus | `object` | 3 | 3 | [details](schema-reference/schemas-benchmark-corpus.schema.json.md) |
| `schemas/claim.schema.json` | x86decomp claim | `object` | 10 | 10 | [details](schema-reference/schemas-claim.schema.json.md) |
| `schemas/coff-archive.schema.json` | x86decomp COFF Archive Inspection | `object` | 7 | 7 | [details](schema-reference/schemas-coff-archive.schema.json.md) |
| `schemas/comdat-resolution.schema.json` | COFF COMDAT resolution report | `object` | 5 | 5 | [details](schema-reference/schemas-comdat-resolution.schema.json.md) |
| `schemas/compiler-ground-truth-comparison.schema.json` | Compiler/version ground-truth corpus comparison | `object` | 6 | 6 | [details](schema-reference/schemas-compiler-ground-truth-comparison.schema.json.md) |
| `schemas/compiler-ground-truth.schema.json` | Compiler ground-truth corpus manifest | `object` | 5 | 3 | [details](schema-reference/schemas-compiler-ground-truth.schema.json.md) |
| `schemas/compiler-lab.schema.json` | Compiler experiment matrix | `object` | 8 | 2 | [details](schema-reference/schemas-compiler-lab.schema.json.md) |
| `schemas/compiler-profile.schema.json` | x86decomp compiler profile | `object` | 14 | 9 | [details](schema-reference/schemas-compiler-profile.schema.json.md) |
| `schemas/convergence-report.schema.json` | Not declared | `object` | 14 | 10 | [details](schema-reference/schemas-convergence-report.schema.json.md) |
| `schemas/cpp-recovery.schema.json` | Not declared | `object` | 12 | 8 | [details](schema-reference/schemas-cpp-recovery.schema.json.md) |
| `schemas/decompme-packet.schema.json` | Local decomp.me-style function packet | `object` | 9 | 9 | [details](schema-reference/schemas-decompme-packet.schema.json.md) |
| `schemas/dependency-audit.schema.json` | x86decomp dependency vulnerability audit | `object` | 12 | 11 | [details](schema-reference/schemas-dependency-audit.schema.json.md) |
| `schemas/drcov-trace.schema.json` | Normalized DynamoRIO drcov text trace | `object` | 10 | 8 | [details](schema-reference/schemas-drcov-trace.schema.json.md) |
| `schemas/dynamic-report.schema.json` | Bounded Unicorn differential report | `object` | 5 | 5 | [details](schema-reference/schemas-dynamic-report.schema.json.md) |
| `schemas/evidence.schema.json` | x86decomp evidence item | `object` | 9 | 9 | [details](schema-reference/schemas-evidence.schema.json.md) |
| `schemas/exe-diff-report.schema.json` | PE function to COFF symbol comparison | `object` | 14 | 8 | [details](schema-reference/schemas-exe-diff-report.schema.json.md) |
| `schemas/execution-harness-generated.schema.json` | Not declared | `object` | 17 | 16 | [details](schema-reference/schemas-execution-harness-generated.schema.json.md) |
| `schemas/execution-harness.schema.json` | Bounded Unicorn execution harness | `object` | 13 | 1 | [details](schema-reference/schemas-execution-harness.schema.json.md) |
| `schemas/function-workflow.schema.json` | x86decomp per-function workflow | `object` | 11 | 9 | [details](schema-reference/schemas-function-workflow.schema.json.md) |
| `schemas/function.schema.json` | x86decomp Ghidra function artifact (schema versions 1 and 2) | `object` | 19 | 11 | [details](schema-reference/schemas-function.schema.json.md) |
| `schemas/governance/campaign.schema.json` | campaign | `object` | 5 | 4 | [details](schema-reference/schemas-governance-campaign.schema.json.md) |
| `schemas/governance/candidate.schema.json` | candidate | `object` | 5 | 3 | [details](schema-reference/schemas-governance-candidate.schema.json.md) |
| `schemas/governance/changeset.schema.json` | changeset manifest | `object` | 6 | 5 | [details](schema-reference/schemas-governance-changeset.schema.json.md) |
| `schemas/governance/consensus.schema.json` | consensus observation | `object` | 9 | 9 | [details](schema-reference/schemas-governance-consensus.schema.json.md) |
| `schemas/governance/counterexample.schema.json` | counterexample | `object` | 7 | 6 | [details](schema-reference/schemas-governance-counterexample.schema.json.md) |
| `schemas/governance/family.schema.json` | binary family report | `object` | 5 | 5 | [details](schema-reference/schemas-governance-family.schema.json.md) |
| `schemas/governance/hypothesis.schema.json` | hypothesis | `object` | 7 | 6 | [details](schema-reference/schemas-governance-hypothesis.schema.json.md) |
| `schemas/governance/knowledge-graph.schema.json` | knowledge graph impact | `object` | 5 | 5 | [details](schema-reference/schemas-governance-knowledge-graph.schema.json.md) |
| `schemas/governance/plugin.schema.json` | plugin manifest | `object` | 5 | 5 | [details](schema-reference/schemas-governance-plugin.schema.json.md) |
| `schemas/governance/proof-bundle.schema.json` | proof bundle manifest | `object` | 4 | 3 | [details](schema-reference/schemas-governance-proof-bundle.schema.json.md) |
| `schemas/governance/review.schema.json` | review item | `object` | 7 | 5 | [details](schema-reference/schemas-governance-review.schema.json.md) |
| `schemas/governance/worker.schema.json` | worker profile | `object` | 5 | 3 | [details](schema-reference/schemas-governance-worker.schema.json.md) |
| `schemas/hybrid-project.schema.json` | Continuously buildable hybrid project | `object` | 6 | 6 | [details](schema-reference/schemas-hybrid-project.schema.json.md) |
| `schemas/image-match-report.schema.json` | Target-specific whole-image match report | `object` | 12 | 10 | [details](schema-reference/schemas-image-match-report.schema.json.md) |
| `schemas/image-profile.schema.json` | Target-specific PE image layout profile | `object` | 9 | 6 | [details](schema-reference/schemas-image-profile.schema.json.md) |
| `schemas/integration-report.schema.json` | Bounded integration comparison report | `object` | 8 | 10 | [details](schema-reference/schemas-integration-report.schema.json.md) |
| `schemas/integration-scenarios.schema.json` | Integration scenario manifest | `object` | 5 | 4 | [details](schema-reference/schemas-integration-scenarios.schema.json.md) |
| `schemas/linker-layout.schema.json` | Linker layout reconstruction report | `object` | 9 | 6 | [details](schema-reference/schemas-linker-layout.schema.json.md) |
| `schemas/linker-reconstruction-plan.schema.json` | Not declared | `object` | 17 | 11 | [details](schema-reference/schemas-linker-reconstruction-plan.schema.json.md) |
| `schemas/local-llm/candidate.schema.json` | Local LLM C proposal response | `object` | 4 | 4 | [details](schema-reference/schemas-local-llm-candidate.schema.json.md) |
| `schemas/local-llm/job.schema.json` | Local LLM C generation and byte-match job | `object` | 16 | 4 | [details](schema-reference/schemas-local-llm-job.schema.json.md) |
| `schemas/local-llm/profile.schema.json` | Local LLM provider profile | `object` | 17 | 17 | [details](schema-reference/schemas-local-llm-profile.schema.json.md) |
| `schemas/local-llm/report.schema.json` | Local LLM exact byte-match report | `object` | 13 | 13 | [details](schema-reference/schemas-local-llm-report.schema.json.md) |
| `schemas/mcp-mutation.schema.json` | Evidence-gated MCP mutation | `object` | 10 | 8 | [details](schema-reference/schemas-mcp-mutation.schema.json.md) |
| `schemas/memory-event.schema.json` | x86decomp project memory event | `object` | 11 | 11 | [details](schema-reference/schemas-memory-event.schema.json.md) |
| `schemas/msvc-metadata.schema.json` | Bounded MSVC metadata analysis report | `object` | 8 | 8 | [details](schema-reference/schemas-msvc-metadata.schema.json.md) |
| `schemas/native/boundary-finding.schema.json` | x86decomp boundary-finding | `object` | 3 | 3 | [details](schema-reference/schemas-native-boundary-finding.schema.json.md) |
| `schemas/native/candidate-manifest.schema.json` | x86decomp candidate-manifest | `object` | 5 | 4 | [details](schema-reference/schemas-native-candidate-manifest.schema.json.md) |
| `schemas/native/function-match.schema.json` | x86decomp function-match | `object` | 5 | 5 | [details](schema-reference/schemas-native-function-match.schema.json.md) |
| `schemas/native/function-slot.schema.json` | x86decomp function-slot | `object` | 5 | 5 | [details](schema-reference/schemas-native-function-slot.schema.json.md) |
| `schemas/native/hybrid-composition.schema.json` | x86decomp hybrid-composition | `object` | 4 | 4 | [details](schema-reference/schemas-native-hybrid-composition.schema.json.md) |
| `schemas/native/loop-run.schema.json` | x86decomp loop-run | `object` | 4 | 4 | [details](schema-reference/schemas-native-loop-run.schema.json.md) |
| `schemas/native/match-run.schema.json` | x86decomp match-run | `object` | 2 | 2 | [details](schema-reference/schemas-native-match-run.schema.json.md) |
| `schemas/native/patch-plan.schema.json` | x86decomp patch-plan | `object` | 3 | 3 | [details](schema-reference/schemas-native-patch-plan.schema.json.md) |
| `schemas/native/runtime-validation.schema.json` | x86decomp runtime-validation | `object` | 4 | 4 | [details](schema-reference/schemas-native-runtime-validation.schema.json.md) |
| `schemas/native/section-export.schema.json` | x86decomp section-export | `object` | 2 | 2 | [details](schema-reference/schemas-native-section-export.schema.json.md) |
| `schemas/native/staging-symbol.schema.json` | x86decomp staging-symbol | `object` | 4 | 4 | [details](schema-reference/schemas-native-staging-symbol.schema.json.md) |
| `schemas/native/windows-tool.schema.json` | x86decomp windows-tool | `object` | 3 | 2 | [details](schema-reference/schemas-native-windows-tool.schema.json.md) |
| `schemas/objdiff-manifest.schema.json` | objdiff external invocation manifest | `object` | 12 | 4 | [details](schema-reference/schemas-objdiff-manifest.schema.json.md) |
| `schemas/pdb.schema.json` | x86decomp bounded PDB/MSF inventory | `object` | 13 | 13 | [details](schema-reference/schemas-pdb.schema.json.md) |
| `schemas/pipeline.schema.json` | Not declared | `object` | 5 | 4 | [details](schema-reference/schemas-pipeline.schema.json.md) |
| `schemas/project-template.schema.json` | Grounded x86decomp project-template contract | `object` | 13 | 11 | [details](schema-reference/schemas-project-template.schema.json.md) |
| `schemas/project.schema.json` | x86decomp project (schema versions 1, 2, and 3) | `object` | 21 | 10 | [details](schema-reference/schemas-project.schema.json.md) |
| `schemas/reconstruction/abi-contract.schema.json` | ABI contract | `object` | 6 | 6 | [details](schema-reference/schemas-reconstruction-abi-contract.schema.json.md) |
| `schemas/reconstruction/build.schema.json` | Build reconstruction contract | `object` | 4 | 4 | [details](schema-reference/schemas-reconstruction-build.schema.json.md) |
| `schemas/reconstruction/capsule.schema.json` | Reconstruction capsule manifest | `object` | 4 | 4 | [details](schema-reference/schemas-reconstruction-capsule.schema.json.md) |
| `schemas/reconstruction/compatibility-shim.schema.json` | Explicit compatibility shim | `object` | 6 | 6 | [details](schema-reference/schemas-reconstruction-compatibility-shim.schema.json.md) |
| `schemas/reconstruction/generated-test.schema.json` | Generated regression test | `object` | 7 | 7 | [details](schema-reference/schemas-reconstruction-generated-test.schema.json.md) |
| `schemas/reconstruction/header.schema.json` | Recovered header contract | `object` | 4 | 4 | [details](schema-reference/schemas-reconstruction-header.schema.json.md) |
| `schemas/reconstruction/library-match.schema.json` | Static library recognition candidate | `object` | 7 | 6 | [details](schema-reference/schemas-reconstruction-library-match.schema.json.md) |
| `schemas/reconstruction/module.schema.json` | Recovered module hypothesis | `object` | 6 | 5 | [details](schema-reference/schemas-reconstruction-module.schema.json.md) |
| `schemas/reconstruction/security-finding.schema.json` | Security finding | `object` | 7 | 7 | [details](schema-reference/schemas-reconstruction-security-finding.schema.json.md) |
| `schemas/reconstruction/semantic-changeset.schema.json` | Semantic changeset | `object` | 5 | 4 | [details](schema-reference/schemas-reconstruction-semantic-changeset.schema.json.md) |
| `schemas/reconstruction/source-provenance.schema.json` | Source provenance record | `object` | 9 | 9 | [details](schema-reference/schemas-reconstruction-source-provenance.schema.json.md) |
| `schemas/reconstruction/translation-unit.schema.json` | Translation unit hypothesis | `object` | 5 | 5 | [details](schema-reference/schemas-reconstruction-translation-unit.schema.json.md) |
| `schemas/release-gate.schema.json` | Not declared | `object` | 9 | 9 | [details](schema-reference/schemas-release-gate.schema.json.md) |
| `schemas/relink-manifest.schema.json` | Manifest-driven full relink | `object` | 9 | 7 | [details](schema-reference/schemas-relink-manifest.schema.json.md) |
| `schemas/reproduction.schema.json` | Not declared | `object` | 13 | 6 | [details](schema-reference/schemas-reproduction.schema.json.md) |
| `schemas/security-audit.schema.json` | Not declared | `object` | 11 | 8 | [details](schema-reference/schemas-security-audit.schema.json.md) |
| `schemas/symbolic-memory-harness.schema.json` | Bounded symbolic memory and alias harness | `object` | 11 | 2 | [details](schema-reference/schemas-symbolic-memory-harness.schema.json.md) |
| `schemas/symbolic-memory-report.schema.json` | Bounded angr symbolic memory-alias comparison | `object` | 11 | 9 | [details](schema-reference/schemas-symbolic-memory-report.schema.json.md) |
| `schemas/symbolic-report.schema.json` | Bounded symbolic comparison report | `object` | 3 | 3 | [details](schema-reference/schemas-symbolic-report.schema.json.md) |
| `schemas/synthetic-corpus.schema.json` | Deterministic synthetic source corpus | `object` | 9 | 9 | [details](schema-reference/schemas-synthetic-corpus.schema.json.md) |
| `schemas/target-decisions.schema.json` | Operator-confirmed target decisions | `object` | 7 | 7 | [details](schema-reference/schemas-target-decisions.schema.json.md) |
| `schemas/target-pack.schema.json` | Not declared | `object` | 12 | 12 | [details](schema-reference/schemas-target-pack.schema.json.md) |
| `schemas/test-bundle-report.schema.json` | x86decomp Static Test Bundle Report | `object` | 12 | 10 | [details](schema-reference/schemas-test-bundle-report.schema.json.md) |
| `schemas/test-bundle.schema.json` | x86decomp Authorized Static Test Bundle | `object` | 6 | 3 | [details](schema-reference/schemas-test-bundle.schema.json.md) |
| `schemas/type-constraint.schema.json` | Type/ABI constraint record | `object` | 8 | 5 | [details](schema-reference/schemas-type-constraint.schema.json.md) |
| `schemas/verification.schema.json` | x86decomp byte verification report | `object` | 13 | 13 | [details](schema-reference/schemas-verification.schema.json.md) |
| `schemas/work-task.schema.json` | Validator-gated work item | `object` | 14 | 12 | [details](schema-reference/schemas-work-task.schema.json.md) |
| `schemas/worker-report.schema.json` | Not declared | `object` | 15 | 7 | [details](schema-reference/schemas-worker-report.schema.json.md) |

## Bundled test-suite schemas

This section covers **3** `test-suite` schema files.

| Source path | Title | Type | Properties | Required | Details |
| --- | --- | --- | ---: | ---: | --- |
| `test-suite/schemas/feature-catalog.schema.json` | x86decomp current-surface catalog | `object` | 14 | 14 | [details](schema-reference/test-suite-schemas-feature-catalog.schema.json.md) |
| `test-suite/schemas/run-report.schema.json` | x86decomp comprehensive test run report | `object` | 9 | 13 | [details](schema-reference/test-suite-schemas-run-report.schema.json.md) |
| `test-suite/schemas/test-config.schema.json` | x86decomp test configuration | `object` | 16 | 15 | [details](schema-reference/test-suite-schemas-test-config.schema.json.md) |

