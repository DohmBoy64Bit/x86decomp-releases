---
title: x86decomp hypothesis
description: Exact parser-derived reference for x86decomp hypothesis in 0.7.5.
---

# `x86decomp hypothesis`

Canonical capability group with 7 routes. Shared group options are shown in every exact usage string.

## `x86decomp hypothesis create`

usage: x86decomp hypothesis create [-h] --origin ORIGIN

### Usage

```text
x86decomp hypothesis create [-h] --origin ORIGIN
                                   statement scope_kind scope_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `statement` | required. No help text is declared; parser destination is `statement`. |
| `scope_kind` | required. No help text is declared; parser destination is `scope_kind`. |
| `scope_id` | required. No help text is declared; parser destination is `scope_id`. |
| `--origin` | required. No help text is declared; parser destination is `origin`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp hypothesis dependency`

usage: x86decomp hypothesis dependency [-h] hypothesis_id depends_on_id

### Usage

```text
x86decomp hypothesis dependency [-h] hypothesis_id depends_on_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `hypothesis_id` | required. No help text is declared; parser destination is `hypothesis_id`. |
| `depends_on_id` | required. No help text is declared; parser destination is `depends_on_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp hypothesis evidence`

usage: x86decomp hypothesis evidence [-h] --stance STANCE --weight WEIGHT

### Usage

```text
x86decomp hypothesis evidence [-h] --stance STANCE --weight WEIGHT
                                     --kind KIND --group GROUP
                                     [--artifact-sha256 ARTIFACT_SHA256]
                                     [--details-json DETAILS_JSON]
                                     hypothesis_id evidence_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `hypothesis_id` | required. No help text is declared; parser destination is `hypothesis_id`. |
| `evidence_id` | required. No help text is declared; parser destination is `evidence_id`. |
| `--stance` | required. No help text is declared; parser destination is `stance`. |
| `--weight` | required · type: `float`. No help text is declared; parser destination is `weight`. |
| `--kind` | required. No help text is declared; parser destination is `kind`. |
| `--group` | required · default: `'hypothesis'`. No help text is declared; parser destination is `group`. |
| `--artifact-sha256` | declared. No help text is declared; parser destination is `artifact_sha256`. |
| `--details-json` | declared. No help text is declared; parser destination is `details_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp hypothesis gate`

usage: x86decomp hypothesis gate [-h] hypothesis_id

### Usage

```text
x86decomp hypothesis gate [-h] hypothesis_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `hypothesis_id` | required. No help text is declared; parser destination is `hypothesis_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp hypothesis list`

usage: x86decomp hypothesis list [-h] [--state STATE] [--scope-id SCOPE_ID]

### Usage

```text
x86decomp hypothesis list [-h] [--state STATE] [--scope-id SCOPE_ID]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--state` | declared. No help text is declared; parser destination is `state`. |
| `--scope-id` | declared. No help text is declared; parser destination is `scope_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp hypothesis show`

usage: x86decomp hypothesis show [-h] hypothesis_id

### Usage

```text
x86decomp hypothesis show [-h] hypothesis_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `hypothesis_id` | required. No help text is declared; parser destination is `hypothesis_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp hypothesis transition`

usage: x86decomp hypothesis transition [-h] --reason REASON [--lock]

### Usage

```text
x86decomp hypothesis transition [-h] --reason REASON [--lock]
                                       hypothesis_id state
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `hypothesis_id` | required. No help text is declared; parser destination is `hypothesis_id`. |
| `state` | required. No help text is declared; parser destination is `state`. |
| `--reason` | required. No help text is declared; parser destination is `reason`. |
| `--lock` | default: `False` · nargs: `0`. No help text is declared; parser destination is `lock`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
