---
title: x86decomp loop
description: Command reference for `x86decomp loop`.
---


# `x86decomp loop`

Canonical loop commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp loop [-h] [--project PROJECT] [--actor ACTOR]
                      {list,run,show} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `list` | `usage: x86decomp loop list [-h]` | `native` |
| `run` | `usage: x86decomp loop run [-h] [--symbol SYMBOL] [--policy POLICY] [--timeout TIMEOUT] [--execute] function_id source compile_command_json candidate original rva slot_size` | `native` |
| `show` | `usage: x86decomp loop show [-h] loop_id` | `native` |

### `x86decomp loop list`

```text
usage: x86decomp loop list [-h]
```

### `x86decomp loop run`

```text
usage: x86decomp loop run [-h] [--symbol SYMBOL] [--policy POLICY]
                          [--timeout TIMEOUT] [--execute]
                          function_id source compile_command_json candidate
                          original rva slot_size
```

| Argument | Details |
| --- | --- |
| `function_id` | required. |
| `source` | required. |
| `compile_command_json` | required. |
| `candidate` | required. |
| `original` | required. |
| `rva` | required. |
| `slot_size` | required · type: `int`. |
| `--symbol` | — |
| `--policy` | default: `'trailing-padding'`. |
| `--timeout` | type: `int` · default: `120`. |
| `--execute` | nargs: `0` · default: `False`. |

### `x86decomp loop show`

```text
usage: x86decomp loop show [-h] loop_id
```

| Argument | Details |
| --- | --- |
| `loop_id` | required. |


