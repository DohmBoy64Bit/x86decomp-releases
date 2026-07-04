---
title: x86decomp match
description: Command reference for `x86decomp match`.
---


# `x86decomp match`

Canonical match commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp match [-h] [--project PROJECT] [--actor ACTOR]
                       {batch,compare,mismatches,report} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `batch` | `usage: x86decomp match batch [-h] [--policy {exact,trailing-padding}] [--pad-bytes-json PAD_BYTES_JSON] original candidates_json` | `native` |
| `compare` | `usage: x86decomp match compare [-h] [--policy {exact,trailing-padding}] [--pad-bytes-json PAD_BYTES_JSON] [--protected-offsets-json PROTECTED_OFFSETS_JSON] original candidate` | `native` |
| `mismatches` | `usage: x86decomp match mismatches [-h] run_id` | `native` |
| `report` | `usage: x86decomp match report [-h] run_id` | `native` |

### `x86decomp match batch`

```text
usage: x86decomp match batch [-h] [--policy {exact,trailing-padding}]
                             [--pad-bytes-json PAD_BYTES_JSON]
                             original candidates_json
```

| Argument | Details |
| --- | --- |
| `original` | required. |
| `candidates_json` | required. |
| `--policy` | choices: `exact`, `trailing-padding` · default: `'trailing-padding'`. |
| `--pad-bytes-json` | — |

### `x86decomp match compare`

```text
usage: x86decomp match compare [-h] [--policy {exact,trailing-padding}]
                               [--pad-bytes-json PAD_BYTES_JSON]
                               [--protected-offsets-json PROTECTED_OFFSETS_JSON]
                               original candidate
```

| Argument | Details |
| --- | --- |
| `original` | required. |
| `candidate` | required. |
| `--policy` | choices: `exact`, `trailing-padding` · default: `'trailing-padding'`. |
| `--pad-bytes-json` | — |
| `--protected-offsets-json` | — |

### `x86decomp match mismatches`

```text
usage: x86decomp match mismatches [-h] run_id
```

| Argument | Details |
| --- | --- |
| `run_id` | required. |

### `x86decomp match report`

```text
usage: x86decomp match report [-h] run_id
```

| Argument | Details |
| --- | --- |
| `run_id` | required. |


