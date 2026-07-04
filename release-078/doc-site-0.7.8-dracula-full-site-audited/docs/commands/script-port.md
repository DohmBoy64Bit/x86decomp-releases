---
title: x86decomp script-port
description: Command reference for `x86decomp script-port`.
---


# `x86decomp script-port`

Canonical script-port commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp script-port [-h] [--project PROJECT] [--actor ACTOR]
                             {audit} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `audit` | `usage: x86decomp script-port audit [-h] [--output OUTPUT] root` | `reconstruction` |

### `x86decomp script-port audit`

```text
usage: x86decomp script-port audit [-h] [--output OUTPUT] root
```

| Argument | Details |
| --- | --- |
| `root` | required. |
| `--output` | — |


