---
title: x86decomp library
description: Command reference for `x86decomp library`.
---


# `x86decomp library`

Canonical library commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp library [-h] [--project PROJECT] [--actor ACTOR]
                         {accept,candidates,externalize,identify,reconstruct,reject} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `accept` | `usage: x86decomp library accept [-h] match_id` | `reconstruction` |
| `candidates` | `usage: x86decomp library candidates [-h] subject_id` | `reconstruction` |
| `externalize` | `usage: x86decomp library externalize [-h] match_id` | `reconstruction` |
| `identify` | `usage: x86decomp library identify [-h] [--version-range VERSION_RANGE] --confidence CONFIDENCE --evidence-json EVIDENCE_JSON subject_id library_name` | `reconstruction` |
| `reconstruct` | `usage: x86decomp library reconstruct [-h] match_id` | `reconstruction` |
| `reject` | `usage: x86decomp library reject [-h] match_id` | `reconstruction` |

### `x86decomp library accept`

```text
usage: x86decomp library accept [-h] match_id
```

| Argument | Details |
| --- | --- |
| `match_id` | required. |

### `x86decomp library candidates`

```text
usage: x86decomp library candidates [-h] subject_id
```

| Argument | Details |
| --- | --- |
| `subject_id` | required. |

### `x86decomp library externalize`

```text
usage: x86decomp library externalize [-h] match_id
```

| Argument | Details |
| --- | --- |
| `match_id` | required. |

### `x86decomp library identify`

```text
usage: x86decomp library identify [-h] [--version-range VERSION_RANGE]
                                  --confidence CONFIDENCE
                                  --evidence-json EVIDENCE_JSON
                                  subject_id library_name
```

| Argument | Details |
| --- | --- |
| `subject_id` | required. |
| `library_name` | required. |
| `--version-range` | — |
| `--confidence` | required · type: `float`. |
| `--evidence-json` | required. |

### `x86decomp library reconstruct`

```text
usage: x86decomp library reconstruct [-h] match_id
```

| Argument | Details |
| --- | --- |
| `match_id` | required. |

### `x86decomp library reject`

```text
usage: x86decomp library reject [-h] match_id
```

| Argument | Details |
| --- | --- |
| `match_id` | required. |


