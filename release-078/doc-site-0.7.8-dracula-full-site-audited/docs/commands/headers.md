---
title: x86decomp headers
description: Command reference for `x86decomp headers`.
---


# `x86decomp headers`

Canonical headers commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp headers [-h] [--project PROJECT] [--actor ACTOR]
                         {create,cycles,declare,explain,include,synthesize,synthesize-project,validate} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

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

| Argument | Details |
| --- | --- |
| `path` | required. |
| `--visibility` | default: `'private'`. |

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

| Argument | Details |
| --- | --- |
| `header_id` | required. |
| `symbol_id` | required. |
| `declaration` | required. |
| `--kind` | default: `'function'`. |
| `--confidence` | type: `float` · default: `1.0`. |
| `--evidence-json` | — |

### `x86decomp headers explain`

```text
usage: x86decomp headers explain [-h] header_id
```

| Argument | Details |
| --- | --- |
| `header_id` | required. |

### `x86decomp headers include`

```text
usage: x86decomp headers include [-h] --reason REASON
                                 source_header_id target_header_id
```

| Argument | Details |
| --- | --- |
| `source_header_id` | required. |
| `target_header_id` | required. |
| `--reason` | required. |

### `x86decomp headers synthesize`

```text
usage: x86decomp headers synthesize [-h] [--output-root OUTPUT_ROOT] header_id
```

| Argument | Details |
| --- | --- |
| `header_id` | required. |
| `--output-root` | — |

### `x86decomp headers synthesize-project`

```text
usage: x86decomp headers synthesize-project [-h] [--module MODULE] output
```

| Argument | Details |
| --- | --- |
| `output` | required. |
| `--module` | — |

### `x86decomp headers validate`

```text
usage: x86decomp headers validate [-h] header_id
```

| Argument | Details |
| --- | --- |
| `header_id` | required. |


