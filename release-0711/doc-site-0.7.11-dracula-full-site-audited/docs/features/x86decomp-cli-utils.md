---
title: x86decomp.cli_utils
description: Module reference for x86decomp.cli_utils.
---

# `x86decomp.cli_utils`

- Area: `toolkit`
- Source path: `src/x86decomp/cli_utils.py`
- SHA-256: `9b51fe87fa1e4b93d5cbae791655451f0c1bf467ea88013aa37fa1176d0c9c97`
- Size: `1279` bytes
- Lines: `39`

## Module docstring

Shared command-line JSON parsing and output helpers.

The toolkit has several capability-specific command parsers.  This module keeps
JSON argument diagnostics and deterministic JSON emission consistent across
those CLIs without changing their public command surface.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `parse_json_arg` | 15 | Parse an optional JSON command argument and return a caller-supplied default. |
| function | `emit_json` | 29 | Print a deterministic JSON representation of a command result. |
