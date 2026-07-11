# Workflows

End-to-end workflow guides for common x86decomp tasks. Each workflow uses a different fictional video game scenario to demonstrate a complete, realistic pipeline with exact commands.

## Matching and Reconstruction

| Workflow | Game Scenario | Primary Commands |
|---|---|---|
| [Matching Decompilation](matching-decompilation.md) | Crystal Empire (RPG, x86-64, GCC 4.8) | init, ghidra-export, coff-inspect, compile, coff-extract, diff-function, patch-image, relink |
| [Full Relink Convergence](full-relink-convergence.md) | Graveyard Shift (horror, x86, lld-link) | inspect-pe, map-inspect, layout-reconstruct, linker-plan, compile, relink, convergence-analyze |
| [Hybrid Project](hybrid-project.md) | Neon Underground (cyberpunk, x86) | init, target-pack-infer, template-materialize, compile, hybrid-generate, patch-image |
| [Patch-Image Integration](patch-image-integration.md) | Iron Battalion (mech combat, MSVC 2008) | ghidra-export, compile, coff-extract, patch-image, diff-bytes |

## Functional and Validation

| Workflow | Game Scenario | Primary Commands |
|---|---|---|
| [Functional Decompilation](functional-decompilation.md) | Velocity Point (racing, x86) | ghidra-export, harness-generate, dynamic-validate, symbolic-validate, integration-run |
| [ABI and Type Recovery](abi-type-recovery.md) | Operation Stormfront (FPS, MSVC 6.0) | ghidra-export, abi-check, db-constraint-add, db-constraint-conflicts, workflow-init |
| [Text Swap](text-swap.md) | Rising Phoenix (fighting, embedded strings) | pe text-swap plan, pe text-swap build, pe text-swap inject, pe text-swap verify |

## Compiler and Benchmarking

| Workflow | Game Scenario | Primary Commands |
|---|---|---|
| [Compiler Laboratory](compiler-laboratory.md) | Aegis Protocol (RTS, unknown compiler) | toolchain-register, compiler-lab, compile, compile-worker, diff-function |
| [Benchmark Validation Corpus](benchmark-validation-corpus.md) | Solar Knights (space combat, x86-64) | corpus-create-manifest, corpus-build, corpus-verify, corpus-generate, benchmark-run |
| [Validation Corpus Benchmarks](validation-corpus-benchmarks.md) | Thunder Rally (arcade racer) | corpus-build, corpus-compare, corpus-generate, compiler-lab, benchmark-run |

## Operations and Evidence

| Workflow | Game Scenario | Primary Commands |
|---|---|---|
| [Project Operations and Recovery](project-operations-recovery.md) | Shadow Circuit (stealth action) | init, project-check, project-migrate, project-backup, project-restore, project-repair, project-gc |
| [Static-Analysis Evidence](static-analysis-evidence.md) | Wild Frontier (open-world, x86-64) | inspect-pe, pdb-inspect, metadata-scan, layout-reconstruct, evidence-add, claim-verify |
| [Target-Release Reproducibility](target-release-reproducibility.md) | Starfall Arena (MOBA) | reproduce-create, reproduce-verify, security-audit, sbom-generate, release-gate |

## AI-Assisted

| Workflow | Game Scenario | Primary Commands |
|---|---|---|
| [Local LLM Exact Match](local-llm-exact-match.md) | Darkwater Cove (adventure, small functions) | llm probe, llm profile-create, llm generate, llm match, llm verify, candidate promote |

## Choosing a workflow

- **New to x86decomp?** Start with [Project Operations and Recovery](project-operations-recovery.md) to understand project lifecycle.
- **Want byte-identical decompilation?** Begin with [Matching Decompilation](matching-decompilation.md), then progress to [Full Relink Convergence](full-relink-convergence.md).
- **Investigating an unknown compiler?** Use [Compiler Laboratory](compiler-laboratory.md) for matrix experiments.
- **Building evidence for type claims?** Follow [ABI and Type Recovery](abi-type-recovery.md) combined with [Static-Analysis Evidence](static-analysis-evidence.md).
- **Preparing for release?** Complete [Target-Release Reproducibility](target-release-reproducibility.md) as the final gate.
- **Exploring LLM-assisted decompilation?** Use [Local LLM Exact Match](local-llm-exact-match.md) with a loopback model provider.
