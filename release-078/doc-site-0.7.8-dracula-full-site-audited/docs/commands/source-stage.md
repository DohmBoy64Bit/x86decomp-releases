---
title: x86decomp source-stage
description: Command reference for `x86decomp source-stage`.
---


# `x86decomp source-stage`

Canonical source-stage commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp source-stage [-h] [--project PROJECT] [--actor ACTOR]
                              {classify} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `classify` | `usage: x86decomp source-stage classify [-h] [--output OUTPUT]` | `reconstruction` |

### `x86decomp source-stage classify`

```text
usage: x86decomp source-stage classify [-h] [--output OUTPUT]
```

| Argument | Details |
| --- | --- |
| `--output` | — |


