---
title: x86decomp library
description: Exact v0.7.8 parser-derived reference for `x86decomp library`.
---


# `x86decomp library`

Canonical library commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp library [-h] [--project PROJECT] [--actor ACTOR]
                         {accept,candidates,externalize,identify,reconstruct,reject} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

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

| Argument | Exact parser declaration |
| --- | --- |
| `match_id` | required · parser destination: `match_id`. No help text declared. |

### `x86decomp library candidates`

```text
usage: x86decomp library candidates [-h] subject_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `subject_id` | required · parser destination: `subject_id`. No help text declared. |

### `x86decomp library externalize`

```text
usage: x86decomp library externalize [-h] match_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `match_id` | required · parser destination: `match_id`. No help text declared. |

### `x86decomp library identify`

```text
usage: x86decomp library identify [-h] [--version-range VERSION_RANGE]
                                  --confidence CONFIDENCE
                                  --evidence-json EVIDENCE_JSON
                                  subject_id library_name
```

| Argument | Exact parser declaration |
| --- | --- |
| `subject_id` | required · parser destination: `subject_id`. No help text declared. |
| `library_name` | required · parser destination: `library_name`. No help text declared. |
| `--version-range` | parser destination: `version_range`. No help text declared. |
| `--confidence` | required · type: `float` · parser destination: `confidence`. No help text declared. |
| `--evidence-json` | required · parser destination: `evidence_json`. No help text declared. |

### `x86decomp library reconstruct`

```text
usage: x86decomp library reconstruct [-h] match_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `match_id` | required · parser destination: `match_id`. No help text declared. |

### `x86decomp library reject`

```text
usage: x86decomp library reject [-h] match_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `match_id` | required · parser destination: `match_id`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
