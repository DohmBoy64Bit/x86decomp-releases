---
title: x86decomp consensus
description: Exact parser-derived reference for x86decomp consensus in 0.7.5.
---

# `x86decomp consensus`

Canonical capability group with 5 routes. Shared group options are shown in every exact usage string.

## `x86decomp consensus conflicts`

usage: x86decomp consensus conflicts [-h]

### Usage

```text
x86decomp consensus conflicts [-h]
```

No route-specific arguments are declared.

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp consensus explain`

usage: x86decomp consensus explain [-h] subject_kind subject_id property_name

### Usage

```text
x86decomp consensus explain [-h] subject_kind subject_id property_name
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `subject_kind` | required. No help text is declared; parser destination is `subject_kind`. |
| `subject_id` | required. No help text is declared; parser destination is `subject_id`. |
| `property_name` | required. No help text is declared; parser destination is `property_name`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp consensus record`

usage: x86decomp consensus record [-h] --adapter ADAPTER

### Usage

```text
x86decomp consensus record [-h] --adapter ADAPTER
                                  --adapter-version ADAPTER_VERSION
                                  --evidence-id EVIDENCE_ID --group GROUP
                                  [--confidence CONFIDENCE]
                                  subject_kind subject_id property_name
                                  value_json
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `subject_kind` | required. No help text is declared; parser destination is `subject_kind`. |
| `subject_id` | required. No help text is declared; parser destination is `subject_id`. |
| `property_name` | required. No help text is declared; parser destination is `property_name`. |
| `value_json` | required. No help text is declared; parser destination is `value_json`. |
| `--adapter` | required. No help text is declared; parser destination is `adapter`. |
| `--adapter-version` | required. No help text is declared; parser destination is `adapter_version`. |
| `--evidence-id` | required. No help text is declared; parser destination is `evidence_id`. |
| `--group` | required · default: `'consensus'`. No help text is declared; parser destination is `group`. |
| `--confidence` | default: `1.0` · type: `float`. No help text is declared; parser destination is `confidence`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp consensus resolve`

usage: x86decomp consensus resolve [-h] --method METHOD --rationale RATIONALE

### Usage

```text
x86decomp consensus resolve [-h] --method METHOD --rationale RATIONALE
                                   [--lock]
                                   subject_kind subject_id property_name
                                   selected_value_json
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `subject_kind` | required. No help text is declared; parser destination is `subject_kind`. |
| `subject_id` | required. No help text is declared; parser destination is `subject_id`. |
| `property_name` | required. No help text is declared; parser destination is `property_name`. |
| `selected_value_json` | required. No help text is declared; parser destination is `selected_value_json`. |
| `--method` | required. No help text is declared; parser destination is `method`. |
| `--rationale` | required. No help text is declared; parser destination is `rationale`. |
| `--lock` | default: `False` · nargs: `0`. No help text is declared; parser destination is `lock`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp consensus scan`

usage: x86decomp consensus scan [-h] [--subject-kind SUBJECT_KIND]

### Usage

```text
x86decomp consensus scan [-h] [--subject-kind SUBJECT_KIND]
                                [--subject-id SUBJECT_ID]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--subject-kind` | declared. No help text is declared; parser destination is `subject_kind`. |
| `--subject-id` | declared. No help text is declared; parser destination is `subject_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
