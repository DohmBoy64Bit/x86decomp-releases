---
title: x86decomp diff
description: Command reference for `x86decomp diff`.
---


# `x86decomp diff`

Canonical diff commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp diff [-h] [--project PROJECT] [--actor ACTOR] {explain} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `explain` | `usage: x86decomp diff explain [-h] [--source SOURCE] [--output OUTPUT] diff_report` | `reconstruction` |

### `x86decomp diff explain`

```text
usage: x86decomp diff explain [-h] [--source SOURCE] [--output OUTPUT]
                              diff_report
```

| Argument | Details |
| --- | --- |
| `diff_report` | required. |
| `--source` | — |
| `--output` | — |


