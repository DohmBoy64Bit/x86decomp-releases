---
title: x86decomp.assembly.materialize
description: Source module reference for x86decomp.assembly.materialize.
---

# `x86decomp.assembly.materialize`

**Source path:** `src/x86decomp/assembly/materialize.py`  
**SHA-256:** `bd19d35efc03ca7bc501fe4b87a028a9c36131d3eeee4a7f98c6aad5bdab2324`  
**Documented symbols:** 16

| Symbol | Kind | Line | End line | Docstring summary |
| --- | --- | ---: | ---: | --- |
| `AssemblerError` | class | 21 | 26 | Assembler failure with source line numbers retained for focused fallback. |
| `__init__` | function | 24 | 26 | no docstring declared |
| `InstructionCandidate` | class | 30 | 42 | no docstring declared |
| `end` | function | 41 | 42 | no docstring declared |
| `_capstone` | function | 45 | 51 | no docstring declared |
| `_safe_symbol` | function | 54 | 55 | no docstring declared |
| `_preferred_addresses` | function | 58 | 72 | no docstring declared |
| `_replace_address_token` | function | 75 | 84 | no docstring declared |
| `_instruction_candidates` | function | 87 | 179 | no docstring declared |
| `_render_source_with_line_map` | function | 182 | 213 | no docstring declared |
| `_render_source` | function | 216 | 231 | no docstring declared |
| `discover_assembler` | function | 234 | 254 | no docstring declared |
| `assemble_coff` | function | 257 | 306 | no docstring declared |
| `_unit_for_offset` | function | 309 | 310 | no docstring declared |
| `verify_existing_source` | function | 313 | 368 | Assemble an existing source file and verify its resolved bytes exactly. |
| `materialize_function` | function | 371 | 603 | Materialize readable assembly and prove exact bytes, falling back per instruction. |
