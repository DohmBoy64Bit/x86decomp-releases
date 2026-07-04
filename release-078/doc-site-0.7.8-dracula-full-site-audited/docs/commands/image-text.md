---
title: x86decomp image-text
description: Command reference for `x86decomp image-text`.
---


# `x86decomp image-text`

Canonical image-text commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp image-text [-h] [--project PROJECT] [--actor ACTOR]
                            {compose} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `compose` | `usage: x86decomp image-text compose [-h] [--function-list FUNCTION_LIST] [--fallback-byte FALLBACK_BYTE] output` | `reconstruction` |

### `x86decomp image-text compose`

```text
usage: x86decomp image-text compose [-h] [--function-list FUNCTION_LIST]
                                    [--fallback-byte FALLBACK_BYTE]
                                    output
```

| Argument | Details |
| --- | --- |
| `output` | required. |
| `--function-list` | — |
| `--fallback-byte` | type: `custom` · default: `204`. |


