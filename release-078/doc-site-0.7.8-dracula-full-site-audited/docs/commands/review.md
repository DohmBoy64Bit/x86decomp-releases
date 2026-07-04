---
title: x86decomp review
description: Command reference for `x86decomp review`.
---


# `x86decomp review`

Canonical review commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp review [-h] [--project PROJECT] [--actor ACTOR]
                        {assign,create,decide,list,lock,show} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `assign` | `usage: x86decomp review assign [-h] review_id assignee` | `governance` |
| `create` | `usage: x86decomp review create [-h] [--priority PRIORITY] [--details-json DETAILS_JSON] kind subject_id summary` | `governance` |
| `decide` | `usage: x86decomp review decide [-h] --rationale RATIONALE [--lock] review_id decision` | `governance` |
| `list` | `usage: x86decomp review list [-h] [--status STATUS] [--limit LIMIT]` | `governance` |
| `lock` | `usage: x86decomp review lock [-h] review_id` | `governance` |
| `show` | `usage: x86decomp review show [-h] review_id` | `governance` |

### `x86decomp review assign`

```text
usage: x86decomp review assign [-h] review_id assignee
```

| Argument | Details |
| --- | --- |
| `review_id` | required. |
| `assignee` | required. |

### `x86decomp review create`

```text
usage: x86decomp review create [-h] [--priority PRIORITY]
                               [--details-json DETAILS_JSON]
                               kind subject_id summary
```

| Argument | Details |
| --- | --- |
| `kind` | required. |
| `subject_id` | required. |
| `summary` | required. |
| `--priority` | type: `int` · default: `50`. |
| `--details-json` | — |

### `x86decomp review decide`

```text
usage: x86decomp review decide [-h] --rationale RATIONALE [--lock]
                               review_id decision
```

| Argument | Details |
| --- | --- |
| `review_id` | required. |
| `decision` | required. |
| `--rationale` | required. |
| `--lock` | nargs: `0` · default: `False`. |

### `x86decomp review list`

```text
usage: x86decomp review list [-h] [--status STATUS] [--limit LIMIT]
```

| Argument | Details |
| --- | --- |
| `--status` | — |
| `--limit` | type: `int` · default: `100`. |

### `x86decomp review lock`

```text
usage: x86decomp review lock [-h] review_id
```

| Argument | Details |
| --- | --- |
| `review_id` | required. |

### `x86decomp review show`

```text
usage: x86decomp review show [-h] review_id
```

| Argument | Details |
| --- | --- |
| `review_id` | required. |


