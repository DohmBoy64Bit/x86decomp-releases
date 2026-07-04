---
title: x86decomp subsystem
description: Command reference for `x86decomp subsystem`.
---


# `x86decomp subsystem`

Canonical subsystem commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp subsystem [-h] [--project PROJECT] [--actor ACTOR]
                           {detect} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `detect` | `usage: x86decomp subsystem detect [-h] [--output OUTPUT] root` | `reconstruction` |

### `x86decomp subsystem detect`

```text
usage: x86decomp subsystem detect [-h] [--output OUTPUT] root
```

| Argument | Details |
| --- | --- |
| `root` | required. |
| `--output` | — |


