---
title: x86decomp ghidra-mcp
---

# `x86decomp ghidra-mcp`

Canonical ghidra-mcp commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp ghidra-mcp [-h] [--project PROJECT] [--actor ACTOR]
                            {batch-decompile,decompile,functions,probe,sync-names} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `batch-decompile` | `usage: x86decomp ghidra-mcp batch-decompile [-h] [--timeout TIMEOUT] url addresses output` |
| `decompile` | `usage: x86decomp ghidra-mcp decompile [-h] [--timeout TIMEOUT] [--output OUTPUT] url address` |
| `functions` | `usage: x86decomp ghidra-mcp functions [-h] [--timeout TIMEOUT] [--output OUTPUT] url` |
| `probe` | `usage: x86decomp ghidra-mcp probe [-h] [--timeout TIMEOUT] [--output OUTPUT] url` |
| `sync-names` | `usage: x86decomp ghidra-mcp sync-names [-h] [--output OUTPUT] names_json` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp ghidra-mcp batch-decompile` | `reconstruction` |
| `x86decomp ghidra-mcp decompile` | `reconstruction` |
| `x86decomp ghidra-mcp functions` | `reconstruction` |
| `x86decomp ghidra-mcp probe` | `reconstruction` |
| `x86decomp ghidra-mcp sync-names` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
