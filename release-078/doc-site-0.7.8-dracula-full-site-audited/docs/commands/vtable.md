---
title: x86decomp vtable
description: Command reference for `x86decomp vtable`.
---


# `x86decomp vtable`

Canonical vtable commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp vtable [-h] [--project PROJECT] [--actor ACTOR] {recover} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `recover` | `usage: x86decomp vtable recover [-h] [--metadata-report METADATA_REPORT] --output OUTPUT image` | `reconstruction` |

### `x86decomp vtable recover`

```text
usage: x86decomp vtable recover [-h] [--metadata-report METADATA_REPORT]
                                --output OUTPUT
                                image
```

| Argument | Details |
| --- | --- |
| `image` | required. |
| `--metadata-report` | — |
| `--output` | required. |


