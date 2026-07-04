---
title: Project Examples source audit
description: Current source hashes for every Project Example evidence ledger.
---

# Project Examples source audit

This ledger is regenerated from the 0.7.5 source tree. Each listed digest is a full SHA-256 of the referenced current file.

## `matching-project.md`

| Source | SHA-256 |
| --- | --- |
| `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/compiler.py` | `f21f38f6ed0804a959188e31f5c9fa498d7d0740536fbb82594a375b12353944` |
| `src/x86decomp/exe_diff.py` | `997ffacbd833a3bb4c0545d1fb1981469e1d575680f4b39b7e6f34a4796abdf0` |
| `src/x86decomp/image_match.py` | `a9c72f376532369da77440496a1ea07564da5071ef8e6108e29c58e33e96fcf4` |
| `src/x86decomp/workflow.py` | `cae8a093f08f66f9412393e59867c4d32ca7caf88533a175d22eebe1f325c0a5` |
| `tests/test_modes_and_db.py` | `7b3e58d0cbef709f782c724956d752cd24fab83ec169cf6eb49562b883b4b174` |

## `functional-project.md`

| Source | SHA-256 |
| --- | --- |
| `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/dynamic.py` | `a09cbba16f498158cf30191397884f0a70051c767b778cd520ac229b6e85e451` |
| `src/x86decomp/symbolic.py` | `93d98f6e85a01a107881131821d5eb04875d310795c4f173448918c5a96fdcd3` |
| `src/x86decomp/integration.py` | `cb8157c8210544e2ed4730e8bdb01f0a77dc9d05f683d43154cba1bf93c1e845` |
| `src/x86decomp/workflow.py` | `cae8a093f08f66f9412393e59867c4d32ca7caf88533a175d22eebe1f325c0a5` |
| `tests/test_dynamic_symbolic.py` | `0b21be2ee69be29d2dde6951f147195bd8042462690dea72fac0b6509deb3402` |

## `hybrid-project.md`

| Source | SHA-256 |
| --- | --- |
| `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/hybrid.py` | `721221b69c86bd2e7152ea2f322c9b48d89a01891feb6906038509a1f4592e2f` |
| `src/x86decomp/workflow.py` | `cae8a093f08f66f9412393e59867c4d32ca7caf88533a175d22eebe1f325c0a5` |
| `src/x86decomp/dynamic.py` | `a09cbba16f498158cf30191397884f0a70051c767b778cd520ac229b6e85e451` |
| `src/x86decomp/symbolic.py` | `93d98f6e85a01a107881131821d5eb04875d310795c4f173448918c5a96fdcd3` |
| `tests/test_pe64_patch_hybrid.py` | `6894dd0e5abce06a30df7ce445f6cf7faa87bcc16dac9f314f187e938697a62f` |

## `static-analysis-evidence.md`

| Source | SHA-256 |
| --- | --- |
| `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/pe.py` | `39a5dd1b26da8d0ef84e8ff247183068eb4943ab38211df3c56c43ca9a6911c0` |
| `src/x86decomp/ghidra.py` | `98657d48a9d3ebb79eaf951aa8676ffd7ca696c2ba2f07fe8a5c4f0ad622c2b3` |
| `src/x86decomp/disassembly.py` | `cc86a46f8c8674a6e14304158bd1d2467fb09ccbb00778c116204b0a639638b3` |
| `src/x86decomp/evidence.py` | `de8befd97c8e7f0529f7c3c2750836f8f38fab52e26987cf390d725faad3ee1e` |
| `src/x86decomp/analysis_db.py` | `409e503d6c264dba48a00e1d1afc475ce735cf25f1ec4aab7ac41b07ed5b9bad` |
| `tests/test_ghidra.py` | `1c9a934bad943761f8d9b6bc22509a054a8ead82747d2091d5f7e84c5682b88b` |

## `compiler-laboratory.md`

| Source | SHA-256 |
| --- | --- |
| `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/compiler.py` | `f21f38f6ed0804a959188e31f5c9fa498d7d0740536fbb82594a375b12353944` |
| `src/x86decomp/compiler_lab.py` | `05a54baba63c926190c0e2fb45bff09c6eb338ed6a479e6e47be210a6b1de859` |
| `src/x86decomp/toolchains.py` | `9dde5962b67d30fec64266313f5488a4e5501de9db26605d4719cbe276cde03f` |
| `tests/test_compiler.py` | `9645daed68779957cd14addad7626d32d99056f551c27d873e3f475cfe862f64` |

## `patch-image-integration.md`

