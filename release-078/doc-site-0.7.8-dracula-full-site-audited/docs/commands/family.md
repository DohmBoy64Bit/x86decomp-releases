---
title: x86decomp family
description: Command reference for `x86decomp family`.
---


# `x86decomp family`

Canonical family commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp family [-h] [--project PROJECT] [--actor ACTOR]
                        {add,correlate,create,report} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `add` | `usage: x86decomp family add [-h] [--metadata-json METADATA_JSON] family_id label path` | `governance` |
| `correlate` | `usage: x86decomp family correlate [-h] [--block-size BLOCK_SIZE] left_member_id right_member_id` | `governance` |
| `create` | `usage: x86decomp family create [-h] name` | `governance` |
| `report` | `usage: x86decomp family report [-h] family_id` | `governance` |

### `x86decomp family add`

```text
usage: x86decomp family add [-h] [--metadata-json METADATA_JSON]
                            family_id label path
```

| Argument | Details |
| --- | --- |
| `family_id` | required. |
| `label` | required. |
| `path` | required. |
| `--metadata-json` | — |

### `x86decomp family correlate`

```text
usage: x86decomp family correlate [-h] [--block-size BLOCK_SIZE]
                                  left_member_id right_member_id
```

| Argument | Details |
| --- | --- |
| `left_member_id` | required. |
| `right_member_id` | required. |
| `--block-size` | type: `int` · default: `64`. |

### `x86decomp family create`

```text
usage: x86decomp family create [-h] name
```

| Argument | Details |
| --- | --- |
| `name` | required. |

### `x86decomp family report`

```text
usage: x86decomp family report [-h] family_id
```

| Argument | Details |
| --- | --- |
| `family_id` | required. |


