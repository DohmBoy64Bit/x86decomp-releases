# Source basis and upstream boundaries

The package is newly written orchestration and validation code. It does not vendor
Ghidra, Capstone, Unicorn, Z3, angr, DynamoRIO, objdiff, decomp.me, LIEF, RetDec or
third-party compiler binaries.

Architecture decisions are based on primary format/tool documentation and direct
executable tests. Important boundaries:

- Ghidra supplies static analysis, C markup and P-code; its output is not ground truth.
- linked PE base relocations are not the complete consumed COFF link-time relocation
  set, so normalization records exactly what was modeled.
- Capstone supplies decoding, not C type recovery or semantic proof.
- Unicorn supplies concrete emulation for the declared harness.
- Z3/angr results are bounded by the instruction, memory and path model.
- DynamoRIO coverage records observed execution only.
- linker and compiler behavior is identified by executable hash and declared command.

Before copying upstream code, review the exact revision and license. Tool names in this
repository denote optional integrations and do not imply endorsement.