| Source | SHA-256 |
| --- | --- |
| `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/patching.py` | `61b9d802fc2c9c89f06877876f72efb7fc16d3a1fb283dddfd561dfd4fe61741` |
| `src/x86decomp/pe32.py` | `746651d78b0b8401565dd22e99f73c8c902b13400fd80094d4675ab52c8c4be5` |
| `tests/test_pe64_patch_hybrid.py` | `6894dd0e5abce06a30df7ce445f6cf7faa87bcc16dac9f314f187e938697a62f` |

## `full-relink-convergence.md`

| Source | SHA-256 |
| --- | --- |
| `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/linker_reconstruction.py` | `f67bc3077e7d54a9a32e542113cc28eadf00fa581c8e3d3c26e5c1b45a4e0900` |
| `src/x86decomp/relink.py` | `d401db042d4cc8300ccd4babd28cea400dca824d187a7caf0a1f3ead407fb296` |
| `src/x86decomp/image_match.py` | `a9c72f376532369da77440496a1ea07564da5071ef8e6108e29c58e33e96fcf4` |
| `src/x86decomp/convergence.py` | `2b943e9c8c2399089e1b8c2815c0de4cb1bcf0468c09e64a647fef3508922f74` |
| `tests/test_relink.py` | `580ca742c9d4f1d53de889f6f6bc5800e04147a31d86f0424a6d7a7252cefbb1` |

## `abi-type-recovery.md`

| Source | SHA-256 |
| --- | --- |
| `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/abi.py` | `e69b8d4ba247b2e3dbd3553cd207ee8fbe24fe244878c4dabb4afffbebb33903` |
| `src/x86decomp/cpp_recovery.py` | `c1f07b15f8649be4235cb56bb2e8f953ed31211b98311633d6beccde38dce8fa` |
| `src/x86decomp/harness_generator.py` | `75ab6f14bcef35574409e280dad90a705f71bc5763d507258f705ad8f4c431f2` |
| `src/x86decomp/analysis_db.py` | `409e503d6c264dba48a00e1d1afc475ce735cf25f1ec4aab7ac41b07ed5b9bad` |
| `tests/test_abi_disassembly.py` | `7707cba729a70b66986595aea747f5c1e782023e2b58134d2786680b52840a64` |

## `target-release-reproducibility.md`

| Source | SHA-256 |
| --- | --- |
| `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/reproducibility.py` | `bcc5e2a773d7eb7589f28df90c0fe898155788b8e695d15e363e6dbad249ae7b` |
| `src/x86decomp/security_audit.py` | `6131424e2b3443bd0e6af244fdcf2418a36ea752afa838a124d5e98bedd913d5` |
| `src/x86decomp/release_gate.py` | `8e79be8c5af67a90063af185b2239a5ce5a8ca828627ee05c14d897f891e02fd` |
| `src/x86decomp/project_state.py` | `2c866a3ccaddff98f1d9342a1eb5397d3dc2bd6d77e4b95c7dd07a8d2e02610f` |
| `tests/test_production.py` | `da0d4bd57f7f4bb68957fa8aa42a67f7eb34347f35137849e360dc95e796db89` |

## `benchmark-validation-corpus.md`

| Source | SHA-256 |
| --- | --- |
| `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/benchmarks.py` | `b9b28fbcb2f38723b274e4150b1c3914ddcbceab1b49461fc5797a84f9e13fb3` |
| `src/x86decomp/ground_truth.py` | `9684fbcda0fd5060b3c1f2d0efb83892900c69190d33e24fd7e49f91885181e2` |
| `src/x86decomp/dynamic.py` | `a09cbba16f498158cf30191397884f0a70051c767b778cd520ac229b6e85e451` |
| `src/x86decomp/symbolic.py` | `93d98f6e85a01a107881131821d5eb04875d310795c4f173448918c5a96fdcd3` |
| `src/x86decomp/integration.py` | `cb8157c8210544e2ed4730e8bdb01f0a77dc9d05f683d43154cba1bf93c1e845` |
| `tests/test_linker_metadata_corpus.py` | `aa88771eecf6bbd2a6fcc6230848165884fea583b48688061d61c14756f9a1de` |

## `project-operations-recovery.md`

| Source | SHA-256 |
| --- | --- |
| `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/project_state.py` | `2c866a3ccaddff98f1d9342a1eb5397d3dc2bd6d77e4b95c7dd07a8d2e02610f` |
| `src/x86decomp/orchestrator.py` | `752a6e6b5d4f931007e93ee7898f6a0d2500b044266c7153a27be7e7eb49477e` |
| `src/x86decomp/content_store.py` | `2348ce9593959da0a9f52b144435a70b30965443a06e701c0ff9cf7c86e7d1a4` |
| `src/x86decomp/security_audit.py` | `6131424e2b3443bd0e6af244fdcf2418a36ea752afa838a124d5e98bedd913d5` |
| `tests/test_project.py` | `04d73c197e4b7979731c140bef24e36ab323099e715d5462c95983a83d558c2b` |
