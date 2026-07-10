---
title: x86decomp image-text
description: Parser-derived command reference page for `image-text`.
---

# `x86decomp image-text`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `compose` | `reconstruction` |
## Parser help

```text
usage: x86decomp image-text [-h] [--project PROJECT] [--actor ACTOR]
                            {compose} ...

Canonical image-text commands implemented by the current capability subsystem.

positional arguments:
  {compose}
    compose          compose command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```
