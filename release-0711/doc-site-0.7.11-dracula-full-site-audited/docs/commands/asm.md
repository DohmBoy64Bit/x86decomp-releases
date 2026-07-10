---
title: x86decomp asm
description: Parser-derived command reference page for `asm`.
---

# `x86decomp asm`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `annotate` | `assembly` |
| `batch` | `assembly` |
| `list` | `assembly` |
| `materialize` | `assembly` |
| `report` | `assembly` |
| `verify-roundtrip` | `assembly` |
## Parser help

```text
usage: x86decomp asm [-h] [--project PROJECT] [--actor ACTOR]
                     {annotate,batch,list,materialize,report,verify-roundtrip} ...

Canonical asm commands implemented by the current capability subsystem.

positional arguments:
  {annotate,batch,list,materialize,report,verify-roundtrip}
    annotate            annotate command
    batch               batch command
    list                list command
    materialize         materialize command
    report              report command
    verify-roundtrip    verify-roundtrip command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```
