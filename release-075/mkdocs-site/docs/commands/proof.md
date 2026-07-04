---
title: x86decomp proof
description: Exact parser-derived reference for x86decomp proof in 0.7.5.
---

# `x86decomp proof`

Canonical capability group with 6 routes. Shared group options are shown in every exact usage string.

## `x86decomp proof evaluate`

usage: x86decomp proof evaluate [-h] obligation_id

### Usage

```text
x86decomp proof evaluate [-h] obligation_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `obligation_id` | required. No help text is declared; parser destination is `obligation_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp proof export`

usage: x86decomp proof export [-h] [--include INCLUDE] output

### Usage

```text
x86decomp proof export [-h] [--include INCLUDE] output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `output` | required. No help text is declared; parser destination is `output`. |
| `--include` | default: `[]`. No help text is declared; parser destination is `include`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp proof inspect`

usage: x86decomp proof inspect [-h] path

### Usage

```text
x86decomp proof inspect [-h] path
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required. No help text is declared; parser destination is `path`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp proof obligation`

usage: x86decomp proof obligation [-h] [--assumptions-json ASSUMPTIONS_JSON]

### Usage

```text
x86decomp proof obligation [-h] [--assumptions-json ASSUMPTIONS_JSON]
                                  scope_kind scope_id property_name
                                  required_status
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `scope_kind` | required. No help text is declared; parser destination is `scope_kind`. |
| `scope_id` | required. No help text is declared; parser destination is `scope_id`. |
| `property_name` | required. No help text is declared; parser destination is `property_name`. |
| `required_status` | required. No help text is declared; parser destination is `required_status`. |
| `--assumptions-json` | declared. No help text is declared; parser destination is `assumptions_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp proof result`

usage: x86decomp proof result [-h] [--artifact-sha256 ARTIFACT_SHA256]

### Usage

```text
x86decomp proof result [-h] [--artifact-sha256 ARTIFACT_SHA256]
                              obligation_id status validator report_json
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `obligation_id` | required. No help text is declared; parser destination is `obligation_id`. |
| `status` | required. No help text is declared; parser destination is `status`. |
| `validator` | required. No help text is declared; parser destination is `validator`. |
| `report_json` | required. No help text is declared; parser destination is `report_json`. |
| `--artifact-sha256` | declared. No help text is declared; parser destination is `artifact_sha256`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp proof verify`

usage: x86decomp proof verify [-h] path

### Usage

```text
x86decomp proof verify [-h] path
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required. No help text is declared; parser destination is `path`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
