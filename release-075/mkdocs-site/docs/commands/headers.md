---
title: x86decomp headers
description: Exact parser-derived reference for x86decomp headers in 0.7.5.
---

# `x86decomp headers`

Canonical capability group with 7 routes. Shared group options are shown in every exact usage string.

## `x86decomp headers create`

usage: x86decomp headers create [-h] [--visibility VISIBILITY] path

### Usage

```text
x86decomp headers create [-h] [--visibility VISIBILITY] path
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required. No help text is declared; parser destination is `path`. |
| `--visibility` | default: `'private'`. No help text is declared; parser destination is `visibility`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp headers cycles`

usage: x86decomp headers cycles [-h]

### Usage

```text
x86decomp headers cycles [-h]
```

No route-specific arguments are declared.

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp headers declare`

usage: x86decomp headers declare [-h] [--kind KIND] [--confidence CONFIDENCE]

### Usage

```text
x86decomp headers declare [-h] [--kind KIND] [--confidence CONFIDENCE]
                                 [--evidence-json EVIDENCE_JSON]
                                 header_id symbol_id declaration
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `header_id` | required. No help text is declared; parser destination is `header_id`. |
| `symbol_id` | required. No help text is declared; parser destination is `symbol_id`. |
| `declaration` | required. No help text is declared; parser destination is `declaration`. |
| `--kind` | default: `'function'`. No help text is declared; parser destination is `kind`. |
| `--confidence` | default: `1.0` · type: `float`. No help text is declared; parser destination is `confidence`. |
| `--evidence-json` | declared. No help text is declared; parser destination is `evidence_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp headers explain`

usage: x86decomp headers explain [-h] header_id

### Usage

```text
x86decomp headers explain [-h] header_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `header_id` | required. No help text is declared; parser destination is `header_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp headers include`

usage: x86decomp headers include [-h] --reason REASON

### Usage

```text
x86decomp headers include [-h] --reason REASON
                                 source_header_id target_header_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `source_header_id` | required. No help text is declared; parser destination is `source_header_id`. |
| `target_header_id` | required. No help text is declared; parser destination is `target_header_id`. |
| `--reason` | required. No help text is declared; parser destination is `reason`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp headers synthesize`

usage: x86decomp headers synthesize [-h] [--output-root OUTPUT_ROOT] header_id

### Usage

```text
x86decomp headers synthesize [-h] [--output-root OUTPUT_ROOT] header_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `header_id` | required. No help text is declared; parser destination is `header_id`. |
| `--output-root` | declared. No help text is declared; parser destination is `output_root`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp headers validate`

usage: x86decomp headers validate [-h] header_id

### Usage

```text
x86decomp headers validate [-h] header_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `header_id` | required. No help text is declared; parser destination is `header_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
