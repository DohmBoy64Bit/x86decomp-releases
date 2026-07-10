---
title: x86decomp source-map
description: Parser-derived command reference page for `source-map`.
---

# `x86decomp source-map`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `annotate` | `reconstruction` |
| `verify` | `reconstruction` |
## Parser help

```text
usage: x86decomp source-map [-h] [--project PROJECT] [--actor ACTOR]
                            {annotate,verify} ...

Canonical source-map commands implemented by the current capability subsystem.

positional arguments:
  {annotate,verify}
    annotate         annotate command
    verify           verify command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```
