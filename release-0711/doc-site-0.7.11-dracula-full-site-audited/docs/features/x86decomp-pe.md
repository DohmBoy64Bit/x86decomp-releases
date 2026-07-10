---
title: x86decomp.pe
description: Module reference for x86decomp.pe.
---

# `x86decomp.pe`

- Area: `toolkit`
- Source path: `src/x86decomp/pe.py`
- SHA-256: `3ebcfae28c9da57b446624277b20cfcde2a1c39960ba30cfb2c08a24b0db3c79`
- Size: `19710` bytes
- Lines: `382`

## Module docstring

Architecture-dispatching PE parser with PE32+ x86-64 support.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `TLS64Info` | 43 | Store validated t l s64 info fields used by toolkit reports and adapters. |
| function | `to_dict` | 53 | Return a serializable dictionary representation. |
| class | `RuntimeFunction` | 67 | Store validated runtime function fields used by toolkit reports and adapters. |
| function | `to_dict` | 73 | Return a serializable dictionary representation. |
| class | `PE64Image` | 83 | Store validated p e64 image fields used by toolkit reports and adapters. |
| function | `entry_va` | 113 | Execute the entry va operation for the current toolkit workflow. |
| function | `to_dict` | 117 | Return a serializable dictionary representation. |
| function | `_parse_imports64` | 158 | Support parse imports64 processing for internal toolkit callers. |
| function | `_parse_tls64` | 192 | Support parse tls64 processing for internal toolkit callers. |
| function | `_parse_delay_imports64` | 214 | Support parse delay imports64 processing for internal toolkit callers. |
| function | `to_rva` | 227 | Execute the to rva operation for the current toolkit workflow. |
| function | `_parse_load_config64` | 258 | Support parse load config64 processing for internal toolkit callers. |
| function | `_parse_runtime_functions` | 274 | Support parse runtime functions processing for internal toolkit callers. |
| function | `parse_pe64` | 285 | Parse pe64 for the current toolkit workflow. |
| function | `inspect_pe_kind` | 361 | Execute the inspect pe kind operation for the current toolkit workflow. |
| function | `parse_pe` | 374 | Parse pe for the current toolkit workflow. |
