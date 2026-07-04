---
title: x86decomp triage
description: Command reference for `x86decomp triage`.
---


# `x86decomp triage`

Canonical triage commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp triage [-h] [--project PROJECT] [--actor ACTOR] {next} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `next` | `usage: x86decomp triage next [-h] [--goal {matching,playable}] [--limit LIMIT] [--output OUTPUT]` | `reconstruction` |

### `x86decomp triage next`

```text
usage: x86decomp triage next [-h] [--goal {matching,playable}] [--limit LIMIT]
                             [--output OUTPUT]
```

| Argument | Details |
| --- | --- |
| `--goal` | choices: `matching`, `playable` · default: `'matching'`. |
| `--limit` | type: `int` · default: `25`. |
| `--output` | — |


