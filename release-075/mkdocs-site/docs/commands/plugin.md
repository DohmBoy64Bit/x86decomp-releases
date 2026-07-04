---
title: x86decomp plugin
description: Exact parser-derived reference for x86decomp plugin in 0.7.5.
---

# `x86decomp plugin`

Canonical capability group with 5 routes. Shared group options are shown in every exact usage string.

## `x86decomp plugin doctor`

usage: x86decomp plugin doctor [-h] plugin_id

### Usage

```text
x86decomp plugin doctor [-h] plugin_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `plugin_id` | required. No help text is declared; parser destination is `plugin_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp plugin install`

usage: x86decomp plugin install [-h] manifest

### Usage

```text
x86decomp plugin install [-h] manifest
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `manifest` | required. No help text is declared; parser destination is `manifest`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp plugin invoke`

usage: x86decomp plugin invoke [-h] [--timeout TIMEOUT]

### Usage

```text
x86decomp plugin invoke [-h] [--timeout TIMEOUT]
                               plugin_id capability request_json
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `plugin_id` | required. No help text is declared; parser destination is `plugin_id`. |
| `capability` | required. No help text is declared; parser destination is `capability`. |
| `request_json` | required. No help text is declared; parser destination is `request_json`. |
| `--timeout` | default: `60` · type: `int`. No help text is declared; parser destination is `timeout`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp plugin list`

usage: x86decomp plugin list [-h]

### Usage

```text
x86decomp plugin list [-h]
```

No route-specific arguments are declared.

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp plugin validate`

usage: x86decomp plugin validate [-h] manifest

### Usage

```text
x86decomp plugin validate [-h] manifest
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `manifest` | required. No help text is declared; parser destination is `manifest`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
