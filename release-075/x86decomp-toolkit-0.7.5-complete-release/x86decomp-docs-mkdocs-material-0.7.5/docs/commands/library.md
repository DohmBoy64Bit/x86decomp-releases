---
title: x86decomp library
description: Exact parser-derived reference for x86decomp library in 0.7.5.
---

# `x86decomp library`

Canonical capability group with 6 routes. Shared group options are shown in every exact usage string.

## `x86decomp library accept`

usage: x86decomp library accept [-h] match_id

### Usage

```text
x86decomp library accept [-h] match_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `match_id` | required. No help text is declared; parser destination is `match_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp library candidates`

usage: x86decomp library candidates [-h] subject_id

### Usage

```text
x86decomp library candidates [-h] subject_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `subject_id` | required. No help text is declared; parser destination is `subject_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp library externalize`

usage: x86decomp library externalize [-h] match_id

### Usage

```text
x86decomp library externalize [-h] match_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `match_id` | required. No help text is declared; parser destination is `match_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp library identify`

usage: x86decomp library identify [-h] [--version-range VERSION_RANGE]

### Usage

```text
x86decomp library identify [-h] [--version-range VERSION_RANGE]
                                  --confidence CONFIDENCE
                                  --evidence-json EVIDENCE_JSON
                                  subject_id library_name
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `subject_id` | required. No help text is declared; parser destination is `subject_id`. |
| `library_name` | required. No help text is declared; parser destination is `library_name`. |
| `--version-range` | declared. No help text is declared; parser destination is `version_range`. |
| `--confidence` | required · type: `float`. No help text is declared; parser destination is `confidence`. |
| `--evidence-json` | required. No help text is declared; parser destination is `evidence_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp library reconstruct`

usage: x86decomp library reconstruct [-h] match_id

### Usage

```text
x86decomp library reconstruct [-h] match_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `match_id` | required. No help text is declared; parser destination is `match_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp library reject`

usage: x86decomp library reject [-h] match_id

### Usage

```text
x86decomp library reject [-h] match_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `match_id` | required. No help text is declared; parser destination is `match_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
