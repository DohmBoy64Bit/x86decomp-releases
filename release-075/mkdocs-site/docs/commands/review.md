---
title: x86decomp review
description: Exact parser-derived reference for x86decomp review in 0.7.5.
---

# `x86decomp review`

Canonical capability group with 6 routes. Shared group options are shown in every exact usage string.

## `x86decomp review assign`

usage: x86decomp review assign [-h] review_id assignee

### Usage

```text
x86decomp review assign [-h] review_id assignee
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `review_id` | required. No help text is declared; parser destination is `review_id`. |
| `assignee` | required. No help text is declared; parser destination is `assignee`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp review create`

usage: x86decomp review create [-h] [--priority PRIORITY]

### Usage

```text
x86decomp review create [-h] [--priority PRIORITY]
                               [--details-json DETAILS_JSON]
                               kind subject_id summary
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `kind` | required. No help text is declared; parser destination is `kind`. |
| `subject_id` | required. No help text is declared; parser destination is `subject_id`. |
| `summary` | required. No help text is declared; parser destination is `summary`. |
| `--priority` | default: `50` · type: `int`. No help text is declared; parser destination is `priority`. |
| `--details-json` | declared. No help text is declared; parser destination is `details_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp review decide`

usage: x86decomp review decide [-h] --rationale RATIONALE [--lock]

### Usage

```text
x86decomp review decide [-h] --rationale RATIONALE [--lock]
                               review_id decision
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `review_id` | required. No help text is declared; parser destination is `review_id`. |
| `decision` | required. No help text is declared; parser destination is `decision`. |
| `--rationale` | required. No help text is declared; parser destination is `rationale`. |
| `--lock` | default: `False` · nargs: `0`. No help text is declared; parser destination is `lock`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp review list`

usage: x86decomp review list [-h] [--status STATUS] [--limit LIMIT]

### Usage

```text
x86decomp review list [-h] [--status STATUS] [--limit LIMIT]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--status` | declared. No help text is declared; parser destination is `status`. |
| `--limit` | default: `100` · type: `int`. No help text is declared; parser destination is `limit`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp review lock`

usage: x86decomp review lock [-h] review_id

### Usage

```text
x86decomp review lock [-h] review_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `review_id` | required. No help text is declared; parser destination is `review_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp review show`

usage: x86decomp review show [-h] review_id

### Usage

```text
x86decomp review show [-h] review_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `review_id` | required. No help text is declared; parser destination is `review_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
