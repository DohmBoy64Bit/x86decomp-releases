---
title: x86decomp reloc
description: Parser-derived command reference page for `reloc`.
---

# `x86decomp reloc`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `inspect` | `assembly` |
| `resolve` | `assembly` |
| `supported` | `assembly` |
## Parser help

```text
usage: x86decomp reloc [-h] [--project PROJECT] [--actor ACTOR]
                       {inspect,resolve,supported} ...

Canonical reloc commands implemented by the current capability subsystem.

positional arguments:
  {inspect,resolve,supported}
    inspect             inspect command
    resolve             resolve command
    supported           supported command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```
