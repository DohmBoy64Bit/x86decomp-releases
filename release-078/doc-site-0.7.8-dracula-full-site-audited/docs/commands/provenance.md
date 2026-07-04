---
title: x86decomp provenance
description: Exact v0.7.8 parser-derived reference for `x86decomp provenance`.
---


# `x86decomp provenance`

Canonical provenance commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp provenance [-h] [--project PROJECT] [--actor ACTOR]
                            {binary,export,record,source} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `binary` | `usage: x86decomp provenance binary [-h] [--address ADDRESS] binary_id` | `reconstruction` |
| `export` | `usage: x86decomp provenance export [-h] output` | `reconstruction` |
| `record` | `usage: x86decomp provenance record [-h] --evidence-json EVIDENCE_JSON --confidence CONFIDENCE source_path line_start line_end binary_id address_start address_end` | `reconstruction` |
| `source` | `usage: x86decomp provenance source [-h] [--line LINE] source_path` | `reconstruction` |

### `x86decomp provenance binary`

```text
usage: x86decomp provenance binary [-h] [--address ADDRESS] binary_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `binary_id` | required · parser destination: `binary_id`. No help text declared. |
| `--address` | parser destination: `address`. No help text declared. |

### `x86decomp provenance export`

```text
usage: x86decomp provenance export [-h] output
```

| Argument | Exact parser declaration |
| --- | --- |
| `output` | required · parser destination: `output`. No help text declared. |

### `x86decomp provenance record`

```text
usage: x86decomp provenance record [-h] --evidence-json EVIDENCE_JSON
                                   --confidence CONFIDENCE
                                   source_path line_start line_end binary_id
                                   address_start address_end
```

| Argument | Exact parser declaration |
| --- | --- |
| `source_path` | required · parser destination: `source_path`. No help text declared. |
| `line_start` | required · type: `int` · parser destination: `line_start`. No help text declared. |
| `line_end` | required · type: `int` · parser destination: `line_end`. No help text declared. |
| `binary_id` | required · parser destination: `binary_id`. No help text declared. |
| `address_start` | required · parser destination: `address_start`. No help text declared. |
| `address_end` | required · parser destination: `address_end`. No help text declared. |
| `--evidence-json` | required · parser destination: `evidence_json`. No help text declared. |
| `--confidence` | required · type: `float` · parser destination: `confidence`. No help text declared. |

### `x86decomp provenance source`

```text
usage: x86decomp provenance source [-h] [--line LINE] source_path
```

| Argument | Exact parser declaration |
| --- | --- |
| `source_path` | required · parser destination: `source_path`. No help text declared. |
| `--line` | type: `int` · parser destination: `line`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
