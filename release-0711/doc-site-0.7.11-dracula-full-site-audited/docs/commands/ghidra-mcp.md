---
title: x86decomp ghidra-mcp
description: Parser-derived command reference page for `ghidra-mcp`.
---

# `x86decomp ghidra-mcp`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `batch-decompile` | `reconstruction` |
| `decompile` | `reconstruction` |
| `functions` | `reconstruction` |
| `probe` | `reconstruction` |
| `sync-names` | `reconstruction` |
## Parser help

```text
usage: x86decomp ghidra-mcp [-h] [--project PROJECT] [--actor ACTOR]
                            {batch-decompile,decompile,functions,probe,sync-names} ...

Canonical ghidra-mcp commands implemented by the current capability subsystem.

positional arguments:
  {batch-decompile,decompile,functions,probe,sync-names}
    batch-decompile     batch-decompile command
    decompile           decompile command
    functions           functions command
    probe               probe command
    sync-names          sync-names command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```
