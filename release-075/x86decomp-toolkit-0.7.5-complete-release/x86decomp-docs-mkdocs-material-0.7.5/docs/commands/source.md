---
title: x86decomp source
description: Exact parser-derived reference for x86decomp source in 0.7.5.
---

# `x86decomp source`

Canonical capability group with 4 routes. Shared group options are shown in every exact usage string.

## `x86decomp source impact`

usage: x86decomp source impact [-h] path

### Usage

```text
x86decomp source impact [-h] path
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required. No help text is declared; parser destination is `path`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp source lock`

usage: x86decomp source lock [-h] --reason REASON path

### Usage

```text
x86decomp source lock [-h] --reason REASON path
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required. No help text is declared; parser destination is `path`. |
| `--reason` | required. No help text is declared; parser destination is `reason`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp source reconcile`

usage: x86decomp source reconcile [-h] [--before-sha256 BEFORE_SHA256]

### Usage

```text
x86decomp source reconcile [-h] [--before-sha256 BEFORE_SHA256]
                                  [--semantic {true,false}]
                                  path
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required. No help text is declared; parser destination is `path`. |
| `--before-sha256` | declared. No help text is declared; parser destination is `before_sha256`. |
| `--semantic` | choices: `true`, `false`. No help text is declared; parser destination is `semantic`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp source unlock`

usage: x86decomp source unlock [-h] path

### Usage

```text
x86decomp source unlock [-h] path
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required. No help text is declared; parser destination is `path`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
