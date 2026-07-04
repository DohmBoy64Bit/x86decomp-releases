---
title: x86decomp source-map
description: Command reference for `x86decomp source-map`.
---


# `x86decomp source-map`

Canonical source-map commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp source-map [-h] [--project PROJECT] [--actor ACTOR]
                            {annotate,verify} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `annotate` | `usage: x86decomp source-map annotate [-h] [--binary BINARY] [--report REPORT] source_root` | `reconstruction` |
| `verify` | `usage: x86decomp source-map verify [-h] [--report REPORT] source_root` | `reconstruction` |

### `x86decomp source-map annotate`

```text
usage: x86decomp source-map annotate [-h] [--binary BINARY] [--report REPORT]
                                     source_root
```

| Argument | Details |
| --- | --- |
| `source_root` | required. |
| `--binary` | default: `'GAME'`. |
| `--report` | — |

### `x86decomp source-map verify`

```text
usage: x86decomp source-map verify [-h] [--report REPORT] source_root
```

| Argument | Details |
| --- | --- |
| `source_root` | required. |
| `--report` | — |


