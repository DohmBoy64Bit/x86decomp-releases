---
title: x86decomp capsule
description: Command reference for `x86decomp capsule`.
---


# `x86decomp capsule`

Canonical capsule commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp capsule [-h] [--project PROJECT] [--actor ACTOR]
                         {create,inspect,reproduce,verify} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `create` | `usage: x86decomp capsule create [-h] [--include INCLUDE] [--external-json EXTERNAL_JSON] name output` | `reconstruction` |
| `inspect` | `usage: x86decomp capsule inspect [-h] path` | `reconstruction` |
| `reproduce` | `usage: x86decomp capsule reproduce [-h] path destination` | `reconstruction` |
| `verify` | `usage: x86decomp capsule verify [-h] path` | `reconstruction` |

### `x86decomp capsule create`

```text
usage: x86decomp capsule create [-h] [--include INCLUDE]
                                [--external-json EXTERNAL_JSON]
                                name output
```

| Argument | Details |
| --- | --- |
| `name` | required. |
| `output` | required. |
| `--include` | default: `[]`. |
| `--external-json` | — |

### `x86decomp capsule inspect`

```text
usage: x86decomp capsule inspect [-h] path
```

| Argument | Details |
| --- | --- |
| `path` | required. |

### `x86decomp capsule reproduce`

```text
usage: x86decomp capsule reproduce [-h] path destination
```

| Argument | Details |
| --- | --- |
| `path` | required. |
| `destination` | required. |

### `x86decomp capsule verify`

```text
usage: x86decomp capsule verify [-h] path
```

| Argument | Details |
| --- | --- |
| `path` | required. |


