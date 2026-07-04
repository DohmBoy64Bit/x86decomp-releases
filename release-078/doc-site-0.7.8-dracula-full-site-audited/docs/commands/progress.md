---
title: x86decomp progress
description: Command reference for `x86decomp progress`.
---


# `x86decomp progress`

Canonical progress commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp progress [-h] [--project PROJECT] [--actor ACTOR]
                          {reconcile} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `reconcile` | `usage: x86decomp progress reconcile [-h] [--output OUTPUT]` | `reconstruction` |

### `x86decomp progress reconcile`

```text
usage: x86decomp progress reconcile [-h] [--output OUTPUT]
```

| Argument | Details |
| --- | --- |
| `--output` | — |


