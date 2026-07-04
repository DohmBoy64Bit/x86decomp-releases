---
title: x86decomp class
description: Command reference for `x86decomp class`.
---


# `x86decomp class`

Canonical class commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp class [-h] [--project PROJECT] [--actor ACTOR] {scaffold} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `scaffold` | `usage: x86decomp class scaffold [-h] [--headers HEADERS] vtable_report output` | `reconstruction` |

### `x86decomp class scaffold`

```text
usage: x86decomp class scaffold [-h] [--headers HEADERS] vtable_report output
```

| Argument | Details |
| --- | --- |
| `vtable_report` | required. |
| `output` | required. |
| `--headers` | — |


