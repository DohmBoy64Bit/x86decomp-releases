---
title: x86decomp loop
---

# `x86decomp loop`

Canonical loop commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp loop [-h] [--project PROJECT] [--actor ACTOR]
                      {list,run,show} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `list` | `usage: x86decomp loop list [-h]` |
| `run` | `usage: x86decomp loop run [-h] [--symbol SYMBOL] [--policy POLICY] [--timeout TIMEOUT] [--execute] function_id source compile_command_json candidate original rva slot_size` |
| `show` | `usage: x86decomp loop show [-h] loop_id` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp loop list` | `native` |
| `x86decomp loop run` | `native` |
| `x86decomp loop show` | `native` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
