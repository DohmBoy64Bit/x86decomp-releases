---
title: x86decomp.pdb
description: Module reference for x86decomp.pdb.
---

# `x86decomp.pdb`

- Area: `toolkit`
- Source path: `src/x86decomp/pdb.py`
- SHA-256: `cafd35f8251e24a91b6b01e36d651ef28b698fac11266a47c7daf9b5e9bd6179`
- Size: `26480` bytes
- Lines: `644`

## Module docstring

Bounded MSF 7.0 / PDB inventory and PE identity correlation.

This parser intentionally inventories stable container, PDB, TPI/IPI, and DBI metadata.
It does not claim complete CodeView type/symbol reconstruction. Every read is bounds checked,
stream blocks may be discontiguous, and unsupported variants fail explicitly.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_require` | 29 | Support require processing for internal toolkit callers. |
| function | `_u16` | 35 | Support u16 processing for internal toolkit callers. |
| function | `_u32` | 41 | Support u32 processing for internal toolkit callers. |
| function | `_cstring` | 47 | Support cstring processing for internal toolkit callers. |
| function | `_align4` | 57 | Support align4 processing for internal toolkit callers. |
| class | `PDBStream` | 63 | Store validated p d b stream fields used by toolkit reports and adapters. |
| function | `to_dict` | 70 | Return a serializable dictionary representation. |
| class | `PDBFile` | 81 | Store validated p d b file fields used by toolkit reports and adapters. |
| function | `to_dict` | 97 | Return a serializable dictionary representation. |
| class | `_MSF` | 129 | Coordinate m s f behavior for the current toolkit workflow. |
| function | `__init__` | 131 | Initialize the instance with validated constructor state. |
| function | `_block` | 159 | Support block processing for internal toolkit callers. |
| function | `_parse_directory` | 166 | Support parse directory processing for internal toolkit callers. |
| function | `stream` | 199 | Execute the stream operation for the current toolkit workflow. |
| function | `_parse_info` | 209 | Support parse info processing for internal toolkit callers. |
| function | `_parse_tpi` | 228 | Support parse tpi processing for internal toolkit callers. |
| function | `_parse_modules` | 276 | Support parse modules processing for internal toolkit callers. |
| function | `_parse_source_info` | 341 | Support parse source info processing for internal toolkit callers. |
| function | `_parse_section_contributions` | 390 | Support parse section contributions processing for internal toolkit callers. |
| function | `_parse_section_map` | 421 | Support parse section map processing for internal toolkit callers. |
| function | `_parse_dbi` | 453 | Support parse dbi processing for internal toolkit callers. |
| function | `_correlate_pe` | 566 | Support correlate pe processing for internal toolkit callers. |
| function | `parse_pdb_bytes` | 598 | Parse pdb bytes for the current toolkit workflow. |
| function | `parse_pdb` | 635 | Parse pdb for the current toolkit workflow. |
