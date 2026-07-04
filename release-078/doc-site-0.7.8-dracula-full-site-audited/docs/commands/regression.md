---
title: x86decomp regression
description: Command reference for `x86decomp regression`.
---


# `x86decomp regression`

Canonical regression commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp regression [-h] [--project PROJECT] [--actor ACTOR]
                            {compare} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `compare` | `usage: x86decomp regression compare [-h] [--allow ALLOW] [--output OUTPUT] baseline modded` | `reconstruction` |

### `x86decomp regression compare`

```text
usage: x86decomp regression compare [-h] [--allow ALLOW] [--output OUTPUT]
                                    baseline modded
```

| Argument | Details |
| --- | --- |
| `baseline` | required. |
| `modded` | required. |
| `--allow` | — |
| `--output` | — |


