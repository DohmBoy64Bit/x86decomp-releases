---
title: x86decomp worker
description: Exact parser-derived reference for x86decomp worker in 0.7.5.
---

# `x86decomp worker`

Canonical capability group with 5 routes. Shared group options are shown in every exact usage string.

## `x86decomp worker doctor`

usage: x86decomp worker doctor [-h] worker_id

### Usage

```text
x86decomp worker doctor [-h] worker_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `worker_id` | required. No help text is declared; parser destination is `worker_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp worker list`

usage: x86decomp worker list [-h] [--status STATUS]

### Usage

```text
x86decomp worker list [-h] [--status STATUS]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--status` | declared. No help text is declared; parser destination is `status`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp worker register`

usage: x86decomp worker register [-h] [--endpoint ENDPOINT]

### Usage

```text
x86decomp worker register [-h] [--endpoint ENDPOINT]
                                 [--environment-sha256 ENVIRONMENT_SHA256]
                                 name capabilities_json
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `name` | required. No help text is declared; parser destination is `name`. |
| `capabilities_json` | required. No help text is declared; parser destination is `capabilities_json`. |
| `--endpoint` | declared. No help text is declared; parser destination is `endpoint`. |
| `--environment-sha256` | declared. No help text is declared; parser destination is `environment_sha256`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp worker select`

usage: x86decomp worker select [-h] required_json

### Usage

```text
x86decomp worker select [-h] required_json
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `required_json` | required. No help text is declared; parser destination is `required_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp worker status`

usage: x86decomp worker status [-h] worker_id status

### Usage

```text
x86decomp worker status [-h] worker_id status
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `worker_id` | required. No help text is declared; parser destination is `worker_id`. |
| `status` | required. No help text is declared; parser destination is `status`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
