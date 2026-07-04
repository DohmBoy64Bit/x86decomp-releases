---
title: x86decomp asset
description: Command reference for `x86decomp asset`.
---


# `x86decomp asset`

Canonical asset commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp asset [-h] [--project PROJECT] [--actor ACTOR]
                       {inventory} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `inventory` | `usage: x86decomp asset inventory [-h] [--output OUTPUT] root` | `reconstruction` |

### `x86decomp asset inventory`

```text
usage: x86decomp asset inventory [-h] [--output OUTPUT] root
```

| Argument | Details |
| --- | --- |
| `root` | required. |
| `--output` | — |


