---
title: Complete packaged-source coverage
description: Complete manifest-backed source coverage
original_path: source-coverage.html
---

<a id="ghidra-exportfunctionartifacts-java"></a>
<a id="ghidra-exportprojectmanifest-java"></a>
<a id="ghidra-queryanalysis-java"></a>

Section: Manifest-backed completeness

# Complete packaged-source coverage

Every file authenticated by the root 0.7.4 source manifest is accounted for below. The standalone test-suite manifest is independently rechecked as a 60-file subset contract.

| Value | Meaning |
| --- | --- |
| 411 | root manifest files |
| 60 | test-suite manifest files |
| 137 | Python modules documented |
| 93 | schemas documented |

> **Source identity.** Release bundle SHA-256: `7fae1658b0eccb980d54a3c80a5f91a6cf09f8eb4e2eb4ebcae3bd477f6d36e8`. Deterministic source ZIP SHA-256: `f6d5f97454b405891dc89ad9329372e2005b91ea9ba0d8116df987023f834d8e`. Both match `release-verification.json`.

## File categories

| Category | Files |
| --- | --- |
| Ghidra script | 3 |
| JSON Schema | 93 |
| automation workflow | 1 |
| documentation or architecture text | 36 |
| example artifact | 20 |
| package/build metadata | 63 |
| test source | 51 |
| toolkit Python module | 108 |
| verification Python module | 29 |
| verification/build script | 7 |

## Ghidra scripts

The three scripts and their usage summaries below are taken from their source headers.

`ExportFunctionArtifacts.java`

Export per-function artifacts without flattening discontiguous bodies. Usage: -postScript ExportFunctionArtifacts.java <output-dir> <all|current|addr,name,...> @category X86Decomp

SHA-256: `2c1a21482d49c2bdd2fcf86e6df9d3c401fc4e5e4c4a36ea358aa9e2ddf6ca49`

`ExportProjectManifest.java`

Export canonical program, section, function, symbol, and metric manifests. Usage: -postScript ExportProjectManifest.java <output-dir> @category X86Decomp

SHA-256: `136d6c725b1dcf122e4cc650f2a008c2dbbaf5322c3e943657074cb3c73d2653`

`QueryAnalysis.java`

Read-only Ghidra analysis queries. Commands: QueryAnalysis.java refs <address> [all|read|write|call] QueryAnalysis.java disasm <start> <end-exclusive> QueryAnalysis.java function <address-or-name> QueryAnalysis.java callers <address-or-name> @category X86Decomp

SHA-256: `5f6b639103a6d104f63db3c1d6cf070d486a461d3a2be9db83f09bcd5d4a6150`

## All root-manifest files

