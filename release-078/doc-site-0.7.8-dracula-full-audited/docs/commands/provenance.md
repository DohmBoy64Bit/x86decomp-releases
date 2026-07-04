---
title: x86decomp provenance
---

# `x86decomp provenance`

Canonical provenance commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp provenance [-h] [--project PROJECT] [--actor ACTOR]
                            {binary,export,record,source} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `binary` | `usage: x86decomp provenance binary [-h] [--address ADDRESS] binary_id` |
| `export` | `usage: x86decomp provenance export [-h] output` |
| `record` | `usage: x86decomp provenance record [-h] --evidence-json EVIDENCE_JSON --confidence CONFIDENCE source_path line_start line_end binary_id address_start address_end` |
| `source` | `usage: x86decomp provenance source [-h] [--line LINE] source_path` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp provenance binary` | `reconstruction` |
| `x86decomp provenance export` | `reconstruction` |
| `x86decomp provenance record` | `reconstruction` |
| `x86decomp provenance source` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
