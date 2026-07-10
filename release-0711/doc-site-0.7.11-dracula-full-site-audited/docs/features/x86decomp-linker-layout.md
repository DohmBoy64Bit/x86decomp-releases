---
title: x86decomp.linker_layout
description: Module reference for x86decomp.linker_layout.
---

# `x86decomp.linker_layout`

- Area: `toolkit`
- Source path: `src/x86decomp/linker_layout.py`
- SHA-256: `695a3353f9f7b93e27e71f6a5ede51882b979997adb6fe47bd53946e87bd73fb`
- Size: `14783` bytes
- Lines: `366`

## Module docstring

MSVC linker-map parsing and object contribution layout reconstruction.

The parser accepts the text format emitted by LINK.EXE ``/MAP`` and LLD's
MSVC-compatible map writer.  It records segment groups, public symbols, object
contributions, preferred load address, and entry point.  Reconstruction is
explicitly evidence driven: a map file and actual COFF objects are required for
claims about original object ordering.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `MapSegment` | 35 | Store validated map segment fields used by toolkit reports and adapters. |
| function | `to_dict` | 43 | Return a serializable dictionary representation. |
| class | `MapContribution` | 55 | Store validated map contribution fields used by toolkit reports and adapters. |
| function | `to_dict` | 62 | Return a serializable dictionary representation. |
| class | `MapPublic` | 73 | Store validated map public fields used by toolkit reports and adapters. |
| function | `to_dict` | 82 | Return a serializable dictionary representation. |
| class | `LinkerMap` | 95 | Store validated linker map fields used by toolkit reports and adapters. |
| function | `to_dict` | 107 | Return a serializable dictionary representation. |
| function | `parse_msvc_map_text` | 126 | Parse msvc map text for the current toolkit workflow. |
| function | `parse_msvc_map` | 224 | Parse msvc map for the current toolkit workflow. |
| function | `_normalize_object_key` | 232 | Support normalize object key processing for internal toolkit callers. |
| function | `reconstruct_linker_layout` | 240 | Reconstruct linker layout for the current toolkit workflow. |
