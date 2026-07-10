---
title: x86decomp.symbolic
description: Module reference for x86decomp.symbolic.
---

# `x86decomp.symbolic`

- Area: `toolkit`
- Source path: `src/x86decomp/symbolic.py`
- SHA-256: `44313e4a9c3ba6fe819da4bad51d85ac75cc08357dcbe9d0678f8b8792ab3d68`
- Size: `37179` bytes
- Lines: `718`

## Module docstring

Bounded symbolic equivalence for small pure x86/x86-64 leaf functions.

The executor intentionally rejects instructions or addressing modes it cannot
model. A successful UNSAT result is therefore meaningful only for the modeled
instruction subset, configured inputs, explored paths, and selected outputs.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_deps` | 18 | Support deps processing for internal toolkit callers. |
| class | `UnsupportedSymbolicInstruction` | 31 | Coordinate unsupported symbolic instruction behavior for the current toolkit workflow. |
| class | `SymState` | 37 | Store validated sym state fields used by toolkit reports and adapters. |
| function | `clone` | 46 | Execute the clone operation for the current toolkit workflow. |
| class | `Outcome` | 59 | Store validated outcome fields used by toolkit reports and adapters. |
| function | `_aliases` | 93 | Support aliases processing for internal toolkit callers. |
| function | `_read_reg` | 98 | Support read reg processing for internal toolkit callers. |
| function | `_write_reg` | 111 | Support write reg processing for internal toolkit callers. |
| function | `_concrete` | 133 | Support concrete processing for internal toolkit callers. |
| function | `_memory_address` | 139 | Support memory address processing for internal toolkit callers. |
| function | `_read_memory` | 159 | Support read memory processing for internal toolkit callers. |
| function | `_write_memory` | 171 | Support write memory processing for internal toolkit callers. |
| function | `_read_operand` | 183 | Support read operand processing for internal toolkit callers. |
| function | `_write_operand` | 196 | Support write operand processing for internal toolkit callers. |
| function | `_coerce_pair` | 209 | Support coerce pair processing for internal toolkit callers. |
| function | `_set_logic_flags` | 219 | Support set logic flags processing for internal toolkit callers. |
| function | `_set_add_flags` | 227 | Support set add flags processing for internal toolkit callers. |
| function | `_set_sub_flags` | 240 | Support set sub flags processing for internal toolkit callers. |
| function | `_condition` | 253 | Support condition processing for internal toolkit callers. |
| function | `_condition_for_family` | 273 | Resolve Jcc, SETcc, and CMOVcc names through the same flag model. |
| function | `_set_adc_flags` | 297 | Support set adc flags processing for internal toolkit callers. |
| function | `_set_sbb_flags` | 314 | Support set sbb flags processing for internal toolkit callers. |
| function | `_is_sat` | 330 | Support is sat processing for internal toolkit callers. |
| function | `symbolic_execute` | 337 | Execute the symbolic execute operation for the current toolkit workflow. |
| function | `_constraint_formula` | 624 | Support constraint formula processing for internal toolkit callers. |
| function | `bounded_symbolic_compare` | 629 | Execute the bounded symbolic compare operation for the current toolkit workflow. |
| function | `bounded_symbolic_compare_files` | 709 | Execute the bounded symbolic compare files operation for the current toolkit workflow. |
