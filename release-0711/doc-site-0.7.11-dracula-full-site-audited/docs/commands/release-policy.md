---
title: x86decomp release-policy
description: Parser-derived command reference page for `release-policy`.
---

# `x86decomp release-policy`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `moddable-source` | `reconstruction` |
## Parser help

```text
usage: x86decomp release-policy [-h] [--project PROJECT] [--actor ACTOR]
                                {moddable-source} ...

Canonical release-policy commands implemented by the current capability
subsystem.

positional arguments:
  {moddable-source}
    moddable-source  moddable-source command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```
