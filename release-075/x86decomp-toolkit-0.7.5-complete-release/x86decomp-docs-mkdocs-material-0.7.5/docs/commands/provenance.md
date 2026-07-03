---
title: x86decomp provenance
description: Exact parser-derived reference for x86decomp provenance in 0.7.5.
---

# `x86decomp provenance`

Canonical capability group with 4 routes. Shared group options are shown in every exact usage string.

## `x86decomp provenance binary`

usage: x86decomp provenance binary [-h] [--address ADDRESS] binary_id

### Usage

```text
x86decomp provenance binary [-h] [--address ADDRESS] binary_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `binary_id` | required. No help text is declared; parser destination is `binary_id`. |
| `--address` | declared. No help text is declared; parser destination is `address`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp provenance export`

usage: x86decomp provenance export [-h] output

### Usage

```text
x86decomp provenance export [-h] output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `output` | required. No help text is declared; parser destination is `output`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp provenance record`

usage: x86decomp provenance record [-h] --evidence-json EVIDENCE_JSON

### Usage

```text
x86decomp provenance record [-h] --evidence-json EVIDENCE_JSON
                                   --confidence CONFIDENCE
                                   source_path line_start line_end binary_id
                                   address_start address_end
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `source_path` | required. No help text is declared; parser destination is `source_path`. |
| `line_start` | required · type: `int`. No help text is declared; parser destination is `line_start`. |
| `line_end` | required · type: `int`. No help text is declared; parser destination is `line_end`. |
| `binary_id` | required. No help text is declared; parser destination is `binary_id`. |
| `address_start` | required. No help text is declared; parser destination is `address_start`. |
| `address_end` | required. No help text is declared; parser destination is `address_end`. |
| `--evidence-json` | required. No help text is declared; parser destination is `evidence_json`. |
| `--confidence` | required · type: `float`. No help text is declared; parser destination is `confidence`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp provenance source`

usage: x86decomp provenance source [-h] [--line LINE] source_path

### Usage

```text
x86decomp provenance source [-h] [--line LINE] source_path
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `source_path` | required. No help text is declared; parser destination is `source_path`. |
| `--line` | type: `int`. No help text is declared; parser destination is `line`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
