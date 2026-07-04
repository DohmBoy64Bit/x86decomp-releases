---
title: x86decomp candidate
description: Exact parser-derived reference for x86decomp candidate in 0.7.5.
---

# `x86decomp candidate`

Canonical capability group with 7 routes. Shared group options are shown in every exact usage string.

## `x86decomp candidate add-file`

usage: x86decomp candidate add-file [-h] candidate_id source relative_path

### Usage

```text
x86decomp candidate add-file [-h] candidate_id source relative_path
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `candidate_id` | required. No help text is declared; parser destination is `candidate_id`. |
| `source` | required. No help text is declared; parser destination is `source`. |
| `relative_path` | required. No help text is declared; parser destination is `relative_path`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp candidate compare`

usage: x86decomp candidate compare [-h] left_id right_id

### Usage

```text
x86decomp candidate compare [-h] left_id right_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `left_id` | required. No help text is declared; parser destination is `left_id`. |
| `right_id` | required. No help text is declared; parser destination is `right_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp candidate create`

usage: x86decomp candidate create [-h] [--campaign-id CAMPAIGN_ID]

### Usage

```text
x86decomp candidate create [-h] [--campaign-id CAMPAIGN_ID]
                                  [--parent PARENT]
                                  [--objective-json OBJECTIVE_JSON]
                                  branch_name
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `branch_name` | required. No help text is declared; parser destination is `branch_name`. |
| `--campaign-id` | declared. No help text is declared; parser destination is `campaign_id`. |
| `--parent` | declared. No help text is declared; parser destination is `parent`. |
| `--objective-json` | declared. No help text is declared; parser destination is `objective_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp candidate evaluate`

usage: x86decomp candidate evaluate [-h] [--value VALUE]

### Usage

```text
x86decomp candidate evaluate [-h] [--value VALUE]
                                    [--details-json DETAILS_JSON]
                                    candidate_id metric status
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `candidate_id` | required. No help text is declared; parser destination is `candidate_id`. |
| `metric` | required. No help text is declared; parser destination is `metric`. |
| `status` | required. No help text is declared; parser destination is `status`. |
| `--value` | type: `float`. No help text is declared; parser destination is `value`. |
| `--details-json` | declared. No help text is declared; parser destination is `details_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp candidate list`

usage: x86decomp candidate list [-h] [--campaign-id CAMPAIGN_ID]

### Usage

```text
x86decomp candidate list [-h] [--campaign-id CAMPAIGN_ID]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--campaign-id` | declared. No help text is declared; parser destination is `campaign_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp candidate show`

usage: x86decomp candidate show [-h] candidate_id

### Usage

```text
x86decomp candidate show [-h] candidate_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `candidate_id` | required. No help text is declared; parser destination is `candidate_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp candidate transition`

usage: x86decomp candidate transition [-h] --reason REASON candidate_id state

### Usage

```text
x86decomp candidate transition [-h] --reason REASON candidate_id state
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `candidate_id` | required. No help text is declared; parser destination is `candidate_id`. |
| `state` | required. No help text is declared; parser destination is `state`. |
| `--reason` | required. No help text is declared; parser destination is `reason`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
