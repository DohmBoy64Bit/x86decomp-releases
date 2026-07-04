---
title: x86decomp project
description: Command reference for `x86decomp project`.
---


# `x86decomp project`

Canonical project commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp project [-h] [--project PROJECT] [--actor ACTOR]
                         {check,doctor-paths,explain-boundaries,export,health,init,synthesize-layout} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `check` | `usage: x86decomp project check [-h]` | `assembly` |
| `doctor-paths` | `usage: x86decomp project doctor-paths [-h] [--output OUTPUT] root` | `reconstruction` |
| `explain-boundaries` | `usage: x86decomp project explain-boundaries [-h] module_id` | `reconstruction` |
| `export` | `usage: x86decomp project export [-h] output` | `reconstruction` |
| `health` | `usage: x86decomp project health [-h] [--output OUTPUT]` | `reconstruction` |
| `init` | `usage: x86decomp project init [-h]` | `assembly` |
| `synthesize-layout` | `usage: x86decomp project synthesize-layout [-h] inventory_json` | `reconstruction` |

### `x86decomp project check`

```text
usage: x86decomp project check [-h]
```

### `x86decomp project doctor-paths`

```text
usage: x86decomp project doctor-paths [-h] [--output OUTPUT] root
```

| Argument | Details |
| --- | --- |
| `root` | required. |
| `--output` | — |

### `x86decomp project explain-boundaries`

```text
usage: x86decomp project explain-boundaries [-h] module_id
```

| Argument | Details |
| --- | --- |
| `module_id` | required. |

### `x86decomp project export`

```text
usage: x86decomp project export [-h] output
```

| Argument | Details |
| --- | --- |
| `output` | required. |

### `x86decomp project health`

```text
usage: x86decomp project health [-h] [--output OUTPUT]
```

| Argument | Details |
| --- | --- |
| `--output` | — |

### `x86decomp project init`

```text
usage: x86decomp project init [-h]
```

### `x86decomp project synthesize-layout`

```text
usage: x86decomp project synthesize-layout [-h] inventory_json
```

| Argument | Details |
| --- | --- |
| `inventory_json` | required. |


