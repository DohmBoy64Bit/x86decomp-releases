---
title: x86decomp mod
description: Command reference for `x86decomp mod`.
---


# `x86decomp mod`

Canonical mod commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp mod [-h] [--project PROJECT] [--actor ACTOR]
                     {branch-init} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `branch-init` | `usage: x86decomp mod branch-init [-h] --baseline BASELINE [--output OUTPUT] name` | `reconstruction` |

### `x86decomp mod branch-init`

```text
usage: x86decomp mod branch-init [-h] --baseline BASELINE [--output OUTPUT]
                                 name
```

| Argument | Details |
| --- | --- |
| `name` | required. |
| `--baseline` | required. |
| `--output` | — |


