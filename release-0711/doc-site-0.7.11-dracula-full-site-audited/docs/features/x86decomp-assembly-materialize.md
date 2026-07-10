---
title: x86decomp.assembly.materialize
description: Module reference for x86decomp.assembly.materialize.
---

# `x86decomp.assembly.materialize`

- Area: `toolkit`
- Source path: `src/x86decomp/assembly/materialize.py`
- SHA-256: `fc6ebc3aff941f6664c7e3b83b874401a86a1a1fc9608a587486046607b686a1`
- Size: `24112` bytes
- Lines: `617`

## Module docstring

Provide the current runtime implementation for the `x86decomp.assembly.materialize` module.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `AssemblerError` | 21 | Assembler failure with source line numbers retained for focused fallback. |
| function | `__init__` | 24 | Initialize the instance with validated constructor state. |
| class | `InstructionCandidate` | 31 | Store validated instruction candidate fields used by toolkit reports and adapters. |
| function | `end` | 43 | Execute the end operation for the current toolkit workflow. |
| function | `_capstone` | 48 | Support capstone processing for internal toolkit callers. |
| function | `_safe_symbol` | 58 | Support safe symbol processing for internal toolkit callers. |
| function | `_preferred_addresses` | 63 | Support preferred addresses processing for internal toolkit callers. |
| function | `_replace_address_token` | 81 | Support replace address token processing for internal toolkit callers. |
| function | `_instruction_candidates` | 94 | Support instruction candidates processing for internal toolkit callers. |
| function | `_render_source_with_line_map` | 190 | Support render source with line map processing for internal toolkit callers. |
| function | `_render_source` | 225 | Support render source processing for internal toolkit callers. |
| function | `discover_assembler` | 244 | Discover assembler for the current toolkit workflow. |
| function | `assemble_coff` | 268 | Execute the assemble coff operation for the current toolkit workflow. |
| function | `_unit_for_offset` | 321 | Support unit for offset processing for internal toolkit callers. |
| function | `verify_existing_source` | 326 | Assemble an existing source file and verify its resolved bytes exactly. |
| function | `materialize_function` | 384 | Materialize readable assembly and prove exact bytes, falling back per instruction. |
