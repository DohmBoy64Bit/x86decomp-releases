# Concept Overview

x86decomp is an evidence-governed toolkit for static analysis, reconstruction, and bounded
validation of native x86 PE32 and x86-64 PE32+ artifacts. This page maps every concept to its
chapter so you can find the right documentation quickly.

## Concept Map

| Concept | Description | Page |
|---|---|---|
| **Decompilation Modes** | Matching (binary-identical), functional (behaviorally equivalent), or hybrid. `default_modes: ["matching", "functional"]`. | [Decompilation Modes](decompilation-modes.md) |
| **Evidence System** | 7 evidence kinds, 3-evidence / 3-group / 2-kind requirement. Claims progress through proposed → corroborated → verified → rejected. | [Evidence and Claims](evidence-and-claims.md) |
| **Matching vs Functional Status** | Two independent state machines track byte-identity and behavioral correctness per function. | [Matching vs Functional](matching-vs-functional.md) |
| **Compiler Laboratory** | Matrix experiments across compiler profiles. `pe_function` and `file` targets. `compare_pe_function_to_coff_symbol` scoring. | [Compiler Laboratory](compiler-laboratory.md) |
| **Linker Reconstruction** | MAP files → COMDAT resolution → COFF correlation → reconstruction plans → relink manifests. | [Linker Reconstruction](linker-reconstruction.md) |
| **ABI and Types** | ABI contracts (calling convention, register usage, stack args), type constraints, C++ vtable/scaffolding recovery. | [ABI and Types](abi-and-types.md) |
| **Static Analysis** | PE parsing, disassembly, COFF analysis, MSVC metadata scanning (RTTI, vtables, unwind, TLS), linker map analysis, COMDAT resolution. | [Static Analysis](static-analysis.md) |
| **Reproducibility** | `reproduce-create` captures project files, tool identities, configs. `reproduce-verify` checks against current state. | [Reproducibility](reproducibility.md) |
| **Local LLM** | 6 provider presets. Loopback-only by default. Match loop: generate → compile → COFF extract → relocation resolve → byte compare. | [Local LLM](local-llm.md) |
| **Ghidra Integration** | 3 Java exporters, MCP client (stdio + Streamable HTTP), read-only with memory-logging, mutation gate with allowlist. | [Ghidra Integration](ghidra-integration.md) |

## Architecture at a Glance

```
 ┌─────────────────────────────────────────────────────────────────┐
 │                         x86decomp                                │
 ├───────────┬───────────┬───────────┬───────────┬─────────────────┤
 │  Binary   │  Analysis │  Compile  │ Validate  │  Reconstruction │
 │  Analysis │           │           │           │                 │
 ├───────────┼───────────┼───────────┼───────────┼─────────────────┤
 │ inspect-pe│crosscheck │  compile  │diff-bytes │  linker-plan    │
 │ pdb-      │ -ghidra   │ compiler- │diff-func  │  image-match    │
 │  inspect  │ coff-     │  lab      │dynamic-   │  relink         │
 │ metadata- │  inspect  │ compile-  │ validate  │  patch-image    │
 │  scan     │ coff-     │  worker   │symbolic-  │  harness-       │
 │ target-   │  extract  │ toolchain │ validate  │  generate       │
 │  pack     │           │           │abi-check  │  cpp-recover    │
 │           │           │           │angr-      │                 │
 │           │           │           │ validate  │                 │
 │           │           │           │objdiff-run│                 │
 ├───────────┴───────────┴───────────┴───────────┴─────────────────┤
 │                    Evidence & Governance                         │
 │  evidence-add  claim-create  claim-verify  memory-add           │
 ├─────────────────────────────────────────────────────────────────┤
 │                    Workflow & Pipeline                           │
 │  workflow-init  workflow-update  pipeline-run                   │
 │  work-create    work-claim       work-validate                  │
 └─────────────────────────────────────────────────────────────────┘
```

!!! tip "Toolkit executable"
    All commands are invoked through the single `x86decomp` executable. Run `x86decomp --help`
    for the full command list, or `x86decomp <command> --help` for per-command syntax.

## How the Concepts Connect

1. **Project initialization** (`x86decomp init`) creates the directory layout. A `project.json`
   records the binary path, architecture, and hashes.

2. **Static analysis** feeds the **evidence system**: PE parsing produces `binary_bytes` evidence,
   disassembly yields `static_analysis` evidence, Ghidra exports produce `external_document` links.

3. **Compiler laboratory** answers "which compiler profile produces the closest output?" before you
   invest manual effort. Results become `compiler_output` evidence.

4. **Matching decompilation** chases byte-identical reproduction. Each function moves through
   `not_started → decompiled → compiles → abi_compatible → instruction_similar → byte_matched →
   image_integrated → full_relink_validated`.

5. **Functional decompilation** validates behavior, not bytes. A function can be
   `differentially_validated` or `symbolically_bounded` without ever being `byte_matched`.

6. **The evidence gate** requires every claim to be backed by 3 evidence records from 3 independent
   groups across 2 evidence kinds before it can be `verified`.

7. **Reproducibility manifests** lock the entire project state for audit and portability.

8. **Local LLM** can propose C source; acceptance requires byte-identity through the complete
   compile→COFF→relocate→compare pipeline.

9. **Ghidra integration** provides external analysis via MCP. Mutations require proposal hashes and
   allowlist approval.

## Command Families

| Family | Purpose | Example Commands |
|---|---|---|
| Project | Creation, verification, migration | `init`, `verify-project`, `project-migrate` |
| Binary Analysis | PE, PDB, COFF, disassembly | `inspect-pe`, `pdb-inspect`, `coff-inspect`, `disassemble` |
| Compilation | Compile, matrix experiments | `compile`, `compiler-lab`, `compile-worker` |
| Validation | Byte, function, dynamic, symbolic | `diff-bytes`, `diff-function`, `dynamic-validate`, `symbolic-validate` |
| Reconstruction | Linker, image, patching | `linker-plan`, `image-match`, `relink`, `patch-image` |
| Workflow | Function state, work queue, evidence | `workflow-init`, `work-create`, `evidence-add`, `claim-verify` |
| Ghidra | Export, MCP read/mutate | `ghidra-export`, `mcp-read`, `mcp-propose`, `mcp-commit` |
| Local LLM | Profile creation, generation, matching | `llm-profile-create`, `llm-generate`, `llm-match-loop` |
| Reproducibility | Manifest creation and verification | `reproduce-create`, `reproduce-verify` |
| Security | Audit, SBOM, release verification | `security-audit`, `sbom-generate`, `release-manifest-verify` |
