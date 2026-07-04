---
title: x86decomp security
description: Exact parser-derived reference for x86decomp security in 0.7.5.
---

# `x86decomp security`

Canonical capability group with 4 routes. Shared group options are shown in every exact usage string.

## `x86decomp security finding`

usage: x86decomp security finding [-h] --evidence-json EVIDENCE_JSON

### Usage

```text
x86decomp security finding [-h] --evidence-json EVIDENCE_JSON
                                  rule_id severity subject_id summary
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `rule_id` | required. No help text is declared; parser destination is `rule_id`. |
| `severity` | required. No help text is declared; parser destination is `severity`. |
| `subject_id` | required. No help text is declared; parser destination is `subject_id`. |
| `summary` | required. No help text is declared; parser destination is `summary`. |
| `--evidence-json` | required. No help text is declared; parser destination is `evidence_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp security policy`

usage: x86decomp security policy [-h] name policy_json

### Usage

```text
x86decomp security policy [-h] name policy_json
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `name` | required. No help text is declared; parser destination is `name`. |
| `policy_json` | required. No help text is declared; parser destination is `policy_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp security report`

usage: x86decomp security report [-h]

### Usage

```text
x86decomp security report [-h]
```

No route-specific arguments are declared.

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp security scan`

usage: x86decomp security scan [-h] observations_json

### Usage

```text
x86decomp security scan [-h] observations_json
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `observations_json` | required. No help text is declared; parser destination is `observations_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
