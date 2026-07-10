---
title: x86decomp provenance
description: Parser-derived command reference page for `provenance`.
---

# `x86decomp provenance`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `binary` | `reconstruction` |
| `export` | `reconstruction` |
| `record` | `reconstruction` |
| `source` | `reconstruction` |
## Parser help

```text
usage: x86decomp provenance [-h] [--project PROJECT] [--actor ACTOR]
                            {binary,export,record,source} ...

Canonical provenance commands implemented by the current capability subsystem.

positional arguments:
  {binary,export,record,source}
    binary              binary command
    export              export command
    record              record command
    source              source command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```
