---
title: x86decomp decompiler
description: Command reference for `x86decomp decompiler`.
---


# `x86decomp decompiler`

Canonical decompiler commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp decompiler [-h] [--project PROJECT] [--actor ACTOR]
                            {cleanup} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `cleanup` | `usage: x86decomp decompiler cleanup [-h] [--compiler COMPILER] [--language LANGUAGE] [--locals-at-top] input_file output` | `reconstruction` |

### `x86decomp decompiler cleanup`

```text
usage: x86decomp decompiler cleanup [-h] [--compiler COMPILER]
                                    [--language LANGUAGE] [--locals-at-top]
                                    input_file output
```

| Argument | Details |
| --- | --- |
| `input_file` | required. |
| `output` | required. |
| `--compiler` | default: `'generic'`. |
| `--language` | default: `'cpp'`. |
| `--locals-at-top` | nargs: `0` · default: `False`. |


