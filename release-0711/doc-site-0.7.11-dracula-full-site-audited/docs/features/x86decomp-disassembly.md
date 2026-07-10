---
title: x86decomp.disassembly
description: Module reference for x86decomp.disassembly.
---

# `x86decomp.disassembly`

- Area: `toolkit`
- Source path: `src/x86decomp/disassembly.py`
- SHA-256: `7beb7f66049ca498017a9180be738f35d1dea545e04bb8d6e69747f0e14e3754`
- Size: `11665` bytes
- Lines: `282`

## Module docstring

Independent Capstone-backed x86/x86-64 decoding and normalization.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_capstone` | 14 | Support capstone processing for internal toolkit callers. |
| class | `InstructionRecord` | 27 | Store validated instruction record fields used by toolkit reports and adapters. |
| function | `to_dict` | 39 | Return a serializable dictionary representation. |
| function | `_is_known_address` | 55 | Support is known address processing for internal toolkit callers. |
| function | `decode_instructions` | 60 | Decode instructions for the current toolkit workflow. |
| function | `control_flow_edges` | 149 | Execute the control flow edges operation for the current toolkit workflow. |
| function | `compare_instruction_streams` | 163 | Compare instruction streams for the current toolkit workflow. |
| function | `cross_check_ghidra_instructions` | 226 | Execute the cross check ghidra instructions operation for the current toolkit workflow. |
