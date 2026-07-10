---
title: x86decomp windows
description: Parser-derived command reference page for `windows`.
---

# `x86decomp windows`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `discover-ghidra` | `native` |
| `doctor` | `native` |
| `response-file` | `native` |
## Parser help

```text
usage: x86decomp windows [-h] [--project PROJECT] [--actor ACTOR]
                         {discover-ghidra,doctor,response-file} ...

Canonical windows commands implemented by the current capability subsystem.

positional arguments:
  {discover-ghidra,doctor,response-file}
    discover-ghidra     discover-ghidra command
    doctor              doctor command
    response-file       response-file command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```
