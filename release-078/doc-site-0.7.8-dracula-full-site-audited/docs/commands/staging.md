---
title: x86decomp staging
description: Command reference for `x86decomp staging`.
---


# `x86decomp staging`

Canonical staging commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp staging [-h] [--project PROJECT] [--actor ACTOR]
                         {compile-check,generate-context,resolve,scan,unresolved} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `compile-check` | `usage: x86decomp staging compile-check [-h] [--cwd CWD] [--timeout TIMEOUT] command_json` | `native` |
| `generate-context` | `usage: x86decomp staging generate-context [-h] output sources [sources ...]` | `native` |
| `resolve` | `usage: x86decomp staging resolve [-h] mapping_json` | `native` |
| `scan` | `usage: x86decomp staging scan [-h] sources [sources ...]` | `native` |
| `unresolved` | `usage: x86decomp staging unresolved [-h]` | `native` |

### `x86decomp staging compile-check`

```text
usage: x86decomp staging compile-check [-h] [--cwd CWD] [--timeout TIMEOUT]
                                       command_json
```

| Argument | Details |
| --- | --- |
| `command_json` | required. |
| `--cwd` | — |
| `--timeout` | type: `int` · default: `120`. |

### `x86decomp staging generate-context`

```text
usage: x86decomp staging generate-context [-h] output sources [sources ...]
```

| Argument | Details |
| --- | --- |
| `output` | required. |
| `sources` | required · nargs: `+`. |

### `x86decomp staging resolve`

```text
usage: x86decomp staging resolve [-h] mapping_json
```

| Argument | Details |
| --- | --- |
| `mapping_json` | required. |

### `x86decomp staging scan`

```text
usage: x86decomp staging scan [-h] sources [sources ...]
```

| Argument | Details |
| --- | --- |
| `sources` | required · nargs: `+`. |

### `x86decomp staging unresolved`

```text
usage: x86decomp staging unresolved [-h]
```


