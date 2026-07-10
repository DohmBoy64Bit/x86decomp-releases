---
title: x86decomp.canonical
description: Module reference for x86decomp.canonical.
---

# `x86decomp.canonical`

- Area: `toolkit`
- Source path: `src/x86decomp/canonical.py`
- SHA-256: `3dd78fd485ff2f9b8fb939d5ab00ed68a23c84f0b36db048a709a4f05ac8df1c`
- Size: `9295` bytes
- Lines: `236`

## Module docstring

Provide the current runtime implementation for the `x86decomp.canonical` module.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_subparsers` | 65 | Support subparsers processing for internal toolkit callers. |
| function | `_source_parsers` | 73 | Support source parsers processing for internal toolkit callers. |
| function | `_group_parsers` | 81 | Support group parsers processing for internal toolkit callers. |
| function | `_leaf_parsers` | 90 | Support leaf parsers processing for internal toolkit callers. |
| function | `_route_owner` | 99 | Support route owner processing for internal toolkit callers. |
| function | `canonical_routes` | 120 | Execute the canonical routes operation for the current toolkit workflow. |
| function | `canonical_groups` | 132 | Execute the canonical groups operation for the current toolkit workflow. |
| function | `command_catalog` | 137 | Execute the command catalog operation for the current toolkit workflow. |
| function | `register_canonical_commands` | 161 | Execute the register canonical commands operation for the current toolkit workflow. |
| function | `dispatch` | 205 | Dispatch parsed command arguments to the matching implementation. |
| function | `build_parser` | 215 | Build the argparse parser for this command surface. |
| function | `main` | 226 | Run the command-line entry point and return its process status. |
