---
title: x86decomp abi
description: Exact parser-derived reference for x86decomp abi in 0.7.5.
---

# `x86decomp abi`

Canonical capability group with 6 routes. Shared group options are shown in every exact usage string.

## `x86decomp abi compare`

usage: x86decomp abi compare [-h] left_id right_id

### Usage

```text
x86decomp abi compare [-h] left_id right_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `left_id` | required. No help text is declared; parser destination is `left_id`. |
| `right_id` | required. No help text is declared; parser destination is `right_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp abi export`

usage: x86decomp abi export [-h] contract_id output

### Usage

```text
x86decomp abi export [-h] contract_id output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `contract_id` | required. No help text is declared; parser destination is `contract_id`. |
| `output` | required. No help text is declared; parser destination is `output`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp abi recover`

usage: x86decomp abi recover [-h] --evidence-json EVIDENCE_JSON

### Usage

```text
x86decomp abi recover [-h] --evidence-json EVIDENCE_JSON
                             subject_kind subject_id architecture
                             contract_json
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `subject_kind` | required. No help text is declared; parser destination is `subject_kind`. |
| `subject_id` | required. No help text is declared; parser destination is `subject_id`. |
| `architecture` | required. No help text is declared; parser destination is `architecture`. |
| `contract_json` | required. No help text is declared; parser destination is `contract_json`. |
| `--evidence-json` | required. No help text is declared; parser destination is `evidence_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp abi shim`

usage: x86decomp abi shim [-h] [--kind KIND] contract_id source_path

### Usage

```text
x86decomp abi shim [-h] [--kind KIND] contract_id source_path
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `contract_id` | required. No help text is declared; parser destination is `contract_id`. |
| `source_path` | required. No help text is declared; parser destination is `source_path`. |
| `--kind` | default: `'wrapped'`. No help text is declared; parser destination is `kind`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp abi show`

usage: x86decomp abi show [-h] contract_id

### Usage

```text
x86decomp abi show [-h] contract_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `contract_id` | required. No help text is declared; parser destination is `contract_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp abi verify`

usage: x86decomp abi verify [-h] contract_id

### Usage

```text
x86decomp abi verify [-h] contract_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `contract_id` | required. No help text is declared; parser destination is `contract_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
