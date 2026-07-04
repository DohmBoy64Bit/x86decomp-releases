---
title: x86decomp headers
description: Exact v0.7.8 parser-derived reference for `x86decomp headers`.
---


# `x86decomp headers`

Canonical headers commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp headers [-h] [--project PROJECT] [--actor ACTOR]
                         {create,cycles,declare,explain,include,synthesize,synthesize-project,validate} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `create` | `usage: x86decomp headers create [-h] [--visibility VISIBILITY] path` | `reconstruction` |
| `cycles` | `usage: x86decomp headers cycles [-h]` | `reconstruction` |
| `declare` | `usage: x86decomp headers declare [-h] [--kind KIND] [--confidence CONFIDENCE] [--evidence-json EVIDENCE_JSON] header_id symbol_id declaration` | `reconstruction` |
| `explain` | `usage: x86decomp headers explain [-h] header_id` | `reconstruction` |
| `include` | `usage: x86decomp headers include [-h] --reason REASON source_header_id target_header_id` | `reconstruction` |
| `synthesize` | `usage: x86decomp headers synthesize [-h] [--output-root OUTPUT_ROOT] header_id` | `reconstruction` |
| `synthesize-project` | `usage: x86decomp headers synthesize-project [-h] [--module MODULE] output` | `reconstruction` |
| `validate` | `usage: x86decomp headers validate [-h] header_id` | `reconstruction` |

### `x86decomp headers create`

```text
usage: x86decomp headers create [-h] [--visibility VISIBILITY] path
```

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required · parser destination: `path`. No help text declared. |
| `--visibility` | default: `'private'` · parser destination: `visibility`. No help text declared. |

### `x86decomp headers cycles`

```text
usage: x86decomp headers cycles [-h]
```

### `x86decomp headers declare`

```text
usage: x86decomp headers declare [-h] [--kind KIND] [--confidence CONFIDENCE]
                                 [--evidence-json EVIDENCE_JSON]
                                 header_id symbol_id declaration
```

| Argument | Exact parser declaration |
| --- | --- |
| `header_id` | required · parser destination: `header_id`. No help text declared. |
| `symbol_id` | required · parser destination: `symbol_id`. No help text declared. |
| `declaration` | required · parser destination: `declaration`. No help text declared. |
| `--kind` | default: `'function'` · parser destination: `kind`. No help text declared. |
| `--confidence` | type: `float` · default: `1.0` · parser destination: `confidence`. No help text declared. |
| `--evidence-json` | parser destination: `evidence_json`. No help text declared. |

### `x86decomp headers explain`

```text
usage: x86decomp headers explain [-h] header_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `header_id` | required · parser destination: `header_id`. No help text declared. |

### `x86decomp headers include`

```text
usage: x86decomp headers include [-h] --reason REASON
                                 source_header_id target_header_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `source_header_id` | required · parser destination: `source_header_id`. No help text declared. |
| `target_header_id` | required · parser destination: `target_header_id`. No help text declared. |
| `--reason` | required · parser destination: `reason`. No help text declared. |

### `x86decomp headers synthesize`

```text
usage: x86decomp headers synthesize [-h] [--output-root OUTPUT_ROOT] header_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `header_id` | required · parser destination: `header_id`. No help text declared. |
| `--output-root` | parser destination: `output_root`. No help text declared. |

### `x86decomp headers synthesize-project`

```text
usage: x86decomp headers synthesize-project [-h] [--module MODULE] output
```

| Argument | Exact parser declaration |
| --- | --- |
| `output` | required · parser destination: `output`. No help text declared. |
| `--module` | parser destination: `module`. No help text declared. |

### `x86decomp headers validate`

```text
usage: x86decomp headers validate [-h] header_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `header_id` | required · parser destination: `header_id`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
