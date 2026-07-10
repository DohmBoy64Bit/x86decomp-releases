---
title: Schemas
description: JSON schema reference for x86decomp 0.7.11.
---

# Schemas

This page lists every JSON schema in the 0.7.11 release bundle with the source hash used by the site audit.

Schema count: **97**

| Schema | Title | Type | SHA-256 |
| --- | --- | --- | --- |
| [schemas/abi-contract.schema.json](schema-reference/schemas-abi-contract.schema.json.md) | x86decomp ABI contract | object | `536e89f5ab760329f3799138b17c8a321170fc1fc729528d97b7f75d4af96c76` |
| [schemas/assembly/asm-function.schema.json](schema-reference/schemas-assembly-asm-function.schema.json.md) | v0.7.11 function assembly result | object | `5203c2e7147c3d4a5b57d7f481e62a341c8a5a49aa6534c27350c51b67f49f4b` |
| [schemas/assembly/asm-run.schema.json](schema-reference/schemas-assembly-asm-run.schema.json.md) | v0.7.11 assembly run | object | `da6ccd5588a1e5a2324c9e99e4ac21bc9246d7393c3042e5436ee5a40ba98736` |
| [schemas/assembly/relocation-resolution.schema.json](schema-reference/schemas-assembly-relocation-resolution.schema.json.md) | v0.7.11 COFF relocation resolution | object | `2cf985f26cc073f194e444ef49215b8bc4f2cd66d0ee546f05e67559afba63a2` |
| [schemas/assembly/roundtrip-report.schema.json](schema-reference/schemas-assembly-roundtrip-report.schema.json.md) | v0.7.11 mnemonic round-trip report | object | `fd727824f525c79838ba3366ea7a3651490cd270d9e267734efca7d9223a3650` |
| [schemas/assembly/symbol-map.schema.json](schema-reference/schemas-assembly-symbol-map.schema.json.md) | v0.7.11 original-RVA symbol map | object | `ddacd944e055f1b3e9e902199252271944479183e3cfc77cbf11ff9443b867d6` |
| [schemas/benchmark-corpus.schema.json](schema-reference/schemas-benchmark-corpus.schema.json.md) | Ground-truth benchmark corpus | object | `0081dd4d038287641f14ccd228dd0e824bff8bd3745f8251aaa0a94c1c61e36c` |
| [schemas/claim.schema.json](schema-reference/schemas-claim.schema.json.md) | x86decomp claim | object | `362341adcb81640a7839c77d37d7203b911e7e79655be6c0ab4115f460609532` |
| [schemas/coff-archive.schema.json](schema-reference/schemas-coff-archive.schema.json.md) | x86decomp COFF Archive Inspection | object | `5f5a43f1ce6ae1221df24107f7b9db057156731736ff4aad5c81c93a73abaab3` |
| [schemas/comdat-resolution.schema.json](schema-reference/schemas-comdat-resolution.schema.json.md) | COFF COMDAT resolution report | object | `01fd177dfa983202ca8770e7985aa623e166fd22c20fdecc1d3d37f9cbfe0aae` |
| [schemas/compiler-ground-truth-comparison.schema.json](schema-reference/schemas-compiler-ground-truth-comparison.schema.json.md) | Compiler/version ground-truth corpus comparison | object | `1ea55d940c62d4e60487f74ac4d9756e4ff4c7cb2c39c9dd629b1d4150646dfb` |
| [schemas/compiler-ground-truth.schema.json](schema-reference/schemas-compiler-ground-truth.schema.json.md) | Compiler ground-truth corpus manifest | object | `1f8d15358ce71168a0f7c4d61ba7ad9db1ef12b534b27444bdda1f77f96392a2` |
| [schemas/compiler-lab.schema.json](schema-reference/schemas-compiler-lab.schema.json.md) | Compiler experiment matrix | object | `37bc55f945daffc31844a78c2b4788191f501589303826a6cee207c5c4717506` |
| [schemas/compiler-profile.schema.json](schema-reference/schemas-compiler-profile.schema.json.md) | x86decomp compiler profile | object | `6903f160acf5cfb8329567efbdd2da82b9f171705971e9842afcae21a4a4f844` |
| [schemas/convergence-report.schema.json](schema-reference/schemas-convergence-report.schema.json.md) | urn:x86decomp:schema:convergence-report:1 | object | `ace195921a16f72366e2920e6e2ce4e464b51f665d4d12ff5117dbea49119185` |
| [schemas/cpp-recovery.schema.json](schema-reference/schemas-cpp-recovery.schema.json.md) | urn:x86decomp:schema:cpp-recovery:1 | object | `9eda5eb04cdd6404ed82077dab0b1f2668f3682b33f864fec3c7348439515d8a` |
| [schemas/decompme-packet.schema.json](schema-reference/schemas-decompme-packet.schema.json.md) | Local decomp.me-style function packet | object | `65cd0a5d3197e6de85ec46c8eb372a387102192d9341ee252a7f40ca83b91704` |
| [schemas/dependency-audit.schema.json](schema-reference/schemas-dependency-audit.schema.json.md) | x86decomp dependency vulnerability audit | object | `2eef4097789050d846536b406ccd7b9e8e639467bdf1ca530045fcc6050c8ee2` |
| [schemas/drcov-trace.schema.json](schema-reference/schemas-drcov-trace.schema.json.md) | Normalized DynamoRIO drcov text trace | object | `aedc8ab92612b4b325552d3de98da9d04e2e4c3aa2bb2ab319e20f85616cfe7f` |
| [schemas/dynamic-report.schema.json](schema-reference/schemas-dynamic-report.schema.json.md) | Bounded Unicorn differential report | object | `1af7c179c9d4fedbf542c098eab126d556fc8345a464176d211640f391effce0` |
| [schemas/evidence.schema.json](schema-reference/schemas-evidence.schema.json.md) | x86decomp evidence item | object | `5c5199ae9f480dbbb28eb3ebd889a53a46c08535cabf346d3a0bf04f4a4aa7bd` |
| [schemas/exe-diff-report.schema.json](schema-reference/schemas-exe-diff-report.schema.json.md) | PE function to COFF symbol comparison | object | `3bfb70b7158750523074f638ff5955cc519097a37543f9f097909f4576373b50` |
| [schemas/execution-harness-generated.schema.json](schema-reference/schemas-execution-harness-generated.schema.json.md) | urn:x86decomp:schema:execution-harness-generated:1 | object | `7ba43bfcb6b5b8736d784112af5531e1a890630e379eb2c345f15442c18a2c6d` |
| [schemas/execution-harness.schema.json](schema-reference/schemas-execution-harness.schema.json.md) | Bounded Unicorn execution harness | object | `2ec27dc202dcf7ab923c646c71e30769b0c18527aaf2e6ba44e70536574e4f68` |
| [schemas/function-workflow.schema.json](schema-reference/schemas-function-workflow.schema.json.md) | x86decomp per-function workflow | object | `972f7c4fef555a4653a57cad04f1dedb186cc70a6c59de7e674645b30c240351` |
| [schemas/function.schema.json](schema-reference/schemas-function.schema.json.md) | x86decomp Ghidra function artifact (schema versions 1 and 2) | object | `00c65be77cc237df28a9112019c07019f88f38072ceb329907adc88bcfc34704` |
| [schemas/governance/campaign.schema.json](schema-reference/schemas-governance-campaign.schema.json.md) | campaign | object | `df027ea63ef0017b5a9ecae133a21ab7fa13f68e00545529e8606b5f39d1f854` |
| [schemas/governance/candidate.schema.json](schema-reference/schemas-governance-candidate.schema.json.md) | candidate | object | `db23f94af8b37ebdfff2798c271a0ef02ea9d77aae83fa8c8ebdab3d2f55ad67` |
| [schemas/governance/changeset.schema.json](schema-reference/schemas-governance-changeset.schema.json.md) | changeset manifest | object | `6788b90056dbf46cdaaaab292bdc6c3102e20ff47c790f131b47c15d08f5cbd3` |
| [schemas/governance/consensus.schema.json](schema-reference/schemas-governance-consensus.schema.json.md) | consensus observation | object | `f3edcf4a5962701cde7a0f4f483a19d49e9f5beea5e6a4dc3c643c9970ee9c43` |
| [schemas/governance/counterexample.schema.json](schema-reference/schemas-governance-counterexample.schema.json.md) | counterexample | object | `0e2b706ed1bf89e6c07a483dd171dbb23fbac4f67c87ef1df16be6c2fe50d19c` |
| [schemas/governance/family.schema.json](schema-reference/schemas-governance-family.schema.json.md) | binary family report | object | `cd02347eefe68396b21d7ec5af6ef9c1554dd4715e962e302ece657cb0b851ed` |
| [schemas/governance/hypothesis.schema.json](schema-reference/schemas-governance-hypothesis.schema.json.md) | hypothesis | object | `1013bee5c093d4cf0e619dbcdc52a2b2ff79c0b768da9c699ad0483bfc283a83` |
| [schemas/governance/knowledge-graph.schema.json](schema-reference/schemas-governance-knowledge-graph.schema.json.md) | knowledge graph impact | object | `d1bc76932c0264e763eb4cdb47d46397ddf00bb57e1c240371ef42049631db28` |
| [schemas/governance/plugin.schema.json](schema-reference/schemas-governance-plugin.schema.json.md) | plugin manifest | object | `1fb5e12f5c8eb5408dea6372c5442273b1694559dc9c09784bbca4309dbf5fd2` |
| [schemas/governance/proof-bundle.schema.json](schema-reference/schemas-governance-proof-bundle.schema.json.md) | proof bundle manifest | object | `b169fcd67f41318514ea5984fa5715cab569020f56547ccb58f93a98679090c0` |
| [schemas/governance/review.schema.json](schema-reference/schemas-governance-review.schema.json.md) | review item | object | `280cfe7963adcdcbbb3a1fde01b921cad82751d2240a4fcdaa9b9543db071bc2` |
| [schemas/governance/worker.schema.json](schema-reference/schemas-governance-worker.schema.json.md) | worker profile | object | `ca8f6768a4c7dfe89e80f2107c4bb43badde4d01d3ec6947ff001c9b207b403c` |
| [schemas/hybrid-project.schema.json](schema-reference/schemas-hybrid-project.schema.json.md) | Continuously buildable hybrid project | object | `c72692b4469f7ba92b2945968974d495371e2c0f03ad438c970418c3ce31d9b0` |
| [schemas/image-match-report.schema.json](schema-reference/schemas-image-match-report.schema.json.md) | Target-specific whole-image match report | object | `f81f81c2581b2941b9a3850aa2d296957e1d14de2ad3d8ee92839b34ccfadc23` |
| [schemas/image-profile.schema.json](schema-reference/schemas-image-profile.schema.json.md) | Target-specific PE image layout profile | object | `5916e3589fb77876a26861ccfea7dfbfbf4b9c55e92243ed66dae4270dad70d7` |
| [schemas/integration-report.schema.json](schema-reference/schemas-integration-report.schema.json.md) | Bounded integration comparison report | object | `4732a3a8f4038739f46c7b7b74b20999c68d9f637bac783a53b03eee91e91d1a` |
| [schemas/integration-scenarios.schema.json](schema-reference/schemas-integration-scenarios.schema.json.md) | Integration scenario manifest | object | `60799068b8df90e7d457415f6e08fa236a0620630ddab2641dec2ff8bac6e43e` |
| [schemas/linker-layout.schema.json](schema-reference/schemas-linker-layout.schema.json.md) | Linker layout reconstruction report | object | `a8faf6022c8b70e04c3375d47a480b9a811e72edd55ea7e0ec4e80a77a8ca934` |
| [schemas/linker-reconstruction-plan.schema.json](schema-reference/schemas-linker-reconstruction-plan.schema.json.md) | urn:x86decomp:schema:linker-reconstruction-plan:1 | object | `1d6fadf9737abed4d02cc90d3859898785edf62d3909c39fe893c8841c57f504` |
| [schemas/local-llm/candidate.schema.json](schema-reference/schemas-local-llm-candidate.schema.json.md) | Local LLM C proposal response | object | `cadff624248794b1841a55fd49f2f980658a442d046530c183ec0c89d44d99ab` |
| [schemas/local-llm/job.schema.json](schema-reference/schemas-local-llm-job.schema.json.md) | Local LLM C generation and byte-match job | object | `6ac68b5f4f22855154f8ec09e599c7caa3ce12d117fb125a0bae8e4dce0197a8` |
| [schemas/local-llm/profile.schema.json](schema-reference/schemas-local-llm-profile.schema.json.md) | Local LLM provider profile | object | `dc3ed501bada8be1896567c329fd550ad843059786ed07bbae6ef3063fdfe3ee` |
| [schemas/local-llm/report.schema.json](schema-reference/schemas-local-llm-report.schema.json.md) | Local LLM exact byte-match report | object | `d61c0308354431848f281d3c62cd32b39c9d61277492bee480a02276e5ad6ac0` |
| [schemas/mcp-mutation.schema.json](schema-reference/schemas-mcp-mutation.schema.json.md) | Evidence-gated MCP mutation | object | `64335798160269133e880d823f14de7f0cb4f2dafbf0c47526e24fb9fb16ea29` |
| [schemas/memory-event.schema.json](schema-reference/schemas-memory-event.schema.json.md) | x86decomp project memory event | object | `d2f38971ac7dda92dda0564bb77bb4858160b5a342476d36fe52238eb5289e74` |
| [schemas/msvc-metadata.schema.json](schema-reference/schemas-msvc-metadata.schema.json.md) | Bounded MSVC metadata analysis report | object | `84d0b6bc880ab47954f951a4eed4db317c14ee33ed5cdbe0ee098ce61c1d6273` |
| [schemas/native/boundary-finding.schema.json](schema-reference/schemas-native-boundary-finding.schema.json.md) | x86decomp boundary-finding | object | `58d723eee6c5c374f78dcac68a23be5d0b60c6f002c3e8285d307eef496e74fc` |
| [schemas/native/candidate-manifest.schema.json](schema-reference/schemas-native-candidate-manifest.schema.json.md) | x86decomp candidate-manifest | object | `d3bad2e693b4b7d6e1c230d9e03ff775298273523c8b562d3b78400c13313029` |
| [schemas/native/function-match.schema.json](schema-reference/schemas-native-function-match.schema.json.md) | x86decomp function-match | object | `e598ca859f33c96b62fe8dac7fcf78ec77b53e4b8f178b9f19e1f288e2725cd1` |
| [schemas/native/function-slot.schema.json](schema-reference/schemas-native-function-slot.schema.json.md) | x86decomp function-slot | object | `61bb10550455068b1c58073dfb30939aea8095cefbd775abab4d044efe9a2914` |
| [schemas/native/hybrid-composition.schema.json](schema-reference/schemas-native-hybrid-composition.schema.json.md) | x86decomp hybrid-composition | object | `feb6682c1aa1ed0a3bc3c06230ce27f006641d96238050151ad22584eb02cb9d` |
| [schemas/native/loop-run.schema.json](schema-reference/schemas-native-loop-run.schema.json.md) | x86decomp loop-run | object | `de5d1a277444c3ea53ae0c4860d1a7978b478893fb893cf4c1ba1fca4a11b038` |
| [schemas/native/match-run.schema.json](schema-reference/schemas-native-match-run.schema.json.md) | x86decomp match-run | object | `7afbfb42c5995ff375a050c93bb119ce50f2a761220c610f2c1622f082c23fb5` |
| [schemas/native/patch-plan.schema.json](schema-reference/schemas-native-patch-plan.schema.json.md) | x86decomp patch-plan | object | `90a1f06eaa3f6a3d6b235cc0439c57fec0187006ccc4c01b8fbb76571bb31958` |
| [schemas/native/runtime-validation.schema.json](schema-reference/schemas-native-runtime-validation.schema.json.md) | x86decomp runtime-validation | object | `f314d1ae2b72314a6ebf6c6d2905a8eb2f314498f256f567e01ae08622da90f3` |
| [schemas/native/section-export.schema.json](schema-reference/schemas-native-section-export.schema.json.md) | x86decomp section-export | object | `121ed87fe1b51a248b230acafd9780b96e74e01c72e9cba7fcd20fbb466eb317` |
| [schemas/native/staging-symbol.schema.json](schema-reference/schemas-native-staging-symbol.schema.json.md) | x86decomp staging-symbol | object | `44b3ce02db0758435f6a230a9ad37bd00c3a6308bf71761836050e5c90c6c4d0` |
| [schemas/native/windows-tool.schema.json](schema-reference/schemas-native-windows-tool.schema.json.md) | x86decomp windows-tool | object | `22af6f0e3266250f1c741e95e231c4ee3d62fd3944e0000e6ab6e652089906e0` |
| [schemas/objdiff-manifest.schema.json](schema-reference/schemas-objdiff-manifest.schema.json.md) | objdiff external invocation manifest | object | `2fe8f65399749687b2890cc643f474c0b8de221e90f6ae5013ce0d8b46590360` |
| [schemas/pdb.schema.json](schema-reference/schemas-pdb.schema.json.md) | x86decomp bounded PDB/MSF inventory | object | `850bbf885fa040ac4601dc4d93c2fb4b3afda1dd86612a0d8866a34bacf07008` |
| [schemas/pipeline.schema.json](schema-reference/schemas-pipeline.schema.json.md) | urn:x86decomp:schema:pipeline:1 | object | `a9b7b790fb6c877370a4c61ecbdf0f92eac13d9aba389cc0ab8d8723aee92ca6` |
| [schemas/project-template.schema.json](schema-reference/schemas-project-template.schema.json.md) | Grounded x86decomp project-template contract | object | `1bf881ea328d3a6c00d727c0cbe1e47763726e70362a085354178add994458ce` |
| [schemas/project.schema.json](schema-reference/schemas-project.schema.json.md) | x86decomp project (schema versions 1, 2, and 3) | object | `4ab19d9064e8d249fdd545d1fa183920902d6afbe647d004ddd571a208295b0b` |
| [schemas/reconstruction/abi-contract.schema.json](schema-reference/schemas-reconstruction-abi-contract.schema.json.md) | ABI contract | object | `d2286943caed629e873a4107fcceb21f18b0759cfebd17b71f761af14e68e016` |
| [schemas/reconstruction/build.schema.json](schema-reference/schemas-reconstruction-build.schema.json.md) | Build reconstruction contract | object | `647d938812825abaa84206de119ebc4a18d8fad70a4f50121f990a4af2571dd0` |
| [schemas/reconstruction/capsule.schema.json](schema-reference/schemas-reconstruction-capsule.schema.json.md) | Reconstruction capsule manifest | object | `c042105ec33667d5f67b4bd36311aa9c2989f97ef6c6c57cd5d0e634ada1437c` |
| [schemas/reconstruction/compatibility-shim.schema.json](schema-reference/schemas-reconstruction-compatibility-shim.schema.json.md) | Explicit compatibility shim | object | `714bcc499ffc2db676e163a5886ce9ca4fca7df0b2382a94488c6dfc5a782926` |
| [schemas/reconstruction/generated-test.schema.json](schema-reference/schemas-reconstruction-generated-test.schema.json.md) | Generated regression test | object | `8e99342ae82922d0c5c17c41e857074a5a2cec9b1269e23572aea09b5715a7b5` |
| [schemas/reconstruction/header.schema.json](schema-reference/schemas-reconstruction-header.schema.json.md) | Recovered header contract | object | `c878f851e64b11db9e0dad34785d5ef3ba3baa753e380af72f554fe44529a850` |
| [schemas/reconstruction/library-match.schema.json](schema-reference/schemas-reconstruction-library-match.schema.json.md) | Static library recognition candidate | object | `cdf8967118c99e0f1d224829f1e3067a2b9db50f31ca945db68a3cec61b0f36e` |
| [schemas/reconstruction/module.schema.json](schema-reference/schemas-reconstruction-module.schema.json.md) | Recovered module hypothesis | object | `4aa87665cf31d30d9395bff7fb9388c9bd55257718808572669a874922436a4f` |
| [schemas/reconstruction/security-finding.schema.json](schema-reference/schemas-reconstruction-security-finding.schema.json.md) | Security finding | object | `9a4f8a220e2e2d1d7dbc8116968bf2752d57a5725e18673faf59a192ace1826e` |
| [schemas/reconstruction/semantic-changeset.schema.json](schema-reference/schemas-reconstruction-semantic-changeset.schema.json.md) | Semantic changeset | object | `2cc66c0075ba39a54d86a20ca3705d4656ce90e922ce5a8c0b9357db1bc27b28` |
| [schemas/reconstruction/source-provenance.schema.json](schema-reference/schemas-reconstruction-source-provenance.schema.json.md) | Source provenance record | object | `d80a00434549c01f14f1afa7c43cb65b9eb653808b42fb5fa10f25b1d7ac1b0c` |
| [schemas/reconstruction/translation-unit.schema.json](schema-reference/schemas-reconstruction-translation-unit.schema.json.md) | Translation unit hypothesis | object | `ea17fb7bfec69c8e9e3eb5d14179194acece94ba90d5e0ad76c5f3e653dca642` |
| [schemas/release-gate.schema.json](schema-reference/schemas-release-gate.schema.json.md) | urn:x86decomp:schema:release-gate:1 | object | `50e1f5a6cb46b67f833c881a7f025be5c7c047c1f23c3607608488afe17256cd` |
| [schemas/relink-manifest.schema.json](schema-reference/schemas-relink-manifest.schema.json.md) | Manifest-driven full relink | object | `ca2b77b7be6b562589e841753a9afa8c6baf1fc7cf8c703409c90fc56507e890` |
| [schemas/reproduction.schema.json](schema-reference/schemas-reproduction.schema.json.md) | urn:x86decomp:schema:reproduction:1 | object | `aea350be271c7795406a2dd55096775e9d0b531215e05f43b75a9c6b5bd98281` |
| [schemas/security-audit.schema.json](schema-reference/schemas-security-audit.schema.json.md) | urn:x86decomp:schema:security-audit:1 | object | `d62a14bd5c6d796dd52aee929ccfdf8e1265f825167070c8ffd680321a00b637` |
| [schemas/symbolic-memory-harness.schema.json](schema-reference/schemas-symbolic-memory-harness.schema.json.md) | Bounded symbolic memory and alias harness | object | `e7ce53b843c172758fc086503e040cd1c60a3836f528b2c8396a7e77ab7c200a` |
| [schemas/symbolic-memory-report.schema.json](schema-reference/schemas-symbolic-memory-report.schema.json.md) | Bounded angr symbolic memory-alias comparison | object | `5e17dedb1bedf6581662f4cced118e40b8075957a161daea2abfab778d0298ba` |
| [schemas/symbolic-report.schema.json](schema-reference/schemas-symbolic-report.schema.json.md) | Bounded symbolic comparison report | object | `cc596ec7c42bc74e7810dbf52bf50cba2d17375e9438f0a3fcbb3dae67a88e29` |
| [schemas/synthetic-corpus.schema.json](schema-reference/schemas-synthetic-corpus.schema.json.md) | Deterministic synthetic source corpus | object | `3c05d2c0a766021805afdd306d6a08068af6a24cdb0adb82fb3eca4d0f1d7c7d` |
| [schemas/target-decisions.schema.json](schema-reference/schemas-target-decisions.schema.json.md) | Operator-confirmed target decisions | object | `647192549c5e079a02e597648a0d3d2ade5078866f869b7e0da34324b5976ed6` |
| [schemas/target-pack.schema.json](schema-reference/schemas-target-pack.schema.json.md) | urn:x86decomp:schema:target-pack:1 | object | `867b89f3738ff1310340d078c5ae530f0087277e96cd00106fa1275cd0bcc954` |
| [schemas/test-bundle-report.schema.json](schema-reference/schemas-test-bundle-report.schema.json.md) | x86decomp Static Test Bundle Report | object | `482f5b618cd46eb5e815392f2655bb9fe4f3683e1f5122b8f7ab0ea69f8a2820` |
| [schemas/test-bundle.schema.json](schema-reference/schemas-test-bundle.schema.json.md) | x86decomp Authorized Static Test Bundle | object | `398d162a3ccc9e3bd1e984af67efbfaf12a840f4013b406c0cf8d150f490deab` |
| [schemas/type-constraint.schema.json](schema-reference/schemas-type-constraint.schema.json.md) | Type/ABI constraint record | object | `f98328b457deccc685ea8be764507320d5ff94deddb366e47c5018a678baa59d` |
| [schemas/verification.schema.json](schema-reference/schemas-verification.schema.json.md) | x86decomp byte verification report | object | `a70e3422e6b0bec967695257c7b66d44f17a0cfe3f15d99799eb1c038ccb7fa0` |
| [schemas/work-task.schema.json](schema-reference/schemas-work-task.schema.json.md) | Validator-gated work item | object | `36794b2e24e785918a28d8bd7f5fedd100c090ed64030c71eefa0a8c933b92c9` |
| [schemas/worker-report.schema.json](schema-reference/schemas-worker-report.schema.json.md) | urn:x86decomp:schema:worker-report:1 | object | `f4fee8d629c5e963519a4f5ab25c4bb0856592421ee218fe7d047b5ebe089b3c` |
