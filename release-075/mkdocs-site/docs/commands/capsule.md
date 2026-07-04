---
title: x86decomp capsule
description: Exact parser-derived reference for x86decomp capsule in 0.7.5.
---

# `x86decomp capsule`

Canonical capability group with 4 routes. Shared group options are shown in every exact usage string.

## `x86decomp capsule create`

usage: x86decomp capsule create [-h] [--include INCLUDE]

### Usage

```text
x86decomp capsule create [-h] [--include INCLUDE]
                                [--external-json EXTERNAL_JSON]
                                name output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `name` | required. No help text is declared; parser destination is `name`. |
| `output` | required. No help text is declared; parser destination is `output`. |
| `--include` | default: `[]`. No help text is declared; parser destination is `include`. |
| `--external-json` | declared. No help text is declared; parser destination is `external_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp capsule inspect`

usage: x86decomp capsule inspect [-h] path

### Usage

```text
x86decomp capsule inspect [-h] path
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required. No help text is declared; parser destination is `path`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp capsule reproduce`

usage: x86decomp capsule reproduce [-h] path destination

### Usage

```text
x86decomp capsule reproduce [-h] path destination
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required. No help text is declared; parser destination is `path`. |
| `destination` | required. No help text is declared; parser destination is `destination`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp capsule verify`

usage: x86decomp capsule verify [-h] path

### Usage

```text
x86decomp capsule verify [-h] path
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required. No help text is declared; parser destination is `path`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
