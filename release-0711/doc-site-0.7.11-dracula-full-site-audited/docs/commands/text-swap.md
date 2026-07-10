---
title: x86decomp text-swap
description: Parser-derived command reference page for `text-swap`.
---

# `x86decomp text-swap`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `build` | `reconstruction` |
| `inject` | `reconstruction` |
| `plan` | `reconstruction` |
| `verify` | `reconstruction` |
## Parser help

```text
usage: x86decomp text-swap [-h] [--project PROJECT] [--actor ACTOR]
                           {build,inject,plan,verify} ...

Canonical text-swap commands implemented by the current capability subsystem.

positional arguments:
  {build,inject,plan,verify}
    build               build command
    inject              inject command
    plan                plan command
    verify              verify command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```
