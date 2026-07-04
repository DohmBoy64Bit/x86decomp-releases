---
title: x86decomp abi
description: Command reference for `x86decomp abi`.
---


# `x86decomp abi`

Canonical abi commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp abi [-h] [--project PROJECT] [--actor ACTOR]
                     {compare,export,recover,shim,show,verify} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `compare` | `usage: x86decomp abi compare [-h] left_id right_id` | `reconstruction` |
| `export` | `usage: x86decomp abi export [-h] contract_id output` | `reconstruction` |
| `recover` | `usage: x86decomp abi recover [-h] --evidence-json EVIDENCE_JSON subject_kind subject_id architecture contract_json` | `reconstruction` |
| `shim` | `usage: x86decomp abi shim [-h] [--kind KIND] contract_id source_path` | `reconstruction` |
| `show` | `usage: x86decomp abi show [-h] contract_id` | `reconstruction` |
| `verify` | `usage: x86decomp abi verify [-h] contract_id` | `reconstruction` |

### `x86decomp abi compare`

```text
usage: x86decomp abi compare [-h] left_id right_id
```

| Argument | Details |
| --- | --- |
| `left_id` | required. |
| `right_id` | required. |

### `x86decomp abi export`

```text
usage: x86decomp abi export [-h] contract_id output
```

| Argument | Details |
| --- | --- |
| `contract_id` | required. |
| `output` | required. |

### `x86decomp abi recover`

```text
usage: x86decomp abi recover [-h] --evidence-json EVIDENCE_JSON
                             subject_kind subject_id architecture
                             contract_json
```

| Argument | Details |
| --- | --- |
| `subject_kind` | required. |
| `subject_id` | required. |
| `architecture` | required. |
| `contract_json` | required. |
| `--evidence-json` | required. |

### `x86decomp abi shim`

```text
usage: x86decomp abi shim [-h] [--kind KIND] contract_id source_path
```

| Argument | Details |
| --- | --- |
| `contract_id` | required. |
| `source_path` | required. |
| `--kind` | default: `'wrapped'`. |

### `x86decomp abi show`

```text
usage: x86decomp abi show [-h] contract_id
```

| Argument | Details |
| --- | --- |
| `contract_id` | required. |

### `x86decomp abi verify`

```text
usage: x86decomp abi verify [-h] contract_id
```

| Argument | Details |
| --- | --- |
| `contract_id` | required. |


