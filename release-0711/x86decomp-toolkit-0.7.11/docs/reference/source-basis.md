# Source basis and upstream boundaries

The package is newly written orchestration and validation code. It does **not** vendor
Ghidra, Capstone, Unicorn, Z3, angr, DynamoRIO, objdiff, decomp.me, LIEF, RetDec or
third-party compiler binaries.

## Upstream boundaries

Architecture decisions are based on primary format/tool documentation and direct
executable tests. Important boundaries:

| Tool | Role | Limitation |
|---|---|---|
| **Ghidra** | Static analysis, C markup, P-code | Output is not ground truth |
| **Capstone** | Instruction decoding | Not C type recovery or semantic proof |
| **Unicorn** | Concrete emulation | For the declared harness only |
| **Z3 / angr** | Symbolic execution | Bounded by instruction, memory, and path model |
| **DynamoRIO** | Coverage recording | Observed execution only |
| **PE relocations** | Linked base relocations | Not the complete consumed COFF link-time relocation set — normalization records exactly what was modeled |
| **Compiler/linker** | Build toolchain | Identified by executable hash and declared command |

!!! warning "Before copying upstream code"
    Review the exact revision and license. Tool names in this repository denote optional
    integrations and do not imply endorsement.
