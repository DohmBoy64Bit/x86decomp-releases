---
title: x86decomp pe
description: Command reference for `x86decomp pe`.
---


# `x86decomp pe`

Canonical pe commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp pe [-h] [--project PROJECT] [--actor ACTOR]
                    {export-coff,export-sections,inventory,patch-apply,patch-plan,text-swap} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `export-coff` | `usage: x86decomp pe export-coff [-h] [--section SECTION] image output` | `native` |
| `export-sections` | `usage: x86decomp pe export-sections [-h] [--section SECTION] image output` | `native` |
| `inventory` | `usage: x86decomp pe inventory [-h] image` | `native` |
| `patch-apply` | `usage: x86decomp pe patch-apply [-h] plan_id` | `native` |
| `patch-plan` | `usage: x86decomp pe patch-plan [-h] original output operations_json` | `native` |
| `text-swap` | `usage: x86decomp pe text-swap [-h] [--section-name SECTION_NAME] original replacement output` | `native` |

### `x86decomp pe export-coff`

```text
usage: x86decomp pe export-coff [-h] [--section SECTION] image output
```

| Argument | Details |
| --- | --- |
| `image` | required. |
| `output` | required. |
| `--section` | — |

### `x86decomp pe export-sections`

```text
usage: x86decomp pe export-sections [-h] [--section SECTION] image output
```

| Argument | Details |
| --- | --- |
| `image` | required. |
| `output` | required. |
| `--section` | — |

### `x86decomp pe inventory`

```text
usage: x86decomp pe inventory [-h] image
```

| Argument | Details |
| --- | --- |
| `image` | required. |

### `x86decomp pe patch-apply`

```text
usage: x86decomp pe patch-apply [-h] plan_id
```

| Argument | Details |
| --- | --- |
| `plan_id` | required. |

### `x86decomp pe patch-plan`

```text
usage: x86decomp pe patch-plan [-h] original output operations_json
```

| Argument | Details |
| --- | --- |
| `original` | required. |
| `output` | required. |
| `operations_json` | required. |

### `x86decomp pe text-swap`

```text
usage: x86decomp pe text-swap [-h] [--section-name SECTION_NAME]
                              original replacement output
```

| Argument | Details |
| --- | --- |
| `original` | required. |
| `replacement` | required. |
| `output` | required. |
| `--section-name` | default: `'.text'`. |


