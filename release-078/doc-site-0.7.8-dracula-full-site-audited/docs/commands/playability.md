---
title: x86decomp playability
description: Command reference for `x86decomp playability`.
---


# `x86decomp playability`

Canonical playability commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp playability [-h] [--project PROJECT] [--actor ACTOR]
                             {smoke-plan} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `smoke-plan` | `usage: x86decomp playability smoke-plan [-h] [--profile PROFILE] target output` | `reconstruction` |

### `x86decomp playability smoke-plan`

```text
usage: x86decomp playability smoke-plan [-h] [--profile PROFILE] target output
```

| Argument | Details |
| --- | --- |
| `target` | required. |
| `output` | required. |
| `--profile` | default: `'windows-game'`. |


