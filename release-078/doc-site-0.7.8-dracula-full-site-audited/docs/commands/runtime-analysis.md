---
title: x86decomp runtime-analysis
description: Command reference for `x86decomp runtime-analysis`.
---


# `x86decomp runtime-analysis`

Canonical runtime-analysis commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp runtime-analysis [-h] [--project PROJECT] [--actor ACTOR]
                                  {identify,match-library,quarantine} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `identify` | `usage: x86decomp runtime-analysis identify [-h] [--output OUTPUT]` | `reconstruction` |
| `match-library` | `usage: x86decomp runtime-analysis match-library [-h] [--output OUTPUT] library_inventory` | `reconstruction` |
| `quarantine` | `usage: x86decomp runtime-analysis quarantine [-h] [--output OUTPUT] identification_report` | `reconstruction` |

### `x86decomp runtime-analysis identify`

```text
usage: x86decomp runtime-analysis identify [-h] [--output OUTPUT]
```

| Argument | Details |
| --- | --- |
| `--output` | — |

### `x86decomp runtime-analysis match-library`

```text
usage: x86decomp runtime-analysis match-library [-h] [--output OUTPUT]
                                                library_inventory
```

| Argument | Details |
| --- | --- |
| `library_inventory` | required. |
| `--output` | — |

### `x86decomp runtime-analysis quarantine`

```text
usage: x86decomp runtime-analysis quarantine [-h] [--output OUTPUT]
                                             identification_report
```

| Argument | Details |
| --- | --- |
| `identification_report` | required. |
| `--output` | — |