| Path | Category | Documentation mapping | Bytes | SHA-256 |
| --- | --- | --- | --- | --- |
| `.github/workflows/ci.yml` | automation workflow | listed on this page | 2906 | `99a936711b46f589c3af298cb9f8be9a258646b0f56fd5aa530049c7338d6bb6` |
| `.gitignore` | package/build metadata | listed on this page | 270 | `eb154655b2dbbff2977bbd627126c84338f553da429720d464adf7e99dc52c26` |
| `AGENTS.md` | documentation or architecture text | listed on this page | 2300 | `288531b0742b8a0eddc07f57531c53c15647d6e6ede303386e2a41171976782c` |
| `CHANGELOG.md` | documentation or architecture text | listed on this page | 1266 | `449fd66ae2a59087535c7ed16820006be65d0ea1d2c20e241149d864a13c8b7f` |
| `FEATURE_PARITY.md` | documentation or architecture text | listed on this page | 1935 | `793ace5467474a1a86384d22a971cbd5ce3c7b104c2cf4347a79f79392687100` |
| `LICENSE` | package/build metadata | listed on this page | 428 | `ac2e979d38c247879e05243433cf891e77f87f71cb39bc24f6efe81ac3e38df3` |
| `MANIFEST.in` | package/build metadata | listed on this page | 835 | `69db866c1421555409f490a901506cf31957aa7944eb920565f0602653783f22` |
| `Makefile` | package/build metadata | listed on this page | 1232 | `d034035386a8ab7bea1c7e4348d3608367b3ab890c0711a488d2bdbdb48806f7` |
| `PROJECT_MEMORY.md` | documentation or architecture text | listed on this page | 1316 | `e9dc688e800b2bbf1c98cea1542a70ac6e9bce0299aeb21d985937f57177a713` |
| `README.md` | documentation or architecture text | listed on this page | 2995 | `a3bf9ff890341f5a1238d2044de0b49ad5ba0e346a6847b8e0e27b409265a61c` |
| `SECURITY.md` | documentation or architecture text | listed on this page | 1084 | `5db99bb8dc8dfac71cbfcc7964bd461542548a59135a78578b82550a698f3480` |
| `VERIFICATION.md` | documentation or architecture text | listed on this page | 1292 | `81b325c9f55a2f696f5eeaa591a33aff97a78a8203442d7c50d9d703d9b078c5` |
| `corpus/ground_truth_sources/aliasing.c` | package/build metadata | listed on this page | 105 | `09a93c1038059384920be8ed617f196950b3b935fa4e7ecdcccd4b38215f222c` |
| `corpus/ground_truth_sources/arithmetic.c` | package/build metadata | listed on this page | 105 | `1a39b20e36efc0d23c5570152a1db30922527835bfc82ddf4b629980c916326e` |
| `corpus/ground_truth_sources/bitfields.c` | package/build metadata | listed on this page | 313 | `44c9a66d27e87a270af05fdb87d82d87512b70fe72600df0bc89f4e091b5a7dd` |
| `corpus/ground_truth_sources/branches.c` | package/build metadata | listed on this page | 125 | `0dcc84cf6d38aa0a3e90a66bd349f349d504cd2dc0160db16933466c56aa99bb` |
| `corpus/ground_truth_sources/calling_conventions.c` | package/build metadata | listed on this page | 343 | `cfb331698f9ccdb113849a7c535a500ee6631a46a716be1d3791e49f9c1e69b3` |
| `corpus/ground_truth_sources/classes.cpp` | package/build metadata | listed on this page | 274 | `d04c86180d9424ea91914dc7b73d93b4b3da432d7a26d8d801ff9d5718701521` |
| `corpus/ground_truth_sources/eh_multiple.cpp` | package/build metadata | listed on this page | 471 | `7b3cc0e687132f70957e55dbbaa5c479d6a4864fde0e11cb49df0c600d6f2665` |
| `corpus/ground_truth_sources/exceptions.cpp` | package/build metadata | listed on this page | 156 | `fd15c6bd23f39262a9aa02f94f02210dacab53a2a5d358aae415bba2c329394e` |
| `corpus/ground_truth_sources/floating_point.c` | package/build metadata | listed on this page | 195 | `ff00c63ae76817932bdd0b4a5b0a0c8bc661e03314889d1eef404e580279bb89` |
| `corpus/ground_truth_sources/globals.c` | package/build metadata | listed on this page | 100 | `e4fbe6bc2a51161e651a23264f5de4e90d052b2e9efcbcea1c1ff76a748528c4` |
| `corpus/ground_truth_sources/indirect_calls.c` | package/build metadata | listed on this page | 204 | `b9b6dc58d6912bf8a54c46868a5a61b321447c9826660dfb29f76f741b21b92e` |
| `corpus/ground_truth_sources/loops.c` | package/build metadata | listed on this page | 242 | `d929c2eb356d9e45d27aa9a9e9929d1ce3fad324d8843d7e53e4dbe7dabe9262` |
| `corpus/ground_truth_sources/member_pointers.cpp` | package/build metadata | listed on this page | 299 | `8e84a7254ebeda7ec4db40335350606cf26227868e20be7db4f4382cdd3e9f69` |
| `corpus/ground_truth_sources/multiple_inheritance.cpp` | package/build metadata | listed on this page | 272 | `2fc99918de8375a035774b6cff12866defb77d2095bf1a6005b6419c4afc4410` |
| `corpus/ground_truth_sources/static_initializers.cpp` | package/build metadata | listed on this page | 143 | `5566d58941846d63fafa6e6047f5f0a70dd19ff484aea58f1eac88cfa1c3156c` |
| `corpus/ground_truth_sources/structs.c` | package/build metadata | listed on this page | 124 | `0b29f69d01886989d3d34fb430acb259ca55c604b8b59c968e5d341972102280` |
| `corpus/ground_truth_sources/switch_dense.c` | package/build metadata | listed on this page | 248 | `2a696a875c034a89e16a9b28359f6603942c536954321bc7403a9b780d24546f` |
| `corpus/ground_truth_sources/tail_calls.c` | package/build metadata | listed on this page | 140 | `874edb70e2470cafdd6bed6a7a05519da95c926d1b0777622d1fba726194ddb3` |
| `corpus/ground_truth_sources/templates.cpp` | package/build metadata | listed on this page | 409 | `cd18fc097a4bbbacacff6685edb8c5e6a0dfe7d8e27a68eb0b0febad6508194b` |
| `corpus/ground_truth_sources/tls.c` | package/build metadata | listed on this page | 240 | `9f917229ae42021f4045f2f56af5ac3116987dc442e304c1b9b6b441200ba54b` |
| `corpus/ground_truth_sources/unions.c` | package/build metadata | listed on this page | 192 | `2906ac1f944da7f6020756df9f20451048f8e2ed81ed5ac6ea06554afe1c7f60` |
| `corpus/ground_truth_sources/varargs.c` | package/build metadata | listed on this page | 244 | `3326edfa00e59cd41f5409c8ef01d1d5b96c0e1a13471972a2a107725032cdbb` |
| `corpus/ground_truth_sources/vectorizable.c` | package/build metadata | listed on this page | 259 | `4e71d283a0479bd5264da8f235bdb4f434a1b841289d9eac335c8b997be10f43` |
| `corpus/ground_truth_sources/virtual_inheritance.cpp` | package/build metadata | listed on this page | 441 | `c8e83579cd4d6159e716c23270110d997349e3b1a609bf1d50c0b93a2e64d1d2` |
| `docs/ARCHITECTURE_MAP.md` | documentation or architecture text | listed on this page | 1695 | `49ca942abe3f9cd3857f7fd63de7cadba7dba34b8c40c99a18cac3a8e1e7443c` |
| `docs/ARCHITECTURE_MAP_ASCII.txt` | documentation or architecture text | listed on this page | 2670 | `92dbd066ae1990a28fe95c2f4a6c59320dc55c5855860278954a8bf3e66b1b67` |
| `docs/architecture.md` | documentation or architecture text | listed on this page | 1216 | `28e4ffa8abc315876febd620b732bc0fdb7ea5f73303d37a32642bbbcb7c3686` |
| `docs/build-and-verification.md` | documentation or architecture text | listed on this page | 1063 | `68e9732da81f372492c7b641cca5099c8fec432c2d23db7566b3586657acdd4c` |
| `docs/contracts.md` | documentation or architecture text | listed on this page | 4497 | `ca03911160dff537c0320208dc20b8dff7d8b44617d2344f40cedd72f28707cd` |
| `docs/evidence-and-claims.md` | documentation or architecture text | listed on this page | 2188 | `a573ac934a840cec2976052600e8631ce736442ac86650cce2116d0011a28f16` |
| `docs/ghidra-integration.md` | documentation or architecture text | listed on this page | 1690 | `c60e3ad7b722d1063d4a11e59e5225ddc5e1468781917992db958aba7387006a` |
| `docs/guardrails.md` | documentation or architecture text | listed on this page | 1915 | `39701950478ea6d1fc9fcb8861895725dd75bdaff41803b98a971758d397aec0` |
| `docs/operations-and-recovery.md` | documentation or architecture text | listed on this page | 4095 | `7430e41f4663a97f752ccc7a8686c1a39693605ea71ad88725c9fa33fe755238` |
| `docs/project-memory.md` | documentation or architecture text | listed on this page | 1179 | `9053e590e5f0394ff3d07534b017e51b593f5d71d225d2b6e71d70dfd51284ea` |
| `docs/roadmap.md` | documentation or architecture text | listed on this page | 379 | `910ad2690ff63134b2e0a0f6de75d2eb480dfda333aadd61d7ff880c078c27a5` |
| `docs/source-basis.md` | documentation or architecture text | listed on this page | 1097 | `b0950b1b47308b283028c141a84c8cbf41f377d68b269d418c239edd7e8e9ee4` |
| `docs/supported-scope.md` | documentation or architecture text | listed on this page | 536 | `c0e6743ef1b73e262c786192ba103189b6f63f27c768b9b82ee3807946976ae8` |
| `docs/target-packs-and-templates.md` | documentation or architecture text | listed on this page | 3822 | `7e65033dff4a1d532861775161d621e8f73ec238363b43fce2b7101a3ba6a2d0` |
| `docs/test-bundle.md` | documentation or architecture text | listed on this page | 4551 | `a46690243ada69526ce92db7b4f667a8aea677db98a286c5a56ff7b18af9f113` |
| `examples/abi/stdcall-two-ints.json` | example artifact | listed on this page | 275 | `f2c7a723de83de7169612e1cdc305a4bd8779e9ad82c7ff3a2ce90d400ac3ace` |
| `examples/benchmarks/bounded-demo.json` | example artifact | listed on this page | 1153 | `980ad9dc8352019f4dca1f06e25a8654ec87248befc178c35490ecc3d129a51a` |
| `examples/compiler-profiles/gcc-i686-object.json` | example artifact | listed on this page | 649 | `dc5dee89f0aff786350b51e24e7b77067de8d2a0a332fc6e880041a330729572` |
| `examples/contracts/command-surface.json` | example artifact | listed on this page | 6963 | `5b613f3e04e659d57339f29f404c03c10967df57d036d6f0feeaa09c3fe48e45` |
| `examples/contracts/public-surface.json` | example artifact | listed on this page | 34407 | `1d197cda0d1172a2456e3cd5988435f9eaac137fcfe3f74b1183320b3a0fc9a8` |
| `examples/integration/bounded-demo.json` | example artifact | listed on this page | 891 | `e1b589e23a5fa0a7c1310c69760ef7729fa912c2a5584985a7cbb487f57eab26` |
| `examples/integration/candidate.py` | example artifact | listed on this page | 160 | `fdec1c8156f57d6ba8a11f898a846634783644a8c8aaaabaa98854aa5adb1bd4` |
| `examples/integration/target.py` | example artifact | listed on this page | 160 | `fdec1c8156f57d6ba8a11f898a846634783644a8c8aaaabaa98854aa5adb1bd4` |
| `examples/labs/gcc-optimization-matrix.json` | example artifact | listed on this page | 376 | `f4f19ea47da16374312c4eff46d2914e3d0c425a229f92a95b2fe99221acbd78` |
| `examples/release/release-gate-policy.json` | example artifact | listed on this page | 425 | `7ad41612264a71c3bd1d1ea44b5ad0f9145710ef926492975796dd9264948026` |
| `examples/release/target-decisions.json` | example artifact | listed on this page | 351 | `91b5bfcd613ac3d76fc020e5bb415d0ae11594886c6cac4317cc06e7ea5df1cb` |
| `examples/relink/lld-link-x64.json` | example artifact | listed on this page | 342 | `6addc382de2d64d223f4e24e47207b5741d2583d1717f4aec04107123a6013ef` |
| `examples/sample_source/add.c` | example artifact | listed on this page | 58 | `860aaedc4520b18df5ce99de71a36487eb333dcdb09f65fce222677c8fe8cd97` |
| `examples/symbolic/symbolic-alias-harness.json` | example artifact | listed on this page | 532 | `e5bbc6d9470e269f41051e95a444a9218f9919140bc74070dd223caf4eb7c130` |
| `examples/test-bundle/x86decomp-test-bundle.json` | example artifact | listed on this page | 593 | `6d88af2c016e6e88a5ba66fab7c88c9d7b56f70c1f5e71d2cb494aab69da6a68` |
| `examples/validators/add_stack_candidate.bin` | example artifact | listed on this page | 9 | `6d1e1d30f2068501de61e0022c4352fda2a7650f29eb96f01ad04fa160305e21` |
| `examples/validators/add_stack_harness.json` | example artifact | listed on this page | 346 | `beeaeeecbe1136402ef0b3c1c3f799256a2613f87bb9457f97b71fe605ec0d0f` |
| `examples/validators/add_stack_target.bin` | example artifact | listed on this page | 9 | `6d1e1d30f2068501de61e0022c4352fda2a7650f29eb96f01ad04fa160305e21` |
| `examples/validators/sub_stack_candidate.bin` | example artifact | listed on this page | 9 | `fe10777e0899cf9cabd2bc8dc3367d711f6af675bdda9c5e28144539792f922f` |
| `ghidra_scripts/ExportFunctionArtifacts.java` | Ghidra script | [Ghidra script details](#ghidra-exportfunctionartifacts-java) | 24555 | `2c1a21482d49c2bdd2fcf86e6df9d3c401fc4e5e4c4a36ea358aa9e2ddf6ca49` |
| `ghidra_scripts/ExportProjectManifest.java` | Ghidra script | [Ghidra script details](#ghidra-exportprojectmanifest-java) | 15263 | `136d6c725b1dcf122e4cc650f2a008c2dbbaf5322c3e943657074cb3c73d2653` |
| `ghidra_scripts/QueryAnalysis.java` | Ghidra script | [Ghidra script details](#ghidra-queryanalysis-java) | 8571 | `5f6b639103a6d104f63db3c1d6cf070d486a461d3a2be9db83f09bcd5d4a6150` |
| `pyproject.toml` | package/build metadata | listed on this page | 1495 | `9206b2902d417f2b7d892cb56490cb14fedd8958e6f2236c146449ad5d46f566` |
| `schemas/abi-contract.schema.json` | JSON Schema | [schema reference](schemas.md#schema-abi-contract-schema-json) | 919 | `536e89f5ab760329f3799138b17c8a321170fc1fc729528d97b7f75d4af96c76` |
| `schemas/assembly/asm-function.schema.json` | JSON Schema | [schema reference](schemas.md#schema-assembly-asm-function-schema-json) | 1283 | `9ae31159426d4b49aa320db1e33a5d38450aaffcb33f5b5329aed4b8819c7fea` |
| `schemas/assembly/asm-run.schema.json` | JSON Schema | [schema reference](schemas.md#schema-assembly-asm-run-schema-json) | 580 | `50c7a6ba318c9380e5ca9ee78e4f8183f9db66b55cbd55071aecd094a86e339f` |
| `schemas/assembly/relocation-resolution.schema.json` | JSON Schema | [schema reference](schemas.md#schema-assembly-relocation-resolution-schema-json) | 1135 | `435ffaa5de3c015c366f7f16c8c258753e8490530fe81a4d4f00b27e024d77a4` |
| `schemas/assembly/roundtrip-report.schema.json` | JSON Schema | [schema reference](schemas.md#schema-assembly-roundtrip-report-schema-json) | 940 | `099b5806f963045b2a3f440dd0c25fe7a1286fe9e71fb5d6e0979f9fb4c1ec26` |
| `schemas/assembly/symbol-map.schema.json` | JSON Schema | [schema reference](schemas.md#schema-assembly-symbol-map-schema-json) | 925 | `e46212d20e9eed2d774dffd1cf2bc62aca637a2025302761a86117430f42f25c` |
| `schemas/benchmark-corpus.schema.json` | JSON Schema | [schema reference](schemas.md#schema-benchmark-corpus-schema-json) | 1048 | `0081dd4d038287641f14ccd228dd0e824bff8bd3745f8251aaa0a94c1c61e36c` |
| `schemas/claim.schema.json` | JSON Schema | [schema reference](schemas.md#schema-claim-schema-json) | 1305 | `362341adcb81640a7839c77d37d7203b911e7e79655be6c0ab4115f460609532` |
| `schemas/coff-archive.schema.json` | JSON Schema | [schema reference](schemas.md#schema-coff-archive-schema-json) | 2079 | `5f5a43f1ce6ae1221df24107f7b9db057156731736ff4aad5c81c93a73abaab3` |
| `schemas/comdat-resolution.schema.json` | JSON Schema | [schema reference](schemas.md#schema-comdat-resolution-schema-json) | 579 | `01fd177dfa983202ca8770e7985aa623e166fd22c20fdecc1d3d37f9cbfe0aae` |
| `schemas/compiler-ground-truth-comparison.schema.json` | JSON Schema | [schema reference](schemas.md#schema-compiler-ground-truth-comparison-schema-json) | 708 | `1ea55d940c62d4e60487f74ac4d9756e4ff4c7cb2c39c9dd629b1d4150646dfb` |
| `schemas/compiler-ground-truth.schema.json` | JSON Schema | [schema reference](schemas.md#schema-compiler-ground-truth-schema-json) | 1514 | `1f8d15358ce71168a0f7c4d61ba7ad9db1ef12b534b27444bdda1f77f96392a2` |
| `schemas/compiler-lab.schema.json` | JSON Schema | [schema reference](schemas.md#schema-compiler-lab-schema-json) | 2141 | `37bc55f945daffc31844a78c2b4788191f501589303826a6cee207c5c4717506` |
| `schemas/compiler-profile.schema.json` | JSON Schema | [schema reference](schemas.md#schema-compiler-profile-schema-json) | 1869 | `6903f160acf5cfb8329567efbdd2da82b9f171705971e9842afcae21a4a4f844` |
| `schemas/convergence-report.schema.json` | JSON Schema | [schema reference](schemas.md#schema-convergence-report-schema-json) | 1059 | `ace195921a16f72366e2920e6e2ce4e464b51f665d4d12ff5117dbea49119185` |
| `schemas/cpp-recovery.schema.json` | JSON Schema | [schema reference](schemas.md#schema-cpp-recovery-schema-json) | 932 | `9eda5eb04cdd6404ed82077dab0b1f2668f3682b33f864fec3c7348439515d8a` |
| `schemas/decompme-packet.schema.json` | JSON Schema | [schema reference](schemas.md#schema-decompme-packet-schema-json) | 1160 | `65cd0a5d3197e6de85ec46c8eb372a387102192d9341ee252a7f40ca83b91704` |
| `schemas/dependency-audit.schema.json` | JSON Schema | [schema reference](schemas.md#schema-dependency-audit-schema-json) | 1002 | `2eef4097789050d846536b406ccd7b9e8e639467bdf1ca530045fcc6050c8ee2` |
| `schemas/drcov-trace.schema.json` | JSON Schema | [schema reference](schemas.md#schema-drcov-trace-schema-json) | 1164 | `aedc8ab92612b4b325552d3de98da9d04e2e4c3aa2bb2ab319e20f85616cfe7f` |
| `schemas/dynamic-report.schema.json` | JSON Schema | [schema reference](schemas.md#schema-dynamic-report-schema-json) | 647 | `1af7c179c9d4fedbf542c098eab126d556fc8345a464176d211640f391effce0` |
| `schemas/evidence.schema.json` | JSON Schema | [schema reference](schemas.md#schema-evidence-schema-json) | 1243 | `5c5199ae9f480dbbb28eb3ebd889a53a46c08535cabf346d3a0bf04f4a4aa7bd` |
| `schemas/exe-diff-report.schema.json` | JSON Schema | [schema reference](schemas.md#schema-exe-diff-report-schema-json) | 1581 | `3bfb70b7158750523074f638ff5955cc519097a37543f9f097909f4576373b50` |
| `schemas/execution-harness-generated.schema.json` | JSON Schema | [schema reference](schemas.md#schema-execution-harness-generated-schema-json) | 1397 | `7ba43bfcb6b5b8736d784112af5531e1a890630e379eb2c345f15442c18a2c6d` |
| `schemas/execution-harness.schema.json` | JSON Schema | [schema reference](schemas.md#schema-execution-harness-schema-json) | 1621 | `2ec27dc202dcf7ab923c646c71e30769b0c18527aaf2e6ba44e70536574e4f68` |
| `schemas/function-workflow.schema.json` | JSON Schema | [schema reference](schemas.md#schema-function-workflow-schema-json) | 1451 | `972f7c4fef555a4653a57cad04f1dedb186cc70a6c59de7e674645b30c240351` |
| `schemas/function.schema.json` | JSON Schema | [schema reference](schemas.md#schema-function-schema-json) | 3676 | `00c65be77cc237df28a9112019c07019f88f38072ceb329907adc88bcfc34704` |
| `schemas/governance/campaign.schema.json` | JSON Schema | [schema reference](schemas.md#schema-governance-campaign-schema-json) | 896 | `df027ea63ef0017b5a9ecae133a21ab7fa13f68e00545529e8606b5f39d1f854` |
| `schemas/governance/candidate.schema.json` | JSON Schema | [schema reference](schemas.md#schema-governance-candidate-schema-json) | 716 | `db23f94af8b37ebdfff2798c271a0ef02ea9d77aae83fa8c8ebdab3d2f55ad67` |
| `schemas/governance/changeset.schema.json` | JSON Schema | [schema reference](schemas.md#schema-governance-changeset-schema-json) | 715 | `6788b90056dbf46cdaaaab292bdc6c3102e20ff47c790f131b47c15d08f5cbd3` |
| `schemas/governance/consensus.schema.json` | JSON Schema | [schema reference](schemas.md#schema-governance-consensus-schema-json) | 851 | `f3edcf4a5962701cde7a0f4f483a19d49e9f5beea5e6a4dc3c643c9970ee9c43` |
| `schemas/governance/counterexample.schema.json` | JSON Schema | [schema reference](schemas.md#schema-governance-counterexample-schema-json) | 757 | `0e2b706ed1bf89e6c07a483dd171dbb23fbac4f67c87ef1df16be6c2fe50d19c` |
| `schemas/governance/family.schema.json` | JSON Schema | [schema reference](schemas.md#schema-governance-family-schema-json) | 668 | `cd02347eefe68396b21d7ec5af6ef9c1554dd4715e962e302ece657cb0b851ed` |
| `schemas/governance/hypothesis.schema.json` | JSON Schema | [schema reference](schemas.md#schema-governance-hypothesis-schema-json) | 929 | `1013bee5c093d4cf0e619dbcdc52a2b2ff79c0b768da9c699ad0483bfc283a83` |
| `schemas/governance/knowledge-graph.schema.json` | JSON Schema | [schema reference](schemas.md#schema-governance-knowledge-graph-schema-json) | 697 | `d1bc76932c0264e763eb4cdb47d46397ddf00bb57e1c240371ef42049631db28` |
| `schemas/governance/plugin.schema.json` | JSON Schema | [schema reference](schemas.md#schema-governance-plugin-schema-json) | 701 | `1fb5e12f5c8eb5408dea6372c5442273b1694559dc9c09784bbca4309dbf5fd2` |
| `schemas/governance/proof-bundle.schema.json` | JSON Schema | [schema reference](schemas.md#schema-governance-proof-bundle-schema-json) | 881 | `1afe8003d5fc80540188ed757588d320f8b29bacdf4b293e5e5ab2275e1e4219` |
| `schemas/governance/review.schema.json` | JSON Schema | [schema reference](schemas.md#schema-governance-review-schema-json) | 778 | `280cfe7963adcdcbbb3a1fde01b921cad82751d2240a4fcdaa9b9543db071bc2` |
| `schemas/governance/worker.schema.json` | JSON Schema | [schema reference](schemas.md#schema-governance-worker-schema-json) | 689 | `ca8f6768a4c7dfe89e80f2107c4bb43badde4d01d3ec6947ff001c9b207b403c` |
| `schemas/hybrid-project.schema.json` | JSON Schema | [schema reference](schemas.md#schema-hybrid-project-schema-json) | 1940 | `c72692b4469f7ba92b2945968974d495371e2c0f03ad438c970418c3ce31d9b0` |
| `schemas/image-match-report.schema.json` | JSON Schema | [schema reference](schemas.md#schema-image-match-report-schema-json) | 1063 | `f81f81c2581b2941b9a3850aa2d296957e1d14de2ad3d8ee92839b34ccfadc23` |
| `schemas/image-profile.schema.json` | JSON Schema | [schema reference](schemas.md#schema-image-profile-schema-json) | 1687 | `5916e3589fb77876a26861ccfea7dfbfbf4b9c55e92243ed66dae4270dad70d7` |
| `schemas/integration-report.schema.json` | JSON Schema | [schema reference](schemas.md#schema-integration-report-schema-json) | 856 | `4732a3a8f4038739f46c7b7b74b20999c68d9f637bac783a53b03eee91e91d1a` |
| `schemas/integration-scenarios.schema.json` | JSON Schema | [schema reference](schemas.md#schema-integration-scenarios-schema-json) | 5710 | `60799068b8df90e7d457415f6e08fa236a0620630ddab2641dec2ff8bac6e43e` |
| `schemas/linker-layout.schema.json` | JSON Schema | [schema reference](schemas.md#schema-linker-layout-schema-json) | 769 | `a8faf6022c8b70e04c3375d47a480b9a811e72edd55ea7e0ec4e80a77a8ca934` |
| `schemas/linker-reconstruction-plan.schema.json` | JSON Schema | [schema reference](schemas.md#schema-linker-reconstruction-plan-schema-json) | 1234 | `1d6fadf9737abed4d02cc90d3859898785edf62d3909c39fe893c8841c57f504` |
| `schemas/mcp-mutation.schema.json` | JSON Schema | [schema reference](schemas.md#schema-mcp-mutation-schema-json) | 1155 | `64335798160269133e880d823f14de7f0cb4f2dafbf0c47526e24fb9fb16ea29` |
| `schemas/memory-event.schema.json` | JSON Schema | [schema reference](schemas.md#schema-memory-event-schema-json) | 1300 | `d2f38971ac7dda92dda0564bb77bb4858160b5a342476d36fe52238eb5289e74` |
| `schemas/msvc-metadata.schema.json` | JSON Schema | [schema reference](schemas.md#schema-msvc-metadata-schema-json) | 688 | `84d0b6bc880ab47954f951a4eed4db317c14ee33ed5cdbe0ee098ce61c1d6273` |
| `schemas/native/boundary-finding.schema.json` | JSON Schema | [schema reference](schemas.md#schema-native-boundary-finding-schema-json) | 539 | `58d723eee6c5c374f78dcac68a23be5d0b60c6f002c3e8285d307eef496e74fc` |
| `schemas/native/candidate-manifest.schema.json` | JSON Schema | [schema reference](schemas.md#schema-native-candidate-manifest-schema-json) | 750 | `d3bad2e693b4b7d6e1c230d9e03ff775298273523c8b562d3b78400c13313029` |
| `schemas/native/function-match.schema.json` | JSON Schema | [schema reference](schemas.md#schema-native-function-match-schema-json) | 754 | `e598ca859f33c96b62fe8dac7fcf78ec77b53e4b8f178b9f19e1f288e2725cd1` |
| `schemas/native/function-slot.schema.json` | JSON Schema | [schema reference](schemas.md#schema-native-function-slot-schema-json) | 751 | `61bb10550455068b1c58073dfb30939aea8095cefbd775abab4d044efe9a2914` |
| `schemas/native/hybrid-composition.schema.json` | JSON Schema | [schema reference](schemas.md#schema-native-hybrid-composition-schema-json) | 599 | `feb6682c1aa1ed0a3bc3c06230ce27f006641d96238050151ad22584eb02cb9d` |
| `schemas/native/loop-run.schema.json` | JSON Schema | [schema reference](schemas.md#schema-native-loop-run-schema-json) | 609 | `de5d1a277444c3ea53ae0c4860d1a7978b478893fb893cf4c1ba1fca4a11b038` |
| `schemas/native/match-run.schema.json` | JSON Schema | [schema reference](schemas.md#schema-native-match-run-schema-json) | 468 | `7afbfb42c5995ff375a050c93bb119ce50f2a761220c610f2c1622f082c23fb5` |
| `schemas/native/patch-plan.schema.json` | JSON Schema | [schema reference](schemas.md#schema-native-patch-plan-schema-json) | 982 | `90a1f06eaa3f6a3d6b235cc0439c57fec0187006ccc4c01b8fbb76571bb31958` |
| `schemas/native/runtime-validation.schema.json` | JSON Schema | [schema reference](schemas.md#schema-native-runtime-validation-schema-json) | 606 | `f314d1ae2b72314a6ebf6c6d2905a8eb2f314498f256f567e01ae08622da90f3` |
| `schemas/native/section-export.schema.json` | JSON Schema | [schema reference](schemas.md#schema-native-section-export-schema-json) | 451 | `121ed87fe1b51a248b230acafd9780b96e74e01c72e9cba7fcd20fbb466eb317` |
| `schemas/native/staging-symbol.schema.json` | JSON Schema | [schema reference](schemas.md#schema-native-staging-symbol-schema-json) | 607 | `44b3ce02db0758435f6a230a9ad37bd00c3a6308bf71761836050e5c90c6c4d0` |
| `schemas/native/windows-tool.schema.json` | JSON Schema | [schema reference](schemas.md#schema-native-windows-tool-schema-json) | 484 | `22af6f0e3266250f1c741e95e231c4ee3d62fd3944e0000e6ab6e652089906e0` |
| `schemas/objdiff-manifest.schema.json` | JSON Schema | [schema reference](schemas.md#schema-objdiff-manifest-schema-json) | 1006 | `2fe8f65399749687b2890cc643f474c0b8de221e90f6ae5013ce0d8b46590360` |
| `schemas/pdb.schema.json` | JSON Schema | [schema reference](schemas.md#schema-pdb-schema-json) | 2594 | `850bbf885fa040ac4601dc4d93c2fb4b3afda1dd86612a0d8866a34bacf07008` |
| `schemas/pipeline.schema.json` | JSON Schema | [schema reference](schemas.md#schema-pipeline-schema-json) | 1850 | `a9b7b790fb6c877370a4c61ecbdf0f92eac13d9aba389cc0ab8d8723aee92ca6` |
| `schemas/project-template.schema.json` | JSON Schema | [schema reference](schemas.md#schema-project-template-schema-json) | 1609 | `1bf881ea328d3a6c00d727c0cbe1e47763726e70362a085354178add994458ce` |
| `schemas/project.schema.json` | JSON Schema | [schema reference](schemas.md#schema-project-schema-json) | 2917 | `4ab19d9064e8d249fdd545d1fa183920902d6afbe647d004ddd571a208295b0b` |
| `schemas/reconstruction/abi-contract.schema.json` | JSON Schema | [schema reference](schemas.md#schema-reconstruction-abi-contract-schema-json) | 960 | `d2286943caed629e873a4107fcceb21f18b0759cfebd17b71f761af14e68e016` |
| `schemas/reconstruction/build.schema.json` | JSON Schema | [schema reference](schemas.md#schema-reconstruction-build-schema-json) | 773 | `647d938812825abaa84206de119ebc4a18d8fad70a4f50121f990a4af2571dd0` |
| `schemas/reconstruction/capsule.schema.json` | JSON Schema | [schema reference](schemas.md#schema-reconstruction-capsule-schema-json) | 1065 | `4c5543017ddf58e9e9268633d7699f648289b431a95de7171bae325938ccb310` |
| `schemas/reconstruction/compatibility-shim.schema.json` | JSON Schema | [schema reference](schemas.md#schema-reconstruction-compatibility-shim-schema-json) | 864 | `714bcc499ffc2db676e163a5886ce9ca4fca7df0b2382a94488c6dfc5a782926` |
| `schemas/reconstruction/generated-test.schema.json` | JSON Schema | [schema reference](schemas.md#schema-reconstruction-generated-test-schema-json) | 1117 | `8e99342ae82922d0c5c17c41e857074a5a2cec9b1269e23572aea09b5715a7b5` |
| `schemas/reconstruction/header.schema.json` | JSON Schema | [schema reference](schemas.md#schema-reconstruction-header-schema-json) | 737 | `c878f851e64b11db9e0dad34785d5ef3ba3baa753e380af72f554fe44529a850` |
| `schemas/reconstruction/library-match.schema.json` | JSON Schema | [schema reference](schemas.md#schema-reconstruction-library-match-schema-json) | 1060 | `cdf8967118c99e0f1d224829f1e3067a2b9db50f31ca945db68a3cec61b0f36e` |
| `schemas/reconstruction/module.schema.json` | JSON Schema | [schema reference](schemas.md#schema-reconstruction-module-schema-json) | 953 | `4aa87665cf31d30d9395bff7fb9388c9bd55257718808572669a874922436a4f` |
| `schemas/reconstruction/security-finding.schema.json` | JSON Schema | [schema reference](schemas.md#schema-reconstruction-security-finding-schema-json) | 945 | `9a4f8a220e2e2d1d7dbc8116968bf2752d57a5725e18673faf59a192ace1826e` |
| `schemas/reconstruction/semantic-changeset.schema.json` | JSON Schema | [schema reference](schemas.md#schema-reconstruction-semantic-changeset-schema-json) | 936 | `2cc66c0075ba39a54d86a20ca3705d4656ce90e922ce5a8c0b9357db1bc27b28` |
| `schemas/reconstruction/source-provenance.schema.json` | JSON Schema | [schema reference](schemas.md#schema-reconstruction-source-provenance-schema-json) | 1200 | `d80a00434549c01f14f1afa7c43cb65b9eb653808b42fb5fa10f25b1d7ac1b0c` |
| `schemas/reconstruction/translation-unit.schema.json` | JSON Schema | [schema reference](schemas.md#schema-reconstruction-translation-unit-schema-json) | 846 | `ea17fb7bfec69c8e9e3eb5d14179194acece94ba90d5e0ad76c5f3e653dca642` |
| `schemas/release-gate.schema.json` | JSON Schema | [schema reference](schemas.md#schema-release-gate-schema-json) | 701 | `50e1f5a6cb46b67f833c881a7f025be5c7c047c1f23c3607608488afe17256cd` |
| `schemas/relink-manifest.schema.json` | JSON Schema | [schema reference](schemas.md#schema-relink-manifest-schema-json) | 1169 | `ca2b77b7be6b562589e841753a9afa8c6baf1fc7cf8c703409c90fc56507e890` |
| `schemas/reproduction.schema.json` | JSON Schema | [schema reference](schemas.md#schema-reproduction-schema-json) | 854 | `aea350be271c7795406a2dd55096775e9d0b531215e05f43b75a9c6b5bd98281` |
| `schemas/security-audit.schema.json` | JSON Schema | [schema reference](schemas.md#schema-security-audit-schema-json) | 821 | `d62a14bd5c6d796dd52aee929ccfdf8e1265f825167070c8ffd680321a00b637` |
| `schemas/symbolic-memory-harness.schema.json` | JSON Schema | [schema reference](schemas.md#schema-symbolic-memory-harness-schema-json) | 1762 | `e7ce53b843c172758fc086503e040cd1c60a3836f528b2c8396a7e77ab7c200a` |
| `schemas/symbolic-memory-report.schema.json` | JSON Schema | [schema reference](schemas.md#schema-symbolic-memory-report-schema-json) | 1042 | `5e17dedb1bedf6581662f4cced118e40b8075957a161daea2abfab778d0298ba` |
| `schemas/symbolic-report.schema.json` | JSON Schema | [schema reference](schemas.md#schema-symbolic-report-schema-json) | 523 | `cc596ec7c42bc74e7810dbf52bf50cba2d17375e9438f0a3fcbb3dae67a88e29` |
| `schemas/synthetic-corpus.schema.json` | JSON Schema | [schema reference](schemas.md#schema-synthetic-corpus-schema-json) | 2225 | `3c05d2c0a766021805afdd306d6a08068af6a24cdb0adb82fb3eca4d0f1d7c7d` |
| `schemas/target-decisions.schema.json` | JSON Schema | [schema reference](schemas.md#schema-target-decisions-schema-json) | 850 | `647192549c5e079a02e597648a0d3d2ade5078866f869b7e0da34324b5976ed6` |
| `schemas/target-pack.schema.json` | JSON Schema | [schema reference](schemas.md#schema-target-pack-schema-json) | 1400 | `867b89f3738ff1310340d078c5ae530f0087277e96cd00106fa1275cd0bcc954` |
| `schemas/test-bundle-report.schema.json` | JSON Schema | [schema reference](schemas.md#schema-test-bundle-report-schema-json) | 863 | `482f5b618cd46eb5e815392f2655bb9fe4f3683e1f5122b8f7ab0ea69f8a2820` |
| `schemas/test-bundle.schema.json` | JSON Schema | [schema reference](schemas.md#schema-test-bundle-schema-json) | 1451 | `398d162a3ccc9e3bd1e984af67efbfaf12a840f4013b406c0cf8d150f490deab` |
| `schemas/type-constraint.schema.json` | JSON Schema | [schema reference](schemas.md#schema-type-constraint-schema-json) | 1023 | `f98328b457deccc685ea8be764507320d5ff94deddb366e47c5018a678baa59d` |
| `schemas/verification.schema.json` | JSON Schema | [schema reference](schemas.md#schema-verification-schema-json) | 1495 | `a70e3422e6b0bec967695257c7b66d44f17a0cfe3f15d99799eb1c038ccb7fa0` |
| `schemas/work-task.schema.json` | JSON Schema | [schema reference](schemas.md#schema-work-task-schema-json) | 2144 | `36794b2e24e785918a28d8bd7f5fedd100c090ed64030c71eefa0a8c933b92c9` |
| `schemas/worker-report.schema.json` | JSON Schema | [schema reference](schemas.md#schema-worker-report-schema-json) | 1073 | `f4fee8d629c5e963519a4f5ab25c4bb0856592421ee218fe7d047b5ebe089b3c` |
| `scripts/run-pytest-partitions.py` | verification/build script | listed on this page | 6259 | `3854181436f04652a6cc59ead85b08729f9e65e29723c316ac33910e44d3d4c4` |
| `scripts/source_hashes.py` | verification/build script | listed on this page | 5190 | `6a9ed5603d441dd17731364bf711bc1bdc99e901b90b655460b5b96a9e886308` |
| `scripts/validate-contracts.py` | verification/build script | listed on this page | 5012 | `e1c21138bc3162f492fae9638971289b5d2bf7ae0a66e8daa140cc90f03ad5fe` |
| `scripts/verify-ghidra.sh` | verification/build script | listed on this page | 2098 | `254ae110f3a9b12b33ca77c698d7185792c180139fcef31017e400523440e111` |
| `scripts/verify.sh` | verification/build script | listed on this page | 359 | `324346ded8358e7fe227f69035deefa0365843e3735dbef904a7ce7387b5e853` |
| `setup.cfg` | package/build metadata | listed on this page | 38 | `1c473cbaee8da5fc46e7f0158794af5cea4414c34a3cf3f180c2001f5e38bd3e` |
| `skills/x86decomp/SKILL.md` | documentation or architecture text | listed on this page | 4082 | `13937e62e087b97e058e6646e5d093b81fd91880f8523c825790469b4739c5b3` |
| `src/x86decomp/__init__.py` | toolkit Python module | [module reference](features/x86decomp.md) | 473 | `104ef3c8b92fc6c70cf9c2ada1da70688fdd5733c5d717259da49ffd87993c92` |
| `src/x86decomp/__main__.py` | toolkit Python module | [module reference](features/x86decomp-main.md) | 48 | `935a1c1166b0c1ea35a82256345000bf2c73ded718d77773bc27a71ecce28f7d` |
| `src/x86decomp/abi.py` | toolkit Python module | [module reference](features/x86decomp-abi.md) | 10340 | `e69b8d4ba247b2e3dbd3553cd207ee8fbe24fe244878c4dabb4afffbebb33903` |
| `src/x86decomp/analysis_db.py` | toolkit Python module | [module reference](features/x86decomp-analysis-db.md) | 10679 | `409e503d6c264dba48a00e1d1afc475ce735cf25f1ec4aab7ac41b07ed5b9bad` |
| `src/x86decomp/angr_backend.py` | toolkit Python module | [module reference](features/x86decomp-angr-backend.md) | 20668 | `b3f95fbeec7f4d726ba52f50df9d4d7986cfad9ed5c789ab0a3932c0dea8b7a3` |
| `src/x86decomp/artifacts.py` | toolkit Python module | [module reference](features/x86decomp-artifacts.md) | 4698 | `171833c573e11e5d40d7791f8fea523536905a8486145a1aa1b96ea2761e6e6b` |
| `src/x86decomp/assembly/__init__.py` | toolkit Python module | [module reference](features/x86decomp-assembly.md) | 438 | `60dcbf406ebd10f56f155b70ea0657b0d40a2405ef65cf3caa32979fd90ca254` |
| `src/x86decomp/assembly/annotation.py` | toolkit Python module | [module reference](features/x86decomp-assembly-annotation.md) | 4176 | `193333b07dc91fcfa6add9200b9f9e170c6d3705e169ac7d76056657759a59ef` |
| `src/x86decomp/assembly/cli.py` | toolkit Python module | [module reference](features/x86decomp-assembly-cli.md) | 9760 | `f9fc081b2048d0c37591959352da1786d262cf26475932cba21977e24b652c58` |
| `src/x86decomp/assembly/materialize.py` | toolkit Python module | [module reference](features/x86decomp-assembly-materialize.md) | 22840 | `709e23ed78dd9f4f143ea56407326b42cf86e91fc86faee1aa73483dae354f2d` |
| `src/x86decomp/assembly/pipeline.py` | toolkit Python module | [module reference](features/x86decomp-assembly-pipeline.md) | 16063 | `f6ffb8a8282636b4f07854e6665bbe250b7bb405ceba0587e872d72d91dae04c` |
| `src/x86decomp/assembly/relocations.py` | toolkit Python module | [module reference](features/x86decomp-assembly-relocations.md) | 15022 | `d9c90ac5d66b3a36560ef8d9539bbef0d2e184574912609d27c7848d4f40666d` |
| `src/x86decomp/assembly/store.py` | toolkit Python module | [module reference](features/x86decomp-assembly-store.md) | 4827 | `cb4fae7b3778e5946398d50f58aece1f042587a3d1c94e96363390c0855679c1` |
| `src/x86decomp/benchmarks.py` | toolkit Python module | [module reference](features/x86decomp-benchmarks.md) | 7267 | `b9b28fbcb2f38723b274e4150b1c3914ddcbceab1b49461fc5797a84f9e13fb3` |
| `src/x86decomp/canonical.py` | toolkit Python module | [module reference](features/x86decomp-canonical.md) | 8293 | `4424ac7f4214c0af367791e1cba7268b5bc1d9ff0d7fa4f56d4c94fff6eae782` |
| `src/x86decomp/cli.py` | toolkit Python module | [module reference](features/x86decomp-cli.md) | 46907 | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/coff.py` | toolkit Python module | [module reference](features/x86decomp-coff.md) | 47852 | `f6900af73b991d2ed380250c78d4a228ff6b10f45bd4bcf04fb449c45f13d28e` |
| `src/x86decomp/coff_archive.py` | toolkit Python module | [module reference](features/x86decomp-coff-archive.md) | 12380 | `51cdfa71d8876054203d3f487c37ee12ece57e831abc8bca35e57112d4089584` |
| `src/x86decomp/compiler.py` | toolkit Python module | [module reference](features/x86decomp-compiler.md) | 9589 | `f21f38f6ed0804a959188e31f5c9fa498d7d0740536fbb82594a375b12353944` |
| `src/x86decomp/compiler_lab.py` | toolkit Python module | [module reference](features/x86decomp-compiler-lab.md) | 5821 | `05a54baba63c926190c0e2fb45bff09c6eb338ed6a479e6e47be210a6b1de859` |
| `src/x86decomp/compiler_worker.py` | toolkit Python module | [module reference](features/x86decomp-compiler-worker.md) | 5631 | `d13aa472af6cfb824c896d7a32c9c99ff7a4fcf07019dbba5aa42beba7f82045` |
| `src/x86decomp/content_store.py` | toolkit Python module | [module reference](features/x86decomp-content-store.md) | 10504 | `4902a167d8d42224690983536869b729211920840f539ad038d67a587c98001a` |
| `src/x86decomp/contracts.py` | toolkit Python module | [module reference](features/x86decomp-contracts.md) | 2851 | `59ed708757edb48209337ba38008c4522cd03106686c9b47b08da0b2a32e98ed` |
| `src/x86decomp/convergence.py` | toolkit Python module | [module reference](features/x86decomp-convergence.md) | 7341 | `2b943e9c8c2399089e1b8c2815c0de4cb1bcf0468c09e64a647fef3508922f74` |
| `src/x86decomp/corpus/ground_truth_sources/aliasing.c` | package/build metadata | listed on this page | 105 | `09a93c1038059384920be8ed617f196950b3b935fa4e7ecdcccd4b38215f222c` |
| `src/x86decomp/corpus/ground_truth_sources/arithmetic.c` | package/build metadata | listed on this page | 105 | `1a39b20e36efc0d23c5570152a1db30922527835bfc82ddf4b629980c916326e` |
| `src/x86decomp/corpus/ground_truth_sources/bitfields.c` | package/build metadata | listed on this page | 313 | `44c9a66d27e87a270af05fdb87d82d87512b70fe72600df0bc89f4e091b5a7dd` |
| `src/x86decomp/corpus/ground_truth_sources/branches.c` | package/build metadata | listed on this page | 125 | `0dcc84cf6d38aa0a3e90a66bd349f349d504cd2dc0160db16933466c56aa99bb` |
| `src/x86decomp/corpus/ground_truth_sources/calling_conventions.c` | package/build metadata | listed on this page | 343 | `cfb331698f9ccdb113849a7c535a500ee6631a46a716be1d3791e49f9c1e69b3` |
| `src/x86decomp/corpus/ground_truth_sources/classes.cpp` | package/build metadata | listed on this page | 274 | `d04c86180d9424ea91914dc7b73d93b4b3da432d7a26d8d801ff9d5718701521` |
| `src/x86decomp/corpus/ground_truth_sources/eh_multiple.cpp` | package/build metadata | listed on this page | 471 | `7b3cc0e687132f70957e55dbbaa5c479d6a4864fde0e11cb49df0c600d6f2665` |
| `src/x86decomp/corpus/ground_truth_sources/exceptions.cpp` | package/build metadata | listed on this page | 156 | `fd15c6bd23f39262a9aa02f94f02210dacab53a2a5d358aae415bba2c329394e` |
| `src/x86decomp/corpus/ground_truth_sources/floating_point.c` | package/build metadata | listed on this page | 195 | `ff00c63ae76817932bdd0b4a5b0a0c8bc661e03314889d1eef404e580279bb89` |
| `src/x86decomp/corpus/ground_truth_sources/globals.c` | package/build metadata | listed on this page | 100 | `e4fbe6bc2a51161e651a23264f5de4e90d052b2e9efcbcea1c1ff76a748528c4` |
| `src/x86decomp/corpus/ground_truth_sources/indirect_calls.c` | package/build metadata | listed on this page | 204 | `b9b6dc58d6912bf8a54c46868a5a61b321447c9826660dfb29f76f741b21b92e` |
| `src/x86decomp/corpus/ground_truth_sources/loops.c` | package/build metadata | listed on this page | 242 | `d929c2eb356d9e45d27aa9a9e9929d1ce3fad324d8843d7e53e4dbe7dabe9262` |
| `src/x86decomp/corpus/ground_truth_sources/member_pointers.cpp` | package/build metadata | listed on this page | 299 | `8e84a7254ebeda7ec4db40335350606cf26227868e20be7db4f4382cdd3e9f69` |
| `src/x86decomp/corpus/ground_truth_sources/multiple_inheritance.cpp` | package/build metadata | listed on this page | 272 | `2fc99918de8375a035774b6cff12866defb77d2095bf1a6005b6419c4afc4410` |
| `src/x86decomp/corpus/ground_truth_sources/static_initializers.cpp` | package/build metadata | listed on this page | 143 | `5566d58941846d63fafa6e6047f5f0a70dd19ff484aea58f1eac88cfa1c3156c` |
| `src/x86decomp/corpus/ground_truth_sources/structs.c` | package/build metadata | listed on this page | 124 | `0b29f69d01886989d3d34fb430acb259ca55c604b8b59c968e5d341972102280` |
| `src/x86decomp/corpus/ground_truth_sources/switch_dense.c` | package/build metadata | listed on this page | 248 | `2a696a875c034a89e16a9b28359f6603942c536954321bc7403a9b780d24546f` |
| `src/x86decomp/corpus/ground_truth_sources/tail_calls.c` | package/build metadata | listed on this page | 140 | `874edb70e2470cafdd6bed6a7a05519da95c926d1b0777622d1fba726194ddb3` |
| `src/x86decomp/corpus/ground_truth_sources/templates.cpp` | package/build metadata | listed on this page | 409 | `cd18fc097a4bbbacacff6685edb8c5e6a0dfe7d8e27a68eb0b0febad6508194b` |
| `src/x86decomp/corpus/ground_truth_sources/tls.c` | package/build metadata | listed on this page | 240 | `9f917229ae42021f4045f2f56af5ac3116987dc442e304c1b9b6b441200ba54b` |
| `src/x86decomp/corpus/ground_truth_sources/unions.c` | package/build metadata | listed on this page | 192 | `2906ac1f944da7f6020756df9f20451048f8e2ed81ed5ac6ea06554afe1c7f60` |
| `src/x86decomp/corpus/ground_truth_sources/varargs.c` | package/build metadata | listed on this page | 244 | `3326edfa00e59cd41f5409c8ef01d1d5b96c0e1a13471972a2a107725032cdbb` |
| `src/x86decomp/corpus/ground_truth_sources/vectorizable.c` | package/build metadata | listed on this page | 259 | `4e71d283a0479bd5264da8f235bdb4f434a1b841289d9eac335c8b997be10f43` |
| `src/x86decomp/corpus/ground_truth_sources/virtual_inheritance.cpp` | package/build metadata | listed on this page | 441 | `c8e83579cd4d6159e716c23270110d997349e3b1a609bf1d50c0b93a2e64d1d2` |
| `src/x86decomp/cpp_recovery.py` | toolkit Python module | [module reference](features/x86decomp-cpp-recovery.md) | 7979 | `c1f07b15f8649be4235cb56bb2e8f953ed31211b98311633d6beccde38dce8fa` |
| `src/x86decomp/decompme.py` | toolkit Python module | [module reference](features/x86decomp-decompme.md) | 3868 | `440f011b1a60d6a9549cd558927a158ce34f1377f699a58b922c696619172fe2` |
| `src/x86decomp/diffing.py` | toolkit Python module | [module reference](features/x86decomp-diffing.md) | 2751 | `e981a093051ff6a0be9462256f6ea50c2784693c15b32df5144a1ca0374814e3` |
| `src/x86decomp/disassembly.py` | toolkit Python module | [module reference](features/x86decomp-disassembly.md) | 11049 | `cc86a46f8c8674a6e14304158bd1d2467fb09ccbb00778c116204b0a639638b3` |
| `src/x86decomp/dynamic.py` | toolkit Python module | [module reference](features/x86decomp-dynamic.md) | 14935 | `a09cbba16f498158cf30191397884f0a70051c767b778cd520ac229b6e85e451` |
| `src/x86decomp/dynamorio.py` | toolkit Python module | [module reference](features/x86decomp-dynamorio.md) | 8058 | `8568a98326d91a775f2feec1847e8d3230c58253e1b015c3ee75dcb9b0d8b30d` |
| `src/x86decomp/errors.py` | toolkit Python module | [module reference](features/x86decomp-errors.md) | 576 | `5bb50a4d169960abdc486866d2e68c894d8c13da401361931d86991ff9f8030d` |
| `src/x86decomp/evidence.py` | toolkit Python module | [module reference](features/x86decomp-evidence.md) | 10277 | `de8befd97c8e7f0529f7c3c2750836f8f38fab52e26987cf390d725faad3ee1e` |
| `src/x86decomp/exe_diff.py` | toolkit Python module | [module reference](features/x86decomp-exe-diff.md) | 7784 | `997ffacbd833a3bb4c0545d1fb1981469e1d575680f4b39b7e6f34a4796abdf0` |
| `src/x86decomp/ghidra.py` | toolkit Python module | [module reference](features/x86decomp-ghidra.md) | 3634 | `98657d48a9d3ebb79eaf951aa8676ffd7ca696c2ba2f07fe8a5c4f0ad622c2b3` |
| `src/x86decomp/governance/__init__.py` | toolkit Python module | [module reference](features/x86decomp-governance.md) | 123 | `a0483ba8e8314f9c9ba3a8387147195d183c6c7a47b067e2f6a92354f6612c00` |
| `src/x86decomp/governance/campaigns.py` | toolkit Python module | [module reference](features/x86decomp-governance-campaigns.md) | 12317 | `0c43e0289c80013abf35c01f68f0214d968d3be681395621632a24e5d09dfd2a` |
| `src/x86decomp/governance/candidates.py` | toolkit Python module | [module reference](features/x86decomp-governance-candidates.md) | 10323 | `45b278d396b79ffecc4cfdd61e42af7e2cd5776f0b76f4f3a6b856283be0f1df` |
| `src/x86decomp/governance/changesets.py` | toolkit Python module | [module reference](features/x86decomp-governance-changesets.md) | 5935 | `b5fc108cbaa2b14f325deff21e849d49841c49550300221beefd8d489ac9fcee` |
| `src/x86decomp/governance/cli.py` | toolkit Python module | [module reference](features/x86decomp-governance-cli.md) | 18420 | `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb` |
| `src/x86decomp/governance/consensus.py` | toolkit Python module | [module reference](features/x86decomp-governance-consensus.md) | 7160 | `41c250face5e2cb3dd5a56c6e741d5cbebdc25e6e9f1531a25181d9d944a5eb3` |
| `src/x86decomp/governance/counterexamples.py` | toolkit Python module | [module reference](features/x86decomp-governance-counterexamples.md) | 6822 | `2223bd0eec9a09b58739850670b5d3434dfce554a3578cbe2ab870e43e698096` |
| `src/x86decomp/governance/family.py` | toolkit Python module | [module reference](features/x86decomp-governance-family.md) | 6721 | `be9c27b2174ab2e046fae2d9937d7df2b73353d738f794db9f923bc11c9ede7c` |
| `src/x86decomp/governance/hypotheses.py` | toolkit Python module | [module reference](features/x86decomp-governance-hypotheses.md) | 12669 | `9b9601b00d885856a2311c6cf10fe62137eef992310ffd400cc0c84f7beff966` |
| `src/x86decomp/governance/knowledge_graph.py` | toolkit Python module | [module reference](features/x86decomp-governance-knowledge-graph.md) | 5459 | `8ab4ed3fe2315a0a44f7ac646a7759127283a436807ed80bc01e865c6eb0cc33` |
| `src/x86decomp/governance/plugins.py` | toolkit Python module | [module reference](features/x86decomp-governance-plugins.md) | 6316 | `49a8f980b23b66c8c08b31355f52524b05119e3aabcedfd7c5e9f5ec0cbbc083` |
| `src/x86decomp/governance/proofs.py` | toolkit Python module | [module reference](features/x86decomp-governance-proofs.md) | 10583 | `4a7cc3e36784a2cfb375b573b253737c0afb18671bd6f7a6a9eec5b3ee50ffec` |
| `src/x86decomp/governance/reviews.py` | toolkit Python module | [module reference](features/x86decomp-governance-reviews.md) | 6028 | `ba9d5d2757485bdcfdb2ed1255287013fe710def654fcbc2cf8a6801fe25312f` |
| `src/x86decomp/governance/store.py` | toolkit Python module | [module reference](features/x86decomp-governance-store.md) | 16427 | `548329cc6771568daa387a41ba8280ed8850391effbb9e450e41259909f862ae` |
| `src/x86decomp/governance/workers.py` | toolkit Python module | [module reference](features/x86decomp-governance-workers.md) | 4223 | `4538ea72a7fe80900916a18a6bbba5ac7a3617d1765b1b981691ebad10f4e656` |
| `src/x86decomp/ground_truth.py` | toolkit Python module | [module reference](features/x86decomp-ground-truth.md) | 16842 | `9684fbcda0fd5060b3c1f2d0efb83892900c69190d33e24fd7e49f91885181e2` |
| `src/x86decomp/harness_generator.py` | toolkit Python module | [module reference](features/x86decomp-harness-generator.md) | 6957 | `75ab6f14bcef35574409e280dad90a705f71bc5763d507258f705ad8f4c431f2` |
| `src/x86decomp/hybrid.py` | toolkit Python module | [module reference](features/x86decomp-hybrid.md) | 9688 | `721221b69c86bd2e7152ea2f322c9b48d89a01891feb6906038509a1f4592e2f` |
| `src/x86decomp/image_match.py` | toolkit Python module | [module reference](features/x86decomp-image-match.md) | 12645 | `a9c72f376532369da77440496a1ea07564da5071ef8e6108e29c58e33e96fcf4` |
| `src/x86decomp/integration.py` | toolkit Python module | [module reference](features/x86decomp-integration.md) | 19791 | `cb8157c8210544e2ed4730e8bdb01f0a77dc9d05f683d43154cba1bf93c1e845` |
| `src/x86decomp/linker_layout.py` | toolkit Python module | [module reference](features/x86decomp-linker-layout.md) | 13933 | `e212e73f09b9559f17e0251eba8260a50b52931091a4972a2deabc462cd68682` |
| `src/x86decomp/linker_reconstruction.py` | toolkit Python module | [module reference](features/x86decomp-linker-reconstruction.md) | 6635 | `f67bc3077e7d54a9a32e542113cc28eadf00fa581c8e3d3c26e5c1b45a4e0900` |
| `src/x86decomp/mcp.py` | toolkit Python module | [module reference](features/x86decomp-mcp.md) | 12457 | `72627e41c628c756443bc5d57e38b583b1744923902735b55a3d6c9e29f6cca9` |
| `src/x86decomp/memory.py` | toolkit Python module | [module reference](features/x86decomp-memory.md) | 5471 | `4fd6948418a67ffdd502b92649a5b18af16376b55272018305b59d5cddcad813` |
| `src/x86decomp/models.py` | toolkit Python module | [module reference](features/x86decomp-models.md) | 1768 | `2afe3f05650301116d1f789854dd5406ea2af88b0bebb19df7a2f1667bf1bd0f` |
| `src/x86decomp/msvc_metadata.py` | toolkit Python module | [module reference](features/x86decomp-msvc-metadata.md) | 31431 | `a09e12dd6d748ba39648bf05d885656080c1c03be63d8dde592e26cb36b72951` |
| `src/x86decomp/native/__init__.py` | toolkit Python module | [module reference](features/x86decomp-native.md) | 158 | `c06bf6b79e240a8ec82b7084a6f50358b49e0c28084ed2cece59bd0f803dfb0d` |
| `src/x86decomp/native/cli.py` | toolkit Python module | [module reference](features/x86decomp-native-cli.md) | 10386 | `da601accbad512ec93400a9fd96a95b3419ce92ea17db8aefd9d03e67bd87950` |
| `src/x86decomp/native/closed_loop.py` | toolkit Python module | [module reference](features/x86decomp-native-closed-loop.md) | 3339 | `2928f6d9ecd646ec05c4cc204048ef0c303865b68e8ae45862aa81cfed3c758b` |
| `src/x86decomp/native/hybrid_composer.py` | toolkit Python module | [module reference](features/x86decomp-native-hybrid-composer.md) | 4354 | `e2cd31ef794c1910a4deb0a7260d88de3bb090bf153c7f77f740024f86a4cea0` |
| `src/x86decomp/native/matching.py` | toolkit Python module | [module reference](features/x86decomp-native-matching.md) | 8354 | `3d2d67bc09fd863ffb366310883c6869b10c04545e48edc75089b7317927478a` |
| `src/x86decomp/native/pe_reconstruction.py` | toolkit Python module | [module reference](features/x86decomp-native-pe-reconstruction.md) | 9233 | `32c4ba5082d59f88439efe2af68c26f8820aaa82d6f551d506a0d7c63b517558` |
| `src/x86decomp/native/runtime.py` | toolkit Python module | [module reference](features/x86decomp-native-runtime.md) | 4288 | `42a582f61d69ef1bc07096d003f19db4c0598d7386be494c124cf4272b1aa854` |
| `src/x86decomp/native/slots.py` | toolkit Python module | [module reference](features/x86decomp-native-slots.md) | 8093 | `e0f7164fa040306cab458e4dfe811590375a3a49023de7a33736e07b44032d2c` |
| `src/x86decomp/native/staging.py` | toolkit Python module | [module reference](features/x86decomp-native-staging.md) | 4698 | `0038cab527aaac36dc4ba8ea02eb526b2683f5329a03c4002673091f622239a1` |
| `src/x86decomp/native/store.py` | toolkit Python module | [module reference](features/x86decomp-native-store.md) | 6452 | `96c94a801677c9f526434ff43b4105a782c422e7418989706da71fa8ee21cd9d` |
| `src/x86decomp/native/windows_tools.py` | toolkit Python module | [module reference](features/x86decomp-native-windows-tools.md) | 3715 | `0de581d6f2316540f99e7daf3d64fbd925e1998f786b3099488d766ed71bb2c0` |
| `src/x86decomp/objdiff_adapter.py` | toolkit Python module | [module reference](features/x86decomp-objdiff-adapter.md) | 7679 | `d312150b8b06b0e9b1656df7dab0a10e0e4a4db6047a4e83663875387b3851c1` |
| `src/x86decomp/orchestrator.py` | toolkit Python module | [module reference](features/x86decomp-orchestrator.md) | 33955 | `752a6e6b5d4f931007e93ee7898f6a0d2500b044266c7153a27be7e7eb49477e` |
| `src/x86decomp/patching.py` | toolkit Python module | [module reference](features/x86decomp-patching.md) | 4029 | `61b9d802fc2c9c89f06877876f72efb7fc16d3a1fb283dddfd561dfd4fe61741` |
| `src/x86decomp/pdb.py` | toolkit Python module | [module reference](features/x86decomp-pdb.md) | 24787 | `0ad9c99f6a1b232ce33268d35097ea6b44343d65052339c701588bf4efa79690` |
| `src/x86decomp/pe.py` | toolkit Python module | [module reference](features/x86decomp-pe.md) | 18352 | `39a5dd1b26da8d0ef84e8ff247183068eb4943ab38211df3c56c43ca9a6911c0` |
| `src/x86decomp/pe32.py` | toolkit Python module | [module reference](features/x86decomp-pe32.md) | 36209 | `746651d78b0b8401565dd22e99f73c8c902b13400fd80094d4675ab52c8c4be5` |
| `src/x86decomp/project.py` | toolkit Python module | [module reference](features/x86decomp-project.md) | 8604 | `a9077107216cddb15d5e0a7ab95ac0e6f63b0817c2d1329842b6b4792f11ec5f` |
| `src/x86decomp/project_state.py` | toolkit Python module | [module reference](features/x86decomp-project-state.md) | 18659 | `8d063061a36ef9a66f1460e44c8a5f2e08bd239e8c3c6d9828f4bfc171bb1fbe` |
| `src/x86decomp/project_template.py` | toolkit Python module | [module reference](features/x86decomp-project-template.md) | 8687 | `2a70050138d13bf73d963a6cb49d404b39c2d12dbc00298e7e1a79999d076f8f` |
| `src/x86decomp/reconstruction/__init__.py` | toolkit Python module | [module reference](features/x86decomp-reconstruction.md) | 179 | `52313d0bee948e0909b7dbad630958a9631187f643927aa9b604acf3184599c8` |
| `src/x86decomp/reconstruction/abi_contracts.py` | toolkit Python module | [module reference](features/x86decomp-reconstruction-abi-contracts.md) | 4940 | `3a604b7e2a1519a524942ec0aa4cc06fa2281bea86cba2b2a29136ba04ab5bf0` |
| `src/x86decomp/reconstruction/builds.py` | toolkit Python module | [module reference](features/x86decomp-reconstruction-builds.md) | 8678 | `b31ec8291d840a45ac78f86bc5ece98f8eca736f2c04eb02d1faba3754826254` |
| `src/x86decomp/reconstruction/capsules.py` | toolkit Python module | [module reference](features/x86decomp-reconstruction-capsules.md) | 4261 | `8aad0081c5ebfc21b3af7484313045cf2a7327d83cb833b8e7c7bcdee865bdf3` |
| `src/x86decomp/reconstruction/cli.py` | toolkit Python module | [module reference](features/x86decomp-reconstruction-cli.md) | 17950 | `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027` |
| `src/x86decomp/reconstruction/generated_tests.py` | toolkit Python module | [module reference](features/x86decomp-reconstruction-generated-tests.md) | 4116 | `6822bf7dc5d508d8ee684f2a6c1f5eb0e141ef86dbb2c580c320561d2b760aaf` |
| `src/x86decomp/reconstruction/headers.py` | toolkit Python module | [module reference](features/x86decomp-reconstruction-headers.md) | 5791 | `438c0233df3581b7634dd878b01f5b32f6918d7dac836115ad7bc1c0c50fdacc` |
| `src/x86decomp/reconstruction/libraries.py` | toolkit Python module | [module reference](features/x86decomp-reconstruction-libraries.md) | 2424 | `4892d5e00011085e4befce6cff5a24c9d065c6647933acd4dcb4618a3f514152` |
| `src/x86decomp/reconstruction/project_layout.py` | toolkit Python module | [module reference](features/x86decomp-reconstruction-project-layout.md) | 8234 | `c56585dbc14339e024cf8fa5d4e4f31f06d7bce0a238b67212a3278a9282f4e7` |
| `src/x86decomp/reconstruction/provenance.py` | toolkit Python module | [module reference](features/x86decomp-reconstruction-provenance.md) | 6491 | `03790dbcf2863491fa3c28e4cb96013dc73be03b87a038fcc367a6f27933f9e3` |
| `src/x86decomp/reconstruction/security.py` | toolkit Python module | [module reference](features/x86decomp-reconstruction-security.md) | 3258 | `0959bd8e9edb807a04058a9b81857c096e9c91ffb6f8591a885d56ae048760ba` |
| `src/x86decomp/reconstruction/semantic_changesets.py` | toolkit Python module | [module reference](features/x86decomp-reconstruction-semantic-changesets.md) | 5013 | `4342cc6206f76716dcc2007d36fd18ed0aff99cd7ebb562ef544adeeb8a537f3` |
| `src/x86decomp/reconstruction/store.py` | toolkit Python module | [module reference](features/x86decomp-reconstruction-store.md) | 10602 | `1fd8bd828f1473a30e5013e610322c6dfdc31c731d4485847e5d8c750f3ebf1b` |
| `src/x86decomp/release_gate.py` | toolkit Python module | [module reference](features/x86decomp-release-gate.md) | 7923 | `8e79be8c5af67a90063af185b2239a5ce5a8ca828627ee05c14d897f891e02fd` |
| `src/x86decomp/relink.py` | toolkit Python module | [module reference](features/x86decomp-relink.md) | 5688 | `d401db042d4cc8300ccd4babd28cea400dca824d187a7caf0a1f3ead407fb296` |
| `src/x86decomp/reproducibility.py` | toolkit Python module | [module reference](features/x86decomp-reproducibility.md) | 6420 | `bcc5e2a773d7eb7589f28df90c0fe898155788b8e695d15e363e6dbad249ae7b` |
| `src/x86decomp/security_audit.py` | toolkit Python module | [module reference](features/x86decomp-security-audit.md) | 9536 | `274c689b0141c11b2376e087427f13b55dc9e87beb3ee8e40851dad5d8e2ba1d` |
| `src/x86decomp/service.py` | toolkit Python module | [module reference](features/x86decomp-service.md) | 7449 | `ef74988c5b19f8d2925ea07fb75a6cb3bea4304348bc9419e82f9ffddbd19584` |
| `src/x86decomp/symbolic.py` | toolkit Python module | [module reference](features/x86decomp-symbolic.md) | 35226 | `93d98f6e85a01a107881131821d5eb04875d310795c4f173448918c5a96fdcd3` |
| `src/x86decomp/synthetic_corpus.py` | toolkit Python module | [module reference](features/x86decomp-synthetic-corpus.md) | 12979 | `a0475235f70093de7171e32cbde918a9290569245efaa06f8549cd1ad480ece0` |
| `src/x86decomp/target_pack.py` | toolkit Python module | [module reference](features/x86decomp-target-pack.md) | 18593 | `18b4fa2ef39b61edd4c9ecc47d543ed6107395e841d81f9191d447dcaa5edb1d` |
| `src/x86decomp/test_bundle.py` | toolkit Python module | [module reference](features/x86decomp-test-bundle.md) | 18583 | `7b65953eff2b3ba85cc543e11a8ab007f85565e85fe29e73e12db9eb099efc31` |
| `src/x86decomp/toolchains.py` | toolkit Python module | [module reference](features/x86decomp-toolchains.md) | 2300 | `9dde5962b67d30fec64266313f5488a4e5501de9db26605d4719cbe276cde03f` |
| `src/x86decomp/tools.py` | toolkit Python module | [module reference](features/x86decomp-tools.md) | 2554 | `8e068c2ef41fb99fd53f45b28808fd2bf3366978bffc6ba22e46207497f08f34` |
| `src/x86decomp/util.py` | toolkit Python module | [module reference](features/x86decomp-util.md) | 3495 | `f38c92cec5d269f8597282a84f5cfb76dd9e952cedb3606be592e8f5f89d8fe1` |
| `src/x86decomp/work_queue.py` | toolkit Python module | [module reference](features/x86decomp-work-queue.md) | 5437 | `b1392399ca7536f6f1c1a78b16b62b61f7b70a744d2a529860e03d3371377c6e` |
| `src/x86decomp/worker.py` | toolkit Python module | [module reference](features/x86decomp-worker.md) | 13460 | `811287668595febda7c8a186d83e1683ad7c58fcc44259efe7271bf5d7b8249c` |
| `src/x86decomp/workflow.py` | toolkit Python module | [module reference](features/x86decomp-workflow.md) | 9170 | `cae8a093f08f66f9412393e59867c4d32ca7caf88533a175d22eebe1f325c0a5` |
| `test-suite/.gitignore` | package/build metadata | listed on this page | 195 | `a436e3b7faa06acfab37ac4d6870f732d0eee90f2d8d5095d25af8fa4af2d2db` |
| `test-suite/CHANGELOG.md` | documentation or architecture text | listed on this page | 626 | `5d031770e713013bd49b1ce4be53b2576f97eb65a956453e74a1881693364ecf` |
| `test-suite/INTEGRATION.md` | documentation or architecture text | listed on this page | 636 | `fe5f824eef33c736b0bbe17d356fc3d79f2cb10442c397de9448a236158a23ba` |
| `test-suite/LICENSE` | package/build metadata | listed on this page | 587 | `469b8fd4bf8c3ead57817703e5a8ea98c7759304f0da851b57810e410decffc5` |
| `test-suite/MAINTENANCE.md` | documentation or architecture text | listed on this page | 658 | `09c5294ae1af2b463f17051e0acc70eebea5d97c30e0b491109834616b464081` |
| `test-suite/MANIFEST.in` | package/build metadata | listed on this page | 599 | `576d360c349d1ac066a139b866a474d5bfcfc8be7db53b924a3cd671d7ae6778` |
| `test-suite/README.md` | documentation or architecture text | listed on this page | 1312 | `7245acaee7af9bc15845582cdf6285c91c128cf63262b48f5dcf88873bef11f3` |
| `test-suite/SECURITY.md` | documentation or architecture text | listed on this page | 632 | `18d7368d55650b2ba1f56496e2468296f514897c7c9d661c2f660d7d7c895577` |
| `test-suite/VERIFICATION.md` | documentation or architecture text | listed on this page | 592 | `3180233de098474a864d40fa6bef8db90a6bad60be5a730c4fc16ad665810d5d` |
| `test-suite/docs/ADAPTERS.md` | documentation or architecture text | listed on this page | 2326 | `4e33ae0e0146443e01f574a84088d9fc37ae3514b451f3b49a725287d7b415bf` |
| `test-suite/docs/ARCHITECTURE.md` | documentation or architecture text | listed on this page | 411 | `953de2e892d9e198d1108eaa0f653b1f3559a882dc001274c6f551bbcd2e61cb` |
| `test-suite/docs/ARCHITECTURE_MAP.md` | documentation or architecture text | listed on this page | 1039 | `622f783b0c2d710d69f72175acbc090d6fc07a2ae02ac2a122f0ff09ff087469` |
| `test-suite/docs/ARCHITECTURE_MAP_ASCII.txt` | documentation or architecture text | listed on this page | 1576 | `db94674ed3890ae7366034b1ceef24273bd28b90f0a9abad729d1b8198d47ef5` |
| `test-suite/docs/COVERAGE_CONTRACT.md` | documentation or architecture text | listed on this page | 1996 | `ec9f63965b35fe1a00d5d5f94d77eab6dad6cc10a7c0fc794672dfcaeb58679e` |
| `test-suite/docs/LOGGING.md` | documentation or architecture text | listed on this page | 339 | `b2628e07c1286adedd41a7a3236d622b61b92b62f1825c9da4b6667c4e226105` |
| `test-suite/docs/TEST_PLAN.md` | documentation or architecture text | listed on this page | 1178 | `e11aed636c83e3e46064546f38ef68b6b8918bf495c4f5e8fca18870f24e861f` |
| `test-suite/examples/x86decomp-test.json` | example artifact | listed on this page | 470 | `5cd31838533f866853e0730aa63ed36958b4d1dc92f8cfb3d5825da9c9d4204d` |
| `test-suite/pyproject.toml` | package/build metadata | listed on this page | 1011 | `88415aa77f84835be5592f8bb30752636cf073343fe367b99c7b2c7489ca02fe` |
| `test-suite/schemas/feature-catalog.schema.json` | package/build metadata | listed on this page | 3652 | `24193181dada623162d221939ab62559c0f6f52e6629339d2787ae042f9ffec3` |
| `test-suite/schemas/run-report.schema.json` | package/build metadata | listed on this page | 1341 | `9d2b3fcab807e52866a5b8e7bac9f7813e6d7e003d4de9f2f80d05e8798e93c6` |
| `test-suite/schemas/test-config.schema.json` | package/build metadata | listed on this page | 1468 | `c33b8ab58a509c7f688ff159d0cef5726a4909801d40fd4899c81c4626eda90d` |
| `test-suite/scripts/run-all.ps1` | verification/build script | listed on this page | 146 | `29211e8199239685346d666b03824714984db61c73526a8ebc8fb1bd461273cf` |
| `test-suite/scripts/run-all.sh` | verification/build script | listed on this page | 114 | `b2ed622ebf3f48fd4735088604e027152df7d446d4283fc63235d81b5c0caef2` |
| `test-suite/setup.cfg` | package/build metadata | listed on this page | 38 | `1c473cbaee8da5fc46e7f0158794af5cea4414c34a3cf3f180c2001f5e38bd3e` |
| `test-suite/src/x86decomp_testkit/__init__.py` | verification Python module | [module reference](features/x86decomp-testkit.md) | 92 | `998bcdf50c9b8e8f7bbc3bd72fd26a3dfaeb15ae501ed6e7f8e6f88f091bb143` |
| `test-suite/src/x86decomp_testkit/__main__.py` | verification Python module | [module reference](features/x86decomp-testkit-main.md) | 48 | `935a1c1166b0c1ea35a82256345000bf2c73ded718d77773bc27a71ecce28f7d` |
| `test-suite/src/x86decomp_testkit/adapters/__init__.py` | verification Python module | [module reference](features/x86decomp-testkit-adapters.md) | 229 | `f827da6e3cd2ae844d65e34b74490f244c092f2c14dc2849af4c839a7270bf13` |
| `test-suite/src/x86decomp_testkit/adapters/catalog.py` | verification Python module | [module reference](features/x86decomp-testkit-adapters-catalog.md) | 11479 | `40b982dede4388ac62813dc2736ee68ec25d9ea4c88b12e0e3b2bc5e10da6867` |
| `test-suite/src/x86decomp_testkit/adapters/detection.py` | verification Python module | [module reference](features/x86decomp-testkit-adapters-detection.md) | 10558 | `31500b9b25721c7bf1e53eb59fa082003db73ca68315ab787e8f24df48e180aa` |
| `test-suite/src/x86decomp_testkit/adapters/download.py` | verification Python module | [module reference](features/x86decomp-testkit-adapters-download.md) | 5818 | `60a341280d4c00b4289c4a0d6ef12e60b86331c5cd0dde794dbfe22ed40f5e77` |
| `test-suite/src/x86decomp_testkit/adapters/installation.py` | verification Python module | [module reference](features/x86decomp-testkit-adapters-installation.md) | 13240 | `44488c89ba434c7bc704118ebc1bb86329eb1a9cfadde5237bcd3b19130266d1` |
| `test-suite/src/x86decomp_testkit/cli.py` | verification Python module | [module reference](features/x86decomp-testkit-cli.md) | 5279 | `fc69ddd59b29350727a5762fe78f440d3538bee7c83d5342478d18ee3a0dcd67` |
| `test-suite/src/x86decomp_testkit/config.py` | verification Python module | [module reference](features/x86decomp-testkit-config.md) | 4029 | `766a7f68f96c2658782d99f806ea342fb09bfa734fd22de5fb890a60b0004427` |
| `test-suite/src/x86decomp_testkit/coverage_audit.py` | verification Python module | [module reference](features/x86decomp-testkit-coverage-audit.md) | 2587 | `8d7312862dc245a37131f5a53b5094684882082f46401920f8623af039f67809` |
| `test-suite/src/x86decomp_testkit/data/feature_catalog.json` | package/build metadata | listed on this page | 87635 | `5536d10339537aedbfe5780faed418051482f7b8cffed4a67620c11aa1da306e` |
| `test-suite/src/x86decomp_testkit/fixtures.py` | verification Python module | [module reference](features/x86decomp-testkit-fixtures.md) | 5479 | `503faabe75a6906a9feda50866fc275f80a0596d8605b6b9125c36330a7ef6ed` |
| `test-suite/src/x86decomp_testkit/inventory.py` | verification Python module | [module reference](features/x86decomp-testkit-inventory.md) | 7427 | `d7c60ef575fc20122b84c635d9cdd8875dd629cabaa9a6f7810aaa1b306242a4` |
| `test-suite/src/x86decomp_testkit/junit.py` | verification Python module | [module reference](features/x86decomp-testkit-junit.md) | 971 | `3651cdaf2fb723366239d6a2cc32f4b0a8af336509784c4c8bf1bf957c317d14` |
| `test-suite/src/x86decomp_testkit/live_adapters.py` | verification Python module | [module reference](features/x86decomp-testkit-live-adapters.md) | 10448 | `49ee078112933e69aa34dd86330f6ddaa35b59c224388206db5600fbd13c9cb5` |
| `test-suite/src/x86decomp_testkit/logging_utils.py` | verification Python module | [module reference](features/x86decomp-testkit-logging-utils.md) | 2096 | `973448e1f8708f80d4efebeec3246c51f90f35e6e1088a620d363b9767af0e8c` |
| `test-suite/src/x86decomp_testkit/models.py` | verification Python module | [module reference](features/x86decomp-testkit-models.md) | 3447 | `8acaf5ce95d26ae135796a0b97eb0165e3fc1c392036e90fa866dd86c22e0e84` |
| `test-suite/src/x86decomp_testkit/orchestrator.py` | verification Python module | [module reference](features/x86decomp-testkit-orchestrator.md) | 4184 | `a475cf9d9e71158d3c15641b1222bdcb5f18dbe3d408553cf664ab9f8688a487` |
| `test-suite/src/x86decomp_testkit/process.py` | verification Python module | [module reference](features/x86decomp-testkit-process.md) | 3434 | `1968fbfaad57ef05e06e85613d6efa7fedf1f2c57aab895bcf1e90cd2854dbf9` |
| `test-suite/src/x86decomp_testkit/reports.py` | verification Python module | [module reference](features/x86decomp-testkit-reports.md) | 5934 | `e339aec1110820fbd64b47be2ff03da04507a055ea0f63eff7cd1e407cc90a1f` |
| `test-suite/src/x86decomp_testkit/self_tests/__init__.py` | verification Python module | [module reference](features/x86decomp-testkit-self-tests.md) | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `test-suite/src/x86decomp_testkit/self_tests/test_adapter_detection_resolution.py` | verification Python module | [module reference](features/x86decomp-testkit-self-tests-test-adapter-detection-resolution.md) | 4303 | `d2b5626de04bac6ee52935b4db6e5437c56a6edf94ef300504008eccdf4d7812` |
| `test-suite/src/x86decomp_testkit/self_tests/test_archive_security.py` | verification Python module | [module reference](features/x86decomp-testkit-self-tests-test-archive-security.md) | 2507 | `e731b4d36cbf94828e09245b2118b858bfd6c284e1d8a4be43c7f72b36412792` |
| `test-suite/src/x86decomp_testkit/self_tests/test_cli_and_installation.py` | verification Python module | [module reference](features/x86decomp-testkit-self-tests-test-cli-and-installation.md) | 1770 | `b2d0c38e67585e901fc45d1a82839da0989a70d099ab9625d092b1d9c38dde4b` |
| `test-suite/src/x86decomp_testkit/self_tests/test_config_models.py` | verification Python module | [module reference](features/x86decomp-testkit-self-tests-test-config-models.md) | 2117 | `1720714230e28811c1bef9e525b9e972075a3d65aab4c8117af23611c97445c4` |
| `test-suite/src/x86decomp_testkit/self_tests/test_inventory_reports_process.py` | verification Python module | [module reference](features/x86decomp-testkit-self-tests-test-inventory-reports-process.md) | 5626 | `15d8fac0bc3a91ab86a6997e86618452b3b317fb57edacb787989539d8eb1f64` |
| `test-suite/src/x86decomp_testkit/suites.py` | verification Python module | [module reference](features/x86decomp-testkit-suites.md) | 20068 | `8b08e944e5d2672abd926d90146ae7a8a7c4103c1c0ddbe3eb5496f8dcb6fc52` |
| `test-suite/src/x86decomp_testkit/timeutil.py` | verification Python module | [module reference](features/x86decomp-testkit-timeutil.md) | 196 | `09f390dc5c11065df3bb8370bc2bbff2dd4f13bab9778fa8209f4c1d4d9c2b66` |
| `test-suite/src/x86decomp_testkit/toolkit_tests/__init__.py` | verification Python module | [module reference](features/x86decomp-testkit-toolkit-tests.md) | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py` | verification Python module | [module reference](features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 23474 | `0db55c2047f507a231d9738d8dc5710114a13726768e81aa0160c3fa5b3ff3eb` |
| `test-suite/tests/test_adapter_detection_resolution.py` | test source | [test reference](tests/test-suite-tests-test-adapter-detection-resolution.md) | 4303 | `d2b5626de04bac6ee52935b4db6e5437c56a6edf94ef300504008eccdf4d7812` |
| `test-suite/tests/test_architecture_maps.py` | test source | [test reference](tests/test-suite-tests-test-architecture-maps.md) | 3584 | `10036d960f0186ccbcbbd7873f0844a38467cb81755710df36d67ecb1ce6e1f4` |
| `test-suite/tests/test_archive_security.py` | test source | [test reference](tests/test-suite-tests-test-archive-security.md) | 2507 | `e731b4d36cbf94828e09245b2118b858bfd6c284e1d8a4be43c7f72b36412792` |
| `test-suite/tests/test_cli_and_installation.py` | test source | [test reference](tests/test-suite-tests-test-cli-and-installation.md) | 1770 | `b2d0c38e67585e901fc45d1a82839da0989a70d099ab9625d092b1d9c38dde4b` |
| `test-suite/tests/test_config_models.py` | test source | [test reference](tests/test-suite-tests-test-config-models.md) | 2117 | `1720714230e28811c1bef9e525b9e972075a3d65aab4c8117af23611c97445c4` |
| `test-suite/tests/test_inventory_reports_process.py` | test source | [test reference](tests/test-suite-tests-test-inventory-reports-process.md) | 5626 | `15d8fac0bc3a91ab86a6997e86618452b3b317fb57edacb787989539d8eb1f64` |
| `tests/assembly/conftest.py` | test source | listed on this page | 196 | `89dd996765210f429269ca0c7c8218e3ff2d5ed956f9d502df9eb492a1964146` |
| `tests/assembly/test_annotation_materialize.py` | test source | [test reference](tests/tests-assembly-test-annotation-materialize.md) | 6280 | `46aeb940a0ccb02b0312ef413ce123c3c647c0224a1f8b1f571d128ab733574f` |
| `tests/assembly/test_helpers_and_relocations.py` | test source | [test reference](tests/tests-assembly-test-helpers-and-relocations.md) | 2191 | `d103e5e3199aa32ceb99dd5867f3454cca6676d33956bd2aca3b035176bd4860` |
| `tests/assembly/test_pipeline_cli_schemas.py` | test source | [test reference](tests/tests-assembly-test-pipeline-cli-schemas.md) | 7220 | `974f3cdeaa3c9954c08b1244d5a0cbdc71339f8355d0797832ce2967c5acccf2` |
| `tests/governance/test_core.py` | test source | [test reference](tests/tests-governance-test-core.md) | 8743 | `d2c62ade326140850549e48c1255cab3a45ec3f69d2374f4aff21380cd1ccc0d` |
| `tests/governance/test_governance_cli_schemas.py` | test source | [test reference](tests/tests-governance-test-governance-cli-schemas.md) | 2547 | `dc1c807a185938728d8c9483e2cacd38ded6634c167fce3f5374759bc5917345` |
| `tests/governance/test_proof_plugin_worker.py` | test source | [test reference](tests/tests-governance-test-proof-plugin-worker.md) | 4472 | `1cf8e1e2877783f7375ac2a2305fa708eafecc1591cc27e6b54d026bc6b03829` |
| `tests/governance/test_worker_thread_safety.py` | test source | [test reference](tests/tests-governance-test-worker-thread-safety.md) | 2390 | `053888fd3453b44860f529fec44c6d6f14824c09c1a381f66976bcc8fdd6f969` |
| `tests/native/conftest.py` | test source | listed on this page | 189 | `2d42379dee188c7576a7309dee52e132f82bf7e0343ba699247c65267cbcc314` |
| `tests/native/test_cli_schemas.py` | test source | [test reference](tests/tests-native-test-cli-schemas.md) | 2232 | `c11f5b352f077d58128f8670171974a1e81afe2d6559168e19ce7fda2c26a9a8` |
| `tests/native/test_inventory_and_loops.py` | test source | [test reference](tests/tests-native-test-inventory-and-loops.md) | 2971 | `92e89da6edbcda1a7371d809975b58c129e85ac8274365b05488d1ccd56d4960` |
| `tests/native/test_pe_hybrid.py` | test source | [test reference](tests/tests-native-test-pe-hybrid.md) | 3253 | `f348168b73353f4da20583dc0c5b4e2d1dfb9e052dc185f236098ff4898cfc1e` |
| `tests/native/test_slots_matching.py` | test source | [test reference](tests/tests-native-test-slots-matching.md) | 2594 | `1a028f9a8c827f3caa937c142c2f11b5234f46ddcb0315e9b1908be2bf5b967e` |
| `tests/native/test_staging_loop_runtime_windows.py` | test source | [test reference](tests/tests-native-test-staging-loop-runtime-windows.md) | 3090 | `da1cf374737a7615578374f772b1d100e2756affcf6abf90c4e56941f4c82fe8` |
| `tests/pe_fixture.py` | test source | listed on this page | 3555 | `cc94413b8549a52a9374403e0f704d57520c6793b6e11f8c26a2d6d8f0eb04d1` |
| `tests/reconstruction/test_capsules_security_changesets.py` | test source | [test reference](tests/tests-reconstruction-test-capsules-security-changesets.md) | 2742 | `a6b9cf3505de163803435daf9b909e5f7f1ead3a660325818faf379abe8979b4` |
| `tests/reconstruction/test_cli_schemas_retention.py` | test source | [test reference](tests/tests-reconstruction-test-cli-schemas-retention.md) | 3228 | `3a163de81011f9ce073b0aaa4345f49e0838494ea700aa78e6fb03c4f36fc8b3` |
| `tests/reconstruction/test_project_headers_builds.py` | test source | [test reference](tests/tests-reconstruction-test-project-headers-builds.md) | 3400 | `48264c55d224edf9ad5026b86eb4ef1ba7c900fe0e1ebe341c12c16aaec57d95` |
| `tests/reconstruction/test_provenance_abi_tests.py` | test source | [test reference](tests/tests-reconstruction-test-provenance-abi-tests.md) | 3297 | `df4e2725330a4cfc5e4d6f5817d062bbcc6c9db120d0e5435a665d453910557d` |
| `tests/test_abi_disassembly.py` | test source | [test reference](tests/tests-test-abi-disassembly.md) | 494 | `7707cba729a70b66986595aea747f5c1e782023e2b58134d2786680b52840a64` |
| `tests/test_artifacts.py` | test source | [test reference](tests/tests-test-artifacts.md) | 2016 | `bcf7a774d955c365b701f002a37884e35babacc396f6a78188c6e2ada40bca67` |
| `tests/test_coff.py` | test source | [test reference](tests/tests-test-coff.md) | 819 | `57797f4ad3e7871224434918b93fa79fc4046042cf54aa4f2c1fc1ddca99a8df` |
| `tests/test_coff_archive.py` | test source | [test reference](tests/tests-test-coff-archive.md) | 4609 | `171e74d6a9f9f1c6d02ddfd6094cd8af2c1250a1689854738abe3baf3f7eeea3` |
| `tests/test_compiler.py` | test source | [test reference](tests/tests-test-compiler.md) | 849 | `9645daed68779957cd14addad7626d32d99056f551c27d873e3f475cfe862f64` |
| `tests/test_decompme_objdiff.py` | test source | [test reference](tests/tests-test-decompme-objdiff.md) | 2522 | `5b9c426c8062799b1dd013a426638767e12d93e03e9425e6f21987abecfdcb60` |
| `tests/test_diffing.py` | test source | [test reference](tests/tests-test-diffing.md) | 634 | `b5fc82c4cba524724ae00431d81a9dc7fc976a5cd7d54053668e153fb51707a5` |
| `tests/test_documentation.py` | test source | [test reference](tests/tests-test-documentation.md) | 2280 | `803da6706a55de973a498ef159c757d5c2bf7b7b9a023885c17b8671d6006e29` |
| `tests/test_dynamic_symbolic.py` | test source | [test reference](tests/tests-test-dynamic-symbolic.md) | 1442 | `0b21be2ee69be29d2dde6951f147195bd8042462690dea72fac0b6509deb3402` |
| `tests/test_dynamorio.py` | test source | [test reference](tests/tests-test-dynamorio.md) | 1467 | `0d182c7c06f6ab60b970935bef97e7327fd18744bdb5d29918a7193d330bde2e` |
| `tests/test_evidence.py` | test source | [test reference](tests/tests-test-evidence.md) | 2802 | `4e8b73d7ad07cbce395ffe1267c272aeabdb861c0d198b6b8fcf5b448341b669` |
| `tests/test_ghidra.py` | test source | [test reference](tests/tests-test-ghidra.md) | 1528 | `1c9a934bad943761f8d9b6bc22509a054a8ead82747d2091d5f7e84c5682b88b` |
| `tests/test_integration.py` | test source | [test reference](tests/tests-test-integration.md) | 2934 | `0175ece91623baf3dd4092ddab3ba03bd47308082bccc85de135ce2b80b47ed0` |
| `tests/test_linker_metadata_corpus.py` | test source | [test reference](tests/tests-test-linker-metadata-corpus.md) | 13232 | `aa88771eecf6bbd2a6fcc6230848165884fea583b48688061d61c14756f9a1de` |
| `tests/test_mcp.py` | test source | [test reference](tests/tests-test-mcp.md) | 2184 | `10922b81d1726dd38b453ed718a7da0ddaedd5db188a9befb7cf8bded8686f49` |
| `tests/test_memory.py` | test source | [test reference](tests/tests-test-memory.md) | 1249 | `dd3384d0fa0c87ed61bde90498b97a3dc2d642d24b57fc9e00f95e52f47ca0b1` |
| `tests/test_modes_and_db.py` | test source | [test reference](tests/tests-test-modes-and-db.md) | 1594 | `7b3e58d0cbef709f782c724956d752cd24fab83ec169cf6eb49562b883b4b174` |
| `tests/test_pdb.py` | test source | [test reference](tests/tests-test-pdb.md) | 3069 | `a0966c606b191d2f1c18cc13e839f50919a8b55f937ac07694a324650200e9db` |
| `tests/test_pe32.py` | test source | [test reference](tests/tests-test-pe32.md) | 1159 | `4952257965fe3a61bc43d6a099b190264e924ecc85fdc8ba4e42e4a32bdc79c4` |
| `tests/test_pe64_patch_hybrid.py` | test source | [test reference](tests/tests-test-pe64-patch-hybrid.md) | 2255 | `6894dd0e5abce06a30df7ce445f6cf7faa87bcc16dac9f314f187e938697a62f` |
| `tests/test_production.py` | test source | [test reference](tests/tests-test-production.md) | 22969 | `da0d4bd57f7f4bb68957fa8aa42a67f7eb34347f35137849e360dc95e796db89` |
| `tests/test_project.py` | test source | [test reference](tests/tests-test-project.md) | 1538 | `04d73c197e4b7979731c140bef24e36ab323099e715d5462c95983a83d558c2b` |
| `tests/test_release_contract.py` | test source | [test reference](tests/tests-test-release-contract.md) | 8949 | `07d1e8f1825baea6ebb7014c9f1a1fb3cfd17b2794848c6f059e2fd62140f5c5` |
| `tests/test_relink.py` | test source | [test reference](tests/tests-test-relink.md) | 1080 | `580ca742c9d4f1d53de889f6f6bc5800e04147a31d86f0424a6d7a7252cefbb1` |
| `tests/test_test_bundle.py` | test source | [test reference](tests/tests-test-test-bundle.md) | 3789 | `e07c08f3155c6ab4b45329aa9076a42632affa7d2c12daa2d70f8657e77e9af6` |
| `tests/test_workqueue.py` | test source | [test reference](tests/tests-test-workqueue.md) | 669 | `97e33711360e2dec914664fbef25f0ece3ba7d6895e7c9331489d8e6fa46a8ed` |
