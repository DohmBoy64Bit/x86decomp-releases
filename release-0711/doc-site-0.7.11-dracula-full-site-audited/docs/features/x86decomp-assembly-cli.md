---
title: x86decomp.assembly.cli
description: Module reference for x86decomp.assembly.cli.
---

# `x86decomp.assembly.cli`

- Area: `toolkit`
- Source path: `src/x86decomp/assembly/cli.py`
- SHA-256: `819bc8a11f0cdce8301add84c746d290057aaa1748cc4628901558073294a788`
- Size: `10322` bytes
- Lines: `260`

## Module docstring

Provide the current runtime implementation for the `x86decomp.assembly.cli` module.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_json_file` | 21 | Load and parse JSON content from a filesystem path. |
| function | `_json_array` | 29 | Support json array processing for internal toolkit callers. |
| function | `_int` | 42 | Support int processing for internal toolkit callers. |
| function | `_emit` | 47 | Support emit processing for internal toolkit callers. |
| function | `build_parser` | 54 | Build the argparse parser for this command surface. |
| function | `dispatch` | 143 | Dispatch parsed command arguments to the matching implementation. |
| function | `main` | 246 | Run the command-line entry point and return its process status. |
