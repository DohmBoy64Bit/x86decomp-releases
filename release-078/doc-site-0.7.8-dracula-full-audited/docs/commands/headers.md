---
title: x86decomp headers
---

# `x86decomp headers`

Canonical headers commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp headers [-h] [--project PROJECT] [--actor ACTOR]
                         {create,cycles,declare,explain,include,synthesize,synthesize-project,validate} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `create` | `usage: x86decomp headers create [-h] [--visibility VISIBILITY] path` |
| `cycles` | `usage: x86decomp headers cycles [-h]` |
| `declare` | `usage: x86decomp headers declare [-h] [--kind KIND] [--confidence CONFIDENCE] [--evidence-json EVIDENCE_JSON] header_id symbol_id declaration` |
| `explain` | `usage: x86decomp headers explain [-h] header_id` |
| `include` | `usage: x86decomp headers include [-h] --reason REASON source_header_id target_header_id` |
| `synthesize` | `usage: x86decomp headers synthesize [-h] [--output-root OUTPUT_ROOT] header_id` |
| `synthesize-project` | `usage: x86decomp headers synthesize-project [-h] [--module MODULE] output` |
| `validate` | `usage: x86decomp headers validate [-h] header_id` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp headers create` | `reconstruction` |
| `x86decomp headers cycles` | `reconstruction` |
| `x86decomp headers declare` | `reconstruction` |
| `x86decomp headers explain` | `reconstruction` |
| `x86decomp headers include` | `reconstruction` |
| `x86decomp headers synthesize` | `reconstruction` |
| `x86decomp headers synthesize-project` | `reconstruction` |
| `x86decomp headers validate` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
