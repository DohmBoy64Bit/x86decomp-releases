---
title: x86decomp source
description: Command reference for `x86decomp source`.
---


# `x86decomp source`

Canonical source commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp source [-h] [--project PROJECT] [--actor ACTOR]
                        {impact,lock,reconcile,unlock} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `impact` | `usage: x86decomp source impact [-h] path` | `reconstruction` |
| `lock` | `usage: x86decomp source lock [-h] --reason REASON path` | `reconstruction` |
| `reconcile` | `usage: x86decomp source reconcile [-h] [--before-sha256 BEFORE_SHA256] [--semantic {true,false}] path` | `reconstruction` |
| `unlock` | `usage: x86decomp source unlock [-h] path` | `reconstruction` |

### `x86decomp source impact`

```text
usage: x86decomp source impact [-h] path
```

| Argument | Details |
| --- | --- |
| `path` | required. |

### `x86decomp source lock`

```text
usage: x86decomp source lock [-h] --reason REASON path
```

| Argument | Details |
| --- | --- |
| `path` | required. |
| `--reason` | required. |

### `x86decomp source reconcile`

```text
usage: x86decomp source reconcile [-h] [--before-sha256 BEFORE_SHA256]
                                  [--semantic {true,false}]
                                  path
```

| Argument | Details |
| --- | --- |
| `path` | required. |
| `--before-sha256` | — |
| `--semantic` | choices: `true`, `false`. |

### `x86decomp source unlock`

```text
usage: x86decomp source unlock [-h] path
```

| Argument | Details |
| --- | --- |
| `path` | required. |


