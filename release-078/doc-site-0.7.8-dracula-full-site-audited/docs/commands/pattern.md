---
title: x86decomp pattern
description: Command reference for `x86decomp pattern`.
---


# `x86decomp pattern`

Canonical pattern commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp pattern [-h] [--project PROJECT] [--actor ACTOR]
                         {catalog,generate,match,promote,scan} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `catalog` | `usage: x86decomp pattern catalog [-h] [--output OUTPUT]` | `reconstruction` |
| `generate` | `usage: x86decomp pattern generate [-h] [--symbol-prefix SYMBOL_PREFIX] scan_report output` | `reconstruction` |
| `match` | `usage: x86decomp pattern match [-h] [--output OUTPUT] generation_report` | `reconstruction` |
| `promote` | `usage: x86decomp pattern promote [-h] --candidate CANDIDATE --report REPORT [--stage STAGE] [--output OUTPUT] [--overwrite] function_id` | `reconstruction` |
| `scan` | `usage: x86decomp pattern scan [-h] [--architecture {x86,x86_64}] [--output OUTPUT] root` | `reconstruction` |

### `x86decomp pattern catalog`

```text
usage: x86decomp pattern catalog [-h] [--output OUTPUT]
```

| Argument | Details |
| --- | --- |
| `--output` | — |

### `x86decomp pattern generate`

```text
usage: x86decomp pattern generate [-h] [--symbol-prefix SYMBOL_PREFIX]
                                  scan_report output
```

| Argument | Details |
| --- | --- |
| `scan_report` | required. |
| `output` | required. |
| `--symbol-prefix` | default: `'sub'`. |

### `x86decomp pattern match`

```text
usage: x86decomp pattern match [-h] [--output OUTPUT] generation_report
```

| Argument | Details |
| --- | --- |
| `generation_report` | required. |
| `--output` | — |

### `x86decomp pattern promote`

```text
usage: x86decomp pattern promote [-h] --candidate CANDIDATE --report REPORT
                                 [--stage STAGE] [--output OUTPUT]
                                 [--overwrite]
                                 function_id
```

| Argument | Details |
| --- | --- |
| `function_id` | required. |
| `--candidate` | required. |
| `--report` | required. |
| `--stage` | default: `'pattern'`. |
| `--output` | — |
| `--overwrite` | nargs: `0` · default: `False`. |

### `x86decomp pattern scan`

```text
usage: x86decomp pattern scan [-h] [--architecture {x86,x86_64}]
                              [--output OUTPUT]
                              root
```

| Argument | Details |
| --- | --- |
| `root` | required. |
| `--architecture` | choices: `x86`, `x86_64`. |
| `--output` | — |


