---
title: v0.7.4 project-examples source audit
description: Exact parser, implementation, and independent verification evidence for
  every project example.
original_path: project-examples/source-audit.html
---

Section: Project examples

# v0.7.4 project-examples source audit

Exact parser, implementation, and independent verification evidence for every project example.

> **Audit scope.** This page records the exact source files, line anchors, and full SHA-256 values used to substantiate the examples. The companion JSON is installed at the site root as [`PROJECT_EXAMPLES_SOURCE_AUDIT.json`](../release-artifacts/PROJECT_EXAMPLES_SOURCE_AUDIT.json).

| Example | Class | Source path | Lines | SHA-256 |
| --- | --- | --- | --- | --- |
| [matching-project](matching-project.md) | parser | `src/x86decomp/cli.py` | L122–L125 | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| [matching-project](matching-project.md) | parser | `src/x86decomp/cli.py` | L132–L135 | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| [matching-project](matching-project.md) | implementation | `src/x86decomp/coff.py` | L875–L878 | `f6900af73b991d2ed380250c78d4a228ff6b10f45bd4bcf04fb449c45f13d28e` |
| [matching-project](matching-project.md) | implementation | `src/x86decomp/exe_diff.py` | L84–L87 | `997ffacbd833a3bb4c0545d1fb1981469e1d575680f4b39b7e6f34a4796abdf0` |
| [matching-project](matching-project.md) | implementation | `src/x86decomp/image_match.py` | L186–L189 | `a9c72f376532369da77440496a1ea07564da5071ef8e6108e29c58e33e96fcf4` |
| [matching-project](matching-project.md) | implementation | `src/x86decomp/workflow.py` | L34–L37 | `cae8a093f08f66f9412393e59867c4d32ca7caf88533a175d22eebe1f325c0a5` |
| [matching-project](matching-project.md) | test | `tests/test_coff.py` | L9–L12 | `57797f4ad3e7871224434918b93fa79fc4046042cf54aa4f2c1fc1ddca99a8df` |
| [matching-project](matching-project.md) | test | `tests/test_linker_metadata_corpus.py` | L109–L112 | `aa88771eecf6bbd2a6fcc6230848165884fea583b48688061d61c14756f9a1de` |
| [matching-project](matching-project.md) | test | `tests/test_modes_and_db.py` | L12–L15 | `7b3e58d0cbef709f782c724956d752cd24fab83ec169cf6eb49562b883b4b174` |
| [functional-project](functional-project.md) | parser | `src/x86decomp/cli.py` | L146–L149 | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| [functional-project](functional-project.md) | parser | `src/x86decomp/cli.py` | L152–L155 | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| [functional-project](functional-project.md) | implementation | `src/x86decomp/dynamic.py` | L280–L283 | `a09cbba16f498158cf30191397884f0a70051c767b778cd520ac229b6e85e451` |
| [functional-project](functional-project.md) | implementation | `src/x86decomp/dynamic.py` | L327–L330 | `a09cbba16f498158cf30191397884f0a70051c767b778cd520ac229b6e85e451` |
| [functional-project](functional-project.md) | implementation | `src/x86decomp/harness_generator.py` | L21–L24 | `75ab6f14bcef35574409e280dad90a705f71bc5763d507258f705ad8f4c431f2` |
| [functional-project](functional-project.md) | implementation | `src/x86decomp/integration.py` | L273–L276 | `cb8157c8210544e2ed4730e8bdb01f0a77dc9d05f683d43154cba1bf93c1e845` |
| [functional-project](functional-project.md) | implementation | `src/x86decomp/symbolic.py` | L605–L608 | `93d98f6e85a01a107881131821d5eb04875d310795c4f173448918c5a96fdcd3` |
| [functional-project](functional-project.md) | implementation | `src/x86decomp/symbolic.py` | L683–L686 | `93d98f6e85a01a107881131821d5eb04875d310795c4f173448918c5a96fdcd3` |
| [functional-project](functional-project.md) | test | `tests/test_dynamic_symbolic.py` | L14–L17 | `0b21be2ee69be29d2dde6951f147195bd8042462690dea72fac0b6509deb3402` |
| [functional-project](functional-project.md) | test | `tests/test_integration.py` | L68–L71 | `0175ece91623baf3dd4092ddab3ba03bd47308082bccc85de135ce2b80b47ed0` |
| [functional-project](functional-project.md) | test | `tests/test_production.py` | L209–L212 | `da0d4bd57f7f4bb68957fa8aa42a67f7eb34347f35137849e360dc95e796db89` |
| [hybrid-project](hybrid-project.md) | parser | `src/x86decomp/cli.py` | L156–L159 | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| [hybrid-project](hybrid-project.md) | schema | `schemas/project-template.schema.json` | L6–L9 | `1bf881ea328d3a6c00d727c0cbe1e47763726e70362a085354178add994458ce` |
| [hybrid-project](hybrid-project.md) | implementation | `src/x86decomp/dynamic.py` | L327–L330 | `a09cbba16f498158cf30191397884f0a70051c767b778cd520ac229b6e85e451` |
| [hybrid-project](hybrid-project.md) | implementation | `src/x86decomp/hybrid.py` | L24–L27 | `721221b69c86bd2e7152ea2f322c9b48d89a01891feb6906038509a1f4592e2f` |
| [hybrid-project](hybrid-project.md) | implementation | `src/x86decomp/symbolic.py` | L683–L686 | `93d98f6e85a01a107881131821d5eb04875d310795c4f173448918c5a96fdcd3` |
| [hybrid-project](hybrid-project.md) | implementation | `src/x86decomp/workflow.py` | L21–L24 | `cae8a093f08f66f9412393e59867c4d32ca7caf88533a175d22eebe1f325c0a5` |
| [hybrid-project](hybrid-project.md) | implementation | `src/x86decomp/workflow.py` | L82–L85 | `cae8a093f08f66f9412393e59867c4d32ca7caf88533a175d22eebe1f325c0a5` |
| [hybrid-project](hybrid-project.md) | test | `tests/test_pe64_patch_hybrid.py` | L33–L36 | `6894dd0e5abce06a30df7ce445f6cf7faa87bcc16dac9f314f187e938697a62f` |
| [static-analysis-evidence](static-analysis-evidence.md) | parser | `src/x86decomp/cli.py` | L108–L111 | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| [static-analysis-evidence](static-analysis-evidence.md) | parser | `src/x86decomp/cli.py` | L198–L201 | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| [static-analysis-evidence](static-analysis-evidence.md) | implementation | `ghidra_scripts/ExportFunctionArtifacts.java` | L162–L165 | `2c1a21482d49c2bdd2fcf86e6df9d3c401fc4e5e4c4a36ea358aa9e2ddf6ca49` |
| [static-analysis-evidence](static-analysis-evidence.md) | implementation | `src/x86decomp/analysis_db.py` | L185–L188 | `409e503d6c264dba48a00e1d1afc475ce735cf25f1ec4aab7ac41b07ed5b9bad` |
| [static-analysis-evidence](static-analysis-evidence.md) | implementation | `src/x86decomp/artifacts.py` | L45–L48 | `171833c573e11e5d40d7791f8fea523536905a8486145a1aa1b96ea2761e6e6b` |
| [static-analysis-evidence](static-analysis-evidence.md) | implementation | `src/x86decomp/evidence.py` | L199–L202 | `de8befd97c8e7f0529f7c3c2750836f8f38fab52e26987cf390d725faad3ee1e` |
| [static-analysis-evidence](static-analysis-evidence.md) | implementation | `src/x86decomp/pe.py` | L278–L281 | `39a5dd1b26da8d0ef84e8ff247183068eb4943ab38211df3c56c43ca9a6911c0` |
| [static-analysis-evidence](static-analysis-evidence.md) | test | `tests/test_artifacts.py` | L31–L34 | `bcf7a774d955c365b701f002a37884e35babacc396f6a78188c6e2ada40bca67` |
| [static-analysis-evidence](static-analysis-evidence.md) | test | `tests/test_evidence.py` | L11–L14 | `4e8b73d7ad07cbce395ffe1267c272aeabdb861c0d198b6b8fcf5b448341b669` |
| [static-analysis-evidence](static-analysis-evidence.md) | doc | `docs/supported-scope.md` | L1–L4 | `c0e6743ef1b73e262c786192ba103189b6f63f27c768b9b82ee3807946976ae8` |
| [compiler-laboratory](compiler-laboratory.md) | parser | `src/x86decomp/cli.py` | L115–L118 | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| [compiler-laboratory](compiler-laboratory.md) | parser | `src/x86decomp/cli.py` | L117–L120 | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| [compiler-laboratory](compiler-laboratory.md) | implementation | `src/x86decomp/compiler.py` | L101–L104 | `f21f38f6ed0804a959188e31f5c9fa498d7d0740536fbb82594a375b12353944` |
| [compiler-laboratory](compiler-laboratory.md) | implementation | `src/x86decomp/compiler_lab.py` | L28–L31 | `05a54baba63c926190c0e2fb45bff09c6eb338ed6a479e6e47be210a6b1de859` |
| [compiler-laboratory](compiler-laboratory.md) | implementation | `src/x86decomp/compiler_lab.py` | L57–L60 | `05a54baba63c926190c0e2fb45bff09c6eb338ed6a479e6e47be210a6b1de859` |
| [compiler-laboratory](compiler-laboratory.md) | implementation | `src/x86decomp/compiler_lab.py` | L77–L80 | `05a54baba63c926190c0e2fb45bff09c6eb338ed6a479e6e47be210a6b1de859` |
| [compiler-laboratory](compiler-laboratory.md) | implementation | `src/x86decomp/toolchains.py` | L12–L15 | `9dde5962b67d30fec64266313f5488a4e5501de9db26605d4719cbe276cde03f` |
| [compiler-laboratory](compiler-laboratory.md) | test | `tests/test_compiler.py` | L13–L16 | `9645daed68779957cd14addad7626d32d99056f551c27d873e3f475cfe862f64` |
| [compiler-laboratory](compiler-laboratory.md) | test | `tests/test_production.py` | L166–L169 | `da0d4bd57f7f4bb68957fa8aa42a67f7eb34347f35137849e360dc95e796db89` |
| [patch-image-integration](patch-image-integration.md) | parser | `src/x86decomp/cli.py` | L154–L157 | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| [patch-image-integration](patch-image-integration.md) | implementation | `src/x86decomp/patching.py` | L39–L42 | `61b9d802fc2c9c89f06877876f72efb7fc16d3a1fb283dddfd561dfd4fe61741` |
| [patch-image-integration](patch-image-integration.md) | implementation | `src/x86decomp/patching.py` | L65–L68 | `61b9d802fc2c9c89f06877876f72efb7fc16d3a1fb283dddfd561dfd4fe61741` |
| [patch-image-integration](patch-image-integration.md) | implementation | `src/x86decomp/pe.py` | L278–L281 | `39a5dd1b26da8d0ef84e8ff247183068eb4943ab38211df3c56c43ca9a6911c0` |
| [patch-image-integration](patch-image-integration.md) | test | `tests/test_pe64_patch_hybrid.py` | L22–L25 | `6894dd0e5abce06a30df7ce445f6cf7faa87bcc16dac9f314f187e938697a62f` |
| [patch-image-integration](patch-image-integration.md) | test | `tests/test_pe64_patch_hybrid.py` | L27–L30 | `6894dd0e5abce06a30df7ce445f6cf7faa87bcc16dac9f314f187e938697a62f` |
| [full-relink-convergence](full-relink-convergence.md) | parser | `src/x86decomp/cli.py` | L225–L228 | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| [full-relink-convergence](full-relink-convergence.md) | parser | `src/x86decomp/cli.py` | L228–L231 | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| [full-relink-convergence](full-relink-convergence.md) | implementation | `src/x86decomp/linker_reconstruction.py` | L21–L24 | `f67bc3077e7d54a9a32e542113cc28eadf00fa581c8e3d3c26e5c1b45a4e0900` |
| [full-relink-convergence](full-relink-convergence.md) | implementation | `src/x86decomp/relink.py` | L23–L26 | `d401db042d4cc8300ccd4babd28cea400dca824d187a7caf0a1f3ead407fb296` |
| [full-relink-convergence](full-relink-convergence.md) | implementation | `src/x86decomp/convergence.py` | L35–L38 | `2b943e9c8c2399089e1b8c2815c0de4cb1bcf0468c09e64a647fef3508922f74` |
| [full-relink-convergence](full-relink-convergence.md) | test | `tests/test_relink.py` | L15–L18 | `580ca742c9d4f1d53de889f6f6bc5800e04147a31d86f0424a6d7a7252cefbb1` |
| [full-relink-convergence](full-relink-convergence.md) | test | `tests/test_production.py` | L236–L239 | `da0d4bd57f7f4bb68957fa8aa42a67f7eb34347f35137849e360dc95e796db89` |
| [abi-type-recovery](abi-type-recovery.md) | parser | `src/x86decomp/cli.py` | L145–L148 | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| [abi-type-recovery](abi-type-recovery.md) | parser | `src/x86decomp/cli.py` | L226–L229 | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| [abi-type-recovery](abi-type-recovery.md) | implementation | `src/x86decomp/abi.py` | L153–L156 | `e69b8d4ba247b2e3dbd3553cd207ee8fbe24fe244878c4dabb4afffbebb33903` |
| [abi-type-recovery](abi-type-recovery.md) | implementation | `src/x86decomp/analysis_db.py` | L39–L42 | `409e503d6c264dba48a00e1d1afc475ce735cf25f1ec4aab7ac41b07ed5b9bad` |
| [abi-type-recovery](abi-type-recovery.md) | implementation | `src/x86decomp/analysis_db.py` | L70–L73 | `409e503d6c264dba48a00e1d1afc475ce735cf25f1ec4aab7ac41b07ed5b9bad` |
| [abi-type-recovery](abi-type-recovery.md) | implementation | `src/x86decomp/cpp_recovery.py` | L55–L58 | `c1f07b15f8649be4235cb56bb2e8f953ed31211b98311633d6beccde38dce8fa` |
| [abi-type-recovery](abi-type-recovery.md) | test | `tests/test_abi_disassembly.py` | L9–L12 | `7707cba729a70b66986595aea747f5c1e782023e2b58134d2786680b52840a64` |
| [abi-type-recovery](abi-type-recovery.md) | test | `tests/test_modes_and_db.py` | L24–L27 | `7b3e58d0cbef709f782c724956d752cd24fab83ec169cf6eb49562b883b4b174` |
| [target-release-reproducibility](target-release-reproducibility.md) | parser | `src/x86decomp/cli.py` | L232–L235 | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| [target-release-reproducibility](target-release-reproducibility.md) | implementation | `src/x86decomp/release_gate.py` | L41–L44 | `8e79be8c5af67a90063af185b2239a5ce5a8ca828627ee05c14d897f891e02fd` |
| [target-release-reproducibility](target-release-reproducibility.md) | implementation | `src/x86decomp/release_gate.py` | L92–L95 | `8e79be8c5af67a90063af185b2239a5ce5a8ca828627ee05c14d897f891e02fd` |
| [target-release-reproducibility](target-release-reproducibility.md) | implementation | `src/x86decomp/reproducibility.py` | L52–L55 | `bcc5e2a773d7eb7589f28df90c0fe898155788b8e695d15e363e6dbad249ae7b` |
| [target-release-reproducibility](target-release-reproducibility.md) | implementation | `src/x86decomp/security_audit.py` | L78–L81 | `274c689b0141c11b2376e087427f13b55dc9e87beb3ee8e40851dad5d8e2ba1d` |
| [target-release-reproducibility](target-release-reproducibility.md) | implementation | `src/x86decomp/workflow.py` | L82–L85 | `cae8a093f08f66f9412393e59867c4d32ca7caf88533a175d22eebe1f325c0a5` |
| [target-release-reproducibility](target-release-reproducibility.md) | test | `tests/test_production.py` | L261–L264 | `da0d4bd57f7f4bb68957fa8aa42a67f7eb34347f35137849e360dc95e796db89` |
| [target-release-reproducibility](target-release-reproducibility.md) | test | `tests/test_production.py` | L486–L489 | `da0d4bd57f7f4bb68957fa8aa42a67f7eb34347f35137849e360dc95e796db89` |
| [benchmark-validation-corpus](benchmark-validation-corpus.md) | parser | `src/x86decomp/cli.py` | L138–L141 | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| [benchmark-validation-corpus](benchmark-validation-corpus.md) | parser | `src/x86decomp/cli.py` | L183–L186 | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| [benchmark-validation-corpus](benchmark-validation-corpus.md) | implementation | `src/x86decomp/benchmarks.py` | L40–L43 | `b9b28fbcb2f38723b274e4150b1c3914ddcbceab1b49461fc5797a84f9e13fb3` |
| [benchmark-validation-corpus](benchmark-validation-corpus.md) | implementation | `src/x86decomp/benchmarks.py` | L51–L54 | `b9b28fbcb2f38723b274e4150b1c3914ddcbceab1b49461fc5797a84f9e13fb3` |
| [benchmark-validation-corpus](benchmark-validation-corpus.md) | implementation | `src/x86decomp/ground_truth.py` | L72–L75 | `9684fbcda0fd5060b3c1f2d0efb83892900c69190d33e24fd7e49f91885181e2` |
| [benchmark-validation-corpus](benchmark-validation-corpus.md) | implementation | `src/x86decomp/synthetic_corpus.py` | L243–L246 | `a0475235f70093de7171e32cbde918a9290569245efaa06f8549cd1ad480ece0` |
| [benchmark-validation-corpus](benchmark-validation-corpus.md) | example | `examples/benchmarks/bounded-demo.json` | L37–L40 | `980ad9dc8352019f4dca1f06e25a8654ec87248befc178c35490ecc3d129a51a` |
| [benchmark-validation-corpus](benchmark-validation-corpus.md) | example | `examples/integration/bounded-demo.json` | L5–L8 | `e1b589e23a5fa0a7c1310c69760ef7729fa912c2a5584985a7cbb487f57eab26` |
| [benchmark-validation-corpus](benchmark-validation-corpus.md) | test | `tests/test_linker_metadata_corpus.py` | L162–L165 | `aa88771eecf6bbd2a6fcc6230848165884fea583b48688061d61c14756f9a1de` |
| [benchmark-validation-corpus](benchmark-validation-corpus.md) | test | `tests/test_production.py` | L507–L510 | `da0d4bd57f7f4bb68957fa8aa42a67f7eb34347f35137849e360dc95e796db89` |
| [project-operations-recovery](project-operations-recovery.md) | parser | `src/x86decomp/cli.py` | L210–L213 | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| [project-operations-recovery](project-operations-recovery.md) | parser | `src/x86decomp/cli.py` | L220–L223 | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| [project-operations-recovery](project-operations-recovery.md) | implementation | `src/x86decomp/content_store.py` | L45–L48 | `4902a167d8d42224690983536869b729211920840f539ad038d67a587c98001a` |
| [project-operations-recovery](project-operations-recovery.md) | implementation | `src/x86decomp/orchestrator.py` | L187–L190 | `752a6e6b5d4f931007e93ee7898f6a0d2500b044266c7153a27be7e7eb49477e` |
| [project-operations-recovery](project-operations-recovery.md) | implementation | `src/x86decomp/project.py` | L103–L106 | `a9077107216cddb15d5e0a7ab95ac0e6f63b0817c2d1329842b6b4792f11ec5f` |
| [project-operations-recovery](project-operations-recovery.md) | implementation | `src/x86decomp/project_state.py` | L186–L189 | `8d063061a36ef9a66f1460e44c8a5f2e08bd239e8c3c6d9828f4bfc171bb1fbe` |
| [project-operations-recovery](project-operations-recovery.md) | implementation | `src/x86decomp/project_state.py` | L243–L246 | `8d063061a36ef9a66f1460e44c8a5f2e08bd239e8c3c6d9828f4bfc171bb1fbe` |
| [project-operations-recovery](project-operations-recovery.md) | test | `tests/test_production.py` | L94–L97 | `da0d4bd57f7f4bb68957fa8aa42a67f7eb34347f35137849e360dc95e796db89` |
| [project-operations-recovery](project-operations-recovery.md) | test | `tests/test_production.py` | L122–L125 | `da0d4bd57f7f4bb68957fa8aa42a67f7eb34347f35137849e360dc95e796db89` |

> **Truth boundary.** Evidence locations establish that the documented command surfaces and semantics exist in the audited 0.7.4 source. They do not make target-specific data, tool availability, or validator outcomes true for a user project.
