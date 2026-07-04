---
title: x86decomp game-pattern
description: Command reference for `x86decomp game-pattern`.
---


# `x86decomp game-pattern`

Canonical game-pattern commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp game-pattern [-h] [--project PROJECT] [--actor ACTOR]
                              {state-machine} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `state-machine` | `usage: x86decomp game-pattern state-machine [-h] [--output OUTPUT] root` | `reconstruction` |

### `x86decomp game-pattern state-machine`

```text
usage: x86decomp game-pattern state-machine [-h] [--output OUTPUT] root
```

| Argument | Details |
| --- | --- |
| `root` | required. |
| `--output` | — |


