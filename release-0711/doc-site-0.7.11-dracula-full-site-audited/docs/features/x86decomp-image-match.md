---
title: x86decomp.image_match
description: Module reference for x86decomp.image_match.
---

# `x86decomp.image_match`

- Area: `toolkit`
- Source path: `src/x86decomp/image_match.py`
- SHA-256: `e4a53eae89cdc55df81e579ead9ff5f386d632c0a1ff9dd75e61489348d095ae`
- Size: `13364` bytes
- Lines: `295`

## Module docstring

Target-specific whole-image matching and deterministic normalization.

A layout profile records which PE fields are expected to match exactly and which
build-produced fields may be normalized.  The matcher never promotes a
normalized match to an exact byte-identical match.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `ByteRange` | 21 | Store validated byte range fields used by toolkit reports and adapters. |
| function | `to_dict` | 27 | Return a serializable dictionary representation. |
| function | `_pe_offsets` | 32 | Support pe offsets processing for internal toolkit callers. |
| function | `derive_layout_profile` | 55 | Execute the derive layout profile operation for the current toolkit workflow. |
| function | `_mask_ranges` | 95 | Support mask ranges processing for internal toolkit callers. |
| function | `_rva_to_file_offset` | 105 | Support rva to file offset processing for internal toolkit callers. |
| function | `_profile_ranges` | 116 | Support profile ranges processing for internal toolkit callers. |
| function | `_apply_rebase` | 152 | Support apply rebase processing for internal toolkit callers. |
| function | `_mismatches` | 181 | Support mismatches processing for internal toolkit callers. |
| function | `compare_whole_images` | 195 | Compare whole images for the current toolkit workflow. |
