---
title: x86decomp release-policy
description: Command reference for `x86decomp release-policy`.
---


# `x86decomp release-policy`

Canonical release-policy commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp release-policy [-h] [--project PROJECT] [--actor ACTOR]
                                {moddable-source} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `moddable-source` | `usage: x86decomp release-policy moddable-source [-h] [--output OUTPUT]` | `reconstruction` |

### `x86decomp release-policy moddable-source`

```text
usage: x86decomp release-policy moddable-source [-h] [--output OUTPUT]
```

| Argument | Details |
| --- | --- |
| `--output` | — |


