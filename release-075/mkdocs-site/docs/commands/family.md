---
title: x86decomp family
description: Exact parser-derived reference for x86decomp family in 0.7.5.
---

# `x86decomp family`

Canonical capability group with 4 routes. Shared group options are shown in every exact usage string.

## `x86decomp family add`

usage: x86decomp family add [-h] [--metadata-json METADATA_JSON]

### Usage

```text
x86decomp family add [-h] [--metadata-json METADATA_JSON]
                            family_id label path
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `family_id` | required. No help text is declared; parser destination is `family_id`. |
| `label` | required. No help text is declared; parser destination is `label`. |
| `path` | required. No help text is declared; parser destination is `path`. |
| `--metadata-json` | declared. No help text is declared; parser destination is `metadata_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp family correlate`

usage: x86decomp family correlate [-h] [--block-size BLOCK_SIZE]

### Usage

```text
x86decomp family correlate [-h] [--block-size BLOCK_SIZE]
                                  left_member_id right_member_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `left_member_id` | required. No help text is declared; parser destination is `left_member_id`. |
| `right_member_id` | required. No help text is declared; parser destination is `right_member_id`. |
| `--block-size` | default: `64` · type: `int`. No help text is declared; parser destination is `block_size`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp family create`

usage: x86decomp family create [-h] name

### Usage

```text
x86decomp family create [-h] name
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `name` | required. No help text is declared; parser destination is `name`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp family report`

usage: x86decomp family report [-h] family_id

### Usage

```text
x86decomp family report [-h] family_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `family_id` | required. No help text is declared; parser destination is `family_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
