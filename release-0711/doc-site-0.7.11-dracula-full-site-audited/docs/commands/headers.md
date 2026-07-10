---
title: x86decomp headers
description: Parser-derived command reference page for `headers`.
---

# `x86decomp headers`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `create` | `reconstruction` |
| `cycles` | `reconstruction` |
| `declare` | `reconstruction` |
| `explain` | `reconstruction` |
| `include` | `reconstruction` |
| `synthesize` | `reconstruction` |
| `synthesize-project` | `reconstruction` |
| `validate` | `reconstruction` |
## Parser help

```text
usage: x86decomp headers [-h] [--project PROJECT] [--actor ACTOR]
                         {create,cycles,declare,explain,include,synthesize,synthesize-project,validate} ...

Canonical headers commands implemented by the current capability subsystem.

positional arguments:
  {create,cycles,declare,explain,include,synthesize,synthesize-project,validate}
    create              create command
    cycles              cycles command
    declare             declare command
    explain             explain command
    include             include command
    synthesize          synthesize command
    synthesize-project  synthesize-project command
    validate            validate command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```
