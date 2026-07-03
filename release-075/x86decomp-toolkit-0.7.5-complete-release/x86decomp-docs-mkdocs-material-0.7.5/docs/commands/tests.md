---
title: x86decomp tests
description: Exact parser-derived reference for x86decomp tests in 0.7.5.
---

# `x86decomp tests`

Canonical capability group with 5 routes. Shared group options are shown in every exact usage string.

## `x86decomp tests add`

usage: x86decomp tests add [-h] --applicability-json APPLICABILITY_JSON

### Usage

```text
x86decomp tests add [-h] --applicability-json APPLICABILITY_JSON
                           --evidence-json EVIDENCE_JSON
                           name scope_kind scope_id test_kind relative_path
                           content_file
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `name` | required. No help text is declared; parser destination is `name`. |
| `scope_kind` | required. No help text is declared; parser destination is `scope_kind`. |
| `scope_id` | required. No help text is declared; parser destination is `scope_id`. |
| `test_kind` | required. No help text is declared; parser destination is `test_kind`. |
| `relative_path` | required. No help text is declared; parser destination is `relative_path`. |
| `content_file` | required. No help text is declared; parser destination is `content_file`. |
| `--applicability-json` | required. No help text is declared; parser destination is `applicability_json`. |
| `--evidence-json` | required. No help text is declared; parser destination is `evidence_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp tests explain`

usage: x86decomp tests explain [-h] test_id

### Usage

```text
x86decomp tests explain [-h] test_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `test_id` | required. No help text is declared; parser destination is `test_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp tests list`

usage: x86decomp tests list [-h]

### Usage

```text
x86decomp tests list [-h]
```

No route-specific arguments are declared.

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp tests promote-counterexample`

usage: x86decomp tests promote-counterexample [-h] [--name NAME]

### Usage

```text
x86decomp tests promote-counterexample [-h] [--name NAME]
                                              counterexample_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `counterexample_id` | required. No help text is declared; parser destination is `counterexample_id`. |
| `--name` | declared. No help text is declared; parser destination is `name`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp tests synthesize`

usage: x86decomp tests synthesize [-h] [--name NAME] scope_kind scope_id

### Usage

```text
x86decomp tests synthesize [-h] [--name NAME] scope_kind scope_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `scope_kind` | required. No help text is declared; parser destination is `scope_kind`. |
| `scope_id` | required. No help text is declared; parser destination is `scope_id`. |
| `--name` | declared. No help text is declared; parser destination is `name`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
