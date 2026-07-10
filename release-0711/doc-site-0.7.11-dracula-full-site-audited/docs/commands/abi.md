---
title: x86decomp abi
description: Parser-derived command reference page for `abi`.
---

# `x86decomp abi`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `compare` | `reconstruction` |
| `export` | `reconstruction` |
| `recover` | `reconstruction` |
| `shim` | `reconstruction` |
| `show` | `reconstruction` |
| `verify` | `reconstruction` |
## Parser help

```text
usage: x86decomp abi [-h] [--project PROJECT] [--actor ACTOR]
                     {compare,export,recover,shim,show,verify} ...

Canonical abi commands implemented by the current capability subsystem.

positional arguments:
  {compare,export,recover,shim,show,verify}
    compare             compare command
    export              export command
    recover             recover command
    shim                shim command
    show                show command
    verify              verify command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```
