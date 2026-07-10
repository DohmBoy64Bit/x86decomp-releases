---
title: Project Example Source Audit
description: Hash ledger for project example and corpus sources in x86decomp 0.7.11.
---

# Project Example Source Audit

This ledger is regenerated from the 0.7.11 source tree. Each listed digest is a full SHA-256 of the referenced current file.

| Path | SHA-256 |
| --- | --- |
| `examples/abi/stdcall-two-ints.json` | `f2c7a723de83de7169612e1cdc305a4bd8779e9ad82c7ff3a2ce90d400ac3ace` |
| `examples/benchmarks/bounded-demo.json` | `980ad9dc8352019f4dca1f06e25a8654ec87248befc178c35490ecc3d129a51a` |
| `examples/compiler-profiles/gcc-i686-object.json` | `dc5dee89f0aff786350b51e24e7b77067de8d2a0a332fc6e880041a330729572` |
| `examples/contracts/command-surface.json` | `d03d54a17a1cdad06398277bae6a9df80ee6bcd11edc4b6457d35631b715e30f` |
| `examples/contracts/public-surface.json` | `7216f4234aa63821ef8dc5a1d03c68e3cbc817b96c91e956ee922690db166d85` |
| `examples/integration/bounded-demo.json` | `e1b589e23a5fa0a7c1310c69760ef7729fa912c2a5584985a7cbb487f57eab26` |
| `examples/integration/candidate.py` | `fdec1c8156f57d6ba8a11f898a846634783644a8c8aaaabaa98854aa5adb1bd4` |
| `examples/integration/candidate_mismatch.py` | `557e63b6c825e0d9a6110de93770a7b57af40118d8b5024563fc2b7b7e88c4dd` |
| `examples/integration/target.py` | `fdec1c8156f57d6ba8a11f898a846634783644a8c8aaaabaa98854aa5adb1bd4` |
| `examples/labs/gcc-optimization-matrix.json` | `f4f19ea47da16374312c4eff46d2914e3d0c425a229f92a95b2fe99221acbd78` |
| `examples/local-llm/add-two-ints-job.json` | `aac7785ac0e8ccc9e408fe583c7a96ca8a4bb01abd51eb17c1553f127a8a86b5` |
| `examples/local-llm/lm-studio-profile.json` | `f8135459f4354bf16ab4797924efb4a02f44b494ac36ee4873464609307c202e` |
| `examples/local-llm/ollama-profile.json` | `f10e53e8646689be08c75c7e06fa238ddf78159aa672da8e35aa3c3df415e5bb` |
| `examples/release/release-gate-policy.json` | `7ad41612264a71c3bd1d1ea44b5ad0f9145710ef926492975796dd9264948026` |
| `examples/release/target-decisions.json` | `91b5bfcd613ac3d76fc020e5bb415d0ae11594886c6cac4317cc06e7ea5df1cb` |
| `examples/relink/lld-link-x64.json` | `6addc382de2d64d223f4e24e47207b5741d2583d1717f4aec04107123a6013ef` |
| `examples/sample_source/add.c` | `860aaedc4520b18df5ce99de71a36487eb333dcdb09f65fce222677c8fe8cd97` |
| `examples/symbolic/symbolic-alias-harness.json` | `e5bbc6d9470e269f41051e95a444a9218f9919140bc74070dd223caf4eb7c130` |
| `examples/test-bundle/x86decomp-test-bundle.json` | `6d88af2c016e6e88a5ba66fab7c88c9d7b56f70c1f5e71d2cb494aab69da6a68` |
| `examples/validators/add_stack_candidate.bin` | `6d1e1d30f2068501de61e0022c4352fda2a7650f29eb96f01ad04fa160305e21` |
| `examples/validators/add_stack_harness.json` | `beeaeeecbe1136402ef0b3c1c3f799256a2613f87bb9457f97b71fe605ec0d0f` |
| `examples/validators/add_stack_target.bin` | `6d1e1d30f2068501de61e0022c4352fda2a7650f29eb96f01ad04fa160305e21` |
| `examples/validators/sub_stack_candidate.bin` | `fe10777e0899cf9cabd2bc8dc3367d711f6af675bdda9c5e28144539792f922f` |
| `corpus/ground_truth_sources/aliasing.c` | `09a93c1038059384920be8ed617f196950b3b935fa4e7ecdcccd4b38215f222c` |
| `corpus/ground_truth_sources/arithmetic.c` | `1a39b20e36efc0d23c5570152a1db30922527835bfc82ddf4b629980c916326e` |
| `corpus/ground_truth_sources/bitfields.c` | `44c9a66d27e87a270af05fdb87d82d87512b70fe72600df0bc89f4e091b5a7dd` |
| `corpus/ground_truth_sources/branches.c` | `0dcc84cf6d38aa0a3e90a66bd349f349d504cd2dc0160db16933466c56aa99bb` |
| `corpus/ground_truth_sources/calling_conventions.c` | `cfb331698f9ccdb113849a7c535a500ee6631a46a716be1d3791e49f9c1e69b3` |
| `corpus/ground_truth_sources/classes.cpp` | `d04c86180d9424ea91914dc7b73d93b4b3da432d7a26d8d801ff9d5718701521` |
| `corpus/ground_truth_sources/eh_multiple.cpp` | `7b3cc0e687132f70957e55dbbaa5c479d6a4864fde0e11cb49df0c600d6f2665` |
| `corpus/ground_truth_sources/exceptions.cpp` | `fd15c6bd23f39262a9aa02f94f02210dacab53a2a5d358aae415bba2c329394e` |
| `corpus/ground_truth_sources/floating_point.c` | `ff00c63ae76817932bdd0b4a5b0a0c8bc661e03314889d1eef404e580279bb89` |
| `corpus/ground_truth_sources/globals.c` | `e4fbe6bc2a51161e651a23264f5de4e90d052b2e9efcbcea1c1ff76a748528c4` |
| `corpus/ground_truth_sources/indirect_calls.c` | `b9b6dc58d6912bf8a54c46868a5a61b321447c9826660dfb29f76f741b21b92e` |
| `corpus/ground_truth_sources/loops.c` | `d929c2eb356d9e45d27aa9a9e9929d1ce3fad324d8843d7e53e4dbe7dabe9262` |
| `corpus/ground_truth_sources/member_pointers.cpp` | `8e84a7254ebeda7ec4db40335350606cf26227868e20be7db4f4382cdd3e9f69` |
| `corpus/ground_truth_sources/multiple_inheritance.cpp` | `2fc99918de8375a035774b6cff12866defb77d2095bf1a6005b6419c4afc4410` |
| `corpus/ground_truth_sources/static_initializers.cpp` | `5566d58941846d63fafa6e6047f5f0a70dd19ff484aea58f1eac88cfa1c3156c` |
| `corpus/ground_truth_sources/structs.c` | `0b29f69d01886989d3d34fb430acb259ca55c604b8b59c968e5d341972102280` |
| `corpus/ground_truth_sources/switch_dense.c` | `2a696a875c034a89e16a9b28359f6603942c536954321bc7403a9b780d24546f` |
| `corpus/ground_truth_sources/tail_calls.c` | `874edb70e2470cafdd6bed6a7a05519da95c926d1b0777622d1fba726194ddb3` |
| `corpus/ground_truth_sources/templates.cpp` | `cd18fc097a4bbbacacff6685edb8c5e6a0dfe7d8e27a68eb0b0febad6508194b` |
| `corpus/ground_truth_sources/tls.c` | `9f917229ae42021f4045f2f56af5ac3116987dc442e304c1b9b6b441200ba54b` |
| `corpus/ground_truth_sources/unions.c` | `2906ac1f944da7f6020756df9f20451048f8e2ed81ed5ac6ea06554afe1c7f60` |
| `corpus/ground_truth_sources/varargs.c` | `3326edfa00e59cd41f5409c8ef01d1d5b96c0e1a13471972a2a107725032cdbb` |
| `corpus/ground_truth_sources/vectorizable.c` | `4e71d283a0479bd5264da8f235bdb4f434a1b841289d9eac335c8b997be10f43` |
| `corpus/ground_truth_sources/virtual_inheritance.cpp` | `c8e83579cd4d6159e716c23270110d997349e3b1a609bf1d50c0b93a2e64d1d2` |
