---
title: x86decomp runtime
---

# `x86decomp runtime`

Canonical runtime commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp runtime [-h] [--project PROJECT] [--actor ACTOR]
                         {launch,map-crash,validate-image} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `launch` | `usage: x86decomp runtime launch [-h] [--argument ARGUMENT] [--timeout TIMEOUT] [--execute] image` |
| `map-crash` | `usage: x86decomp runtime map-crash [-h] rva` |
| `validate-image` | `usage: x86decomp runtime validate-image [-h] image` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp runtime launch` | `native` |
| `x86decomp runtime map-crash` | `native` |
| `x86decomp runtime validate-image` | `native` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
