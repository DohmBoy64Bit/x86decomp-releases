---
title: x86decomp.assembly.materialize
description: Source module reference for x86decomp.assembly.materialize.
---

# `x86decomp.assembly.materialize`

**Source path:** `src/x86decomp/assembly/materialize.py`  
**Documented symbols:** 16

| Symbol | Kind | Line | End line | Docstring summary |
| --- | --- | ---: | ---: | --- |
| `AssemblerError` | class | 21 | 26 | Assembler failure with source line numbers retained for focused fallback. |
| `__init__` | function | 24 | 26 | — |
| `InstructionCandidate` | class | 30 | 42 | — |
| `end` | function | 41 | 42 | — |
| `_capstone` | function | 45 | 51 | — |
| `_safe_symbol` | function | 54 | 55 | — |
| `_preferred_addresses` | function | 58 | 72 | — |
| `_replace_address_token` | function | 75 | 84 | — |
| `_instruction_candidates` | function | 87 | 179 | — |
| `_render_source_with_line_map` | function | 182 | 213 | — |
| `_render_source` | function | 216 | 231 | — |
| `discover_assembler` | function | 234 | 254 | — |
| `assemble_coff` | function | 257 | 306 | — |
| `_unit_for_offset` | function | 309 | 310 | — |
| `verify_existing_source` | function | 313 | 368 | Assemble an existing source file and verify its resolved bytes exactly. |
| `materialize_function` | function | 371 | 603 | Materialize readable assembly and prove exact bytes, falling back per instruction. |
