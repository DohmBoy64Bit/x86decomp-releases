---
title: x86decomp function
description: Command reference for `x86decomp function`.
---


# `x86decomp function`

Canonical function commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp function [-h] [--project PROJECT] [--actor ACTOR]
                          {classify,discover,reconcile,sort} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `classify` | `usage: x86decomp function classify [-h] [--output OUTPUT] functions_json` | `reconstruction` |
| `discover` | `usage: x86decomp function discover [-h] [--profile {prologue,ret-boundary}] [--architecture {x86,x86_64}] [--min-size MIN_SIZE] [--max-size MAX_SIZE] [--align ALIGN] [--output OUTPUT] image` | `reconstruction` |
| `reconcile` | `usage: x86decomp function reconcile [-h] [--output OUTPUT] reports [reports ...]` | `reconstruction` |
| `sort` | `usage: x86decomp function sort [-h] [--key KEY] [--output OUTPUT] functions_json` | `reconstruction` |

### `x86decomp function classify`

```text
usage: x86decomp function classify [-h] [--output OUTPUT] functions_json
```

| Argument | Details |
| --- | --- |
| `functions_json` | required. |
| `--output` | — |

### `x86decomp function discover`

```text
usage: x86decomp function discover [-h] [--profile {prologue,ret-boundary}]
                                   [--architecture {x86,x86_64}]
                                   [--min-size MIN_SIZE] [--max-size MAX_SIZE]
                                   [--align ALIGN] [--output OUTPUT]
                                   image
```

| Argument | Details |
| --- | --- |
| `image` | required. |
| `--profile` | choices: `prologue`, `ret-boundary` · default: `'prologue'`. |
| `--architecture` | choices: `x86`, `x86_64` · default: `'x86'`. |
| `--min-size` | type: `int` · default: `1`. |
| `--max-size` | type: `int` · default: `1048576`. |
| `--align` | type: `int` · default: `1`. |
| `--output` | — |

### `x86decomp function reconcile`

```text
usage: x86decomp function reconcile [-h] [--output OUTPUT]
                                    reports [reports ...]
```

| Argument | Details |
| --- | --- |
| `reports` | required · nargs: `+`. |
| `--output` | — |

### `x86decomp function sort`

```text
usage: x86decomp function sort [-h] [--key KEY] [--output OUTPUT]
                               functions_json
```

| Argument | Details |
| --- | --- |
| `functions_json` | required. |
| `--key` | default: `'rva'`. |
| `--output` | — |


