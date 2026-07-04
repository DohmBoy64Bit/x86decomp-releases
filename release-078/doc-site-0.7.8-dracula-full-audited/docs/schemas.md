---
title: JSON Schema Reference
description: Source-derived JSON Schema coverage for x86decomp 0.7.8.
---

# JSON Schema Reference

This page covers **97** schema files from the toolkit source tree. Paths and hashes are exact source-relative values.

| Source path | Title | Type | Properties | Required | SHA-256 |
| --- | --- | --- | ---: | ---: | --- |
| `schemas/abi-contract.schema.json` | x86decomp ABI contract | `object` | 10 | 2 | `536e89f5ab760329f3799138b17c8a321170fc1fc729528d97b7f75d4af96c76` |
| `schemas/assembly/asm-function.schema.json` | v0.7.8 function assembly result | `object` | 14 | 8 | `db7f1658e6121216219cbe02f674ad829a1dc71fd1e38ff60be82909aeff852f` |
| `schemas/assembly/asm-run.schema.json` | v0.7.8 assembly run | `object` | 5 | 5 | `a0d7cfbc8e8c5c9b01ed78c6942892a141c4f4be96f60e6ce774906b1ccc19ab` |
| `schemas/assembly/relocation-resolution.schema.json` | v0.7.8 COFF relocation resolution | `object` | 8 | 8 | `12f0d874e789ea1fb40eed10321b5b24d6e9231630c0b24bb2c39fe843e192cf` |
| `schemas/assembly/roundtrip-report.schema.json` | v0.7.8 mnemonic round-trip report | `object` | 10 | 9 | `00ecc65165836a423b5f53482d5367d4a70b88891dda997f0da0b6bd854ac1ac` |
| `schemas/assembly/symbol-map.schema.json` | v0.7.8 original-RVA symbol map | `object` | 0 | 0 | `3f208d4dd418fbfed4999ef6a6f9b8290227644c4d07d09beb265792ff1a7e5e` |
| `schemas/benchmark-corpus.schema.json` | Ground-truth benchmark corpus | `object` | 3 | 3 | `0081dd4d038287641f14ccd228dd0e824bff8bd3745f8251aaa0a94c1c61e36c` |
| `schemas/claim.schema.json` | x86decomp claim | `object` | 10 | 10 | `362341adcb81640a7839c77d37d7203b911e7e79655be6c0ab4115f460609532` |
| `schemas/coff-archive.schema.json` | x86decomp COFF Archive Inspection | `object` | 7 | 7 | `5f5a43f1ce6ae1221df24107f7b9db057156731736ff4aad5c81c93a73abaab3` |
| `schemas/comdat-resolution.schema.json` | COFF COMDAT resolution report | `object` | 5 | 5 | `01fd177dfa983202ca8770e7985aa623e166fd22c20fdecc1d3d37f9cbfe0aae` |
| `schemas/compiler-ground-truth-comparison.schema.json` | Compiler/version ground-truth corpus comparison | `object` | 6 | 6 | `1ea55d940c62d4e60487f74ac4d9756e4ff4c7cb2c39c9dd629b1d4150646dfb` |
| `schemas/compiler-ground-truth.schema.json` | Compiler ground-truth corpus manifest | `object` | 5 | 3 | `1f8d15358ce71168a0f7c4d61ba7ad9db1ef12b534b27444bdda1f77f96392a2` |
| `schemas/compiler-lab.schema.json` | Compiler experiment matrix | `object` | 8 | 2 | `37bc55f945daffc31844a78c2b4788191f501589303826a6cee207c5c4717506` |
| `schemas/compiler-profile.schema.json` | x86decomp compiler profile | `object` | 14 | 9 | `6903f160acf5cfb8329567efbdd2da82b9f171705971e9842afcae21a4a4f844` |
| `schemas/convergence-report.schema.json` | — | `object` | 14 | 10 | `ace195921a16f72366e2920e6e2ce4e464b51f665d4d12ff5117dbea49119185` |
| `schemas/cpp-recovery.schema.json` | — | `object` | 12 | 8 | `9eda5eb04cdd6404ed82077dab0b1f2668f3682b33f864fec3c7348439515d8a` |
| `schemas/decompme-packet.schema.json` | Local decomp.me-style function packet | `object` | 9 | 9 | `65cd0a5d3197e6de85ec46c8eb372a387102192d9341ee252a7f40ca83b91704` |
| `schemas/dependency-audit.schema.json` | x86decomp dependency vulnerability audit | `object` | 12 | 11 | `2eef4097789050d846536b406ccd7b9e8e639467bdf1ca530045fcc6050c8ee2` |
| `schemas/drcov-trace.schema.json` | Normalized DynamoRIO drcov text trace | `object` | 10 | 8 | `aedc8ab92612b4b325552d3de98da9d04e2e4c3aa2bb2ab319e20f85616cfe7f` |
| `schemas/dynamic-report.schema.json` | Bounded Unicorn differential report | `object` | 5 | 5 | `1af7c179c9d4fedbf542c098eab126d556fc8345a464176d211640f391effce0` |
| `schemas/evidence.schema.json` | x86decomp evidence item | `object` | 9 | 9 | `5c5199ae9f480dbbb28eb3ebd889a53a46c08535cabf346d3a0bf04f4a4aa7bd` |
| `schemas/exe-diff-report.schema.json` | PE function to COFF symbol comparison | `object` | 14 | 8 | `3bfb70b7158750523074f638ff5955cc519097a37543f9f097909f4576373b50` |
| `schemas/execution-harness-generated.schema.json` | — | `object` | 17 | 16 | `7ba43bfcb6b5b8736d784112af5531e1a890630e379eb2c345f15442c18a2c6d` |
| `schemas/execution-harness.schema.json` | Bounded Unicorn execution harness | `object` | 13 | 1 | `2ec27dc202dcf7ab923c646c71e30769b0c18527aaf2e6ba44e70536574e4f68` |
| `schemas/function-workflow.schema.json` | x86decomp per-function workflow | `object` | 11 | 9 | `972f7c4fef555a4653a57cad04f1dedb186cc70a6c59de7e674645b30c240351` |
| `schemas/function.schema.json` | x86decomp Ghidra function artifact (schema versions 1 and 2) | `object` | 19 | 11 | `00c65be77cc237df28a9112019c07019f88f38072ceb329907adc88bcfc34704` |
| `schemas/governance/campaign.schema.json` | campaign | `object` | 5 | 4 | `df027ea63ef0017b5a9ecae133a21ab7fa13f68e00545529e8606b5f39d1f854` |
| `schemas/governance/candidate.schema.json` | candidate | `object` | 5 | 3 | `db23f94af8b37ebdfff2798c271a0ef02ea9d77aae83fa8c8ebdab3d2f55ad67` |
| `schemas/governance/changeset.schema.json` | changeset manifest | `object` | 6 | 5 | `6788b90056dbf46cdaaaab292bdc6c3102e20ff47c790f131b47c15d08f5cbd3` |
| `schemas/governance/consensus.schema.json` | consensus observation | `object` | 9 | 9 | `f3edcf4a5962701cde7a0f4f483a19d49e9f5beea5e6a4dc3c643c9970ee9c43` |
| `schemas/governance/counterexample.schema.json` | counterexample | `object` | 7 | 6 | `0e2b706ed1bf89e6c07a483dd171dbb23fbac4f67c87ef1df16be6c2fe50d19c` |
| `schemas/governance/family.schema.json` | binary family report | `object` | 5 | 5 | `cd02347eefe68396b21d7ec5af6ef9c1554dd4715e962e302ece657cb0b851ed` |
| `schemas/governance/hypothesis.schema.json` | hypothesis | `object` | 7 | 6 | `1013bee5c093d4cf0e619dbcdc52a2b2ff79c0b768da9c699ad0483bfc283a83` |
| `schemas/governance/knowledge-graph.schema.json` | knowledge graph impact | `object` | 5 | 5 | `d1bc76932c0264e763eb4cdb47d46397ddf00bb57e1c240371ef42049631db28` |
| `schemas/governance/plugin.schema.json` | plugin manifest | `object` | 5 | 5 | `1fb5e12f5c8eb5408dea6372c5442273b1694559dc9c09784bbca4309dbf5fd2` |
| `schemas/governance/proof-bundle.schema.json` | proof bundle manifest | `object` | 4 | 3 | `b2619861c68f06f1ea0149a8649c5c215d0485472cad1317a463fe8eac5adf41` |
| `schemas/governance/review.schema.json` | review item | `object` | 7 | 5 | `280cfe7963adcdcbbb3a1fde01b921cad82751d2240a4fcdaa9b9543db071bc2` |
| `schemas/governance/worker.schema.json` | worker profile | `object` | 5 | 3 | `ca8f6768a4c7dfe89e80f2107c4bb43badde4d01d3ec6947ff001c9b207b403c` |
| `schemas/hybrid-project.schema.json` | Continuously buildable hybrid project | `object` | 6 | 6 | `c72692b4469f7ba92b2945968974d495371e2c0f03ad438c970418c3ce31d9b0` |
| `schemas/image-match-report.schema.json` | Target-specific whole-image match report | `object` | 12 | 10 | `f81f81c2581b2941b9a3850aa2d296957e1d14de2ad3d8ee92839b34ccfadc23` |
| `schemas/image-profile.schema.json` | Target-specific PE image layout profile | `object` | 9 | 6 | `5916e3589fb77876a26861ccfea7dfbfbf4b9c55e92243ed66dae4270dad70d7` |
| `schemas/integration-report.schema.json` | Bounded integration comparison report | `object` | 8 | 10 | `4732a3a8f4038739f46c7b7b74b20999c68d9f637bac783a53b03eee91e91d1a` |
| `schemas/integration-scenarios.schema.json` | Integration scenario manifest | `object` | 5 | 4 | `60799068b8df90e7d457415f6e08fa236a0620630ddab2641dec2ff8bac6e43e` |
| `schemas/linker-layout.schema.json` | Linker layout reconstruction report | `object` | 9 | 6 | `a8faf6022c8b70e04c3375d47a480b9a811e72edd55ea7e0ec4e80a77a8ca934` |
| `schemas/linker-reconstruction-plan.schema.json` | — | `object` | 17 | 11 | `1d6fadf9737abed4d02cc90d3859898785edf62d3909c39fe893c8841c57f504` |
| `schemas/local-llm/candidate.schema.json` | Local LLM C proposal response | `object` | 4 | 4 | `cadff624248794b1841a55fd49f2f980658a442d046530c183ec0c89d44d99ab` |
| `schemas/local-llm/job.schema.json` | Local LLM C generation and byte-match job | `object` | 16 | 4 | `6ac68b5f4f22855154f8ec09e599c7caa3ce12d117fb125a0bae8e4dce0197a8` |
| `schemas/local-llm/profile.schema.json` | Local LLM provider profile | `object` | 17 | 17 | `dc3ed501bada8be1896567c329fd550ad843059786ed07bbae6ef3063fdfe3ee` |
| `schemas/local-llm/report.schema.json` | Local LLM exact byte-match report | `object` | 13 | 13 | `d61c0308354431848f281d3c62cd32b39c9d61277492bee480a02276e5ad6ac0` |
| `schemas/mcp-mutation.schema.json` | Evidence-gated MCP mutation | `object` | 10 | 8 | `64335798160269133e880d823f14de7f0cb4f2dafbf0c47526e24fb9fb16ea29` |
| `schemas/memory-event.schema.json` | x86decomp project memory event | `object` | 11 | 11 | `d2f38971ac7dda92dda0564bb77bb4858160b5a342476d36fe52238eb5289e74` |
| `schemas/msvc-metadata.schema.json` | Bounded MSVC metadata analysis report | `object` | 8 | 8 | `84d0b6bc880ab47954f951a4eed4db317c14ee33ed5cdbe0ee098ce61c1d6273` |
| `schemas/native/boundary-finding.schema.json` | x86decomp boundary-finding | `object` | 3 | 3 | `58d723eee6c5c374f78dcac68a23be5d0b60c6f002c3e8285d307eef496e74fc` |
| `schemas/native/candidate-manifest.schema.json` | x86decomp candidate-manifest | `object` | 5 | 4 | `d3bad2e693b4b7d6e1c230d9e03ff775298273523c8b562d3b78400c13313029` |
| `schemas/native/function-match.schema.json` | x86decomp function-match | `object` | 5 | 5 | `e598ca859f33c96b62fe8dac7fcf78ec77b53e4b8f178b9f19e1f288e2725cd1` |
| `schemas/native/function-slot.schema.json` | x86decomp function-slot | `object` | 5 | 5 | `61bb10550455068b1c58073dfb30939aea8095cefbd775abab4d044efe9a2914` |
| `schemas/native/hybrid-composition.schema.json` | x86decomp hybrid-composition | `object` | 4 | 4 | `feb6682c1aa1ed0a3bc3c06230ce27f006641d96238050151ad22584eb02cb9d` |
| `schemas/native/loop-run.schema.json` | x86decomp loop-run | `object` | 4 | 4 | `de5d1a277444c3ea53ae0c4860d1a7978b478893fb893cf4c1ba1fca4a11b038` |
| `schemas/native/match-run.schema.json` | x86decomp match-run | `object` | 2 | 2 | `7afbfb42c5995ff375a050c93bb119ce50f2a761220c610f2c1622f082c23fb5` |
| `schemas/native/patch-plan.schema.json` | x86decomp patch-plan | `object` | 3 | 3 | `90a1f06eaa3f6a3d6b235cc0439c57fec0187006ccc4c01b8fbb76571bb31958` |
| `schemas/native/runtime-validation.schema.json` | x86decomp runtime-validation | `object` | 4 | 4 | `f314d1ae2b72314a6ebf6c6d2905a8eb2f314498f256f567e01ae08622da90f3` |
| `schemas/native/section-export.schema.json` | x86decomp section-export | `object` | 2 | 2 | `121ed87fe1b51a248b230acafd9780b96e74e01c72e9cba7fcd20fbb466eb317` |
| `schemas/native/staging-symbol.schema.json` | x86decomp staging-symbol | `object` | 4 | 4 | `44b3ce02db0758435f6a230a9ad37bd00c3a6308bf71761836050e5c90c6c4d0` |
| `schemas/native/windows-tool.schema.json` | x86decomp windows-tool | `object` | 3 | 2 | `22af6f0e3266250f1c741e95e231c4ee3d62fd3944e0000e6ab6e652089906e0` |
| `schemas/objdiff-manifest.schema.json` | objdiff external invocation manifest | `object` | 12 | 4 | `2fe8f65399749687b2890cc643f474c0b8de221e90f6ae5013ce0d8b46590360` |
| `schemas/pdb.schema.json` | x86decomp bounded PDB/MSF inventory | `object` | 13 | 13 | `850bbf885fa040ac4601dc4d93c2fb4b3afda1dd86612a0d8866a34bacf07008` |
| `schemas/pipeline.schema.json` | — | `object` | 5 | 4 | `a9b7b790fb6c877370a4c61ecbdf0f92eac13d9aba389cc0ab8d8723aee92ca6` |
| `schemas/project-template.schema.json` | Grounded x86decomp project-template contract | `object` | 13 | 11 | `1bf881ea328d3a6c00d727c0cbe1e47763726e70362a085354178add994458ce` |
| `schemas/project.schema.json` | x86decomp project (schema versions 1, 2, and 3) | `object` | 21 | 10 | `4ab19d9064e8d249fdd545d1fa183920902d6afbe647d004ddd571a208295b0b` |
| `schemas/reconstruction/abi-contract.schema.json` | ABI contract | `object` | 6 | 6 | `d2286943caed629e873a4107fcceb21f18b0759cfebd17b71f761af14e68e016` |
| `schemas/reconstruction/build.schema.json` | Build reconstruction contract | `object` | 4 | 4 | `647d938812825abaa84206de119ebc4a18d8fad70a4f50121f990a4af2571dd0` |
| `schemas/reconstruction/capsule.schema.json` | Reconstruction capsule manifest | `object` | 4 | 4 | `78eac1212fd7e2b41fc2bd180515f95d2d60fe26046a4fdb3ea51f810704ffb9` |
| `schemas/reconstruction/compatibility-shim.schema.json` | Explicit compatibility shim | `object` | 6 | 6 | `714bcc499ffc2db676e163a5886ce9ca4fca7df0b2382a94488c6dfc5a782926` |
| `schemas/reconstruction/generated-test.schema.json` | Generated regression test | `object` | 7 | 7 | `8e99342ae82922d0c5c17c41e857074a5a2cec9b1269e23572aea09b5715a7b5` |
| `schemas/reconstruction/header.schema.json` | Recovered header contract | `object` | 4 | 4 | `c878f851e64b11db9e0dad34785d5ef3ba3baa753e380af72f554fe44529a850` |
| `schemas/reconstruction/library-match.schema.json` | Static library recognition candidate | `object` | 7 | 6 | `cdf8967118c99e0f1d224829f1e3067a2b9db50f31ca945db68a3cec61b0f36e` |
| `schemas/reconstruction/module.schema.json` | Recovered module hypothesis | `object` | 6 | 5 | `4aa87665cf31d30d9395bff7fb9388c9bd55257718808572669a874922436a4f` |
| `schemas/reconstruction/security-finding.schema.json` | Security finding | `object` | 7 | 7 | `9a4f8a220e2e2d1d7dbc8116968bf2752d57a5725e18673faf59a192ace1826e` |
| `schemas/reconstruction/semantic-changeset.schema.json` | Semantic changeset | `object` | 5 | 4 | `2cc66c0075ba39a54d86a20ca3705d4656ce90e922ce5a8c0b9357db1bc27b28` |
| `schemas/reconstruction/source-provenance.schema.json` | Source provenance record | `object` | 9 | 9 | `d80a00434549c01f14f1afa7c43cb65b9eb653808b42fb5fa10f25b1d7ac1b0c` |
| `schemas/reconstruction/translation-unit.schema.json` | Translation unit hypothesis | `object` | 5 | 5 | `ea17fb7bfec69c8e9e3eb5d14179194acece94ba90d5e0ad76c5f3e653dca642` |
| `schemas/release-gate.schema.json` | — | `object` | 9 | 9 | `50e1f5a6cb46b67f833c881a7f025be5c7c047c1f23c3607608488afe17256cd` |
| `schemas/relink-manifest.schema.json` | Manifest-driven full relink | `object` | 9 | 7 | `ca2b77b7be6b562589e841753a9afa8c6baf1fc7cf8c703409c90fc56507e890` |
| `schemas/reproduction.schema.json` | — | `object` | 13 | 6 | `aea350be271c7795406a2dd55096775e9d0b531215e05f43b75a9c6b5bd98281` |
| `schemas/security-audit.schema.json` | — | `object` | 11 | 8 | `d62a14bd5c6d796dd52aee929ccfdf8e1265f825167070c8ffd680321a00b637` |
| `schemas/symbolic-memory-harness.schema.json` | Bounded symbolic memory and alias harness | `object` | 11 | 2 | `e7ce53b843c172758fc086503e040cd1c60a3836f528b2c8396a7e77ab7c200a` |
| `schemas/symbolic-memory-report.schema.json` | Bounded angr symbolic memory-alias comparison | `object` | 11 | 9 | `5e17dedb1bedf6581662f4cced118e40b8075957a161daea2abfab778d0298ba` |
| `schemas/symbolic-report.schema.json` | Bounded symbolic comparison report | `object` | 3 | 3 | `cc596ec7c42bc74e7810dbf52bf50cba2d17375e9438f0a3fcbb3dae67a88e29` |
| `schemas/synthetic-corpus.schema.json` | Deterministic synthetic source corpus | `object` | 9 | 9 | `3c05d2c0a766021805afdd306d6a08068af6a24cdb0adb82fb3eca4d0f1d7c7d` |
| `schemas/target-decisions.schema.json` | Operator-confirmed target decisions | `object` | 7 | 7 | `647192549c5e079a02e597648a0d3d2ade5078866f869b7e0da34324b5976ed6` |
| `schemas/target-pack.schema.json` | — | `object` | 12 | 12 | `867b89f3738ff1310340d078c5ae530f0087277e96cd00106fa1275cd0bcc954` |
| `schemas/test-bundle-report.schema.json` | x86decomp Static Test Bundle Report | `object` | 12 | 10 | `482f5b618cd46eb5e815392f2655bb9fe4f3683e1f5122b8f7ab0ea69f8a2820` |
| `schemas/test-bundle.schema.json` | x86decomp Authorized Static Test Bundle | `object` | 6 | 3 | `398d162a3ccc9e3bd1e984af67efbfaf12a840f4013b406c0cf8d150f490deab` |
| `schemas/type-constraint.schema.json` | Type/ABI constraint record | `object` | 8 | 5 | `f98328b457deccc685ea8be764507320d5ff94deddb366e47c5018a678baa59d` |
| `schemas/verification.schema.json` | x86decomp byte verification report | `object` | 13 | 13 | `a70e3422e6b0bec967695257c7b66d44f17a0cfe3f15d99799eb1c038ccb7fa0` |
| `schemas/work-task.schema.json` | Validator-gated work item | `object` | 14 | 12 | `36794b2e24e785918a28d8bd7f5fedd100c090ed64030c71eefa0a8c933b92c9` |
| `schemas/worker-report.schema.json` | — | `object` | 15 | 7 | `f4fee8d629c5e963519a4f5ab25c4bb0856592421ee218fe7d047b5ebe089b3c` |
