---
title: x86decomp runtime
description: Command reference for `x86decomp runtime`.
---


# `x86decomp runtime`

Canonical runtime commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp runtime [-h] [--project PROJECT] [--actor ACTOR]
                         {launch,map-crash,validate-image} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `launch` | `usage: x86decomp runtime launch [-h] [--argument ARGUMENT] [--timeout TIMEOUT] [--execute] image` | `native` |
| `map-crash` | `usage: x86decomp runtime map-crash [-h] rva` | `native` |
| `validate-image` | `usage: x86decomp runtime validate-image [-h] image` | `native` |

### `x86decomp runtime launch`

```text
usage: x86decomp runtime launch [-h] [--argument ARGUMENT] [--timeout TIMEOUT]
                                [--execute]
                                image
```

| Argument | Details |
| --- | --- |
| `image` | required. |
| `--argument` | default: `[]`. |
| `--timeout` | type: `int` · default: `10`. |
| `--execute` | nargs: `0` · default: `False`. |

### `x86decomp runtime map-crash`

```text
usage: x86decomp runtime map-crash [-h] rva
```

| Argument | Details |
| --- | --- |
| `rva` | required. |

### `x86decomp runtime validate-image`

```text
usage: x86decomp runtime validate-image [-h] image
```

| Argument | Details |
| --- | --- |
| `image` | required. |


