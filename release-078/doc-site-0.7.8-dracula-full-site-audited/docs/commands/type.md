---
title: x86decomp type
description: Command reference for `x86decomp type`.
---


# `x86decomp type`

Canonical type commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp type [-h] [--project PROJECT] [--actor ACTOR] {propagate} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `propagate` | `usage: x86decomp type propagate [-h] [--output OUTPUT]` | `reconstruction` |

### `x86decomp type propagate`

```text
usage: x86decomp type propagate [-h] [--output OUTPUT]
```

| Argument | Details |
| --- | --- |
| `--output` | — |


