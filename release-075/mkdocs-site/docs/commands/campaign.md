---
title: x86decomp campaign
description: Exact parser-derived reference for x86decomp campaign in 0.7.5.
---

# `x86decomp campaign`

Canonical capability group with 10 routes. Shared group options are shown in every exact usage string.

## `x86decomp campaign branch`

usage: x86decomp campaign branch [-h] [--parent PARENT] campaign_id name

### Usage

```text
x86decomp campaign branch [-h] [--parent PARENT] campaign_id name
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `campaign_id` | required. No help text is declared; parser destination is `campaign_id`. |
| `name` | required. No help text is declared; parser destination is `name`. |
| `--parent` | declared. No help text is declared; parser destination is `parent`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp campaign create`

usage: x86decomp campaign create [-h] [--budget-json BUDGET_JSON]

### Usage

```text
x86decomp campaign create [-h] [--budget-json BUDGET_JSON]
                                 [--policy-json POLICY_JSON]
                                 goal
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `goal` | required. No help text is declared; parser destination is `goal`. |
| `--budget-json` | declared. No help text is declared; parser destination is `budget_json`. |
| `--policy-json` | declared. No help text is declared; parser destination is `policy_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp campaign list`

usage: x86decomp campaign list [-h]

### Usage

```text
x86decomp campaign list [-h]
```

No route-specific arguments are declared.

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp campaign pause`

usage: x86decomp campaign pause [-h] campaign_id

### Usage

```text
x86decomp campaign pause [-h] campaign_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `campaign_id` | required. No help text is declared; parser destination is `campaign_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp campaign plan`

usage: x86decomp campaign plan [-h] campaign_id

### Usage

```text
x86decomp campaign plan [-h] campaign_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `campaign_id` | required. No help text is declared; parser destination is `campaign_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp campaign resume`

usage: x86decomp campaign resume [-h] campaign_id

### Usage

```text
x86decomp campaign resume [-h] campaign_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `campaign_id` | required. No help text is declared; parser destination is `campaign_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp campaign snapshot`

usage: x86decomp campaign snapshot [-h] campaign_id

### Usage

```text
x86decomp campaign snapshot [-h] campaign_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `campaign_id` | required. No help text is declared; parser destination is `campaign_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp campaign start`

usage: x86decomp campaign start [-h] campaign_id

### Usage

```text
x86decomp campaign start [-h] campaign_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `campaign_id` | required. No help text is declared; parser destination is `campaign_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp campaign status`

usage: x86decomp campaign status [-h] campaign_id

### Usage

```text
x86decomp campaign status [-h] campaign_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `campaign_id` | required. No help text is declared; parser destination is `campaign_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp campaign stop`

usage: x86decomp campaign stop [-h] campaign_id

### Usage

```text
x86decomp campaign stop [-h] campaign_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `campaign_id` | required. No help text is declared; parser destination is `campaign_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
