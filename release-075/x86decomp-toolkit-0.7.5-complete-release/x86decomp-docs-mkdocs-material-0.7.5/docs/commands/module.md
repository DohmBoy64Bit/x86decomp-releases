---
title: x86decomp module
description: Exact parser-derived reference for x86decomp module in 0.7.5.
---

# `x86decomp module`

Canonical capability group with 7 routes. Shared group options are shown in every exact usage string.

## `x86decomp module add-member`

usage: x86decomp module add-member [-h] [--ordinal ORDINAL]

### Usage

```text
x86decomp module add-member [-h] [--ordinal ORDINAL]
                                   [--evidence-json EVIDENCE_JSON]
                                   module_id member_kind member_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `module_id` | required. No help text is declared; parser destination is `module_id`. |
| `member_kind` | required. No help text is declared; parser destination is `member_kind`. |
| `member_id` | required. No help text is declared; parser destination is `member_id`. |
| `--ordinal` | default: `0` · type: `int`. No help text is declared; parser destination is `ordinal`. |
| `--evidence-json` | declared. No help text is declared; parser destination is `evidence_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp module add-unit-member`

usage: x86decomp module add-unit-member [-h] [--linkage LINKAGE]

### Usage

```text
x86decomp module add-unit-member [-h] [--linkage LINKAGE]
                                        [--ordinal ORDINAL]
                                        unit_id member_kind member_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `unit_id` | required. No help text is declared; parser destination is `unit_id`. |
| `member_kind` | required. No help text is declared; parser destination is `member_kind`. |
| `member_id` | required. No help text is declared; parser destination is `member_id`. |
| `--linkage` | default: `'external'`. No help text is declared; parser destination is `linkage`. |
| `--ordinal` | default: `0` · type: `int`. No help text is declared; parser destination is `ordinal`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp module create`

usage: x86decomp module create [-h] [--kind KIND] [--source-path SOURCE_PATH]

### Usage

```text
x86decomp module create [-h] [--kind KIND] [--source-path SOURCE_PATH]
                               [--confidence CONFIDENCE]
                               [--evidence-json EVIDENCE_JSON]
                               name
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `name` | required. No help text is declared; parser destination is `name`. |
| `--kind` | default: `'static-library'`. No help text is declared; parser destination is `kind`. |
| `--source-path` | declared. No help text is declared; parser destination is `source_path`. |
| `--confidence` | default: `1.0` · type: `float`. No help text is declared; parser destination is `confidence`. |
| `--evidence-json` | declared. No help text is declared; parser destination is `evidence_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp module create-unit`

usage: x86decomp module create-unit [-h] [--module-id MODULE_ID]

### Usage

```text
x86decomp module create-unit [-h] [--module-id MODULE_ID]
                                    [--language LANGUAGE]
                                    [--confidence CONFIDENCE]
                                    [--evidence-json EVIDENCE_JSON]
                                    source_path
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `source_path` | required. No help text is declared; parser destination is `source_path`. |
| `--module-id` | declared. No help text is declared; parser destination is `module_id`. |
| `--language` | default: `'cpp'`. No help text is declared; parser destination is `language`. |
| `--confidence` | default: `1.0` · type: `float`. No help text is declared; parser destination is `confidence`. |
| `--evidence-json` | declared. No help text is declared; parser destination is `evidence_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp module list`

usage: x86decomp module list [-h]

### Usage

```text
x86decomp module list [-h]
```

No route-specific arguments are declared.

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp module show`

usage: x86decomp module show [-h] module_id

### Usage

```text
x86decomp module show [-h] module_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `module_id` | required. No help text is declared; parser destination is `module_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp module show-unit`

usage: x86decomp module show-unit [-h] unit_id

### Usage

```text
x86decomp module show-unit [-h] unit_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `unit_id` | required. No help text is declared; parser destination is `unit_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
