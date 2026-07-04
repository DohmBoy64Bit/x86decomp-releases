---
title: x86decomp text-swap
description: Command reference for `x86decomp text-swap`.
---


# `x86decomp text-swap`

Canonical text-swap commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp text-swap [-h] [--project PROJECT] [--actor ACTOR]
                           {build,inject,plan,verify} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `build` | `usage: x86decomp text-swap build [-h] --original ORIGINAL [--section-name SECTION_NAME] replacement output` | `reconstruction` |
| `inject` | `usage: x86decomp text-swap inject [-h] [--output OUTPUT] plan` | `reconstruction` |
| `plan` | `usage: x86decomp text-swap plan [-h] [--section-name SECTION_NAME] original replacement output` | `reconstruction` |
| `verify` | `usage: x86decomp text-swap verify [-h] [--output OUTPUT] plan image` | `reconstruction` |

### `x86decomp text-swap build`

```text
usage: x86decomp text-swap build [-h] --original ORIGINAL
                                 [--section-name SECTION_NAME]
                                 replacement output
```

| Argument | Details |
| --- | --- |
| `replacement` | required. |
| `output` | required. |
| `--original` | required. |
| `--section-name` | default: `'.text'`. |

### `x86decomp text-swap inject`

```text
usage: x86decomp text-swap inject [-h] [--output OUTPUT] plan
```

| Argument | Details |
| --- | --- |
| `plan` | required. |
| `--output` | — |

### `x86decomp text-swap plan`

```text
usage: x86decomp text-swap plan [-h] [--section-name SECTION_NAME]
                                original replacement output
```

| Argument | Details |
| --- | --- |
| `original` | required. |
| `replacement` | required. |
| `output` | required. |
| `--section-name` | default: `'.text'`. |

### `x86decomp text-swap verify`

```text
usage: x86decomp text-swap verify [-h] [--output OUTPUT] plan image
```

| Argument | Details |
| --- | --- |
| `plan` | required. |
| `image` | required. |
| `--output` | — |


