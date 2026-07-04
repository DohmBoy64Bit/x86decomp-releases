---
title: x86decomp graph
description: Exact parser-derived reference for x86decomp graph in 0.7.5.
---

# `x86decomp graph`

Canonical capability group with 3 routes. Shared group options are shown in every exact usage string.

## `x86decomp graph edge`

usage: x86decomp graph edge [-h] [--attributes-json ATTRIBUTES_JSON]

### Usage

```text
x86decomp graph edge [-h] [--attributes-json ATTRIBUTES_JSON]
                            source_id target_id relation
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `source_id` | required. No help text is declared; parser destination is `source_id`. |
| `target_id` | required. No help text is declared; parser destination is `target_id`. |
| `relation` | required. No help text is declared; parser destination is `relation`. |
| `--attributes-json` | declared. No help text is declared; parser destination is `attributes_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp graph impact`

usage: x86decomp graph impact [-h] [--direction DIRECTION]

### Usage

```text
x86decomp graph impact [-h] [--direction DIRECTION]
                              [--max-depth MAX_DEPTH] [--relations RELATIONS]
                              node_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `node_id` | required. No help text is declared; parser destination is `node_id`. |
| `--direction` | default: `'outbound'`. No help text is declared; parser destination is `direction`. |
| `--max-depth` | default: `8` · type: `int`. No help text is declared; parser destination is `max_depth`. |
| `--relations` | declared. No help text is declared; parser destination is `relations`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp graph node`

usage: x86decomp graph node [-h] [--attributes-json ATTRIBUTES_JSON]

### Usage

```text
x86decomp graph node [-h] [--attributes-json ATTRIBUTES_JSON]
                            node_id kind label
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `node_id` | required. No help text is declared; parser destination is `node_id`. |
| `kind` | required. No help text is declared; parser destination is `kind`. |
| `label` | required. No help text is declared; parser destination is `label`. |
| `--attributes-json` | declared. No help text is declared; parser destination is `attributes_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
