---
title: x86decomp provenance
description: Command reference for `x86decomp provenance`.
---


# `x86decomp provenance`

Canonical provenance commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp provenance [-h] [--project PROJECT] [--actor ACTOR]
                            {binary,export,record,source} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

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

| Argument | Details |
| --- | --- |
| `binary_id` | required. |
| `--address` | — |

### `x86decomp provenance export`

```text
usage: x86decomp provenance export [-h] output
```

| Argument | Details |
| --- | --- |
| `output` | required. |

### `x86decomp provenance record`

```text
usage: x86decomp provenance record [-h] --evidence-json EVIDENCE_JSON
                                   --confidence CONFIDENCE
                                   source_path line_start line_end binary_id
                                   address_start address_end
```

| Argument | Details |
| --- | --- |
| `source_path` | required. |
| `line_start` | required · type: `int`. |
| `line_end` | required · type: `int`. |
| `binary_id` | required. |
| `address_start` | required. |
| `address_end` | required. |
| `--evidence-json` | required. |
| `--confidence` | required · type: `float`. |

### `x86decomp provenance source`

```text
usage: x86decomp provenance source [-h] [--line LINE] source_path
```

| Argument | Details |
| --- | --- |
| `source_path` | required. |
| `--line` | type: `int`. |


